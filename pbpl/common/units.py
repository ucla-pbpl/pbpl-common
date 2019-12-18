from math import pi

__all__ = [
    'meter', 'kg', 'sec', 'amp', 'kelvin', 'mol',
    'hertz', 'coulomb', 'joule', 'newton', 'tesla', 'volt',
    'pascal', 'farad', 'henry', 'ohm', 'watt',
    'cm', 'mm', 'um', 'nm', 'pm', 'fm',
    'gram',
    'ms', 'us', 'ns', 'ps', 'fs',
    'kHz', 'MHz', 'GHz', 'THz',
    'mK',
    'mC', 'uC', 'nC', 'pC', 'fC',
    'kV', 'MV', 'GV', 'TV',
    'GJ', 'MJ', 'kJ', 'mJ', 'uJ', 'nJ', 'pJ',
    'GOhm', 'MOhm', 'kOhm', 'mOhm', 'uOhm', 'nOhm', 'pOhm', 'fOhm',
    'mF', 'uF', 'nF', 'pF', 'fF',
    'uH', 'nH', 'pH',
    'rad', 'sr', 'mrad', 'urad', 'deg', 'pi', 'twopi', 'fourpi',
    'NA', 'R_gas', 'Torr','atm', 'bar', 'c_light', 'c2',
    'eplus', 'eps0', 'hbar', 'kB', 'm_amu', 'mbar',
    'me', 'mu0', 'planck', 're', 'a0', 'alpha0',
    'eV', 'keV', 'MeV', 'GeV', 'TeV' ]

def define_constants(internal_units):
    global meter, kg, sec, amp, kelvin, mol
    global hertz, coulomb, joule, newton, tesla, volt
    global pascal, farad, henry, ohm, watt
    global cm, mm, um, nm, nm, pm, fm
    global gram
    global ms, us, ns, ps, fs
    global kHz, MHz, GHz, THz
    global mK
    global mC, uC, nC, pC, fC
    global kV, MV, GV, TV
    global GJ, MJ, kJ, mJ, uJ, nJ, pJ
    global GOhm, MOhm, kOhm, mOhm, uOhm, nOhm, pOhm, fOhm
    global mF, uF, nF, pF, fF
    global uH, nH, pH
    global rad, sr, mrad, urad, deg, twopi, fourpi
    global NA, R_gas, Torr, atm, bar, c_light, c2
    global eplus, eps0, hbar, kB, m_amu, mbar
    global me, mu0, planck, re, a0, alpha0
    global eV, keV, MeV, GeV, TeV

    if internal_units == 'SI':
        meter = 1.0
        kg = 1.0
        sec = 1.0
        amp = 1.0
        kelvin = 1.0
        mol = 1.0

    elif internal_units == 'Hartree':
        meter = 1.0/(5.291772192e-11)
        kg = 1.0/(9.10938215e-31)
        sec = 1.0/(2.418884326505e-17)
        amp = (1.0/1.602176565e-19)/sec
        kelvin = 1.0/3.1577464e5
        mol = 1.0

    elif internal_units == 'MEEP':
        # Meep internal units
        c_light = 1.0
        eps0 = 1.0
        mu0 = 1.0
        mol = 1.0
        meter = 1.0
        amp = 1.0

        # the rest is determined self-consistently
        sec = (299792458.0 * meter) / c_light
        henry = mu0 * meter / (4 * pi * 1e-7)
        volt = henry * amp / sec
        kg = volt * sec**3 * amp / meter**2
        kelvin = 1.3806488e-23 * (meter/sec)**2 * kg

    else:
        raise Exception("Illegal value for 'internal_units'")

    # derived units solely expressed in terms of base units
    hertz = 1/sec
    coulomb = amp*sec
    joule = kg*(meter/sec)**2
    newton = kg*meter/sec**2
    tesla = kg/(sec**2*amp)
    volt = kg*meter**2/(sec**3*amp)

    # derived units depending on other base units
    pascal = newton/meter**2
    farad = coulomb/volt
    henry = volt*sec/amp
    ohm = volt/amp
    watt = joule/sec

    # metric prefixes
    cm = 1e-2*meter
    mm = 1e-3*meter
    um = 1e-6*meter
    nm = 1e-9*meter
    pm = 1e-12*meter
    fm = 1e-15*meter
    gram = 1e-3*kg
    ms = 1e-3*sec
    us = 1e-6*sec
    ns = 1e-9*sec
    ps = 1e-12*sec
    fs = 1e-15*sec
    kHz = 1e3*hertz
    MHz = 1e6*hertz
    GHz = 1e9*hertz
    THz = 1e12*hertz
    mK = 1e-3*kelvin
    mC = 1e-3*coulomb
    uC = 1e-6*coulomb
    nC = 1e-9*coulomb
    pC = 1e-12*coulomb
    fC = 1e-15*coulomb
    kV = 1e3*volt
    MV = 1e6*volt
    GV = 1e9*volt
    TV = 1e12*volt
    GJ = 1e9*joule
    MJ = 1e6*joule
    kJ = 1e3*joule
    mJ = 1e-3*joule
    uJ = 1e-6*joule
    nJ = 1e-9*joule
    pJ = 1e-12*joule
    GOhm = 1e9*ohm
    MOhm = 1e6*ohm
    kOhm = 1e3*ohm
    mOhm = 1e-3*ohm
    uOhm = 1e-6*ohm
    nOhm = 1e-9*ohm
    pOhm = 1e-12*ohm
    fOhm = 1e-15*ohm
    mF = 1e-3*farad
    uF = 1e-6*farad
    nF = 1e-9*farad
    pF = 1e-12*farad
    fF = 1e-15*farad
    uH = 1e-6*henry
    nH = 1e-9*henry
    pH = 1e-12*henry

    # geometric constants
    rad = 1.0
    sr = 1.0
    mrad = 1e-3
    urad = 1e-6
    deg = pi/180
    twopi = 2*pi
    fourpi = 4*pi

    # physical constants
    NA = 6.0221415e23
    R_gas = 8.3144621 * joule / (kelvin * mol)
    Torr = 133.3224*pascal
    atm = 101325.0*pascal
    bar = 1e5*pascal
    c_light = 299792458.0*meter/sec
    c2 = c_light**2

    eplus = 1.602176565e-19*coulomb
    eps0 = 8.854187817e-12*coulomb/(volt*meter)
    hbar = 1.054571725e-34*joule*sec
    kB = 1.3806488e-23 * (meter/sec)**2 * kg / kelvin
    m_amu = 1.660538921e-27*kg
    mbar = 1e-3*bar
    me = 9.10938215e-31*kg
    mu0 = 4*pi*1e-7*henry/meter
    planck = hbar*2*pi
    re = (eplus**2/(me*c_light**2))/(4*pi*eps0)
    a0 = hbar**2/(me*eplus**2)
    alpha0 = (1/(4*pi*eps0))*(eplus**2/(hbar*c_light))

    eV = eplus*volt
    keV = 1e3*eV
    MeV = 1e6*eV
    GeV = 1e9*eV
    TeV = 1e12*eV

define_constants('SI')
