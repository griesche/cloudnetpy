"""Initial Metadata of Cloudnet variables for NetCDF file writing.
"""

from collections import namedtuple

FIELDS = (
    'long_name',
    'units',
    'plot_range',
    'plot_scale',
    'comment',
    'definition',
    'references',
    'ancillary_variables',
    'positive')

MetaData = namedtuple('MetaData', FIELDS, defaults=(None,)*len(FIELDS))

_LOG = 'logarithmic'
_LIN = 'linear'

_DEFINITIONS = {
    'category_bits':
    ('\nBit 0: Small liquid droplets are present.'
     '\nBit 1: Falling hydrometeors are present; if Bit 2 is set then these are most'
     '       \nlikely ice particles, otherwise they are drizzle or rain drops.'
     '\nBit 2: Wet-bulb temperature is less than 0 degrees C, implying'
     '       \nthe phase of Bit-1 particles.'
     '\nBit 3: Melting ice particles are present.'
     '\nBit 4: Aerosol particles are present and visible to the lidar.'
     '\nBit 5: Insects are present and visible to the radar.'),

    'quality_bits':
    ('\nBit 0: An echo is detected by the radar.'
     '\nBit 1: An echo is detected by the lidar.'
     '\nBit 2: The apparent echo detected by the radar is ground clutter'
     '       \nor some other non-atmospheric artifact.'
     '\nBit 3: The lidar echo is due to clear-air molecular scattering.'
     '\nBit 4: Liquid water cloud, rainfall or melting ice below this pixel'
     '       \nwill have caused radar and lidar attenuation; if bit 5 is set then'
     '       \na correction for the radar attenuation has been performed;'
     '       \notherwise do not trust the absolute values of reflectivity factor.'
     '       \nNo correction is performed for lidar attenuation.'
     '\nBit 5: Radar reflectivity has been corrected for liquid-water attenuation'
     '       \nusing the microwave radiometer measurements of liquid water path'
     '       \nand the lidar estimation of the location of liquid water cloud;'
     '       \nbe aware that errors in reflectivity may result.'),

    'model_number':
        ('\n0: Single polarisation radar.'
         '\n1: Dual polarisation radar.'),

    'dual_polarization':
        ('\n0: Single polarisation radar.'
         '\n1: Dual polarisation radar in linear depolarisation ratio (LDR) mode.'
         '\n2: Dual polarisation radar in simultaneous transmission simultaneous reception (STSR) mode.'),

    'FFT_window':
        ('\n0: square'
         '\n1: parzen'
         '\n2: blackman'
         '\n3: welch'
         '\n4: slepian2'
         '\n5: slepian3'),

    'quality_flag':
        ('\nBit 0: ADC saturation.'
         '\nBit 1: Spectral width too high.'
         '\nBit 2: No transmission power levelling.')


}

_COMMENTS = {
    'category_bits':
    ('This variable contains information on the nature of the targets\n'
     'at each pixel, thereby facilitating the application of algorithms that work\n'
     'with only one type of target. The information is in the form of an array of\n'
     'bits, each of which states either whether a certain type of particle is present\n'
     '(e.g. aerosols), or the whether some of the target particles have a particular\n'
     'property. The definitions of each bit are given in the definition attribute.\n'
     'Bit 0 is the least significant.'),

    'quality_bits':
    ('This variable contains information on the quality of the\n'
     'data at each pixel. The information is in the form of an array\n'
     'of bits, and the definitions of each bit are given in the definition\n'
     'attribute. Bit 0 is the least significant.'),

    'radar_liquid_atten':
    ('This variable was calculated from the liquid water path\n'
     'measured by microwave radiometer using lidar and radar returns to perform\n'
     'an approximate partioning of the liquid water content with height. Bit 5 of\n'
     'the quality_bits variable indicates where a correction for liquid water\n'
     'attenuation has been performed.'),

    'radar_gas_atten':
    ('This variable was calculated from the model temperature,\n'
     'pressure and humidity, but forcing pixels containing liquid cloud to saturation\n'
     'with respect to liquid water. It was calculated using the millimeter-wave propagation\n'
     'model of Liebe (1985, Radio Sci. 20(5), 1069-1089). It has been used to correct Z.'),

    'Tw':
    ('This variable was calculated from model T, P and relative humidity, first\n'
     'interpolated into measurement grid.'),

    'Z_sensitivity':
    ('This variable is an estimate of the radar sensitivity,\n'
     'i.e. the minimum detectable radar reflectivity, as a function\n'
     'of height. It includes the effect of ground clutter and gas attenuation\n'
     'but not liquid attenuation.'),

    'Z_error':
    ('This variable is an estimate of the one-standard-deviation\n'
     'random error in radar reflectivity factor. It originates\n'
     'from the following independent sources of error:\n'
     '1) Precision in reflectivity estimate due to finite signal to noise\n'
     '   and finite number of pulses\n'
     '2) 10% uncertainty in gaseous attenuation correction (mainly due to\n'
     '   error in model humidity field)\n'
     '3) Error in liquid water path (given by the variable lwp_error) and\n'
     '   its partitioning with height).'),

    'Z':
    ('This variable has been corrected for attenuation by gaseous\n'
     'attenuation (using the thermodynamic variables from a forecast\n'
     'model; see the radar_gas_atten variable) and liquid attenuation\n'
     '(using liquid water path from a microwave radiometer; see the\n'
     'radar_liquid_atten variable) but rain and melting-layer attenuation\n'
     'has not been corrected. Calibration convention: in the absence of\n'
     'attenuation, a cloud at 273 K containing one million 100-micron droplets\n'
     'per cubic metre will have a reflectivity of 0 dBZ at all frequencies.'),

    'bias':
    'This variable is an estimate of the one-standard-deviation calibration error.',

    'ldr':
    'This parameter is the ratio of cross-polar to co-polar reflectivity.',

    'width':
    ('This parameter is the standard deviation of the reflectivity-weighted\n'
     'velocities in the radar pulse volume.'),

    'v':
    ('This parameter is the radial component of the velocity, with positive\n'
     'velocities are away from the radar.'),

}

ATTRIBUTES = {
    'time': MetaData(
        'Time UTC',
        'decimal hours since midnight'
    ),
    'model_time': MetaData(
        'model time UTC',
        'decimal hours since midnight'
    ),
    'height': MetaData(
        'Height above mean sea level',
        'm'
    ),
    'model_height': MetaData(
        'Height of model variables above mean sea level',
        'm'
    ),
    'range': MetaData(
        'Height above ground',
        'm'
    ),
    'latitude': MetaData(
        'Latitude of site',
        'degrees_north'
    ),
    'longitude': MetaData(
        'Longitude of site',
        'degrees_north'
    ),
    'altitude': MetaData(
        'Altitude of site',
        'm'
    ),
    'radar_frequency': MetaData(
        'Radar transmit frequency',
        'GHz'
    ),
    'lidar_wavelength': MetaData(
        'Laser wavelength',
        'nm'
    ),
    'ldr': MetaData(
        'Linear depolarisation ratio',
        'dB',
        (-30, 0),
        _LIN,
        comment=_COMMENTS['ldr']
    ),
    'width': MetaData(
        'Spectral width',
        'm s-1',
        (0, 3),
        _LOG,
        comment=_COMMENTS['width']
    ),
    'v': MetaData(
        'Doppler velocity',
        'm s-1',
        (-4, 2),
        _LIN,
        comment=_COMMENTS['v'],
        positive='up',
    ),
    'SNR': MetaData(
        'Signal-to-noise ratio',
        'dB',
        (-20, 60),
        _LIN
    ),
    'Z': MetaData(
        'Radar reflectivity factor',
        'dBZ',
        (-40, 20),
        _LIN,
        comment=_COMMENTS['Z'],
        ancillary_variables='Z_error Z_bias Z_sensitivity'
    ),
    'Z_error': MetaData(
        'Error in radar reflectivity factor',
        'dB',
        comment=_COMMENTS['Z_error']
    ),
    'Z_bias': MetaData(
        'Bias in radar reflectivity factor',
        'dB',
        comment=_COMMENTS['bias']
    ),
    'Z_sensitivity': MetaData(
        'Minimum detectable radar reflectivity',
        'dBZ',
        comment=_COMMENTS['Z_sensitivity']
    ),
    'Zh': MetaData(
        'Radar reflectivity factor (uncorrected), horizontal polarization',
        'dBZ',
        (-40, 20),
        _LIN
    ),
    'radar_liquid_atten': MetaData(
        'Approximate two-way radar attenuation due to liquid water',
        'dB',
        (0, 10),
        _LIN,
        comment=_COMMENTS['radar_liquid_atten']
    ),
    'radar_gas_atten': MetaData(
        'Two-way radar attenuation due to atmospheric gases',
        'dB',
        (0, 4),
        _LIN,
        comment=_COMMENTS['radar_gas_atten']
    ),
    'Tw': MetaData(
        'Wet-bulb temperature',
        'K',
        (200, 300),
        _LIN,
        comment=_COMMENTS['Tw']
    ),
    'vwind': MetaData(
        'Meridional wind',
        'm s-1',        
        (-50, 50),
        _LIN
    ),
    'uwind': MetaData(
        'Zonal wind',
        'm s-1',
        (-50, 50),
        _LIN
    ),
    'q': MetaData(
        'Specific humidity',
        '',
        (0, 0.2),
        _LIN
    ),
    'temperature': MetaData(
        'Temperature',
        'K',
        (200, 300),
        _LIN
    ),
    'pressure': MetaData(
        'Pressure',
        'Pa',
        (0, 110000),
        _LIN
    ),
    'beta': MetaData(
        'Attenuated backscatter coefficient',
        'sr-1 m-1',
        (1e-7, 1e-4),
        _LOG,
        ancillary_variables='beta_error beta_bias'
    ),
    'beta_raw': MetaData(
        'Raw attenuated backscatter coefficient',
        'sr-1 m-1',
        (1e-7, 1e-4),
        _LOG,
    ),
    'beta_error': MetaData(
        'Error in attenuated backscatter coefficient',
        'dB',
    ),
    'beta_bias': MetaData(
        'Bias in attenuated backscatter coefficient',
        'dB',
    ),
    'lwp': MetaData(
        'Liquid water path',
        'g m-2',
        (-100, 1000),
        _LIN
    ),
    'lwp_error': MetaData(
        'Error in liquid water path',
        'g m-2',
    ),
    'category_bits': MetaData(
        'Target categorization bits',
        comment=_COMMENTS['category_bits'],
        definition=_DEFINITIONS['category_bits']
    ),
    'quality_bits': MetaData(
        'Data quality bits',
        comment=_COMMENTS['quality_bits'],
        definition=_DEFINITIONS['quality_bits']
    ),
    'insect_prob': MetaData(
        'Insect probability',
        '',
        (0, 1),
        _LIN
    ),
    # RPG variables:
    'Ze': MetaData(
        'Radar reflectivity factor (uncorrected), vertical polarization',
        'dBZ',
        (-40, 20),
        _LIN
    ),
    'rain_rate': MetaData(
        'Rain rate',
        'mm h-1',
    ),
    'input_voltage_range': MetaData(
        'ADC input voltage range (+/-)',
        'mV',
    ),
    'noise_threshold': MetaData(
        'Noise filter threshold factor',
        '',
        comment='Multiple of the standard deviation of Doppler spectra.'
    ),
    'antenna_separation': MetaData(
        'Antenna separation',
        'm',
    ),
    'antenna_diameter': MetaData(
        'Antenna diameter',
        'm',
    ),
    'antenna_gain': MetaData(
        'Antenna gain',
        'dB',
    ),
    'range_resolution': MetaData(
        'Vertical resolution of range',
        'm',
    ),
    'half_power_beam_width': MetaData(
        'Half power beam width',
        'degrees',
    ),
    'transmitter_temperature': MetaData(
        'Transmitter temperature',
        'K',
    ),
    'pc_temperature': MetaData(
        'PC temperature',
        'K',
    ),
    'receiver_temperature': MetaData(
        'Receiver temperature',
        'K',
    ),
    'transmitted_power': MetaData(
        'Transmitted power',
        'W',
    ),
    'number_of_spectral_samples': MetaData(
        'Number of spectral samples in each chirp sequence',
        '',
    ),
    'skewness': MetaData(
        'Skewness of spectra',
        '',
    ),
    'kurtosis': MetaData(
        'Kurtosis of spectra',
    ),
    'azimuth': MetaData(
        'Azimuth angle of the instrument',
        'degrees',
    ),
    'elevation': MetaData(
        'Elevation above horizon',
        'degrees',
    ),
    'if_power': MetaData(
        'IF power',
        'uW',
    ),
    'brightness_temperature': MetaData(
        'Brightness temperature',
        'K',
    ),
    'voltage': MetaData(
        'Voltage',
        'V',
    ),
    'wind_direction': MetaData(
        'Wind direction',
        'degrees',
    ),
    'wind_speed': MetaData(
        'Wind speed',
        'm s-1',
    ),
    'time_ms': MetaData(
        'Time ms',
        'ms',
    ),
    'integration_time': MetaData(
        'Integration time',
        's',
        comment='Effective integration time of chirp sequence',
    ),
    'file_code': MetaData(
        'File code',
        comment='Indicates the RPG software version.',
    ),
    'program_number': MetaData(
        'Program number',
    ),
    'model_number': MetaData(
        'Model number',
        definition=_DEFINITIONS['model_number']
    ),
    'sample_duration': MetaData(
        'Sample duration',
        's'
    ),
    'dual_polarization': MetaData(
        'Dual polarisation type',
        definition=_DEFINITIONS['dual_polarization']
    ),
    'number_of_averaged_chirps': MetaData(
        'Number of averaged chirps in sequence'
    ),
    'chirp_start_indices': MetaData(
        'Chirp sequences start indices'
    ),
    'calibration_interval': MetaData(
        'Calibration interval in samples'
    ),
    'status_flag': MetaData(
        'Status flag for heater and blower'
    ),
    'FFT_window': MetaData(
        'FFT window type',
        definition=_DEFINITIONS['FFT_window']
    ),
    'quality_flag': MetaData(
        'Quality flag',
        definition=_DEFINITIONS['quality_flag']
    ),
    'nyquist_velocity': MetaData(
        'Nyquist velocity',
        'm s-1'
    ),
    'correlation_coefficient': MetaData(
        'Correlation coefficient',
        ''
    ),
    'Zdr': MetaData(
        'Differential reflectivity',
        'dB'
    ),
    'spectral_differential_phase': MetaData(
        'Spectral differential phase',
        ''
    ),

}
