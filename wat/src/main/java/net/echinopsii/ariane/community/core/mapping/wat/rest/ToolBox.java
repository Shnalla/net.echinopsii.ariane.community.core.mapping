/**
 * Mapping Web Service :
 * provide a mapping DS Web Service and REST Service
 *
 * Copyright (C) 2013  Mathilde Ffrench
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
package net.echinopsii.ariane.community.core.mapping.wat.rest;

import net.echinopsii.ariane.community.core.mapping.wat.json.PropertiesException;
import net.echinopsii.ariane.community.core.mapping.wat.json.PropertiesJSON;

import java.io.*;

public class ToolBox {

    public static String getOuputStreamContent(ByteArrayOutputStream out, String encoding) throws IOException {
        ByteArrayInputStream input = new ByteArrayInputStream(((ByteArrayOutputStream) out).toByteArray());
        BufferedReader br = new BufferedReader(new InputStreamReader(input, encoding));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            sb.append(line);
            sb.append('\n');
        }
        return sb.toString();
    }

    public static Object extractPropertyObjectValueFromString(String value, String type) throws IOException, PropertiesException {
        Object ovalue = null;
        switch (type.toLowerCase()) {
            case "int":
            case "integer":
                ovalue = new Integer(value);
                break;
            case "long":
                ovalue = new Long(value);
                break;
            case "double":
                ovalue = new Double(value);
                break;
            case "boolean":
                ovalue = new Boolean(value);
                break;
            case "array":
            case "map":
                ovalue = PropertiesJSON.JSONStringToPropertyObject(type, value);
                break;
            case "string":
                ovalue = value;
                break;
            default:
                throw new PropertiesException("Invalid property type ("+type.toLowerCase()+"). Supported property types are : array, boolean, double, int, long, map and String");
        }
        return ovalue;
    }
}
