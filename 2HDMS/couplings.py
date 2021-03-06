# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 11.3.0 for Mac OS X x86 (64-bit) (March 7, 2018)
# Date: Thu 30 May 2019 11:32:35


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-G',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = '-(cb*complex(0,1)*I1a11)',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '-(cb*complex(0,1)*I1a22)',
                 order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-(cb*complex(0,1)*I1a33)',
                 order = {'QED':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'cb*complex(0,1)*I2a11',
                 order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = 'cb*complex(0,1)*I2a22',
                 order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = 'cb*complex(0,1)*I2a33',
                 order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = 'cb*complex(0,1)*I3a11',
                 order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = 'cb*complex(0,1)*I3a22',
                 order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = 'cb*complex(0,1)*I3a33',
                 order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '-(cb*complex(0,1)*I4a11)',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '-(cb*complex(0,1)*I4a22)',
                 order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '-(cb*complex(0,1)*I4a33)',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '-3*complex(0,1)*lam1*RA1x1**4 - 6*complex(0,1)*lam3*RA1x1**2*RA1x2**2 - 6*complex(0,1)*lam4*RA1x1**2*RA1x2**2 - 6*complex(0,1)*lam5*RA1x1**2*RA1x2**2 - 3*complex(0,1)*lam2*RA1x2**4 - 6*complex(0,1)*lam7*RA1x1**2*RA1x3**2 - 6*complex(0,1)*lam8*RA1x2**2*RA1x3**2 - 3*complex(0,1)*lam6*RA1x3**4',
                 order = {'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '-3*complex(0,1)*lam1*RA1x1**3*RA2x1 - 3*complex(0,1)*lam3*RA1x1*RA1x2**2*RA2x1 - 3*complex(0,1)*lam4*RA1x1*RA1x2**2*RA2x1 - 3*complex(0,1)*lam5*RA1x1*RA1x2**2*RA2x1 - 3*complex(0,1)*lam7*RA1x1*RA1x3**2*RA2x1 - 3*complex(0,1)*lam3*RA1x1**2*RA1x2*RA2x2 - 3*complex(0,1)*lam4*RA1x1**2*RA1x2*RA2x2 - 3*complex(0,1)*lam5*RA1x1**2*RA1x2*RA2x2 - 3*complex(0,1)*lam2*RA1x2**3*RA2x2 - 3*complex(0,1)*lam8*RA1x2*RA1x3**2*RA2x2 - 3*complex(0,1)*lam7*RA1x1**2*RA1x3*RA2x3 - 3*complex(0,1)*lam8*RA1x2**2*RA1x3*RA2x3 - 3*complex(0,1)*lam6*RA1x3**3*RA2x3',
                 order = {'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '-3*complex(0,1)*lam1*RA1x1**2*RA2x1**2 - complex(0,1)*lam3*RA1x2**2*RA2x1**2 - complex(0,1)*lam4*RA1x2**2*RA2x1**2 - complex(0,1)*lam5*RA1x2**2*RA2x1**2 - complex(0,1)*lam7*RA1x3**2*RA2x1**2 - 4*complex(0,1)*lam3*RA1x1*RA1x2*RA2x1*RA2x2 - 4*complex(0,1)*lam4*RA1x1*RA1x2*RA2x1*RA2x2 - 4*complex(0,1)*lam5*RA1x1*RA1x2*RA2x1*RA2x2 - complex(0,1)*lam3*RA1x1**2*RA2x2**2 - complex(0,1)*lam4*RA1x1**2*RA2x2**2 - complex(0,1)*lam5*RA1x1**2*RA2x2**2 - 3*complex(0,1)*lam2*RA1x2**2*RA2x2**2 - complex(0,1)*lam8*RA1x3**2*RA2x2**2 - 4*complex(0,1)*lam7*RA1x1*RA1x3*RA2x1*RA2x3 - 4*complex(0,1)*lam8*RA1x2*RA1x3*RA2x2*RA2x3 - complex(0,1)*lam7*RA1x1**2*RA2x3**2 - complex(0,1)*lam8*RA1x2**2*RA2x3**2 - 3*complex(0,1)*lam6*RA1x3**2*RA2x3**2',
                 order = {'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '-3*complex(0,1)*lam1*RA1x1*RA2x1**3 - 3*complex(0,1)*lam3*RA1x2*RA2x1**2*RA2x2 - 3*complex(0,1)*lam4*RA1x2*RA2x1**2*RA2x2 - 3*complex(0,1)*lam5*RA1x2*RA2x1**2*RA2x2 - 3*complex(0,1)*lam3*RA1x1*RA2x1*RA2x2**2 - 3*complex(0,1)*lam4*RA1x1*RA2x1*RA2x2**2 - 3*complex(0,1)*lam5*RA1x1*RA2x1*RA2x2**2 - 3*complex(0,1)*lam2*RA1x2*RA2x2**3 - 3*complex(0,1)*lam7*RA1x3*RA2x1**2*RA2x3 - 3*complex(0,1)*lam8*RA1x3*RA2x2**2*RA2x3 - 3*complex(0,1)*lam7*RA1x1*RA2x1*RA2x3**2 - 3*complex(0,1)*lam8*RA1x2*RA2x2*RA2x3**2 - 3*complex(0,1)*lam6*RA1x3*RA2x3**3',
                 order = {'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '-3*complex(0,1)*lam1*RA2x1**4 - 6*complex(0,1)*lam3*RA2x1**2*RA2x2**2 - 6*complex(0,1)*lam4*RA2x1**2*RA2x2**2 - 6*complex(0,1)*lam5*RA2x1**2*RA2x2**2 - 3*complex(0,1)*lam2*RA2x2**4 - 6*complex(0,1)*lam7*RA2x1**2*RA2x3**2 - 6*complex(0,1)*lam8*RA2x2**2*RA2x3**2 - 3*complex(0,1)*lam6*RA2x3**4',
                 order = {'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '-3*complex(0,1)*lam1*RA1x1**3*RA3x1 - 3*complex(0,1)*lam3*RA1x1*RA1x2**2*RA3x1 - 3*complex(0,1)*lam4*RA1x1*RA1x2**2*RA3x1 - 3*complex(0,1)*lam5*RA1x1*RA1x2**2*RA3x1 - 3*complex(0,1)*lam7*RA1x1*RA1x3**2*RA3x1 - 3*complex(0,1)*lam3*RA1x1**2*RA1x2*RA3x2 - 3*complex(0,1)*lam4*RA1x1**2*RA1x2*RA3x2 - 3*complex(0,1)*lam5*RA1x1**2*RA1x2*RA3x2 - 3*complex(0,1)*lam2*RA1x2**3*RA3x2 - 3*complex(0,1)*lam8*RA1x2*RA1x3**2*RA3x2 - 3*complex(0,1)*lam7*RA1x1**2*RA1x3*RA3x3 - 3*complex(0,1)*lam8*RA1x2**2*RA1x3*RA3x3 - 3*complex(0,1)*lam6*RA1x3**3*RA3x3',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '-3*complex(0,1)*lam1*RA1x1**2*RA2x1*RA3x1 - complex(0,1)*lam3*RA1x2**2*RA2x1*RA3x1 - complex(0,1)*lam4*RA1x2**2*RA2x1*RA3x1 - complex(0,1)*lam5*RA1x2**2*RA2x1*RA3x1 - complex(0,1)*lam7*RA1x3**2*RA2x1*RA3x1 - 2*complex(0,1)*lam3*RA1x1*RA1x2*RA2x2*RA3x1 - 2*complex(0,1)*lam4*RA1x1*RA1x2*RA2x2*RA3x1 - 2*complex(0,1)*lam5*RA1x1*RA1x2*RA2x2*RA3x1 - 2*complex(0,1)*lam7*RA1x1*RA1x3*RA2x3*RA3x1 - 2*complex(0,1)*lam3*RA1x1*RA1x2*RA2x1*RA3x2 - 2*complex(0,1)*lam4*RA1x1*RA1x2*RA2x1*RA3x2 - 2*complex(0,1)*lam5*RA1x1*RA1x2*RA2x1*RA3x2 - complex(0,1)*lam3*RA1x1**2*RA2x2*RA3x2 - complex(0,1)*lam4*RA1x1**2*RA2x2*RA3x2 - complex(0,1)*lam5*RA1x1**2*RA2x2*RA3x2 - 3*complex(0,1)*lam2*RA1x2**2*RA2x2*RA3x2 - complex(0,1)*lam8*RA1x3**2*RA2x2*RA3x2 - 2*complex(0,1)*lam8*RA1x2*RA1x3*RA2x3*RA3x2 - 2*complex(0,1)*lam7*RA1x1*RA1x3*RA2x1*RA3x3 - 2*complex(0,1)*lam8*RA1x2*RA1x3*RA2x2*RA3x3 - complex(0,1)*lam7*RA1x1**2*RA2x3*RA3x3 - complex(0,1)*lam8*RA1x2**2*RA2x3*RA3x3 - 3*complex(0,1)*lam6*RA1x3**2*RA2x3*RA3x3',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '-3*complex(0,1)*lam1*RA1x1*RA2x1**2*RA3x1 - 2*complex(0,1)*lam3*RA1x2*RA2x1*RA2x2*RA3x1 - 2*complex(0,1)*lam4*RA1x2*RA2x1*RA2x2*RA3x1 - 2*complex(0,1)*lam5*RA1x2*RA2x1*RA2x2*RA3x1 - complex(0,1)*lam3*RA1x1*RA2x2**2*RA3x1 - complex(0,1)*lam4*RA1x1*RA2x2**2*RA3x1 - complex(0,1)*lam5*RA1x1*RA2x2**2*RA3x1 - 2*complex(0,1)*lam7*RA1x3*RA2x1*RA2x3*RA3x1 - complex(0,1)*lam7*RA1x1*RA2x3**2*RA3x1 - complex(0,1)*lam3*RA1x2*RA2x1**2*RA3x2 - complex(0,1)*lam4*RA1x2*RA2x1**2*RA3x2 - complex(0,1)*lam5*RA1x2*RA2x1**2*RA3x2 - 2*complex(0,1)*lam3*RA1x1*RA2x1*RA2x2*RA3x2 - 2*complex(0,1)*lam4*RA1x1*RA2x1*RA2x2*RA3x2 - 2*complex(0,1)*lam5*RA1x1*RA2x1*RA2x2*RA3x2 - 3*complex(0,1)*lam2*RA1x2*RA2x2**2*RA3x2 - 2*complex(0,1)*lam8*RA1x3*RA2x2*RA2x3*RA3x2 - complex(0,1)*lam8*RA1x2*RA2x3**2*RA3x2 - complex(0,1)*lam7*RA1x3*RA2x1**2*RA3x3 - complex(0,1)*lam8*RA1x3*RA2x2**2*RA3x3 - 2*complex(0,1)*lam7*RA1x1*RA2x1*RA2x3*RA3x3 - 2*complex(0,1)*lam8*RA1x2*RA2x2*RA2x3*RA3x3 - 3*complex(0,1)*lam6*RA1x3*RA2x3**2*RA3x3',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '-3*complex(0,1)*lam1*RA2x1**3*RA3x1 - 3*complex(0,1)*lam3*RA2x1*RA2x2**2*RA3x1 - 3*complex(0,1)*lam4*RA2x1*RA2x2**2*RA3x1 - 3*complex(0,1)*lam5*RA2x1*RA2x2**2*RA3x1 - 3*complex(0,1)*lam7*RA2x1*RA2x3**2*RA3x1 - 3*complex(0,1)*lam3*RA2x1**2*RA2x2*RA3x2 - 3*complex(0,1)*lam4*RA2x1**2*RA2x2*RA3x2 - 3*complex(0,1)*lam5*RA2x1**2*RA2x2*RA3x2 - 3*complex(0,1)*lam2*RA2x2**3*RA3x2 - 3*complex(0,1)*lam8*RA2x2*RA2x3**2*RA3x2 - 3*complex(0,1)*lam7*RA2x1**2*RA2x3*RA3x3 - 3*complex(0,1)*lam8*RA2x2**2*RA2x3*RA3x3 - 3*complex(0,1)*lam6*RA2x3**3*RA3x3',
                 order = {'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '-3*complex(0,1)*lam1*RA1x1**2*RA3x1**2 - complex(0,1)*lam3*RA1x2**2*RA3x1**2 - complex(0,1)*lam4*RA1x2**2*RA3x1**2 - complex(0,1)*lam5*RA1x2**2*RA3x1**2 - complex(0,1)*lam7*RA1x3**2*RA3x1**2 - 4*complex(0,1)*lam3*RA1x1*RA1x2*RA3x1*RA3x2 - 4*complex(0,1)*lam4*RA1x1*RA1x2*RA3x1*RA3x2 - 4*complex(0,1)*lam5*RA1x1*RA1x2*RA3x1*RA3x2 - complex(0,1)*lam3*RA1x1**2*RA3x2**2 - complex(0,1)*lam4*RA1x1**2*RA3x2**2 - complex(0,1)*lam5*RA1x1**2*RA3x2**2 - 3*complex(0,1)*lam2*RA1x2**2*RA3x2**2 - complex(0,1)*lam8*RA1x3**2*RA3x2**2 - 4*complex(0,1)*lam7*RA1x1*RA1x3*RA3x1*RA3x3 - 4*complex(0,1)*lam8*RA1x2*RA1x3*RA3x2*RA3x3 - complex(0,1)*lam7*RA1x1**2*RA3x3**2 - complex(0,1)*lam8*RA1x2**2*RA3x3**2 - 3*complex(0,1)*lam6*RA1x3**2*RA3x3**2',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '-3*complex(0,1)*lam1*RA1x1*RA2x1*RA3x1**2 - complex(0,1)*lam3*RA1x2*RA2x2*RA3x1**2 - complex(0,1)*lam4*RA1x2*RA2x2*RA3x1**2 - complex(0,1)*lam5*RA1x2*RA2x2*RA3x1**2 - complex(0,1)*lam7*RA1x3*RA2x3*RA3x1**2 - 2*complex(0,1)*lam3*RA1x2*RA2x1*RA3x1*RA3x2 - 2*complex(0,1)*lam4*RA1x2*RA2x1*RA3x1*RA3x2 - 2*complex(0,1)*lam5*RA1x2*RA2x1*RA3x1*RA3x2 - 2*complex(0,1)*lam3*RA1x1*RA2x2*RA3x1*RA3x2 - 2*complex(0,1)*lam4*RA1x1*RA2x2*RA3x1*RA3x2 - 2*complex(0,1)*lam5*RA1x1*RA2x2*RA3x1*RA3x2 - complex(0,1)*lam3*RA1x1*RA2x1*RA3x2**2 - complex(0,1)*lam4*RA1x1*RA2x1*RA3x2**2 - complex(0,1)*lam5*RA1x1*RA2x1*RA3x2**2 - 3*complex(0,1)*lam2*RA1x2*RA2x2*RA3x2**2 - complex(0,1)*lam8*RA1x3*RA2x3*RA3x2**2 - 2*complex(0,1)*lam7*RA1x3*RA2x1*RA3x1*RA3x3 - 2*complex(0,1)*lam7*RA1x1*RA2x3*RA3x1*RA3x3 - 2*complex(0,1)*lam8*RA1x3*RA2x2*RA3x2*RA3x3 - 2*complex(0,1)*lam8*RA1x2*RA2x3*RA3x2*RA3x3 - complex(0,1)*lam7*RA1x1*RA2x1*RA3x3**2 - complex(0,1)*lam8*RA1x2*RA2x2*RA3x3**2 - 3*complex(0,1)*lam6*RA1x3*RA2x3*RA3x3**2',
                 order = {'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '-3*complex(0,1)*lam1*RA2x1**2*RA3x1**2 - complex(0,1)*lam3*RA2x2**2*RA3x1**2 - complex(0,1)*lam4*RA2x2**2*RA3x1**2 - complex(0,1)*lam5*RA2x2**2*RA3x1**2 - complex(0,1)*lam7*RA2x3**2*RA3x1**2 - 4*complex(0,1)*lam3*RA2x1*RA2x2*RA3x1*RA3x2 - 4*complex(0,1)*lam4*RA2x1*RA2x2*RA3x1*RA3x2 - 4*complex(0,1)*lam5*RA2x1*RA2x2*RA3x1*RA3x2 - complex(0,1)*lam3*RA2x1**2*RA3x2**2 - complex(0,1)*lam4*RA2x1**2*RA3x2**2 - complex(0,1)*lam5*RA2x1**2*RA3x2**2 - 3*complex(0,1)*lam2*RA2x2**2*RA3x2**2 - complex(0,1)*lam8*RA2x3**2*RA3x2**2 - 4*complex(0,1)*lam7*RA2x1*RA2x3*RA3x1*RA3x3 - 4*complex(0,1)*lam8*RA2x2*RA2x3*RA3x2*RA3x3 - complex(0,1)*lam7*RA2x1**2*RA3x3**2 - complex(0,1)*lam8*RA2x2**2*RA3x3**2 - 3*complex(0,1)*lam6*RA2x3**2*RA3x3**2',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '-3*complex(0,1)*lam1*RA1x1*RA3x1**3 - 3*complex(0,1)*lam3*RA1x2*RA3x1**2*RA3x2 - 3*complex(0,1)*lam4*RA1x2*RA3x1**2*RA3x2 - 3*complex(0,1)*lam5*RA1x2*RA3x1**2*RA3x2 - 3*complex(0,1)*lam3*RA1x1*RA3x1*RA3x2**2 - 3*complex(0,1)*lam4*RA1x1*RA3x1*RA3x2**2 - 3*complex(0,1)*lam5*RA1x1*RA3x1*RA3x2**2 - 3*complex(0,1)*lam2*RA1x2*RA3x2**3 - 3*complex(0,1)*lam7*RA1x3*RA3x1**2*RA3x3 - 3*complex(0,1)*lam8*RA1x3*RA3x2**2*RA3x3 - 3*complex(0,1)*lam7*RA1x1*RA3x1*RA3x3**2 - 3*complex(0,1)*lam8*RA1x2*RA3x2*RA3x3**2 - 3*complex(0,1)*lam6*RA1x3*RA3x3**3',
                 order = {'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '-3*complex(0,1)*lam1*RA2x1*RA3x1**3 - 3*complex(0,1)*lam3*RA2x2*RA3x1**2*RA3x2 - 3*complex(0,1)*lam4*RA2x2*RA3x1**2*RA3x2 - 3*complex(0,1)*lam5*RA2x2*RA3x1**2*RA3x2 - 3*complex(0,1)*lam3*RA2x1*RA3x1*RA3x2**2 - 3*complex(0,1)*lam4*RA2x1*RA3x1*RA3x2**2 - 3*complex(0,1)*lam5*RA2x1*RA3x1*RA3x2**2 - 3*complex(0,1)*lam2*RA2x2*RA3x2**3 - 3*complex(0,1)*lam7*RA2x3*RA3x1**2*RA3x3 - 3*complex(0,1)*lam8*RA2x3*RA3x2**2*RA3x3 - 3*complex(0,1)*lam7*RA2x1*RA3x1*RA3x3**2 - 3*complex(0,1)*lam8*RA2x2*RA3x2*RA3x3**2 - 3*complex(0,1)*lam6*RA2x3*RA3x3**3',
                 order = {'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '-3*complex(0,1)*lam1*RA3x1**4 - 6*complex(0,1)*lam3*RA3x1**2*RA3x2**2 - 6*complex(0,1)*lam4*RA3x1**2*RA3x2**2 - 6*complex(0,1)*lam5*RA3x1**2*RA3x2**2 - 3*complex(0,1)*lam2*RA3x2**4 - 6*complex(0,1)*lam7*RA3x1**2*RA3x3**2 - 6*complex(0,1)*lam8*RA3x2**2*RA3x3**2 - 3*complex(0,1)*lam6*RA3x3**4',
                 order = {'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '-(complex(0,1)*I1a11*sb)',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '-(complex(0,1)*I1a22*sb)',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '-(complex(0,1)*I1a33*sb)',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = 'complex(0,1)*I2a11*sb',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = 'complex(0,1)*I2a22*sb',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = 'complex(0,1)*I2a33*sb',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = 'complex(0,1)*I3a11*sb',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = 'complex(0,1)*I3a22*sb',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = 'complex(0,1)*I3a33*sb',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '-(complex(0,1)*I4a11*sb)',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-(complex(0,1)*I4a22*sb)',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-(complex(0,1)*I4a33*sb)',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-(cb*ee**2*complex(0,1)*RA1x2)/(2.*cw) + (ee**2*complex(0,1)*RA1x1*sb)/(2.*cw)',
                 order = {'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '-(cb*ee**2*complex(0,1)*RA1x1)/(2.*cw) - (ee**2*complex(0,1)*RA1x2*sb)/(2.*cw)',
                 order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '-(cb*ee**2*complex(0,1)*RA2x2)/(2.*cw) + (ee**2*complex(0,1)*RA2x1*sb)/(2.*cw)',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '-(cb*ee**2*complex(0,1)*RA2x1)/(2.*cw) - (ee**2*complex(0,1)*RA2x2*sb)/(2.*cw)',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '-(cb*ee**2*complex(0,1)*RA3x2)/(2.*cw) + (ee**2*complex(0,1)*RA3x1*sb)/(2.*cw)',
                 order = {'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '-(cb*ee**2*complex(0,1)*RA3x1)/(2.*cw) - (ee**2*complex(0,1)*RA3x2*sb)/(2.*cw)',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '-(cb**2*ee*complex(0,1)) - ee*complex(0,1)*sb**2',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '2*cb**2*ee**2*complex(0,1) + 2*ee**2*complex(0,1)*sb**2',
                 order = {'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '-(cb**2*ee**2)/(2.*cw) - (ee**2*sb**2)/(2.*cw)',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '(cb**2*ee**2)/(2.*cw) + (ee**2*sb**2)/(2.*cw)',
                 order = {'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '-(cb**2*complex(0,1)*lam4*RA1x1*RA1x2) - cb**2*complex(0,1)*lam5*RA1x1*RA1x2 + cb*complex(0,1)*lam1*RA1x1**2*sb - cb*complex(0,1)*lam3*RA1x1**2*sb - cb*complex(0,1)*lam2*RA1x2**2*sb + cb*complex(0,1)*lam3*RA1x2**2*sb + cb*complex(0,1)*lam7*RA1x3**2*sb - cb*complex(0,1)*lam8*RA1x3**2*sb + complex(0,1)*lam4*RA1x1*RA1x2*sb**2 + complex(0,1)*lam5*RA1x1*RA1x2*sb**2',
                 order = {'QED':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '-2*cb**2*complex(0,1)*lam5*RA1x1*RA1x2 + cb*complex(0,1)*lam1*RA1x1**2*sb - cb*complex(0,1)*lam3*RA1x1**2*sb - cb*complex(0,1)*lam4*RA1x1**2*sb + cb*complex(0,1)*lam5*RA1x1**2*sb - cb*complex(0,1)*lam2*RA1x2**2*sb + cb*complex(0,1)*lam3*RA1x2**2*sb + cb*complex(0,1)*lam4*RA1x2**2*sb - cb*complex(0,1)*lam5*RA1x2**2*sb + cb*complex(0,1)*lam7*RA1x3**2*sb - cb*complex(0,1)*lam8*RA1x3**2*sb + 2*complex(0,1)*lam5*RA1x1*RA1x2*sb**2',
                 order = {'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '-(cb**2*complex(0,1)*lam3*RA1x1**2) - cb**2*complex(0,1)*lam2*RA1x2**2 - cb**2*complex(0,1)*lam8*RA1x3**2 + 2*cb*complex(0,1)*lam4*RA1x1*RA1x2*sb + 2*cb*complex(0,1)*lam5*RA1x1*RA1x2*sb - complex(0,1)*lam1*RA1x1**2*sb**2 - complex(0,1)*lam3*RA1x2**2*sb**2 - complex(0,1)*lam7*RA1x3**2*sb**2',
                 order = {'QED':2})

GC_61 = Coupling(name = 'GC_61',
                 value = '-(cb**2*complex(0,1)*lam3*RA1x1**2) - cb**2*complex(0,1)*lam4*RA1x1**2 + cb**2*complex(0,1)*lam5*RA1x1**2 - cb**2*complex(0,1)*lam2*RA1x2**2 - cb**2*complex(0,1)*lam8*RA1x3**2 + 4*cb*complex(0,1)*lam5*RA1x1*RA1x2*sb - complex(0,1)*lam1*RA1x1**2*sb**2 - complex(0,1)*lam3*RA1x2**2*sb**2 - complex(0,1)*lam4*RA1x2**2*sb**2 + complex(0,1)*lam5*RA1x2**2*sb**2 - complex(0,1)*lam7*RA1x3**2*sb**2',
                 order = {'QED':2})

GC_62 = Coupling(name = 'GC_62',
                 value = '-(cb**2*complex(0,1)*lam1*RA1x1**2) - cb**2*complex(0,1)*lam3*RA1x2**2 - cb**2*complex(0,1)*lam7*RA1x3**2 - 2*cb*complex(0,1)*lam4*RA1x1*RA1x2*sb - 2*cb*complex(0,1)*lam5*RA1x1*RA1x2*sb - complex(0,1)*lam3*RA1x1**2*sb**2 - complex(0,1)*lam2*RA1x2**2*sb**2 - complex(0,1)*lam8*RA1x3**2*sb**2',
                 order = {'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '-(cb**2*complex(0,1)*lam1*RA1x1**2) - cb**2*complex(0,1)*lam3*RA1x2**2 - cb**2*complex(0,1)*lam4*RA1x2**2 + cb**2*complex(0,1)*lam5*RA1x2**2 - cb**2*complex(0,1)*lam7*RA1x3**2 - 4*cb*complex(0,1)*lam5*RA1x1*RA1x2*sb - complex(0,1)*lam3*RA1x1**2*sb**2 - complex(0,1)*lam4*RA1x1**2*sb**2 + complex(0,1)*lam5*RA1x1**2*sb**2 - complex(0,1)*lam2*RA1x2**2*sb**2 - complex(0,1)*lam8*RA1x3**2*sb**2',
                 order = {'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '-(cb**2*complex(0,1)*lam4*RA1x2*RA2x1)/2. - (cb**2*complex(0,1)*lam5*RA1x2*RA2x1)/2. - (cb**2*complex(0,1)*lam4*RA1x1*RA2x2)/2. - (cb**2*complex(0,1)*lam5*RA1x1*RA2x2)/2. + cb*complex(0,1)*lam1*RA1x1*RA2x1*sb - cb*complex(0,1)*lam3*RA1x1*RA2x1*sb - cb*complex(0,1)*lam2*RA1x2*RA2x2*sb + cb*complex(0,1)*lam3*RA1x2*RA2x2*sb + cb*complex(0,1)*lam7*RA1x3*RA2x3*sb - cb*complex(0,1)*lam8*RA1x3*RA2x3*sb + (complex(0,1)*lam4*RA1x2*RA2x1*sb**2)/2. + (complex(0,1)*lam5*RA1x2*RA2x1*sb**2)/2. + (complex(0,1)*lam4*RA1x1*RA2x2*sb**2)/2. + (complex(0,1)*lam5*RA1x1*RA2x2*sb**2)/2.',
                 order = {'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = '-(cb**2*complex(0,1)*lam5*RA1x2*RA2x1) - cb**2*complex(0,1)*lam5*RA1x1*RA2x2 + cb*complex(0,1)*lam1*RA1x1*RA2x1*sb - cb*complex(0,1)*lam3*RA1x1*RA2x1*sb - cb*complex(0,1)*lam4*RA1x1*RA2x1*sb + cb*complex(0,1)*lam5*RA1x1*RA2x1*sb - cb*complex(0,1)*lam2*RA1x2*RA2x2*sb + cb*complex(0,1)*lam3*RA1x2*RA2x2*sb + cb*complex(0,1)*lam4*RA1x2*RA2x2*sb - cb*complex(0,1)*lam5*RA1x2*RA2x2*sb + cb*complex(0,1)*lam7*RA1x3*RA2x3*sb - cb*complex(0,1)*lam8*RA1x3*RA2x3*sb + complex(0,1)*lam5*RA1x2*RA2x1*sb**2 + complex(0,1)*lam5*RA1x1*RA2x2*sb**2',
                 order = {'QED':2})

GC_66 = Coupling(name = 'GC_66',
                 value = '-(cb**2*complex(0,1)*lam4*RA2x1*RA2x2) - cb**2*complex(0,1)*lam5*RA2x1*RA2x2 + cb*complex(0,1)*lam1*RA2x1**2*sb - cb*complex(0,1)*lam3*RA2x1**2*sb - cb*complex(0,1)*lam2*RA2x2**2*sb + cb*complex(0,1)*lam3*RA2x2**2*sb + cb*complex(0,1)*lam7*RA2x3**2*sb - cb*complex(0,1)*lam8*RA2x3**2*sb + complex(0,1)*lam4*RA2x1*RA2x2*sb**2 + complex(0,1)*lam5*RA2x1*RA2x2*sb**2',
                 order = {'QED':2})

GC_67 = Coupling(name = 'GC_67',
                 value = '-2*cb**2*complex(0,1)*lam5*RA2x1*RA2x2 + cb*complex(0,1)*lam1*RA2x1**2*sb - cb*complex(0,1)*lam3*RA2x1**2*sb - cb*complex(0,1)*lam4*RA2x1**2*sb + cb*complex(0,1)*lam5*RA2x1**2*sb - cb*complex(0,1)*lam2*RA2x2**2*sb + cb*complex(0,1)*lam3*RA2x2**2*sb + cb*complex(0,1)*lam4*RA2x2**2*sb - cb*complex(0,1)*lam5*RA2x2**2*sb + cb*complex(0,1)*lam7*RA2x3**2*sb - cb*complex(0,1)*lam8*RA2x3**2*sb + 2*complex(0,1)*lam5*RA2x1*RA2x2*sb**2',
                 order = {'QED':2})

GC_68 = Coupling(name = 'GC_68',
                 value = '-(cb**2*complex(0,1)*lam3*RA1x1*RA2x1) - cb**2*complex(0,1)*lam2*RA1x2*RA2x2 - cb**2*complex(0,1)*lam8*RA1x3*RA2x3 + cb*complex(0,1)*lam4*RA1x2*RA2x1*sb + cb*complex(0,1)*lam5*RA1x2*RA2x1*sb + cb*complex(0,1)*lam4*RA1x1*RA2x2*sb + cb*complex(0,1)*lam5*RA1x1*RA2x2*sb - complex(0,1)*lam1*RA1x1*RA2x1*sb**2 - complex(0,1)*lam3*RA1x2*RA2x2*sb**2 - complex(0,1)*lam7*RA1x3*RA2x3*sb**2',
                 order = {'QED':2})

GC_69 = Coupling(name = 'GC_69',
                 value = '-(cb**2*complex(0,1)*lam3*RA1x1*RA2x1) - cb**2*complex(0,1)*lam4*RA1x1*RA2x1 + cb**2*complex(0,1)*lam5*RA1x1*RA2x1 - cb**2*complex(0,1)*lam2*RA1x2*RA2x2 - cb**2*complex(0,1)*lam8*RA1x3*RA2x3 + 2*cb*complex(0,1)*lam5*RA1x2*RA2x1*sb + 2*cb*complex(0,1)*lam5*RA1x1*RA2x2*sb - complex(0,1)*lam1*RA1x1*RA2x1*sb**2 - complex(0,1)*lam3*RA1x2*RA2x2*sb**2 - complex(0,1)*lam4*RA1x2*RA2x2*sb**2 + complex(0,1)*lam5*RA1x2*RA2x2*sb**2 - complex(0,1)*lam7*RA1x3*RA2x3*sb**2',
                 order = {'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '-(cb**2*complex(0,1)*lam1*RA1x1*RA2x1) - cb**2*complex(0,1)*lam3*RA1x2*RA2x2 - cb**2*complex(0,1)*lam7*RA1x3*RA2x3 - cb*complex(0,1)*lam4*RA1x2*RA2x1*sb - cb*complex(0,1)*lam5*RA1x2*RA2x1*sb - cb*complex(0,1)*lam4*RA1x1*RA2x2*sb - cb*complex(0,1)*lam5*RA1x1*RA2x2*sb - complex(0,1)*lam3*RA1x1*RA2x1*sb**2 - complex(0,1)*lam2*RA1x2*RA2x2*sb**2 - complex(0,1)*lam8*RA1x3*RA2x3*sb**2',
                 order = {'QED':2})

GC_71 = Coupling(name = 'GC_71',
                 value = '-(cb**2*complex(0,1)*lam1*RA1x1*RA2x1) - cb**2*complex(0,1)*lam3*RA1x2*RA2x2 - cb**2*complex(0,1)*lam4*RA1x2*RA2x2 + cb**2*complex(0,1)*lam5*RA1x2*RA2x2 - cb**2*complex(0,1)*lam7*RA1x3*RA2x3 - 2*cb*complex(0,1)*lam5*RA1x2*RA2x1*sb - 2*cb*complex(0,1)*lam5*RA1x1*RA2x2*sb - complex(0,1)*lam3*RA1x1*RA2x1*sb**2 - complex(0,1)*lam4*RA1x1*RA2x1*sb**2 + complex(0,1)*lam5*RA1x1*RA2x1*sb**2 - complex(0,1)*lam2*RA1x2*RA2x2*sb**2 - complex(0,1)*lam8*RA1x3*RA2x3*sb**2',
                 order = {'QED':2})

GC_72 = Coupling(name = 'GC_72',
                 value = '-(cb**2*complex(0,1)*lam3*RA2x1**2) - cb**2*complex(0,1)*lam2*RA2x2**2 - cb**2*complex(0,1)*lam8*RA2x3**2 + 2*cb*complex(0,1)*lam4*RA2x1*RA2x2*sb + 2*cb*complex(0,1)*lam5*RA2x1*RA2x2*sb - complex(0,1)*lam1*RA2x1**2*sb**2 - complex(0,1)*lam3*RA2x2**2*sb**2 - complex(0,1)*lam7*RA2x3**2*sb**2',
                 order = {'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '-(cb**2*complex(0,1)*lam3*RA2x1**2) - cb**2*complex(0,1)*lam4*RA2x1**2 + cb**2*complex(0,1)*lam5*RA2x1**2 - cb**2*complex(0,1)*lam2*RA2x2**2 - cb**2*complex(0,1)*lam8*RA2x3**2 + 4*cb*complex(0,1)*lam5*RA2x1*RA2x2*sb - complex(0,1)*lam1*RA2x1**2*sb**2 - complex(0,1)*lam3*RA2x2**2*sb**2 - complex(0,1)*lam4*RA2x2**2*sb**2 + complex(0,1)*lam5*RA2x2**2*sb**2 - complex(0,1)*lam7*RA2x3**2*sb**2',
                 order = {'QED':2})

GC_74 = Coupling(name = 'GC_74',
                 value = '-(cb**2*complex(0,1)*lam1*RA2x1**2) - cb**2*complex(0,1)*lam3*RA2x2**2 - cb**2*complex(0,1)*lam7*RA2x3**2 - 2*cb*complex(0,1)*lam4*RA2x1*RA2x2*sb - 2*cb*complex(0,1)*lam5*RA2x1*RA2x2*sb - complex(0,1)*lam3*RA2x1**2*sb**2 - complex(0,1)*lam2*RA2x2**2*sb**2 - complex(0,1)*lam8*RA2x3**2*sb**2',
                 order = {'QED':2})

GC_75 = Coupling(name = 'GC_75',
                 value = '-(cb**2*complex(0,1)*lam1*RA2x1**2) - cb**2*complex(0,1)*lam3*RA2x2**2 - cb**2*complex(0,1)*lam4*RA2x2**2 + cb**2*complex(0,1)*lam5*RA2x2**2 - cb**2*complex(0,1)*lam7*RA2x3**2 - 4*cb*complex(0,1)*lam5*RA2x1*RA2x2*sb - complex(0,1)*lam3*RA2x1**2*sb**2 - complex(0,1)*lam4*RA2x1**2*sb**2 + complex(0,1)*lam5*RA2x1**2*sb**2 - complex(0,1)*lam2*RA2x2**2*sb**2 - complex(0,1)*lam8*RA2x3**2*sb**2',
                 order = {'QED':2})

GC_76 = Coupling(name = 'GC_76',
                 value = '-(cb**2*complex(0,1)*lam4*RA1x2*RA3x1)/2. - (cb**2*complex(0,1)*lam5*RA1x2*RA3x1)/2. - (cb**2*complex(0,1)*lam4*RA1x1*RA3x2)/2. - (cb**2*complex(0,1)*lam5*RA1x1*RA3x2)/2. + cb*complex(0,1)*lam1*RA1x1*RA3x1*sb - cb*complex(0,1)*lam3*RA1x1*RA3x1*sb - cb*complex(0,1)*lam2*RA1x2*RA3x2*sb + cb*complex(0,1)*lam3*RA1x2*RA3x2*sb + cb*complex(0,1)*lam7*RA1x3*RA3x3*sb - cb*complex(0,1)*lam8*RA1x3*RA3x3*sb + (complex(0,1)*lam4*RA1x2*RA3x1*sb**2)/2. + (complex(0,1)*lam5*RA1x2*RA3x1*sb**2)/2. + (complex(0,1)*lam4*RA1x1*RA3x2*sb**2)/2. + (complex(0,1)*lam5*RA1x1*RA3x2*sb**2)/2.',
                 order = {'QED':2})

GC_77 = Coupling(name = 'GC_77',
                 value = '-(cb**2*complex(0,1)*lam5*RA1x2*RA3x1) - cb**2*complex(0,1)*lam5*RA1x1*RA3x2 + cb*complex(0,1)*lam1*RA1x1*RA3x1*sb - cb*complex(0,1)*lam3*RA1x1*RA3x1*sb - cb*complex(0,1)*lam4*RA1x1*RA3x1*sb + cb*complex(0,1)*lam5*RA1x1*RA3x1*sb - cb*complex(0,1)*lam2*RA1x2*RA3x2*sb + cb*complex(0,1)*lam3*RA1x2*RA3x2*sb + cb*complex(0,1)*lam4*RA1x2*RA3x2*sb - cb*complex(0,1)*lam5*RA1x2*RA3x2*sb + cb*complex(0,1)*lam7*RA1x3*RA3x3*sb - cb*complex(0,1)*lam8*RA1x3*RA3x3*sb + complex(0,1)*lam5*RA1x2*RA3x1*sb**2 + complex(0,1)*lam5*RA1x1*RA3x2*sb**2',
                 order = {'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '-(cb**2*complex(0,1)*lam4*RA2x2*RA3x1)/2. - (cb**2*complex(0,1)*lam5*RA2x2*RA3x1)/2. - (cb**2*complex(0,1)*lam4*RA2x1*RA3x2)/2. - (cb**2*complex(0,1)*lam5*RA2x1*RA3x2)/2. + cb*complex(0,1)*lam1*RA2x1*RA3x1*sb - cb*complex(0,1)*lam3*RA2x1*RA3x1*sb - cb*complex(0,1)*lam2*RA2x2*RA3x2*sb + cb*complex(0,1)*lam3*RA2x2*RA3x2*sb + cb*complex(0,1)*lam7*RA2x3*RA3x3*sb - cb*complex(0,1)*lam8*RA2x3*RA3x3*sb + (complex(0,1)*lam4*RA2x2*RA3x1*sb**2)/2. + (complex(0,1)*lam5*RA2x2*RA3x1*sb**2)/2. + (complex(0,1)*lam4*RA2x1*RA3x2*sb**2)/2. + (complex(0,1)*lam5*RA2x1*RA3x2*sb**2)/2.',
                 order = {'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '-(cb**2*complex(0,1)*lam5*RA2x2*RA3x1) - cb**2*complex(0,1)*lam5*RA2x1*RA3x2 + cb*complex(0,1)*lam1*RA2x1*RA3x1*sb - cb*complex(0,1)*lam3*RA2x1*RA3x1*sb - cb*complex(0,1)*lam4*RA2x1*RA3x1*sb + cb*complex(0,1)*lam5*RA2x1*RA3x1*sb - cb*complex(0,1)*lam2*RA2x2*RA3x2*sb + cb*complex(0,1)*lam3*RA2x2*RA3x2*sb + cb*complex(0,1)*lam4*RA2x2*RA3x2*sb - cb*complex(0,1)*lam5*RA2x2*RA3x2*sb + cb*complex(0,1)*lam7*RA2x3*RA3x3*sb - cb*complex(0,1)*lam8*RA2x3*RA3x3*sb + complex(0,1)*lam5*RA2x2*RA3x1*sb**2 + complex(0,1)*lam5*RA2x1*RA3x2*sb**2',
                 order = {'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = '-(cb**2*complex(0,1)*lam4*RA3x1*RA3x2) - cb**2*complex(0,1)*lam5*RA3x1*RA3x2 + cb*complex(0,1)*lam1*RA3x1**2*sb - cb*complex(0,1)*lam3*RA3x1**2*sb - cb*complex(0,1)*lam2*RA3x2**2*sb + cb*complex(0,1)*lam3*RA3x2**2*sb + cb*complex(0,1)*lam7*RA3x3**2*sb - cb*complex(0,1)*lam8*RA3x3**2*sb + complex(0,1)*lam4*RA3x1*RA3x2*sb**2 + complex(0,1)*lam5*RA3x1*RA3x2*sb**2',
                 order = {'QED':2})

GC_81 = Coupling(name = 'GC_81',
                 value = '-2*cb**2*complex(0,1)*lam5*RA3x1*RA3x2 + cb*complex(0,1)*lam1*RA3x1**2*sb - cb*complex(0,1)*lam3*RA3x1**2*sb - cb*complex(0,1)*lam4*RA3x1**2*sb + cb*complex(0,1)*lam5*RA3x1**2*sb - cb*complex(0,1)*lam2*RA3x2**2*sb + cb*complex(0,1)*lam3*RA3x2**2*sb + cb*complex(0,1)*lam4*RA3x2**2*sb - cb*complex(0,1)*lam5*RA3x2**2*sb + cb*complex(0,1)*lam7*RA3x3**2*sb - cb*complex(0,1)*lam8*RA3x3**2*sb + 2*complex(0,1)*lam5*RA3x1*RA3x2*sb**2',
                 order = {'QED':2})

GC_82 = Coupling(name = 'GC_82',
                 value = '-(cb**2*complex(0,1)*lam3*RA1x1*RA3x1) - cb**2*complex(0,1)*lam2*RA1x2*RA3x2 - cb**2*complex(0,1)*lam8*RA1x3*RA3x3 + cb*complex(0,1)*lam4*RA1x2*RA3x1*sb + cb*complex(0,1)*lam5*RA1x2*RA3x1*sb + cb*complex(0,1)*lam4*RA1x1*RA3x2*sb + cb*complex(0,1)*lam5*RA1x1*RA3x2*sb - complex(0,1)*lam1*RA1x1*RA3x1*sb**2 - complex(0,1)*lam3*RA1x2*RA3x2*sb**2 - complex(0,1)*lam7*RA1x3*RA3x3*sb**2',
                 order = {'QED':2})

GC_83 = Coupling(name = 'GC_83',
                 value = '-(cb**2*complex(0,1)*lam3*RA1x1*RA3x1) - cb**2*complex(0,1)*lam4*RA1x1*RA3x1 + cb**2*complex(0,1)*lam5*RA1x1*RA3x1 - cb**2*complex(0,1)*lam2*RA1x2*RA3x2 - cb**2*complex(0,1)*lam8*RA1x3*RA3x3 + 2*cb*complex(0,1)*lam5*RA1x2*RA3x1*sb + 2*cb*complex(0,1)*lam5*RA1x1*RA3x2*sb - complex(0,1)*lam1*RA1x1*RA3x1*sb**2 - complex(0,1)*lam3*RA1x2*RA3x2*sb**2 - complex(0,1)*lam4*RA1x2*RA3x2*sb**2 + complex(0,1)*lam5*RA1x2*RA3x2*sb**2 - complex(0,1)*lam7*RA1x3*RA3x3*sb**2',
                 order = {'QED':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '-(cb**2*complex(0,1)*lam1*RA1x1*RA3x1) - cb**2*complex(0,1)*lam3*RA1x2*RA3x2 - cb**2*complex(0,1)*lam7*RA1x3*RA3x3 - cb*complex(0,1)*lam4*RA1x2*RA3x1*sb - cb*complex(0,1)*lam5*RA1x2*RA3x1*sb - cb*complex(0,1)*lam4*RA1x1*RA3x2*sb - cb*complex(0,1)*lam5*RA1x1*RA3x2*sb - complex(0,1)*lam3*RA1x1*RA3x1*sb**2 - complex(0,1)*lam2*RA1x2*RA3x2*sb**2 - complex(0,1)*lam8*RA1x3*RA3x3*sb**2',
                 order = {'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '-(cb**2*complex(0,1)*lam1*RA1x1*RA3x1) - cb**2*complex(0,1)*lam3*RA1x2*RA3x2 - cb**2*complex(0,1)*lam4*RA1x2*RA3x2 + cb**2*complex(0,1)*lam5*RA1x2*RA3x2 - cb**2*complex(0,1)*lam7*RA1x3*RA3x3 - 2*cb*complex(0,1)*lam5*RA1x2*RA3x1*sb - 2*cb*complex(0,1)*lam5*RA1x1*RA3x2*sb - complex(0,1)*lam3*RA1x1*RA3x1*sb**2 - complex(0,1)*lam4*RA1x1*RA3x1*sb**2 + complex(0,1)*lam5*RA1x1*RA3x1*sb**2 - complex(0,1)*lam2*RA1x2*RA3x2*sb**2 - complex(0,1)*lam8*RA1x3*RA3x3*sb**2',
                 order = {'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = '-(cb**2*complex(0,1)*lam3*RA2x1*RA3x1) - cb**2*complex(0,1)*lam2*RA2x2*RA3x2 - cb**2*complex(0,1)*lam8*RA2x3*RA3x3 + cb*complex(0,1)*lam4*RA2x2*RA3x1*sb + cb*complex(0,1)*lam5*RA2x2*RA3x1*sb + cb*complex(0,1)*lam4*RA2x1*RA3x2*sb + cb*complex(0,1)*lam5*RA2x1*RA3x2*sb - complex(0,1)*lam1*RA2x1*RA3x1*sb**2 - complex(0,1)*lam3*RA2x2*RA3x2*sb**2 - complex(0,1)*lam7*RA2x3*RA3x3*sb**2',
                 order = {'QED':2})

GC_87 = Coupling(name = 'GC_87',
                 value = '-(cb**2*complex(0,1)*lam3*RA2x1*RA3x1) - cb**2*complex(0,1)*lam4*RA2x1*RA3x1 + cb**2*complex(0,1)*lam5*RA2x1*RA3x1 - cb**2*complex(0,1)*lam2*RA2x2*RA3x2 - cb**2*complex(0,1)*lam8*RA2x3*RA3x3 + 2*cb*complex(0,1)*lam5*RA2x2*RA3x1*sb + 2*cb*complex(0,1)*lam5*RA2x1*RA3x2*sb - complex(0,1)*lam1*RA2x1*RA3x1*sb**2 - complex(0,1)*lam3*RA2x2*RA3x2*sb**2 - complex(0,1)*lam4*RA2x2*RA3x2*sb**2 + complex(0,1)*lam5*RA2x2*RA3x2*sb**2 - complex(0,1)*lam7*RA2x3*RA3x3*sb**2',
                 order = {'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '-(cb**2*complex(0,1)*lam1*RA2x1*RA3x1) - cb**2*complex(0,1)*lam3*RA2x2*RA3x2 - cb**2*complex(0,1)*lam7*RA2x3*RA3x3 - cb*complex(0,1)*lam4*RA2x2*RA3x1*sb - cb*complex(0,1)*lam5*RA2x2*RA3x1*sb - cb*complex(0,1)*lam4*RA2x1*RA3x2*sb - cb*complex(0,1)*lam5*RA2x1*RA3x2*sb - complex(0,1)*lam3*RA2x1*RA3x1*sb**2 - complex(0,1)*lam2*RA2x2*RA3x2*sb**2 - complex(0,1)*lam8*RA2x3*RA3x3*sb**2',
                 order = {'QED':2})

GC_89 = Coupling(name = 'GC_89',
                 value = '-(cb**2*complex(0,1)*lam1*RA2x1*RA3x1) - cb**2*complex(0,1)*lam3*RA2x2*RA3x2 - cb**2*complex(0,1)*lam4*RA2x2*RA3x2 + cb**2*complex(0,1)*lam5*RA2x2*RA3x2 - cb**2*complex(0,1)*lam7*RA2x3*RA3x3 - 2*cb*complex(0,1)*lam5*RA2x2*RA3x1*sb - 2*cb*complex(0,1)*lam5*RA2x1*RA3x2*sb - complex(0,1)*lam3*RA2x1*RA3x1*sb**2 - complex(0,1)*lam4*RA2x1*RA3x1*sb**2 + complex(0,1)*lam5*RA2x1*RA3x1*sb**2 - complex(0,1)*lam2*RA2x2*RA3x2*sb**2 - complex(0,1)*lam8*RA2x3*RA3x3*sb**2',
                 order = {'QED':2})

GC_90 = Coupling(name = 'GC_90',
                 value = '-(cb**2*complex(0,1)*lam3*RA3x1**2) - cb**2*complex(0,1)*lam2*RA3x2**2 - cb**2*complex(0,1)*lam8*RA3x3**2 + 2*cb*complex(0,1)*lam4*RA3x1*RA3x2*sb + 2*cb*complex(0,1)*lam5*RA3x1*RA3x2*sb - complex(0,1)*lam1*RA3x1**2*sb**2 - complex(0,1)*lam3*RA3x2**2*sb**2 - complex(0,1)*lam7*RA3x3**2*sb**2',
                 order = {'QED':2})

GC_91 = Coupling(name = 'GC_91',
                 value = '-(cb**2*complex(0,1)*lam3*RA3x1**2) - cb**2*complex(0,1)*lam4*RA3x1**2 + cb**2*complex(0,1)*lam5*RA3x1**2 - cb**2*complex(0,1)*lam2*RA3x2**2 - cb**2*complex(0,1)*lam8*RA3x3**2 + 4*cb*complex(0,1)*lam5*RA3x1*RA3x2*sb - complex(0,1)*lam1*RA3x1**2*sb**2 - complex(0,1)*lam3*RA3x2**2*sb**2 - complex(0,1)*lam4*RA3x2**2*sb**2 + complex(0,1)*lam5*RA3x2**2*sb**2 - complex(0,1)*lam7*RA3x3**2*sb**2',
                 order = {'QED':2})

GC_92 = Coupling(name = 'GC_92',
                 value = '-(cb**2*complex(0,1)*lam1*RA3x1**2) - cb**2*complex(0,1)*lam3*RA3x2**2 - cb**2*complex(0,1)*lam7*RA3x3**2 - 2*cb*complex(0,1)*lam4*RA3x1*RA3x2*sb - 2*cb*complex(0,1)*lam5*RA3x1*RA3x2*sb - complex(0,1)*lam3*RA3x1**2*sb**2 - complex(0,1)*lam2*RA3x2**2*sb**2 - complex(0,1)*lam8*RA3x3**2*sb**2',
                 order = {'QED':2})

GC_93 = Coupling(name = 'GC_93',
                 value = '-(cb**2*complex(0,1)*lam1*RA3x1**2) - cb**2*complex(0,1)*lam3*RA3x2**2 - cb**2*complex(0,1)*lam4*RA3x2**2 + cb**2*complex(0,1)*lam5*RA3x2**2 - cb**2*complex(0,1)*lam7*RA3x3**2 - 4*cb*complex(0,1)*lam5*RA3x1*RA3x2*sb - complex(0,1)*lam3*RA3x1**2*sb**2 - complex(0,1)*lam4*RA3x1**2*sb**2 + complex(0,1)*lam5*RA3x1**2*sb**2 - complex(0,1)*lam2*RA3x2**2*sb**2 - complex(0,1)*lam8*RA3x3**2*sb**2',
                 order = {'QED':2})

GC_94 = Coupling(name = 'GC_94',
                 value = '-(cb**3*complex(0,1)*lam2*sb) + cb**3*complex(0,1)*lam3*sb + cb**3*complex(0,1)*lam4*sb + cb**3*complex(0,1)*lam5*sb + cb*complex(0,1)*lam1*sb**3 - cb*complex(0,1)*lam3*sb**3 - cb*complex(0,1)*lam4*sb**3 - cb*complex(0,1)*lam5*sb**3',
                 order = {'QED':2})

GC_95 = Coupling(name = 'GC_95',
                 value = 'cb**3*complex(0,1)*lam1*sb - cb**3*complex(0,1)*lam3*sb - cb**3*complex(0,1)*lam4*sb - cb**3*complex(0,1)*lam5*sb - cb*complex(0,1)*lam2*sb**3 + cb*complex(0,1)*lam3*sb**3 + cb*complex(0,1)*lam4*sb**3 + cb*complex(0,1)*lam5*sb**3',
                 order = {'QED':2})

GC_96 = Coupling(name = 'GC_96',
                 value = '-2*cb**3*complex(0,1)*lam2*sb + 2*cb**3*complex(0,1)*lam3*sb + 2*cb**3*complex(0,1)*lam4*sb + 2*cb**3*complex(0,1)*lam5*sb + 2*cb*complex(0,1)*lam1*sb**3 - 2*cb*complex(0,1)*lam3*sb**3 - 2*cb*complex(0,1)*lam4*sb**3 - 2*cb*complex(0,1)*lam5*sb**3',
                 order = {'QED':2})

GC_97 = Coupling(name = 'GC_97',
                 value = '2*cb**3*complex(0,1)*lam1*sb - 2*cb**3*complex(0,1)*lam3*sb - 2*cb**3*complex(0,1)*lam4*sb - 2*cb**3*complex(0,1)*lam5*sb - 2*cb*complex(0,1)*lam2*sb**3 + 2*cb*complex(0,1)*lam3*sb**3 + 2*cb*complex(0,1)*lam4*sb**3 + 2*cb*complex(0,1)*lam5*sb**3',
                 order = {'QED':2})

GC_98 = Coupling(name = 'GC_98',
                 value = '-3*cb**3*complex(0,1)*lam2*sb + 3*cb**3*complex(0,1)*lam3*sb + 3*cb**3*complex(0,1)*lam4*sb + 3*cb**3*complex(0,1)*lam5*sb + 3*cb*complex(0,1)*lam1*sb**3 - 3*cb*complex(0,1)*lam3*sb**3 - 3*cb*complex(0,1)*lam4*sb**3 - 3*cb*complex(0,1)*lam5*sb**3',
                 order = {'QED':2})

GC_99 = Coupling(name = 'GC_99',
                 value = '3*cb**3*complex(0,1)*lam1*sb - 3*cb**3*complex(0,1)*lam3*sb - 3*cb**3*complex(0,1)*lam4*sb - 3*cb**3*complex(0,1)*lam5*sb - 3*cb*complex(0,1)*lam2*sb**3 + 3*cb*complex(0,1)*lam3*sb**3 + 3*cb*complex(0,1)*lam4*sb**3 + 3*cb*complex(0,1)*lam5*sb**3',
                 order = {'QED':2})

GC_100 = Coupling(name = 'GC_100',
                  value = '-(cb**3*lam4*RA1x2)/2. + (cb**3*lam5*RA1x2)/2. + (cb**2*lam4*RA1x1*sb)/2. - (cb**2*lam5*RA1x1*sb)/2. - (cb*lam4*RA1x2*sb**2)/2. + (cb*lam5*RA1x2*sb**2)/2. + (lam4*RA1x1*sb**3)/2. - (lam5*RA1x1*sb**3)/2.',
                  order = {'QED':2})

GC_101 = Coupling(name = 'GC_101',
                  value = '(cb**3*lam4*RA1x2)/2. - (cb**3*lam5*RA1x2)/2. - (cb**2*lam4*RA1x1*sb)/2. + (cb**2*lam5*RA1x1*sb)/2. + (cb*lam4*RA1x2*sb**2)/2. - (cb*lam5*RA1x2*sb**2)/2. - (lam4*RA1x1*sb**3)/2. + (lam5*RA1x1*sb**3)/2.',
                  order = {'QED':2})

GC_102 = Coupling(name = 'GC_102',
                  value = '(cb**3*lam4*RA1x1)/2. - (cb**3*lam5*RA1x1)/2. + (cb**2*lam4*RA1x2*sb)/2. - (cb**2*lam5*RA1x2*sb)/2. + (cb*lam4*RA1x1*sb**2)/2. - (cb*lam5*RA1x1*sb**2)/2. + (lam4*RA1x2*sb**3)/2. - (lam5*RA1x2*sb**3)/2.',
                  order = {'QED':2})

GC_103 = Coupling(name = 'GC_103',
                  value = '-(cb**3*lam4*RA1x1)/2. + (cb**3*lam5*RA1x1)/2. - (cb**2*lam4*RA1x2*sb)/2. + (cb**2*lam5*RA1x2*sb)/2. - (cb*lam4*RA1x1*sb**2)/2. + (cb*lam5*RA1x1*sb**2)/2. - (lam4*RA1x2*sb**3)/2. + (lam5*RA1x2*sb**3)/2.',
                  order = {'QED':2})

GC_104 = Coupling(name = 'GC_104',
                  value = '-(cb**3*lam4*RA2x2)/2. + (cb**3*lam5*RA2x2)/2. + (cb**2*lam4*RA2x1*sb)/2. - (cb**2*lam5*RA2x1*sb)/2. - (cb*lam4*RA2x2*sb**2)/2. + (cb*lam5*RA2x2*sb**2)/2. + (lam4*RA2x1*sb**3)/2. - (lam5*RA2x1*sb**3)/2.',
                  order = {'QED':2})

GC_105 = Coupling(name = 'GC_105',
                  value = '(cb**3*lam4*RA2x2)/2. - (cb**3*lam5*RA2x2)/2. - (cb**2*lam4*RA2x1*sb)/2. + (cb**2*lam5*RA2x1*sb)/2. + (cb*lam4*RA2x2*sb**2)/2. - (cb*lam5*RA2x2*sb**2)/2. - (lam4*RA2x1*sb**3)/2. + (lam5*RA2x1*sb**3)/2.',
                  order = {'QED':2})

GC_106 = Coupling(name = 'GC_106',
                  value = '(cb**3*lam4*RA2x1)/2. - (cb**3*lam5*RA2x1)/2. + (cb**2*lam4*RA2x2*sb)/2. - (cb**2*lam5*RA2x2*sb)/2. + (cb*lam4*RA2x1*sb**2)/2. - (cb*lam5*RA2x1*sb**2)/2. + (lam4*RA2x2*sb**3)/2. - (lam5*RA2x2*sb**3)/2.',
                  order = {'QED':2})

GC_107 = Coupling(name = 'GC_107',
                  value = '-(cb**3*lam4*RA2x1)/2. + (cb**3*lam5*RA2x1)/2. - (cb**2*lam4*RA2x2*sb)/2. + (cb**2*lam5*RA2x2*sb)/2. - (cb*lam4*RA2x1*sb**2)/2. + (cb*lam5*RA2x1*sb**2)/2. - (lam4*RA2x2*sb**3)/2. + (lam5*RA2x2*sb**3)/2.',
                  order = {'QED':2})

GC_108 = Coupling(name = 'GC_108',
                  value = '-(cb**3*lam4*RA3x2)/2. + (cb**3*lam5*RA3x2)/2. + (cb**2*lam4*RA3x1*sb)/2. - (cb**2*lam5*RA3x1*sb)/2. - (cb*lam4*RA3x2*sb**2)/2. + (cb*lam5*RA3x2*sb**2)/2. + (lam4*RA3x1*sb**3)/2. - (lam5*RA3x1*sb**3)/2.',
                  order = {'QED':2})

GC_109 = Coupling(name = 'GC_109',
                  value = '(cb**3*lam4*RA3x2)/2. - (cb**3*lam5*RA3x2)/2. - (cb**2*lam4*RA3x1*sb)/2. + (cb**2*lam5*RA3x1*sb)/2. + (cb*lam4*RA3x2*sb**2)/2. - (cb*lam5*RA3x2*sb**2)/2. - (lam4*RA3x1*sb**3)/2. + (lam5*RA3x1*sb**3)/2.',
                  order = {'QED':2})

GC_110 = Coupling(name = 'GC_110',
                  value = '(cb**3*lam4*RA3x1)/2. - (cb**3*lam5*RA3x1)/2. + (cb**2*lam4*RA3x2*sb)/2. - (cb**2*lam5*RA3x2*sb)/2. + (cb*lam4*RA3x1*sb**2)/2. - (cb*lam5*RA3x1*sb**2)/2. + (lam4*RA3x2*sb**3)/2. - (lam5*RA3x2*sb**3)/2.',
                  order = {'QED':2})

GC_111 = Coupling(name = 'GC_111',
                  value = '-(cb**3*lam4*RA3x1)/2. + (cb**3*lam5*RA3x1)/2. - (cb**2*lam4*RA3x2*sb)/2. + (cb**2*lam5*RA3x2*sb)/2. - (cb*lam4*RA3x1*sb**2)/2. + (cb*lam5*RA3x1*sb**2)/2. - (lam4*RA3x2*sb**3)/2. + (lam5*RA3x2*sb**3)/2.',
                  order = {'QED':2})

GC_112 = Coupling(name = 'GC_112',
                  value = '-(cb**4*complex(0,1)*lam2) - 2*cb**2*complex(0,1)*lam3*sb**2 - 2*cb**2*complex(0,1)*lam4*sb**2 - 2*cb**2*complex(0,1)*lam5*sb**2 - complex(0,1)*lam1*sb**4',
                  order = {'QED':2})

GC_113 = Coupling(name = 'GC_113',
                  value = '-2*cb**4*complex(0,1)*lam2 - 4*cb**2*complex(0,1)*lam3*sb**2 - 4*cb**2*complex(0,1)*lam4*sb**2 - 4*cb**2*complex(0,1)*lam5*sb**2 - 2*complex(0,1)*lam1*sb**4',
                  order = {'QED':2})

GC_114 = Coupling(name = 'GC_114',
                  value = '-3*cb**4*complex(0,1)*lam2 - 6*cb**2*complex(0,1)*lam3*sb**2 - 6*cb**2*complex(0,1)*lam4*sb**2 - 6*cb**2*complex(0,1)*lam5*sb**2 - 3*complex(0,1)*lam1*sb**4',
                  order = {'QED':2})

GC_115 = Coupling(name = 'GC_115',
                  value = '-(cb**4*complex(0,1)*lam1) - 2*cb**2*complex(0,1)*lam3*sb**2 - 2*cb**2*complex(0,1)*lam4*sb**2 - 2*cb**2*complex(0,1)*lam5*sb**2 - complex(0,1)*lam2*sb**4',
                  order = {'QED':2})

GC_116 = Coupling(name = 'GC_116',
                  value = '-2*cb**4*complex(0,1)*lam1 - 4*cb**2*complex(0,1)*lam3*sb**2 - 4*cb**2*complex(0,1)*lam4*sb**2 - 4*cb**2*complex(0,1)*lam5*sb**2 - 2*complex(0,1)*lam2*sb**4',
                  order = {'QED':2})

GC_117 = Coupling(name = 'GC_117',
                  value = '-3*cb**4*complex(0,1)*lam1 - 6*cb**2*complex(0,1)*lam3*sb**2 - 6*cb**2*complex(0,1)*lam4*sb**2 - 6*cb**2*complex(0,1)*lam5*sb**2 - 3*complex(0,1)*lam2*sb**4',
                  order = {'QED':2})

GC_118 = Coupling(name = 'GC_118',
                  value = '-(cb**4*complex(0,1)*lam3) - cb**2*complex(0,1)*lam1*sb**2 - cb**2*complex(0,1)*lam2*sb**2 + 2*cb**2*complex(0,1)*lam4*sb**2 + 2*cb**2*complex(0,1)*lam5*sb**2 - complex(0,1)*lam3*sb**4',
                  order = {'QED':2})

GC_119 = Coupling(name = 'GC_119',
                  value = '-(cb**4*complex(0,1)*lam3) - cb**4*complex(0,1)*lam4 - 2*cb**2*complex(0,1)*lam1*sb**2 - 2*cb**2*complex(0,1)*lam2*sb**2 + 2*cb**2*complex(0,1)*lam3*sb**2 + 2*cb**2*complex(0,1)*lam4*sb**2 + 4*cb**2*complex(0,1)*lam5*sb**2 - complex(0,1)*lam3*sb**4 - complex(0,1)*lam4*sb**4',
                  order = {'QED':2})

GC_120 = Coupling(name = 'GC_120',
                  value = '-(cb**4*complex(0,1)*lam4)/2. - (cb**4*complex(0,1)*lam5)/2. - cb**2*complex(0,1)*lam1*sb**2 - cb**2*complex(0,1)*lam2*sb**2 + 2*cb**2*complex(0,1)*lam3*sb**2 + cb**2*complex(0,1)*lam4*sb**2 + cb**2*complex(0,1)*lam5*sb**2 - (complex(0,1)*lam4*sb**4)/2. - (complex(0,1)*lam5*sb**4)/2.',
                  order = {'QED':2})

GC_121 = Coupling(name = 'GC_121',
                  value = '-(cb**4*complex(0,1)*lam3) - cb**4*complex(0,1)*lam4 - cb**4*complex(0,1)*lam5 - 3*cb**2*complex(0,1)*lam1*sb**2 - 3*cb**2*complex(0,1)*lam2*sb**2 + 4*cb**2*complex(0,1)*lam3*sb**2 + 4*cb**2*complex(0,1)*lam4*sb**2 + 4*cb**2*complex(0,1)*lam5*sb**2 - complex(0,1)*lam3*sb**4 - complex(0,1)*lam4*sb**4 - complex(0,1)*lam5*sb**4',
                  order = {'QED':2})

GC_122 = Coupling(name = 'GC_122',
                  value = '-2*cb**4*complex(0,1)*lam5 - 2*cb**2*complex(0,1)*lam1*sb**2 - 2*cb**2*complex(0,1)*lam2*sb**2 + 4*cb**2*complex(0,1)*lam3*sb**2 + 4*cb**2*complex(0,1)*lam4*sb**2 - 2*complex(0,1)*lam5*sb**4',
                  order = {'QED':2})

GC_123 = Coupling(name = 'GC_123',
                  value = '(ee**2*complex(0,1)*RA1x1**2)/(2.*sw**2) + (ee**2*complex(0,1)*RA1x2**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_124 = Coupling(name = 'GC_124',
                  value = '(ee**2*complex(0,1)*RA1x1*RA2x1)/(2.*sw**2) + (ee**2*complex(0,1)*RA1x2*RA2x2)/(2.*sw**2)',
                  order = {'QED':2})

GC_125 = Coupling(name = 'GC_125',
                  value = '(ee**2*complex(0,1)*RA2x1**2)/(2.*sw**2) + (ee**2*complex(0,1)*RA2x2**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_126 = Coupling(name = 'GC_126',
                  value = '(ee**2*complex(0,1)*RA1x1*RA3x1)/(2.*sw**2) + (ee**2*complex(0,1)*RA1x2*RA3x2)/(2.*sw**2)',
                  order = {'QED':2})

GC_127 = Coupling(name = 'GC_127',
                  value = '(ee**2*complex(0,1)*RA2x1*RA3x1)/(2.*sw**2) + (ee**2*complex(0,1)*RA2x2*RA3x2)/(2.*sw**2)',
                  order = {'QED':2})

GC_128 = Coupling(name = 'GC_128',
                  value = '(ee**2*complex(0,1)*RA3x1**2)/(2.*sw**2) + (ee**2*complex(0,1)*RA3x2**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_129 = Coupling(name = 'GC_129',
                  value = '(cb**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sb**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_130 = Coupling(name = 'GC_130',
                  value = '(cb*ee*complex(0,1)*RA1x2)/(2.*sw) - (ee*complex(0,1)*RA1x1*sb)/(2.*sw)',
                  order = {'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '-(cb*ee*complex(0,1)*RA1x2)/(2.*sw) + (ee*complex(0,1)*RA1x1*sb)/(2.*sw)',
                  order = {'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '(cb*ee**2*complex(0,1)*RA1x2)/(2.*sw) - (ee**2*complex(0,1)*RA1x1*sb)/(2.*sw)',
                  order = {'QED':2})

GC_133 = Coupling(name = 'GC_133',
                  value = '-(cb*ee*complex(0,1)*RA1x1)/(2.*sw) - (ee*complex(0,1)*RA1x2*sb)/(2.*sw)',
                  order = {'QED':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '(cb*ee*complex(0,1)*RA1x1)/(2.*sw) + (ee*complex(0,1)*RA1x2*sb)/(2.*sw)',
                  order = {'QED':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '(cb*ee**2*complex(0,1)*RA1x1)/(2.*sw) + (ee**2*complex(0,1)*RA1x2*sb)/(2.*sw)',
                  order = {'QED':2})

GC_136 = Coupling(name = 'GC_136',
                  value = '(cb*ee*complex(0,1)*RA2x2)/(2.*sw) - (ee*complex(0,1)*RA2x1*sb)/(2.*sw)',
                  order = {'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '-(cb*ee*complex(0,1)*RA2x2)/(2.*sw) + (ee*complex(0,1)*RA2x1*sb)/(2.*sw)',
                  order = {'QED':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '(cb*ee**2*complex(0,1)*RA2x2)/(2.*sw) - (ee**2*complex(0,1)*RA2x1*sb)/(2.*sw)',
                  order = {'QED':2})

GC_139 = Coupling(name = 'GC_139',
                  value = '-(cb*ee*complex(0,1)*RA2x1)/(2.*sw) - (ee*complex(0,1)*RA2x2*sb)/(2.*sw)',
                  order = {'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '(cb*ee*complex(0,1)*RA2x1)/(2.*sw) + (ee*complex(0,1)*RA2x2*sb)/(2.*sw)',
                  order = {'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '(cb*ee**2*complex(0,1)*RA2x1)/(2.*sw) + (ee**2*complex(0,1)*RA2x2*sb)/(2.*sw)',
                  order = {'QED':2})

GC_142 = Coupling(name = 'GC_142',
                  value = '(cb*ee*complex(0,1)*RA3x2)/(2.*sw) - (ee*complex(0,1)*RA3x1*sb)/(2.*sw)',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '-(cb*ee*complex(0,1)*RA3x2)/(2.*sw) + (ee*complex(0,1)*RA3x1*sb)/(2.*sw)',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '(cb*ee**2*complex(0,1)*RA3x2)/(2.*sw) - (ee**2*complex(0,1)*RA3x1*sb)/(2.*sw)',
                  order = {'QED':2})

GC_145 = Coupling(name = 'GC_145',
                  value = '-(cb*ee*complex(0,1)*RA3x1)/(2.*sw) - (ee*complex(0,1)*RA3x2*sb)/(2.*sw)',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '(cb*ee*complex(0,1)*RA3x1)/(2.*sw) + (ee*complex(0,1)*RA3x2*sb)/(2.*sw)',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '(cb*ee**2*complex(0,1)*RA3x1)/(2.*sw) + (ee**2*complex(0,1)*RA3x2*sb)/(2.*sw)',
                  order = {'QED':2})

GC_148 = Coupling(name = 'GC_148',
                  value = '(cb**2*ee)/(2.*sw) + (ee*sb**2)/(2.*sw)',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '-(cb**2*ee**2)/(2.*sw) - (ee**2*sb**2)/(2.*sw)',
                  order = {'QED':2})

GC_150 = Coupling(name = 'GC_150',
                  value = '(cb**2*ee**2)/(2.*sw) + (ee**2*sb**2)/(2.*sw)',
                  order = {'QED':2})

GC_151 = Coupling(name = 'GC_151',
                  value = '-((ee**2*complex(0,1))/sw**2)',
                  order = {'QED':2})

GC_152 = Coupling(name = 'GC_152',
                  value = '(cw**2*ee**2*complex(0,1))/sw**2',
                  order = {'QED':2})

GC_153 = Coupling(name = 'GC_153',
                  value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '-(cw*ee*complex(0,1))/(2.*sw)',
                  order = {'QED':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '(cw*ee*complex(0,1))/(2.*sw)',
                  order = {'QED':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '-((cw*ee*complex(0,1))/sw)',
                  order = {'QED':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '(cw*ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '(-2*cw*ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_159 = Coupling(name = 'GC_159',
                  value = '-(ee*complex(0,1)*sw)/(6.*cw)',
                  order = {'QED':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '(ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_161 = Coupling(name = 'GC_161',
                  value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_162 = Coupling(name = 'GC_162',
                  value = '-(cb*cw*ee*RA1x2)/(2.*sw) + (cw*ee*RA1x1*sb)/(2.*sw) - (cb*ee*RA1x2*sw)/(2.*cw) + (ee*RA1x1*sb*sw)/(2.*cw)',
                  order = {'QED':1})

GC_163 = Coupling(name = 'GC_163',
                  value = '-(cb*cw*ee*RA1x1)/(2.*sw) - (cw*ee*RA1x2*sb)/(2.*sw) - (cb*ee*RA1x1*sw)/(2.*cw) - (ee*RA1x2*sb*sw)/(2.*cw)',
                  order = {'QED':1})

GC_164 = Coupling(name = 'GC_164',
                  value = '-(cb*cw*ee*RA2x2)/(2.*sw) + (cw*ee*RA2x1*sb)/(2.*sw) - (cb*ee*RA2x2*sw)/(2.*cw) + (ee*RA2x1*sb*sw)/(2.*cw)',
                  order = {'QED':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '-(cb*cw*ee*RA2x1)/(2.*sw) - (cw*ee*RA2x2*sb)/(2.*sw) - (cb*ee*RA2x1*sw)/(2.*cw) - (ee*RA2x2*sb*sw)/(2.*cw)',
                  order = {'QED':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '-(cb*cw*ee*RA3x2)/(2.*sw) + (cw*ee*RA3x1*sb)/(2.*sw) - (cb*ee*RA3x2*sw)/(2.*cw) + (ee*RA3x1*sb*sw)/(2.*cw)',
                  order = {'QED':1})

GC_167 = Coupling(name = 'GC_167',
                  value = '-(cb*cw*ee*RA3x1)/(2.*sw) - (cw*ee*RA3x2*sb)/(2.*sw) - (cb*ee*RA3x1*sw)/(2.*cw) - (ee*RA3x2*sb*sw)/(2.*cw)',
                  order = {'QED':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '-(cb**2*cw*ee*complex(0,1))/(2.*sw) - (cw*ee*complex(0,1)*sb**2)/(2.*sw) + (cb**2*ee*complex(0,1)*sw)/(2.*cw) + (ee*complex(0,1)*sb**2*sw)/(2.*cw)',
                  order = {'QED':1})

GC_169 = Coupling(name = 'GC_169',
                  value = '(cb**2*cw*ee**2*complex(0,1))/sw + (cw*ee**2*complex(0,1)*sb**2)/sw - (cb**2*ee**2*complex(0,1)*sw)/cw - (ee**2*complex(0,1)*sb**2*sw)/cw',
                  order = {'QED':2})

GC_170 = Coupling(name = 'GC_170',
                  value = 'ee**2*complex(0,1)*RA1x1**2 + ee**2*complex(0,1)*RA1x2**2 + (cw**2*ee**2*complex(0,1)*RA1x1**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*RA1x2**2)/(2.*sw**2) + (ee**2*complex(0,1)*RA1x1**2*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*RA1x2**2*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_171 = Coupling(name = 'GC_171',
                  value = 'ee**2*complex(0,1)*RA1x1*RA2x1 + ee**2*complex(0,1)*RA1x2*RA2x2 + (cw**2*ee**2*complex(0,1)*RA1x1*RA2x1)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*RA1x2*RA2x2)/(2.*sw**2) + (ee**2*complex(0,1)*RA1x1*RA2x1*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*RA1x2*RA2x2*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_172 = Coupling(name = 'GC_172',
                  value = 'ee**2*complex(0,1)*RA2x1**2 + ee**2*complex(0,1)*RA2x2**2 + (cw**2*ee**2*complex(0,1)*RA2x1**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*RA2x2**2)/(2.*sw**2) + (ee**2*complex(0,1)*RA2x1**2*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*RA2x2**2*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_173 = Coupling(name = 'GC_173',
                  value = 'ee**2*complex(0,1)*RA1x1*RA3x1 + ee**2*complex(0,1)*RA1x2*RA3x2 + (cw**2*ee**2*complex(0,1)*RA1x1*RA3x1)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*RA1x2*RA3x2)/(2.*sw**2) + (ee**2*complex(0,1)*RA1x1*RA3x1*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*RA1x2*RA3x2*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_174 = Coupling(name = 'GC_174',
                  value = 'ee**2*complex(0,1)*RA2x1*RA3x1 + ee**2*complex(0,1)*RA2x2*RA3x2 + (cw**2*ee**2*complex(0,1)*RA2x1*RA3x1)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*RA2x2*RA3x2)/(2.*sw**2) + (ee**2*complex(0,1)*RA2x1*RA3x1*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*RA2x2*RA3x2*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_175 = Coupling(name = 'GC_175',
                  value = 'ee**2*complex(0,1)*RA3x1**2 + ee**2*complex(0,1)*RA3x2**2 + (cw**2*ee**2*complex(0,1)*RA3x1**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*RA3x2**2)/(2.*sw**2) + (ee**2*complex(0,1)*RA3x1**2*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*RA3x2**2*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_176 = Coupling(name = 'GC_176',
                  value = '-(cb**2*ee**2*complex(0,1)) - ee**2*complex(0,1)*sb**2 + (cb**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*sb**2)/(2.*sw**2) + (cb**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*sb**2*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_177 = Coupling(name = 'GC_177',
                  value = 'cb**2*ee**2*complex(0,1) + ee**2*complex(0,1)*sb**2 + (cb**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*sb**2)/(2.*sw**2) + (cb**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*sb**2*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_178 = Coupling(name = 'GC_178',
                  value = '-(cb*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_179 = Coupling(name = 'GC_179',
                  value = '(cb*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '-(ee**2*complex(0,1)*RA1x1*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_181 = Coupling(name = 'GC_181',
                  value = '-(ee**2*complex(0,1)*RA2x1*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_182 = Coupling(name = 'GC_182',
                  value = '-(ee**2*complex(0,1)*RA3x1*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_183 = Coupling(name = 'GC_183',
                  value = '-(ee**2*sb*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_184 = Coupling(name = 'GC_184',
                  value = '(ee**2*sb*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_185 = Coupling(name = 'GC_185',
                  value = '-(ee**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_186 = Coupling(name = 'GC_186',
                  value = '(ee**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_187 = Coupling(name = 'GC_187',
                  value = '-(cb**2*ee**2*complex(0,1)*vev)/(2.*cw) - (ee**2*complex(0,1)*sb**2*vev)/(2.*cw)',
                  order = {'QED':1})

GC_188 = Coupling(name = 'GC_188',
                  value = '(cb**4*lam4*vev)/2. - (cb**4*lam5*vev)/2. + cb**2*lam4*sb**2*vev - cb**2*lam5*sb**2*vev + (lam4*sb**4*vev)/2. - (lam5*sb**4*vev)/2.',
                  order = {'QED':1})

GC_189 = Coupling(name = 'GC_189',
                  value = '-(cb**4*lam4*vev)/2. + (cb**4*lam5*vev)/2. - cb**2*lam4*sb**2*vev + cb**2*lam5*sb**2*vev - (lam4*sb**4*vev)/2. + (lam5*sb**4*vev)/2.',
                  order = {'QED':1})

GC_190 = Coupling(name = 'GC_190',
                  value = '-(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_191 = Coupling(name = 'GC_191',
                  value = '(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_192 = Coupling(name = 'GC_192',
                  value = '-(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '(cb*ee**2*complex(0,1)*RA1x1*vev)/(2.*sw**2) + (ee**2*complex(0,1)*RA1x2*sb*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '(cb*ee**2*complex(0,1)*RA2x1*vev)/(2.*sw**2) + (ee**2*complex(0,1)*RA2x2*sb*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_196 = Coupling(name = 'GC_196',
                  value = '(cb*ee**2*complex(0,1)*RA3x1*vev)/(2.*sw**2) + (ee**2*complex(0,1)*RA3x2*sb*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '(cb**2*ee**2*complex(0,1)*vev)/(2.*sw) + (ee**2*complex(0,1)*sb**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_198 = Coupling(name = 'GC_198',
                  value = '-(ee**2*complex(0,1)*RA1x1*vev)/2. - (cw**2*ee**2*complex(0,1)*RA1x1*vev)/(4.*sw**2) - (ee**2*complex(0,1)*RA1x1*sw**2*vev)/(4.*cw**2)',
                  order = {'QED':1})

GC_199 = Coupling(name = 'GC_199',
                  value = '-(ee**2*complex(0,1)*RA2x1*vev)/2. - (cw**2*ee**2*complex(0,1)*RA2x1*vev)/(4.*sw**2) - (ee**2*complex(0,1)*RA2x1*sw**2*vev)/(4.*cw**2)',
                  order = {'QED':1})

GC_200 = Coupling(name = 'GC_200',
                  value = '-(ee**2*complex(0,1)*RA3x1*vev)/2. - (cw**2*ee**2*complex(0,1)*RA3x1*vev)/(4.*sw**2) - (ee**2*complex(0,1)*RA3x1*sw**2*vev)/(4.*cw**2)',
                  order = {'QED':1})

GC_201 = Coupling(name = 'GC_201',
                  value = 'cb*ee**2*complex(0,1)*RA1x1*vev + ee**2*complex(0,1)*RA1x2*sb*vev + (cb*cw**2*ee**2*complex(0,1)*RA1x1*vev)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*RA1x2*sb*vev)/(2.*sw**2) + (cb*ee**2*complex(0,1)*RA1x1*sw**2*vev)/(2.*cw**2) + (ee**2*complex(0,1)*RA1x2*sb*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_202 = Coupling(name = 'GC_202',
                  value = 'cb*ee**2*complex(0,1)*RA2x1*vev + ee**2*complex(0,1)*RA2x2*sb*vev + (cb*cw**2*ee**2*complex(0,1)*RA2x1*vev)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*RA2x2*sb*vev)/(2.*sw**2) + (cb*ee**2*complex(0,1)*RA2x1*sw**2*vev)/(2.*cw**2) + (ee**2*complex(0,1)*RA2x2*sb*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_203 = Coupling(name = 'GC_203',
                  value = 'cb*ee**2*complex(0,1)*RA3x1*vev + ee**2*complex(0,1)*RA3x2*sb*vev + (cb*cw**2*ee**2*complex(0,1)*RA3x1*vev)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*RA3x2*sb*vev)/(2.*sw**2) + (cb*ee**2*complex(0,1)*RA3x1*sw**2*vev)/(2.*cw**2) + (ee**2*complex(0,1)*RA3x2*sb*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_204 = Coupling(name = 'GC_204',
                  value = '-3*cb*complex(0,1)*lam1*RA1x1**3*vev - 3*cb*complex(0,1)*lam3*RA1x1*RA1x2**2*vev - 3*cb*complex(0,1)*lam4*RA1x1*RA1x2**2*vev - 3*cb*complex(0,1)*lam5*RA1x1*RA1x2**2*vev - 3*cb*complex(0,1)*lam7*RA1x1*RA1x3**2*vev - 3*complex(0,1)*lam3*RA1x1**2*RA1x2*sb*vev - 3*complex(0,1)*lam4*RA1x1**2*RA1x2*sb*vev - 3*complex(0,1)*lam5*RA1x1**2*RA1x2*sb*vev - 3*complex(0,1)*lam2*RA1x2**3*sb*vev - 3*complex(0,1)*lam8*RA1x2*RA1x3**2*sb*vev - 3*complex(0,1)*lam7*RA1x1**2*RA1x3*vev3 - 3*complex(0,1)*lam8*RA1x2**2*RA1x3*vev3 - 3*complex(0,1)*lam6*RA1x3**3*vev3',
                  order = {'QED':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '-3*cb*complex(0,1)*lam1*RA1x1**2*RA2x1*vev - cb*complex(0,1)*lam3*RA1x2**2*RA2x1*vev - cb*complex(0,1)*lam4*RA1x2**2*RA2x1*vev - cb*complex(0,1)*lam5*RA1x2**2*RA2x1*vev - cb*complex(0,1)*lam7*RA1x3**2*RA2x1*vev - 2*cb*complex(0,1)*lam3*RA1x1*RA1x2*RA2x2*vev - 2*cb*complex(0,1)*lam4*RA1x1*RA1x2*RA2x2*vev - 2*cb*complex(0,1)*lam5*RA1x1*RA1x2*RA2x2*vev - 2*cb*complex(0,1)*lam7*RA1x1*RA1x3*RA2x3*vev - 2*complex(0,1)*lam3*RA1x1*RA1x2*RA2x1*sb*vev - 2*complex(0,1)*lam4*RA1x1*RA1x2*RA2x1*sb*vev - 2*complex(0,1)*lam5*RA1x1*RA1x2*RA2x1*sb*vev - complex(0,1)*lam3*RA1x1**2*RA2x2*sb*vev - complex(0,1)*lam4*RA1x1**2*RA2x2*sb*vev - complex(0,1)*lam5*RA1x1**2*RA2x2*sb*vev - 3*complex(0,1)*lam2*RA1x2**2*RA2x2*sb*vev - complex(0,1)*lam8*RA1x3**2*RA2x2*sb*vev - 2*complex(0,1)*lam8*RA1x2*RA1x3*RA2x3*sb*vev - 2*complex(0,1)*lam7*RA1x1*RA1x3*RA2x1*vev3 - 2*complex(0,1)*lam8*RA1x2*RA1x3*RA2x2*vev3 - complex(0,1)*lam7*RA1x1**2*RA2x3*vev3 - complex(0,1)*lam8*RA1x2**2*RA2x3*vev3 - 3*complex(0,1)*lam6*RA1x3**2*RA2x3*vev3',
                  order = {'QED':1})

GC_206 = Coupling(name = 'GC_206',
                  value = '-3*cb*complex(0,1)*lam1*RA1x1*RA2x1**2*vev - 2*cb*complex(0,1)*lam3*RA1x2*RA2x1*RA2x2*vev - 2*cb*complex(0,1)*lam4*RA1x2*RA2x1*RA2x2*vev - 2*cb*complex(0,1)*lam5*RA1x2*RA2x1*RA2x2*vev - cb*complex(0,1)*lam3*RA1x1*RA2x2**2*vev - cb*complex(0,1)*lam4*RA1x1*RA2x2**2*vev - cb*complex(0,1)*lam5*RA1x1*RA2x2**2*vev - 2*cb*complex(0,1)*lam7*RA1x3*RA2x1*RA2x3*vev - cb*complex(0,1)*lam7*RA1x1*RA2x3**2*vev - complex(0,1)*lam3*RA1x2*RA2x1**2*sb*vev - complex(0,1)*lam4*RA1x2*RA2x1**2*sb*vev - complex(0,1)*lam5*RA1x2*RA2x1**2*sb*vev - 2*complex(0,1)*lam3*RA1x1*RA2x1*RA2x2*sb*vev - 2*complex(0,1)*lam4*RA1x1*RA2x1*RA2x2*sb*vev - 2*complex(0,1)*lam5*RA1x1*RA2x1*RA2x2*sb*vev - 3*complex(0,1)*lam2*RA1x2*RA2x2**2*sb*vev - 2*complex(0,1)*lam8*RA1x3*RA2x2*RA2x3*sb*vev - complex(0,1)*lam8*RA1x2*RA2x3**2*sb*vev - complex(0,1)*lam7*RA1x3*RA2x1**2*vev3 - complex(0,1)*lam8*RA1x3*RA2x2**2*vev3 - 2*complex(0,1)*lam7*RA1x1*RA2x1*RA2x3*vev3 - 2*complex(0,1)*lam8*RA1x2*RA2x2*RA2x3*vev3 - 3*complex(0,1)*lam6*RA1x3*RA2x3**2*vev3',
                  order = {'QED':1})

GC_207 = Coupling(name = 'GC_207',
                  value = '-3*cb*complex(0,1)*lam1*RA2x1**3*vev - 3*cb*complex(0,1)*lam3*RA2x1*RA2x2**2*vev - 3*cb*complex(0,1)*lam4*RA2x1*RA2x2**2*vev - 3*cb*complex(0,1)*lam5*RA2x1*RA2x2**2*vev - 3*cb*complex(0,1)*lam7*RA2x1*RA2x3**2*vev - 3*complex(0,1)*lam3*RA2x1**2*RA2x2*sb*vev - 3*complex(0,1)*lam4*RA2x1**2*RA2x2*sb*vev - 3*complex(0,1)*lam5*RA2x1**2*RA2x2*sb*vev - 3*complex(0,1)*lam2*RA2x2**3*sb*vev - 3*complex(0,1)*lam8*RA2x2*RA2x3**2*sb*vev - 3*complex(0,1)*lam7*RA2x1**2*RA2x3*vev3 - 3*complex(0,1)*lam8*RA2x2**2*RA2x3*vev3 - 3*complex(0,1)*lam6*RA2x3**3*vev3',
                  order = {'QED':1})

GC_208 = Coupling(name = 'GC_208',
                  value = '-3*cb*complex(0,1)*lam1*RA1x1**2*RA3x1*vev - cb*complex(0,1)*lam3*RA1x2**2*RA3x1*vev - cb*complex(0,1)*lam4*RA1x2**2*RA3x1*vev - cb*complex(0,1)*lam5*RA1x2**2*RA3x1*vev - cb*complex(0,1)*lam7*RA1x3**2*RA3x1*vev - 2*cb*complex(0,1)*lam3*RA1x1*RA1x2*RA3x2*vev - 2*cb*complex(0,1)*lam4*RA1x1*RA1x2*RA3x2*vev - 2*cb*complex(0,1)*lam5*RA1x1*RA1x2*RA3x2*vev - 2*cb*complex(0,1)*lam7*RA1x1*RA1x3*RA3x3*vev - 2*complex(0,1)*lam3*RA1x1*RA1x2*RA3x1*sb*vev - 2*complex(0,1)*lam4*RA1x1*RA1x2*RA3x1*sb*vev - 2*complex(0,1)*lam5*RA1x1*RA1x2*RA3x1*sb*vev - complex(0,1)*lam3*RA1x1**2*RA3x2*sb*vev - complex(0,1)*lam4*RA1x1**2*RA3x2*sb*vev - complex(0,1)*lam5*RA1x1**2*RA3x2*sb*vev - 3*complex(0,1)*lam2*RA1x2**2*RA3x2*sb*vev - complex(0,1)*lam8*RA1x3**2*RA3x2*sb*vev - 2*complex(0,1)*lam8*RA1x2*RA1x3*RA3x3*sb*vev - 2*complex(0,1)*lam7*RA1x1*RA1x3*RA3x1*vev3 - 2*complex(0,1)*lam8*RA1x2*RA1x3*RA3x2*vev3 - complex(0,1)*lam7*RA1x1**2*RA3x3*vev3 - complex(0,1)*lam8*RA1x2**2*RA3x3*vev3 - 3*complex(0,1)*lam6*RA1x3**2*RA3x3*vev3',
                  order = {'QED':1})

GC_209 = Coupling(name = 'GC_209',
                  value = '-3*cb*complex(0,1)*lam1*RA1x1*RA2x1*RA3x1*vev - cb*complex(0,1)*lam3*RA1x2*RA2x2*RA3x1*vev - cb*complex(0,1)*lam4*RA1x2*RA2x2*RA3x1*vev - cb*complex(0,1)*lam5*RA1x2*RA2x2*RA3x1*vev - cb*complex(0,1)*lam7*RA1x3*RA2x3*RA3x1*vev - cb*complex(0,1)*lam3*RA1x2*RA2x1*RA3x2*vev - cb*complex(0,1)*lam4*RA1x2*RA2x1*RA3x2*vev - cb*complex(0,1)*lam5*RA1x2*RA2x1*RA3x2*vev - cb*complex(0,1)*lam3*RA1x1*RA2x2*RA3x2*vev - cb*complex(0,1)*lam4*RA1x1*RA2x2*RA3x2*vev - cb*complex(0,1)*lam5*RA1x1*RA2x2*RA3x2*vev - cb*complex(0,1)*lam7*RA1x3*RA2x1*RA3x3*vev - cb*complex(0,1)*lam7*RA1x1*RA2x3*RA3x3*vev - complex(0,1)*lam3*RA1x2*RA2x1*RA3x1*sb*vev - complex(0,1)*lam4*RA1x2*RA2x1*RA3x1*sb*vev - complex(0,1)*lam5*RA1x2*RA2x1*RA3x1*sb*vev - complex(0,1)*lam3*RA1x1*RA2x2*RA3x1*sb*vev - complex(0,1)*lam4*RA1x1*RA2x2*RA3x1*sb*vev - complex(0,1)*lam5*RA1x1*RA2x2*RA3x1*sb*vev - complex(0,1)*lam3*RA1x1*RA2x1*RA3x2*sb*vev - complex(0,1)*lam4*RA1x1*RA2x1*RA3x2*sb*vev - complex(0,1)*lam5*RA1x1*RA2x1*RA3x2*sb*vev - 3*complex(0,1)*lam2*RA1x2*RA2x2*RA3x2*sb*vev - complex(0,1)*lam8*RA1x3*RA2x3*RA3x2*sb*vev - complex(0,1)*lam8*RA1x3*RA2x2*RA3x3*sb*vev - complex(0,1)*lam8*RA1x2*RA2x3*RA3x3*sb*vev - complex(0,1)*lam7*RA1x3*RA2x1*RA3x1*vev3 - complex(0,1)*lam7*RA1x1*RA2x3*RA3x1*vev3 - complex(0,1)*lam8*RA1x3*RA2x2*RA3x2*vev3 - complex(0,1)*lam8*RA1x2*RA2x3*RA3x2*vev3 - complex(0,1)*lam7*RA1x1*RA2x1*RA3x3*vev3 - complex(0,1)*lam8*RA1x2*RA2x2*RA3x3*vev3 - 3*complex(0,1)*lam6*RA1x3*RA2x3*RA3x3*vev3',
                  order = {'QED':1})

GC_210 = Coupling(name = 'GC_210',
                  value = '-3*cb*complex(0,1)*lam1*RA2x1**2*RA3x1*vev - cb*complex(0,1)*lam3*RA2x2**2*RA3x1*vev - cb*complex(0,1)*lam4*RA2x2**2*RA3x1*vev - cb*complex(0,1)*lam5*RA2x2**2*RA3x1*vev - cb*complex(0,1)*lam7*RA2x3**2*RA3x1*vev - 2*cb*complex(0,1)*lam3*RA2x1*RA2x2*RA3x2*vev - 2*cb*complex(0,1)*lam4*RA2x1*RA2x2*RA3x2*vev - 2*cb*complex(0,1)*lam5*RA2x1*RA2x2*RA3x2*vev - 2*cb*complex(0,1)*lam7*RA2x1*RA2x3*RA3x3*vev - 2*complex(0,1)*lam3*RA2x1*RA2x2*RA3x1*sb*vev - 2*complex(0,1)*lam4*RA2x1*RA2x2*RA3x1*sb*vev - 2*complex(0,1)*lam5*RA2x1*RA2x2*RA3x1*sb*vev - complex(0,1)*lam3*RA2x1**2*RA3x2*sb*vev - complex(0,1)*lam4*RA2x1**2*RA3x2*sb*vev - complex(0,1)*lam5*RA2x1**2*RA3x2*sb*vev - 3*complex(0,1)*lam2*RA2x2**2*RA3x2*sb*vev - complex(0,1)*lam8*RA2x3**2*RA3x2*sb*vev - 2*complex(0,1)*lam8*RA2x2*RA2x3*RA3x3*sb*vev - 2*complex(0,1)*lam7*RA2x1*RA2x3*RA3x1*vev3 - 2*complex(0,1)*lam8*RA2x2*RA2x3*RA3x2*vev3 - complex(0,1)*lam7*RA2x1**2*RA3x3*vev3 - complex(0,1)*lam8*RA2x2**2*RA3x3*vev3 - 3*complex(0,1)*lam6*RA2x3**2*RA3x3*vev3',
                  order = {'QED':1})

GC_211 = Coupling(name = 'GC_211',
                  value = '-3*cb*complex(0,1)*lam1*RA1x1*RA3x1**2*vev - 2*cb*complex(0,1)*lam3*RA1x2*RA3x1*RA3x2*vev - 2*cb*complex(0,1)*lam4*RA1x2*RA3x1*RA3x2*vev - 2*cb*complex(0,1)*lam5*RA1x2*RA3x1*RA3x2*vev - cb*complex(0,1)*lam3*RA1x1*RA3x2**2*vev - cb*complex(0,1)*lam4*RA1x1*RA3x2**2*vev - cb*complex(0,1)*lam5*RA1x1*RA3x2**2*vev - 2*cb*complex(0,1)*lam7*RA1x3*RA3x1*RA3x3*vev - cb*complex(0,1)*lam7*RA1x1*RA3x3**2*vev - complex(0,1)*lam3*RA1x2*RA3x1**2*sb*vev - complex(0,1)*lam4*RA1x2*RA3x1**2*sb*vev - complex(0,1)*lam5*RA1x2*RA3x1**2*sb*vev - 2*complex(0,1)*lam3*RA1x1*RA3x1*RA3x2*sb*vev - 2*complex(0,1)*lam4*RA1x1*RA3x1*RA3x2*sb*vev - 2*complex(0,1)*lam5*RA1x1*RA3x1*RA3x2*sb*vev - 3*complex(0,1)*lam2*RA1x2*RA3x2**2*sb*vev - 2*complex(0,1)*lam8*RA1x3*RA3x2*RA3x3*sb*vev - complex(0,1)*lam8*RA1x2*RA3x3**2*sb*vev - complex(0,1)*lam7*RA1x3*RA3x1**2*vev3 - complex(0,1)*lam8*RA1x3*RA3x2**2*vev3 - 2*complex(0,1)*lam7*RA1x1*RA3x1*RA3x3*vev3 - 2*complex(0,1)*lam8*RA1x2*RA3x2*RA3x3*vev3 - 3*complex(0,1)*lam6*RA1x3*RA3x3**2*vev3',
                  order = {'QED':1})

GC_212 = Coupling(name = 'GC_212',
                  value = '-3*cb*complex(0,1)*lam1*RA2x1*RA3x1**2*vev - 2*cb*complex(0,1)*lam3*RA2x2*RA3x1*RA3x2*vev - 2*cb*complex(0,1)*lam4*RA2x2*RA3x1*RA3x2*vev - 2*cb*complex(0,1)*lam5*RA2x2*RA3x1*RA3x2*vev - cb*complex(0,1)*lam3*RA2x1*RA3x2**2*vev - cb*complex(0,1)*lam4*RA2x1*RA3x2**2*vev - cb*complex(0,1)*lam5*RA2x1*RA3x2**2*vev - 2*cb*complex(0,1)*lam7*RA2x3*RA3x1*RA3x3*vev - cb*complex(0,1)*lam7*RA2x1*RA3x3**2*vev - complex(0,1)*lam3*RA2x2*RA3x1**2*sb*vev - complex(0,1)*lam4*RA2x2*RA3x1**2*sb*vev - complex(0,1)*lam5*RA2x2*RA3x1**2*sb*vev - 2*complex(0,1)*lam3*RA2x1*RA3x1*RA3x2*sb*vev - 2*complex(0,1)*lam4*RA2x1*RA3x1*RA3x2*sb*vev - 2*complex(0,1)*lam5*RA2x1*RA3x1*RA3x2*sb*vev - 3*complex(0,1)*lam2*RA2x2*RA3x2**2*sb*vev - 2*complex(0,1)*lam8*RA2x3*RA3x2*RA3x3*sb*vev - complex(0,1)*lam8*RA2x2*RA3x3**2*sb*vev - complex(0,1)*lam7*RA2x3*RA3x1**2*vev3 - complex(0,1)*lam8*RA2x3*RA3x2**2*vev3 - 2*complex(0,1)*lam7*RA2x1*RA3x1*RA3x3*vev3 - 2*complex(0,1)*lam8*RA2x2*RA3x2*RA3x3*vev3 - 3*complex(0,1)*lam6*RA2x3*RA3x3**2*vev3',
                  order = {'QED':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '-3*cb*complex(0,1)*lam1*RA3x1**3*vev - 3*cb*complex(0,1)*lam3*RA3x1*RA3x2**2*vev - 3*cb*complex(0,1)*lam4*RA3x1*RA3x2**2*vev - 3*cb*complex(0,1)*lam5*RA3x1*RA3x2**2*vev - 3*cb*complex(0,1)*lam7*RA3x1*RA3x3**2*vev - 3*complex(0,1)*lam3*RA3x1**2*RA3x2*sb*vev - 3*complex(0,1)*lam4*RA3x1**2*RA3x2*sb*vev - 3*complex(0,1)*lam5*RA3x1**2*RA3x2*sb*vev - 3*complex(0,1)*lam2*RA3x2**3*sb*vev - 3*complex(0,1)*lam8*RA3x2*RA3x3**2*sb*vev - 3*complex(0,1)*lam7*RA3x1**2*RA3x3*vev3 - 3*complex(0,1)*lam8*RA3x2**2*RA3x3*vev3 - 3*complex(0,1)*lam6*RA3x3**3*vev3',
                  order = {'QED':1})

GC_214 = Coupling(name = 'GC_214',
                  value = '-(cb**3*complex(0,1)*lam4*RA1x2*vev)/2. - (cb**3*complex(0,1)*lam5*RA1x2*vev)/2. + cb**2*complex(0,1)*lam1*RA1x1*sb*vev - cb**2*complex(0,1)*lam3*RA1x1*sb*vev - (cb**2*complex(0,1)*lam4*RA1x1*sb*vev)/2. - (cb**2*complex(0,1)*lam5*RA1x1*sb*vev)/2. - cb*complex(0,1)*lam2*RA1x2*sb**2*vev + cb*complex(0,1)*lam3*RA1x2*sb**2*vev + (cb*complex(0,1)*lam4*RA1x2*sb**2*vev)/2. + (cb*complex(0,1)*lam5*RA1x2*sb**2*vev)/2. + (complex(0,1)*lam4*RA1x1*sb**3*vev)/2. + (complex(0,1)*lam5*RA1x1*sb**3*vev)/2. + cb*complex(0,1)*lam7*RA1x3*sb*vev3 - cb*complex(0,1)*lam8*RA1x3*sb*vev3',
                  order = {'QED':1})

GC_215 = Coupling(name = 'GC_215',
                  value = '-(cb**3*complex(0,1)*lam5*RA1x2*vev) + cb**2*complex(0,1)*lam1*RA1x1*sb*vev - cb**2*complex(0,1)*lam3*RA1x1*sb*vev - cb**2*complex(0,1)*lam4*RA1x1*sb*vev - cb*complex(0,1)*lam2*RA1x2*sb**2*vev + cb*complex(0,1)*lam3*RA1x2*sb**2*vev + cb*complex(0,1)*lam4*RA1x2*sb**2*vev + complex(0,1)*lam5*RA1x1*sb**3*vev + cb*complex(0,1)*lam7*RA1x3*sb*vev3 - cb*complex(0,1)*lam8*RA1x3*sb*vev3',
                  order = {'QED':1})

GC_216 = Coupling(name = 'GC_216',
                  value = '-(cb**3*complex(0,1)*lam4*RA2x2*vev)/2. - (cb**3*complex(0,1)*lam5*RA2x2*vev)/2. + cb**2*complex(0,1)*lam1*RA2x1*sb*vev - cb**2*complex(0,1)*lam3*RA2x1*sb*vev - (cb**2*complex(0,1)*lam4*RA2x1*sb*vev)/2. - (cb**2*complex(0,1)*lam5*RA2x1*sb*vev)/2. - cb*complex(0,1)*lam2*RA2x2*sb**2*vev + cb*complex(0,1)*lam3*RA2x2*sb**2*vev + (cb*complex(0,1)*lam4*RA2x2*sb**2*vev)/2. + (cb*complex(0,1)*lam5*RA2x2*sb**2*vev)/2. + (complex(0,1)*lam4*RA2x1*sb**3*vev)/2. + (complex(0,1)*lam5*RA2x1*sb**3*vev)/2. + cb*complex(0,1)*lam7*RA2x3*sb*vev3 - cb*complex(0,1)*lam8*RA2x3*sb*vev3',
                  order = {'QED':1})

GC_217 = Coupling(name = 'GC_217',
                  value = '-(cb**3*complex(0,1)*lam5*RA2x2*vev) + cb**2*complex(0,1)*lam1*RA2x1*sb*vev - cb**2*complex(0,1)*lam3*RA2x1*sb*vev - cb**2*complex(0,1)*lam4*RA2x1*sb*vev - cb*complex(0,1)*lam2*RA2x2*sb**2*vev + cb*complex(0,1)*lam3*RA2x2*sb**2*vev + cb*complex(0,1)*lam4*RA2x2*sb**2*vev + complex(0,1)*lam5*RA2x1*sb**3*vev + cb*complex(0,1)*lam7*RA2x3*sb*vev3 - cb*complex(0,1)*lam8*RA2x3*sb*vev3',
                  order = {'QED':1})

GC_218 = Coupling(name = 'GC_218',
                  value = '-(cb**3*complex(0,1)*lam4*RA3x2*vev)/2. - (cb**3*complex(0,1)*lam5*RA3x2*vev)/2. + cb**2*complex(0,1)*lam1*RA3x1*sb*vev - cb**2*complex(0,1)*lam3*RA3x1*sb*vev - (cb**2*complex(0,1)*lam4*RA3x1*sb*vev)/2. - (cb**2*complex(0,1)*lam5*RA3x1*sb*vev)/2. - cb*complex(0,1)*lam2*RA3x2*sb**2*vev + cb*complex(0,1)*lam3*RA3x2*sb**2*vev + (cb*complex(0,1)*lam4*RA3x2*sb**2*vev)/2. + (cb*complex(0,1)*lam5*RA3x2*sb**2*vev)/2. + (complex(0,1)*lam4*RA3x1*sb**3*vev)/2. + (complex(0,1)*lam5*RA3x1*sb**3*vev)/2. + cb*complex(0,1)*lam7*RA3x3*sb*vev3 - cb*complex(0,1)*lam8*RA3x3*sb*vev3',
                  order = {'QED':1})

GC_219 = Coupling(name = 'GC_219',
                  value = '-(cb**3*complex(0,1)*lam5*RA3x2*vev) + cb**2*complex(0,1)*lam1*RA3x1*sb*vev - cb**2*complex(0,1)*lam3*RA3x1*sb*vev - cb**2*complex(0,1)*lam4*RA3x1*sb*vev - cb*complex(0,1)*lam2*RA3x2*sb**2*vev + cb*complex(0,1)*lam3*RA3x2*sb**2*vev + cb*complex(0,1)*lam4*RA3x2*sb**2*vev + complex(0,1)*lam5*RA3x1*sb**3*vev + cb*complex(0,1)*lam7*RA3x3*sb*vev3 - cb*complex(0,1)*lam8*RA3x3*sb*vev3',
                  order = {'QED':1})

GC_220 = Coupling(name = 'GC_220',
                  value = '-(cb**3*complex(0,1)*lam3*RA1x1*vev) - cb**2*complex(0,1)*lam2*RA1x2*sb*vev + cb**2*complex(0,1)*lam4*RA1x2*sb*vev + cb**2*complex(0,1)*lam5*RA1x2*sb*vev - cb*complex(0,1)*lam1*RA1x1*sb**2*vev + cb*complex(0,1)*lam4*RA1x1*sb**2*vev + cb*complex(0,1)*lam5*RA1x1*sb**2*vev - complex(0,1)*lam3*RA1x2*sb**3*vev - cb**2*complex(0,1)*lam8*RA1x3*vev3 - complex(0,1)*lam7*RA1x3*sb**2*vev3',
                  order = {'QED':1})

GC_221 = Coupling(name = 'GC_221',
                  value = '-(cb**3*complex(0,1)*lam3*RA1x1*vev) - cb**3*complex(0,1)*lam4*RA1x1*vev + cb**3*complex(0,1)*lam5*RA1x1*vev - cb**2*complex(0,1)*lam2*RA1x2*sb*vev + 2*cb**2*complex(0,1)*lam5*RA1x2*sb*vev - cb*complex(0,1)*lam1*RA1x1*sb**2*vev + 2*cb*complex(0,1)*lam5*RA1x1*sb**2*vev - complex(0,1)*lam3*RA1x2*sb**3*vev - complex(0,1)*lam4*RA1x2*sb**3*vev + complex(0,1)*lam5*RA1x2*sb**3*vev - cb**2*complex(0,1)*lam8*RA1x3*vev3 - complex(0,1)*lam7*RA1x3*sb**2*vev3',
                  order = {'QED':1})

GC_222 = Coupling(name = 'GC_222',
                  value = '-(cb**3*complex(0,1)*lam1*RA1x1*vev) - cb**2*complex(0,1)*lam3*RA1x2*sb*vev - cb**2*complex(0,1)*lam4*RA1x2*sb*vev - cb**2*complex(0,1)*lam5*RA1x2*sb*vev - cb*complex(0,1)*lam3*RA1x1*sb**2*vev - cb*complex(0,1)*lam4*RA1x1*sb**2*vev - cb*complex(0,1)*lam5*RA1x1*sb**2*vev - complex(0,1)*lam2*RA1x2*sb**3*vev - cb**2*complex(0,1)*lam7*RA1x3*vev3 - complex(0,1)*lam8*RA1x3*sb**2*vev3',
                  order = {'QED':1})

GC_223 = Coupling(name = 'GC_223',
                  value = '-(cb**3*complex(0,1)*lam3*RA2x1*vev) - cb**2*complex(0,1)*lam2*RA2x2*sb*vev + cb**2*complex(0,1)*lam4*RA2x2*sb*vev + cb**2*complex(0,1)*lam5*RA2x2*sb*vev - cb*complex(0,1)*lam1*RA2x1*sb**2*vev + cb*complex(0,1)*lam4*RA2x1*sb**2*vev + cb*complex(0,1)*lam5*RA2x1*sb**2*vev - complex(0,1)*lam3*RA2x2*sb**3*vev - cb**2*complex(0,1)*lam8*RA2x3*vev3 - complex(0,1)*lam7*RA2x3*sb**2*vev3',
                  order = {'QED':1})

GC_224 = Coupling(name = 'GC_224',
                  value = '-(cb**3*complex(0,1)*lam3*RA2x1*vev) - cb**3*complex(0,1)*lam4*RA2x1*vev + cb**3*complex(0,1)*lam5*RA2x1*vev - cb**2*complex(0,1)*lam2*RA2x2*sb*vev + 2*cb**2*complex(0,1)*lam5*RA2x2*sb*vev - cb*complex(0,1)*lam1*RA2x1*sb**2*vev + 2*cb*complex(0,1)*lam5*RA2x1*sb**2*vev - complex(0,1)*lam3*RA2x2*sb**3*vev - complex(0,1)*lam4*RA2x2*sb**3*vev + complex(0,1)*lam5*RA2x2*sb**3*vev - cb**2*complex(0,1)*lam8*RA2x3*vev3 - complex(0,1)*lam7*RA2x3*sb**2*vev3',
                  order = {'QED':1})

GC_225 = Coupling(name = 'GC_225',
                  value = '-(cb**3*complex(0,1)*lam1*RA2x1*vev) - cb**2*complex(0,1)*lam3*RA2x2*sb*vev - cb**2*complex(0,1)*lam4*RA2x2*sb*vev - cb**2*complex(0,1)*lam5*RA2x2*sb*vev - cb*complex(0,1)*lam3*RA2x1*sb**2*vev - cb*complex(0,1)*lam4*RA2x1*sb**2*vev - cb*complex(0,1)*lam5*RA2x1*sb**2*vev - complex(0,1)*lam2*RA2x2*sb**3*vev - cb**2*complex(0,1)*lam7*RA2x3*vev3 - complex(0,1)*lam8*RA2x3*sb**2*vev3',
                  order = {'QED':1})

GC_226 = Coupling(name = 'GC_226',
                  value = '-(cb**3*complex(0,1)*lam3*RA3x1*vev) - cb**2*complex(0,1)*lam2*RA3x2*sb*vev + cb**2*complex(0,1)*lam4*RA3x2*sb*vev + cb**2*complex(0,1)*lam5*RA3x2*sb*vev - cb*complex(0,1)*lam1*RA3x1*sb**2*vev + cb*complex(0,1)*lam4*RA3x1*sb**2*vev + cb*complex(0,1)*lam5*RA3x1*sb**2*vev - complex(0,1)*lam3*RA3x2*sb**3*vev - cb**2*complex(0,1)*lam8*RA3x3*vev3 - complex(0,1)*lam7*RA3x3*sb**2*vev3',
                  order = {'QED':1})

GC_227 = Coupling(name = 'GC_227',
                  value = '-(cb**3*complex(0,1)*lam3*RA3x1*vev) - cb**3*complex(0,1)*lam4*RA3x1*vev + cb**3*complex(0,1)*lam5*RA3x1*vev - cb**2*complex(0,1)*lam2*RA3x2*sb*vev + 2*cb**2*complex(0,1)*lam5*RA3x2*sb*vev - cb*complex(0,1)*lam1*RA3x1*sb**2*vev + 2*cb*complex(0,1)*lam5*RA3x1*sb**2*vev - complex(0,1)*lam3*RA3x2*sb**3*vev - complex(0,1)*lam4*RA3x2*sb**3*vev + complex(0,1)*lam5*RA3x2*sb**3*vev - cb**2*complex(0,1)*lam8*RA3x3*vev3 - complex(0,1)*lam7*RA3x3*sb**2*vev3',
                  order = {'QED':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '-(cb**3*complex(0,1)*lam1*RA3x1*vev) - cb**2*complex(0,1)*lam3*RA3x2*sb*vev - cb**2*complex(0,1)*lam4*RA3x2*sb*vev - cb**2*complex(0,1)*lam5*RA3x2*sb*vev - cb*complex(0,1)*lam3*RA3x1*sb**2*vev - cb*complex(0,1)*lam4*RA3x1*sb**2*vev - cb*complex(0,1)*lam5*RA3x1*sb**2*vev - complex(0,1)*lam2*RA3x2*sb**3*vev - cb**2*complex(0,1)*lam7*RA3x3*vev3 - complex(0,1)*lam8*RA3x3*sb**2*vev3',
                  order = {'QED':1})

GC_229 = Coupling(name = 'GC_229',
                  value = '-((cb*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '-((complex(0,1)*RA1x2*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '-((complex(0,1)*RA2x2*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_232 = Coupling(name = 'GC_232',
                  value = '-((complex(0,1)*RA3x2*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_233 = Coupling(name = 'GC_233',
                  value = '-((sb*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_234 = Coupling(name = 'GC_234',
                  value = '(cb*yc)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_235 = Coupling(name = 'GC_235',
                  value = '-((complex(0,1)*RA1x2*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_236 = Coupling(name = 'GC_236',
                  value = '-((complex(0,1)*RA2x2*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_237 = Coupling(name = 'GC_237',
                  value = '-((complex(0,1)*RA3x2*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_238 = Coupling(name = 'GC_238',
                  value = '(sb*yc)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_239 = Coupling(name = 'GC_239',
                  value = '-((cb*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_240 = Coupling(name = 'GC_240',
                  value = '-((complex(0,1)*RA1x2*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_241 = Coupling(name = 'GC_241',
                  value = '-((complex(0,1)*RA2x2*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_242 = Coupling(name = 'GC_242',
                  value = '-((complex(0,1)*RA3x2*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_243 = Coupling(name = 'GC_243',
                  value = '-((sb*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_244 = Coupling(name = 'GC_244',
                  value = '-(cb*complex(0,1)*ye)',
                  order = {'QED':1})

GC_245 = Coupling(name = 'GC_245',
                  value = '-((cb*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_246 = Coupling(name = 'GC_246',
                  value = '-((complex(0,1)*RA1x1*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_247 = Coupling(name = 'GC_247',
                  value = '-((complex(0,1)*RA2x1*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_248 = Coupling(name = 'GC_248',
                  value = '-((complex(0,1)*RA3x1*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_249 = Coupling(name = 'GC_249',
                  value = 'complex(0,1)*sb*ye',
                  order = {'QED':1})

GC_250 = Coupling(name = 'GC_250',
                  value = '(sb*ye)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_251 = Coupling(name = 'GC_251',
                  value = '-(cb*complex(0,1)*ym)',
                  order = {'QED':1})

GC_252 = Coupling(name = 'GC_252',
                  value = '-((cb*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_253 = Coupling(name = 'GC_253',
                  value = '-((complex(0,1)*RA1x1*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_254 = Coupling(name = 'GC_254',
                  value = '-((complex(0,1)*RA2x1*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_255 = Coupling(name = 'GC_255',
                  value = '-((complex(0,1)*RA3x1*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_256 = Coupling(name = 'GC_256',
                  value = 'complex(0,1)*sb*ym',
                  order = {'QED':1})

GC_257 = Coupling(name = 'GC_257',
                  value = '(sb*ym)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_258 = Coupling(name = 'GC_258',
                  value = '-((cb*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_259 = Coupling(name = 'GC_259',
                  value = '-((complex(0,1)*RA1x2*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_260 = Coupling(name = 'GC_260',
                  value = '-((complex(0,1)*RA2x2*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_261 = Coupling(name = 'GC_261',
                  value = '-((complex(0,1)*RA3x2*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_262 = Coupling(name = 'GC_262',
                  value = '-((sb*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_263 = Coupling(name = 'GC_263',
                  value = '(cb*yt)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_264 = Coupling(name = 'GC_264',
                  value = '-((complex(0,1)*RA1x2*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_265 = Coupling(name = 'GC_265',
                  value = '-((complex(0,1)*RA2x2*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_266 = Coupling(name = 'GC_266',
                  value = '-((complex(0,1)*RA3x2*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_267 = Coupling(name = 'GC_267',
                  value = '(sb*yt)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_268 = Coupling(name = 'GC_268',
                  value = '-(cb*complex(0,1)*ytau)',
                  order = {'QED':1})

GC_269 = Coupling(name = 'GC_269',
                  value = '-((cb*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_270 = Coupling(name = 'GC_270',
                  value = '-((complex(0,1)*RA1x1*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_271 = Coupling(name = 'GC_271',
                  value = '-((complex(0,1)*RA2x1*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_272 = Coupling(name = 'GC_272',
                  value = '-((complex(0,1)*RA3x1*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_273 = Coupling(name = 'GC_273',
                  value = 'complex(0,1)*sb*ytau',
                  order = {'QED':1})

GC_274 = Coupling(name = 'GC_274',
                  value = '(sb*ytau)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_275 = Coupling(name = 'GC_275',
                  value = '(cb*yup)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_276 = Coupling(name = 'GC_276',
                  value = '-((complex(0,1)*RA1x2*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_277 = Coupling(name = 'GC_277',
                  value = '-((complex(0,1)*RA2x2*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_278 = Coupling(name = 'GC_278',
                  value = '-((complex(0,1)*RA3x2*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_279 = Coupling(name = 'GC_279',
                  value = '(sb*yup)/cmath.sqrt(2)',
                  order = {'QED':1})

