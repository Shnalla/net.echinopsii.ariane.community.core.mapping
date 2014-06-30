require.config({
    baseUrl: '../../../js',
    paths: {
        'jquery': 'jquery/jquery-1.9.1',
        'eve': 'raphael/eve',
        'raphael-core': 'raphael/raphael.core',
        'raphael-svg': 'raphael/raphael.svg',
        'raphael-vml': 'raphael/raphael.vml',
        'raphael': 'raphael/raphael.amd'
    }
});

requirejs (
    [
        'raphael'
    ],
    function (Raphael) {

        function mariadbLogo(x, y, layer1) {

            var transform1 = "t-252.94671,-292.65607s0.3t-190,-130t"+x+","+y;
            var transform2 = "t-252.94671,-292.65607s0.3t-308,-205t"+x+","+y;
            var transform3 = "t-252.94671,-292.65607s0.3t-335,-25t"+x+","+y;
            var transform4 = "t-252.94671,-292.65607s0.3t-380,-15t"+x+","+y;

            layer1.attr({'id': 'layer1','name': 'layer1'});
            layer1.transform("t-252.94671,-292.65607");
            var layer2 = rsr.set();

            var backPath = rsr.path("M 428.82171,292.65922 C 426.04264,292.74803 426.92153,293.54877 420.91654,295.02655 C 414.8526,296.51884 407.44539,296.06125 400.91546,298.79984 C " +
                "381.42246,306.97484 377.51145,334.91583 359.79046,344.92484 C 346.54446,352.40684 333.18047,353.00359 321.16546,356.76859 C 313.26946,359.24459 304.63196,364.32235 " +
                "297.47796,370.48734 C 291.92496,375.27434 291.77997,379.48335 285.97796,385.48734 C 279.77196,391.90934 261.31271,385.59586 252.94671,395.42484 C 255.64171,398.14984 " +
                "256.82322,398.9131 262.13421,398.20609 C 261.03464,400.29018 254.5529,402.0465 255.82171,405.11234 C 257.15677,408.33826 272.8269,410.52508 287.07171,401.92484 C " +
                "293.70571,397.91959 298.98972,392.1466 309.32171,390.76859 C 322.69171,388.98659 338.09372,391.9116 353.57171,394.14359 C 351.27671,400.98659 346.66897,405.53734 " +
                "342.97796,410.98734 C 341.83496,412.21834 345.2737,412.35633 349.19671,411.61234 C 356.25371,409.86734 361.33947,408.46234 366.66546,405.36234 C 373.20846,401.55334 " +
                "374.19997,391.78785 382.22796,389.67484 C 386.70096,396.54984 398.86649,398.17385 406.41546,392.67484 C 399.79146,390.79984 397.96073,376.70034 400.19671,370.48734 C " +
                "402.31471,364.60634 404.40749,355.19884 406.54046,347.42484 C 408.83046,339.07584 409.67529,328.55269 412.44671,324.29984 C 416.61636,317.90135 421.22366,315.70409 " +
                "425.22363,312.09604 C 429.22359,308.48799 432.88484,304.97584 432.76469,296.71988 C 432.72599,294.06068 431.35105,292.57839 428.82171,292.65922 z").
                attr({id: 'backPath',parent: 'layer1',fill: '#002b64',"fill-opacity": '1',
                    "fill-rule": 'evenodd',stroke: 'none','stroke-width':'1','stroke-opacity':'1',"stroke-width": '0.2',
                    "stroke-miterlimit": '4',"stroke-dasharray": 'none',"stroke-opacity": '1'}).
                transform(transform1).data('id', 'backPath');

            var frontPath1 = rsr.path("M 258.70071,404.52409 C 268.84471,405.97709 275.01371,404.52409 283.15971,400.99109 C 290.09071,397.98509 296.78471,391.78809 304.96971,389.16109 C " +
                "316.99071,385.30409 330.17271,389.16609 343.02271,389.93609 C 346.15171,390.12409 349.26071,390.12609 352.32971,389.79209 C 357.11671,386.85009 357.01771,375.84509 " +
                "361.67671,374.83709 C 361.53971,390.27709 355.20971,399.52809 348.58971,408.48609 C 362.54171,406.02209 370.89071,397.95209 376.52971,387.17409 C 378.24071,383.90609 " +
                "379.70171,380.39009 380.99371,376.70509 C 382.99071,378.23809 381.85871,382.90209 382.86271,385.42909 C 392.47271,380.07609 397.97571,367.85909 401.61971,355.50309 C " +
                "405.83571,341.20309 407.56171,326.72309 410.28071,322.49209 C 412.93471,318.36209 417.06471,315.81609 420.83471,313.17209 C 425.11871,310.16609 428.93971,307.03309 429.59971," +
                "301.30509 C 425.08171,300.88709 424.03671,299.84209 423.36871,297.56509 C 421.10671,298.84009 419.02671,299.11309 416.67671,299.18309 C 414.63771,299.24509 412.39771," +
                "299.15409 409.66171,299.43509 C 387.03471,301.75909 384.15971,326.69809 369.65671,340.83609 C 368.60171,341.86409 367.46071,342.82309 366.25471,343.72309 C 361.17571," +
                "347.50809 354.94471,350.21309 349.21471,352.40309 C 339.93971,355.94709 331.12171,356.19909 322.41971,359.25809 C 316.03171,361.50309 309.54071,364.76009 304.29371," +
                "368.35109 C 302.98171,369.24809 301.74571,370.16709 300.60871,371.09709 C 297.52971,373.61609 295.50871,376.41109 293.55371,379.28609 C 291.53771,382.24909 289.59071," +
                "385.29709 286.62271,388.20909 C 281.81471,392.93009 263.84871,389.58609 257.52371,393.96409 C 256.81871,394.45109 256.25871,395.03609 255.87771,395.73809 C 259.32871," +
                "397.30609 261.63371,396.34409 265.60371,396.78309 C 266.12471,400.55009 257.41271,402.78909 258.70071,404.52409 z").
                attr({id: 'frontPath1',parent: 'layer1',fill: '#ffffff',stroke: 'none','stroke-width':'1','stroke-opacity':'1',"stroke-width": '0.25'}).
                transform(transform1).
                data('id', 'frontPath1');

            var frontPath2 = rsr.path("M 395.78457,377.38405 C 396.05457,381.70605 398.56357,390.28105 400.77857,392.36505 C 396.44057,393.42005 388.96757,391.67705 387.05057,388.61705 C " +
                "388.03557,384.19905 393.16157,380.16005 395.78457,377.38405 z").
                attr({id: 'frontPath2',"clip-rule": 'evenodd',parent: 'layer1',fill: '#ffffff',"fill-rule": 'evenodd',"fill-opacity": '1','stroke-width': '0','stroke-opacity': '1'}).
                transform(transform2).
                data('id', 'frontPath2');

            var eye = rsr.path("M 402.13957,308.79227 C 405.34257,311.57327 412.06357,309.34127 410.86257,303.80827 C 405.88557,303.39627 403.00257,305.08527 402.13957,308.79227 z").
                attr({id: 'eye',"clip-rule": 'evenodd',parent: 'layer1',fill: '#002b64',"fill-rule": 'evenodd','stroke-width': '0','stroke-opacity': '1'}).
                transform(transform3).
                data('id', 'eye');

            var poil1 = rsr.path("M 424.47057,302.32627 C 423.61857,304.11327 421.98757,306.41727 421.98757,310.96627 C 421.98057,311.74727 421.39457,312.28227 421.38457,311.07827 C " +
                "421.42857,306.63227 422.60557,304.71027 423.85557,302.18427 C 424.43657,301.14927 424.78657,301.57627 424.47057,302.32627 z").
                attr({id: 'poil1',parent: 'layer1',fill: '#002b64','stroke-width': '0','stroke-opacity': '1'}).
                transform(transform4).
                data('id', 'poil1');

            var poil2 = rsr.path("M 423.61257,301.65327 C 422.60757,303.35827 420.18757,306.46827 419.78757,311.00027 C 419.71357,311.77727 419.08157,312.25827 419.17757,311.05727 C " +
                "419.61357,306.63327 421.54757,303.86427 423.01557,301.45727 C 423.68157,300.47827 423.99457,300.93427 423.61257,301.65327 z").
                attr({id: 'poil2',parent: 'layer1',fill: '#002b64','stroke-width': '0','stroke-opacity': '1'}).
                transform(transform4).
                data('id', 'poil2');

            var poil3 = rsr.path("M 422.83057,300.76127 C 421.68557,302.37527 417.96057,306.11027 417.18157,310.59327 C 417.04157,311.36027 416.37157,311.78827 416.56857,310.59927 C " +
                "417.37457,306.22627 420.58557,302.78927 422.25057,300.51627 C 422.99657,299.59527 423.26957,300.07627 422.83057,300.76127 z").
                attr({id: 'poil3',parent: 'layer1',fill: '#002b64','stroke-width': '0','stroke-opacity': '1'}).
                transform(transform4).
                data('id', 'poil3');

            var poil4 = rsr.path("M 422.13257,299.76627 C 420.77257,301.20327 416.33157,305.96627 414.93157,310.29427 C 414.68357,311.03427 413.96057,311.36427 414.32357,310.21427 C " +
                "415.73557,305.99827 419.62457,301.45727 421.59257,299.44127 C 422.46157,298.63427 422.66357,299.14927 422.13257,299.76627 z").
                attr({id: 'poil4',parent: 'layer1',fill: '#002b64','stroke-width': '0','stroke-opacity': '1'}).
                transform(transform4).
                data('id', 'poil4');

            layer2.attr({'id': 'layer2','transformG': 'translate(-252.94671,-292.65607)','parent': 'layer1','name': 'layer2'});

            var rsrGroups = [layer1,layer2];
            layer1.push();
            layer2.push(
                backPath ,
                frontPath1 ,
                frontPath2 ,
                eye ,
                poil1 ,
                poil2 ,
                poil3 ,
                poil4
            );
        }

        var rsr = Raphael('rsr', '1200', '1200');

        var x=100
        var y=100

        var layer1 = rsr.set();

        mariadbLogo(x, y, layer1);
    });
