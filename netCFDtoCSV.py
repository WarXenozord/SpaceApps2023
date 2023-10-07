import netCDF4
import numpy as np

nc_file = 'data/AQUA_MODIS.20230101.L3m.DAY.CHL.chlor_a.4km.NRT.nc'
nc = netCDF4.Dataset(nc_file, mode='r')

nc.variables.keys()

lat = nc.variables['lat'][:]
lon = nc.variables['lon'][:]
chloro = nc.variables['chlor_a'][:]


np.savetxt('lat.csv', lat, delimiter=',')
np.savetxt('lon.csv', lon, delimiter=',')
np.savetxt('chloro.csv', chloro, delimiter=',')
