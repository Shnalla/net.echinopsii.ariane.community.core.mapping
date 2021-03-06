// ┌──────────────────────────────────────────────────────────────────────────────────────┐ \\
// │ Taitale - JavaScript Taitale Library - TOOLS - loader                                │ \\
// │ Use Raphael.js                                                                       │ \\
// │ -------------------------------------------------------------------------------------│ \\
// │ Taitale - provide an infrastructure mapping graph engine                             │ \\
// │ Copyright (C) 2013  Mathilde Ffrench												  │ \\
// │ 																					  │ \\
// │ This program is free software: you can redistribute it and/or modify                 │ \\
// │ it under the terms of the GNU Affero General Public License as                       │ \\
// │ published by the Free Software Foundation, either version 3 of the                   │ \\
// │ License, or (at your option) any later version.									  │ \\
// │																					  │ \\
// │ This program is distributed in the hope that it will be useful,					  │ \\
// │ but WITHOUT ANY WARRANTY; without even the implied warranty of						  │ \\
// │ MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the						  │ \\
// │ GNU Affero General Public License for more details.								  │ \\
// │																					  │ \\
// │ You should have received a copy of the GNU Affero General Public License			  │ \\
// │ along with this program.  If not, see <http://www.gnu.org/licenses/>.				  │ \\
// └──────────────────────────────────────────────────────────────────────────────────────┘ \\

define(
    [
        'jquery',
        'raphael',
        'raphael-zpd',
        'taitale-params',
        'taitale-map',
        'taitale-helper',
        'taitale-ext-raphael'
    ],
    function($,Raphael,RaphelZPD,params,map,helper) {

        function loader () {

            // SAMPLE PURPOSE => when ajax sync we display a map whatever the httpd server state.
            //jQuery.ajaxSetup({async:false});
            //jQuery.ajaxSetup({timeout:8000});

            var helper_  = new helper(),
                loader   = this,
                r        = null,
                zpd      = null,
                mappy    = null;

            var menu              = null,
                menuSet           = null,
                menuFillColor     = params.map_menuFillColor,
                menuStrokeColor   = params.map_menuStrokeColor,
                menuOpacity       = params.map_menuOpacity,
                menuStrokeWidth   = params.map_menuStrokeWidth,
                menuHided         = true;

            var refreshZPDOffset = null;

            var mainMouseDown = function(e) {

                var offsets = r.getHTMLOffsets();

                var posx = 0;
                var posy = 0;
                if (!e) e = window.event;
                if (e.clientX || e.clientY) {
                    posx = e.clientX + document.body.scrollLeft
                        + document.documentElement.scrollLeft - offsets.left;
                    posy = e.clientY + document.body.scrollTop
                        + document.documentElement.scrollTop - offsets.top;
                }

                if (e.which == 3) {
                    if (r.getDisplayMainMenu() && posx > 0 && posy > 0) {
                        for (var i = 0, ii = menuSet.length ; i < ii ; i++) {
                            if (i==0)
                                menuSet[i].attr({"x": posx, "y": posy+10});
                            else if (i==1)
                                menuSet[i].attr({"x": posx, "y": posy+30});
                            else
                                menuSet[i].attr({"x": posx, "y": posy+30+(i-1)*15});
                        }
                        if (menuHided) {
                            menu = r.menu(posx,posy,menuSet).attr({fill: menuFillColor, stroke: menuStrokeColor, "stroke-width": menuStrokeWidth, "fill-opacity": menuOpacity});
                            menu.toFront();
                            menu.show();
                            menuSet.toFront();
                            menuSet.show();
                            menuHided=false;
                        } else {
                            menu.remove();
                            menuSet.toBack();
                            menuSet.hide();
                            menuHided=true;
                        }
                    }
                    r.setDisplayMainMenu(true);
                }
            };

            this.normalSize = function() {
                var mapLayoutDivHeight = helper_.getMappyLayoutDivSize().height,
                    mapCanvasWidth     = helper_.getMappyCanvasDivSize().width,
                    mapCanvasHeight    = mapLayoutDivHeight + helper_.getMappyCanvasDivSize().height,
                    mapCanvasCenterX   = mapCanvasWidth/ 2,
                    mapCanvasCenterY   = mapCanvasHeight/2;

                mappy.updateSize();

                var mappyWidth    = mappy.getMapSize().width,
                    mappyHeight   = mappy.getMapSize().height,
                    mappyTopLeftX = mappy.getTopLeftCoords().topLeftX,
                    mappyTopLeftY = mappy.getTopLeftCoords().topLeftY,
                    mappyCenterX  = (mappyTopLeftX + mappyWidth)/2,
                    mappyCenterY  = (mappyTopLeftY + mappyHeight)/2;

                //helper_.debug("=>normal size");
                r.ZPDNormalSize(mapCanvasCenterX, mapCanvasCenterY);

                //helper_.debug("=>pan");
                var transX = mapCanvasCenterX-mappyCenterX,
                    transY = mapCanvasCenterY-mappyCenterY;
                r.ZPDPanTo(transX,transY);
            };

            this.centerMappy = function() {
                var mapLayoutDivHeight = helper_.getMappyLayoutDivSize().height,
                    mapCanvasWidth     = helper_.getMappyCanvasDivSize().width,
                    mapCanvasHeight    = mapLayoutDivHeight + helper_.getMappyCanvasDivSize().height,
                    mapCanvasCenterX   = mapCanvasWidth/ 2,
                    mapCanvasCenterY   = mapCanvasHeight/2;

                /**
                 * normale size and center
                 */
                this.normalSize();

                var mappyWidth    = mappy.getMapSize().width,
                    mappyHeight   = mappy.getMapSize().height;

                /**
                 * scale
                 */
                //helper_.debug("=>scale to center");
                var deltaX = mapCanvasWidth/mappyWidth,
                    deltaY = mapCanvasHeight/mappyHeight;
                if (deltaX < 1 || deltaY < 1) {
                    var delta = Math.min(deltaX,deltaY) - 1;
                    //helper_.debug(deltaX + "," + deltaY + "," + delta);
                    r.ZPDScaleTo(delta, mapCanvasCenterX, mapCanvasCenterY);
                }
            };

            this.loadMappy = function() {
                var mapLayoutDivHeight = helper_.getMappyLayoutDivSize().height,
                    mapCanvasWidth     = helper_.getMappyCanvasDivSize().width,
                    mapCanvasHeight    = mapLayoutDivHeight + helper_.getMappyCanvasDivSize().height;

                document.getElementById("mappyCanvas").innerHTML = "";
                r = Raphael("mappyCanvas", mapCanvasWidth, mapCanvasHeight);

                /**
                 * Init raphael JS object outside ZPD
                 */
                r.setMainMenuSet();
                //r.setEndpointMenuSet();
                //r.raphael.mousedown(mainMouseDown);
                r.raphael.getColor.reset();

                menuSet = r.getMainMenuSet();
                zpd = new RaphaelZPD(r, { zoom: true, pan: true, drag: false }, mappy);
                mappy.print(r);

                if (refreshZPDOffset!=null) {
                    zpd.ZPDRefreshLastOffset(refreshZPDOffset.x,refreshZPDOffset.y);
                }

                this.centerMappy();
            };

            var httpJSONmap = null;

            this.buildMappy = function(options) {
                mappy       = new map(options);
                mappy.parseJSON(httpJSONmap);
                mappy.buildMap();

                this.loadMappy();

                helper_.growlMsgs(
                    {
                        severity: 'info',
                        summary: 'Map successfully loaded ',
                        detail: 'Layout: '+options.getLayout() //+"<br>Mode: "+options.getMode()
                    }
                );
            };

            this.loadMap = function(options) {
                document.getElementById('mappyLoading').style.display = "";
                document.getElementById('mappyCanvas').style.display = "none";
                $.ajax({
                        url: options.getURI(),
                        success:
                            function(data)	{
                                if( !data || data === ""){
                                    // error
                                    return;
                                }

                                document.getElementById('mappyLoading').style.display = "none";
                                document.getElementById('mappyCanvas').style.display = "";

                                var json = null;
                                try {
                                    json = JSON.parse(data);
                                } catch (e) {
                                    throw   {
                                        stack: new Error("JSON parse error").stack,
                                        severity: 'error',
                                        summary: 'JSON parse error',
                                        detail: 'Unable to parse JSON from following url : '.concat(options.getURI()).concat('<br> error raised: ').concat(e.message),
                                        sticky: true
                                    };
                                }

                                httpJSONmap=json;
                                loader.buildMappy(options);
                            },
                        error:
                            function (xhr, ajaxOptions, thrownError){
                                document.getElementById('mappyLoading').style.display = "none";
                                document.getElementById('mappyCanvas').style.display = "";
                                throw   {
                                    stack: new Error("JSON parse error").stack,
                                    severity: 'error',
                                    summary: 'JSON parse error',
                                    detail: 'Unable to parse JSON from following url : '.concat(options.getURI()).concat('<br> error raised: ').concat(thrownError),
                                    sticky: true
                                };
                            },
                        dataType: "text"});
            };

            this.reloadMap = function(options) {
                if (zpd!=null)
                    zpd.ZPDClearEvents();
                if (r!=null) {
                    //r.raphael.unmousedown(mainMouseDown);
                    r.clear();
                }
                refreshZPDOffset=null;
                this.loadMap(options);
            };

            this.rebuildMap = function(options) {
                if (zpd!=null)
                    zpd.ZPDClearEvents();
                if (r!=null) {
                    //r.raphael.unmousedown(mainMouseDown);
                    r.clear();
                }
                refreshZPDOffset=null;
                this.buildMappy(options);
            };

            this.refreshMap = function(options) {
                if (zpd!=null) {
                    if (r!=null) {
                        refreshZPDOffset = r.getZPDoffsets();
                    }
                    zpd.ZPDClearEvents();
                }
                if (r!=null) {
                    //r.raphael.unmousedown(mainMouseDown);
                    r.clear();
                }
                loader.loadMappy();

                helper_.growlMsgs(
                    {
                        severity: 'info',
                        summary: 'Map successfully refreshed ',
                        detail: '<br>Layout: '+options.getLayout()//+"<br>Mode: "+options.getMode()
                    }
                );
            };

            this.displayDC = function(display) {
                if (mappy!=null && display!=null) mappy.displayDC(display);
            };

            this.displayArea = function(display) {
                if (mappy!=null && display!=null) mappy.displayArea(display);
            };

            this.displayLan = function(display) {
                if (mappy!=null && display!=null) mappy.displayLan(display);
            };

            this.sortRootTree = function(sort) {
                if (mappy!=null && sort!=null) mappy.sortRootTree(sort);
            };

            this.sortSubTrees = function(sort) {
                if (mappy!=null && sort!=null) mappy.sortSubTrees(sort);
            };

            this.rebuildMapTreeLayout = function()  {
                if (mappy!=null) mappy.rebuildMapTreeLayout();
            }
        }

        return loader;
});