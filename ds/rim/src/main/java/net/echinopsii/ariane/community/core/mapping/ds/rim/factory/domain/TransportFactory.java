/**
 * Mapping Datastore Runtime Injectection Manager :
 * provide a Mapping DS configuration parser, factories and registry to inject
 * Mapping DS interface implementation dependencies.
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

package net.echinopsii.ariane.community.core.mapping.ds.rim.factory.domain;

import net.echinopsii.ariane.community.core.mapping.ds.domain.Transport;
import net.echinopsii.ariane.community.core.mapping.ds.rim.registry.MappingDSRegistry;

public class TransportFactory {

	public static Transport make(String type) throws ClassNotFoundException, InstantiationException, IllegalAccessException {
		Transport ret = null;
		String transportClassName = MappingDSRegistry.getEntityFromRegistry(type).getTransportFactoryClassName();
		ClassLoader loader = new TransportFactory().getClass().getClassLoader();
		@SuppressWarnings("unchecked")
		Class<? extends Transport> transportClass = (Class<? extends Transport>) loader.loadClass(transportClassName); 
		ret = transportClass.newInstance();
		return ret;		
	}	
}