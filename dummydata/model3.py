from dummydata import DummyData

#~ import numpy

class Model3(DummyData):
    """
    Dummydata that mimic Model data with three spatial dimensions
    """
    def __init__(self, var='dummyVariable', month=3, oname="DummyM3.nc", **kwargs):
        """
        create an empty 3D file

        Parameters
        ----------
        month : int
            number of months
        var : str
            variable name to specify
        """
        super(Model3, self).__init__(oname, **kwargs)
        self.oname = oname

        self.month = month
        self.var = var

        self.createM3Dimension()
        self.createM3Variable()
        self.addM3Data()
        self.close()

    def createM3Dimension(self):
        self._create_time_dimension()
        self._create_coordinate_dimensions()
        self._create_bnds_dimensions()
        self.createDimension('plev', 17)



    def createM3Variable(self):
        # create time variable
        self._create_time_variable()

        # create coordinates
        self._create_coordinates()


        self.createVariable('plev', 'f8', ('plev',))

        self.createVariable(
            self.var,
            'f4',
            ('time',
             'plev',
             'lat',
             'lon',
             ),
            fill_value=1.e+20)


        self.variables['plev'].units = 'Pa'
        self.variables['plev'].axis = 'Z'
        self.variables['plev'].positive = 'down'
        self.variables['plev'].long_name = 'pressure'
        self.variables['plev'].standard_name = 'air_pressure'

        self.variables[self.var].standard_name = 'air_temperature'
        self.variables[self.var].long_name = 'Air Temperature'
        self.variables[self.var].units = 'K'
        self.variables[self.var].original_name = 'T,PS'
        self.variables[self.var].comment = 'T interpolated to standard plevs'
        self.variables[self.var].cell_methods = 'time: mean (interval: 30 days)'
        self.variables[self.var].cell_measures = 'area: areacella'
        self.variables[self.var].history = ''
        self.variables[self.var].missing_value = 1.e+20



        self._set_metadata()




    def addM3Data(self):
        self.variables['plev'][:] = [
            100000,
            92500,
            85000,
            70000,
            60000,
            50000,
            40000,
            30000,
            25000,
            20000,
            15000,
            10000,
            7000,
            5000,
            3000,
            2000,
            1000]

        # set variable data
        self.variables[self.var][0:self.month, :, :, :] = self._get_variable_data()

        # set coordinates
        self._set_coordinate_data()

        # set the time
        self._set_time_data()

