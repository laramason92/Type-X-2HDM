# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 11.3.0 for Mac OS X x86 (64-bit) (March 7, 2018)
# Date: Thu 23 May 2019 19:57:50


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
                value = 'complex(0,1)*I1a11*sinb',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = 'complex(0,1)*I1a22*sinb',
                 order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = 'complex(0,1)*I1a33*sinb',
                 order = {'QED':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '-(complex(0,1)*I2a11*sinb)',
                 order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '-(complex(0,1)*I2a22*sinb)',
                 order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(complex(0,1)*I2a33*sinb)',
                 order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '-(complex(0,1)*I3a11*sinb)',
                 order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '-(complex(0,1)*I3a22*sinb)',
                 order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '-(complex(0,1)*I3a33*sinb)',
                 order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = 'complex(0,1)*I4a11*sinb',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = 'complex(0,1)*I4a22*sinb',
                 order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = 'complex(0,1)*I4a33*sinb',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '-(cosb*ee**2*complex(0,1)*RA1x2)/(2.*cw) + (ee**2*complex(0,1)*RA1x1*sinb)/(2.*cw)',
                 order = {'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '-(cosb*ee**2*complex(0,1)*RA2x2)/(2.*cw) + (ee**2*complex(0,1)*RA2x1*sinb)/(2.*cw)',
                 order = {'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '-(cosb*ee**2*complex(0,1)*RA3x2)/(2.*cw) + (ee**2*complex(0,1)*RA3x1*sinb)/(2.*cw)',
                 order = {'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '-(cosb**2*ee*complex(0,1)) - ee*complex(0,1)*sinb**2',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '2*cosb**2*ee**2*complex(0,1) + 2*ee**2*complex(0,1)*sinb**2',
                 order = {'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '-(cosb**2*ee**2)/(2.*cw) - (ee**2*sinb**2)/(2.*cw)',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '(cosb**2*ee**2)/(2.*cw) + (ee**2*sinb**2)/(2.*cw)',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '(ee**2*complex(0,1)*RA1x1**2)/(2.*sw**2) + (ee**2*complex(0,1)*RA1x2**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(ee**2*complex(0,1)*RA1x1*RA2x1)/(2.*sw**2) + (ee**2*complex(0,1)*RA1x2*RA2x2)/(2.*sw**2)',
                 order = {'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '(ee**2*complex(0,1)*RA2x1**2)/(2.*sw**2) + (ee**2*complex(0,1)*RA2x2**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '(ee**2*complex(0,1)*RA1x1*RA3x1)/(2.*sw**2) + (ee**2*complex(0,1)*RA1x2*RA3x2)/(2.*sw**2)',
                 order = {'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '(ee**2*complex(0,1)*RA2x1*RA3x1)/(2.*sw**2) + (ee**2*complex(0,1)*RA2x2*RA3x2)/(2.*sw**2)',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '(ee**2*complex(0,1)*RA3x1**2)/(2.*sw**2) + (ee**2*complex(0,1)*RA3x2**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '(cosb**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sinb**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '(cosb*ee*complex(0,1)*RA1x2)/(2.*sw) - (ee*complex(0,1)*RA1x1*sinb)/(2.*sw)',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '-(cosb*ee*complex(0,1)*RA1x2)/(2.*sw) + (ee*complex(0,1)*RA1x1*sinb)/(2.*sw)',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(cosb*ee**2*complex(0,1)*RA1x2)/(2.*sw) - (ee**2*complex(0,1)*RA1x1*sinb)/(2.*sw)',
                 order = {'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '(cosb*ee*complex(0,1)*RA2x2)/(2.*sw) - (ee*complex(0,1)*RA2x1*sinb)/(2.*sw)',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '-(cosb*ee*complex(0,1)*RA2x2)/(2.*sw) + (ee*complex(0,1)*RA2x1*sinb)/(2.*sw)',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '(cosb*ee**2*complex(0,1)*RA2x2)/(2.*sw) - (ee**2*complex(0,1)*RA2x1*sinb)/(2.*sw)',
                 order = {'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '(cosb*ee*complex(0,1)*RA3x2)/(2.*sw) - (ee*complex(0,1)*RA3x1*sinb)/(2.*sw)',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-(cosb*ee*complex(0,1)*RA3x2)/(2.*sw) + (ee*complex(0,1)*RA3x1*sinb)/(2.*sw)',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(cosb*ee**2*complex(0,1)*RA3x2)/(2.*sw) - (ee**2*complex(0,1)*RA3x1*sinb)/(2.*sw)',
                 order = {'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '(cosb**2*ee)/(2.*sw) + (ee*sinb**2)/(2.*sw)',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '-(cosb**2*ee**2)/(2.*sw) - (ee**2*sinb**2)/(2.*sw)',
                 order = {'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '(cosb**2*ee**2)/(2.*sw) + (ee**2*sinb**2)/(2.*sw)',
                 order = {'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '-(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '-(ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '-(cosb*cw*ee*RA1x2)/(2.*sw) + (cw*ee*RA1x1*sinb)/(2.*sw) - (cosb*ee*RA1x2*sw)/(2.*cw) + (ee*RA1x1*sinb*sw)/(2.*cw)',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-(cosb*cw*ee*RA2x2)/(2.*sw) + (cw*ee*RA2x1*sinb)/(2.*sw) - (cosb*ee*RA2x2*sw)/(2.*cw) + (ee*RA2x1*sinb*sw)/(2.*cw)',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '-(cosb*cw*ee*RA3x2)/(2.*sw) + (cw*ee*RA3x1*sinb)/(2.*sw) - (cosb*ee*RA3x2*sw)/(2.*cw) + (ee*RA3x1*sinb*sw)/(2.*cw)',
                 order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '-(cosb**2*cw*ee*complex(0,1))/(2.*sw) - (cw*ee*complex(0,1)*sinb**2)/(2.*sw) + (cosb**2*ee*complex(0,1)*sw)/(2.*cw) + (ee*complex(0,1)*sinb**2*sw)/(2.*cw)',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '(cosb**2*cw*ee**2*complex(0,1))/sw + (cw*ee**2*complex(0,1)*sinb**2)/sw - (cosb**2*ee**2*complex(0,1)*sw)/cw - (ee**2*complex(0,1)*sinb**2*sw)/cw',
                 order = {'QED':2})

GC_62 = Coupling(name = 'GC_62',
                 value = 'ee**2*complex(0,1)*RA1x1**2 + ee**2*complex(0,1)*RA1x2**2 + (cw**2*ee**2*complex(0,1)*RA1x1**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*RA1x2**2)/(2.*sw**2) + (ee**2*complex(0,1)*RA1x1**2*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*RA1x2**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = 'ee**2*complex(0,1)*RA1x1*RA2x1 + ee**2*complex(0,1)*RA1x2*RA2x2 + (cw**2*ee**2*complex(0,1)*RA1x1*RA2x1)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*RA1x2*RA2x2)/(2.*sw**2) + (ee**2*complex(0,1)*RA1x1*RA2x1*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*RA1x2*RA2x2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = 'ee**2*complex(0,1)*RA2x1**2 + ee**2*complex(0,1)*RA2x2**2 + (cw**2*ee**2*complex(0,1)*RA2x1**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*RA2x2**2)/(2.*sw**2) + (ee**2*complex(0,1)*RA2x1**2*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*RA2x2**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = 'ee**2*complex(0,1)*RA1x1*RA3x1 + ee**2*complex(0,1)*RA1x2*RA3x2 + (cw**2*ee**2*complex(0,1)*RA1x1*RA3x1)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*RA1x2*RA3x2)/(2.*sw**2) + (ee**2*complex(0,1)*RA1x1*RA3x1*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*RA1x2*RA3x2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_66 = Coupling(name = 'GC_66',
                 value = 'ee**2*complex(0,1)*RA2x1*RA3x1 + ee**2*complex(0,1)*RA2x2*RA3x2 + (cw**2*ee**2*complex(0,1)*RA2x1*RA3x1)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*RA2x2*RA3x2)/(2.*sw**2) + (ee**2*complex(0,1)*RA2x1*RA3x1*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*RA2x2*RA3x2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_67 = Coupling(name = 'GC_67',
                 value = 'ee**2*complex(0,1)*RA3x1**2 + ee**2*complex(0,1)*RA3x2**2 + (cw**2*ee**2*complex(0,1)*RA3x1**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*RA3x2**2)/(2.*sw**2) + (ee**2*complex(0,1)*RA3x1**2*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*RA3x2**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_68 = Coupling(name = 'GC_68',
                 value = '-(cosb**2*ee**2*complex(0,1)) - ee**2*complex(0,1)*sinb**2 + (cosb**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*sinb**2)/(2.*sw**2) + (cosb**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*sinb**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_69 = Coupling(name = 'GC_69',
                 value = 'cosb**2*ee**2*complex(0,1) + ee**2*complex(0,1)*sinb**2 + (cosb**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*sinb**2)/(2.*sw**2) + (cosb**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2) + (ee**2*complex(0,1)*sinb**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '(cosb**5*complex(0,1)*m12**2)/(sinb**3*vev**2) - (cosb**4*complex(0,1)*Mh1**2*RA1x2**2)/(sinb**2*vev**2) - (cosb**4*complex(0,1)*Mh2**2*RA2x2**2)/(sinb**2*vev**2) - (cosb**4*complex(0,1)*MS**2*RA3x2**2)/(sinb**2*vev**2) - (2*cosb*complex(0,1)*m12**2*sinb)/vev**2 - (2*cosb*complex(0,1)*Mh1**2*RA1x1*RA1x2*sinb)/vev**2 - (2*cosb*complex(0,1)*Mh2**2*RA2x1*RA2x2*sinb)/vev**2 - (2*cosb*complex(0,1)*MS**2*RA3x1*RA3x2*sinb)/vev**2 - (complex(0,1)*Mh1**2*RA1x1**2*sinb**4)/(cosb**2*vev**2) - (complex(0,1)*Mh2**2*RA2x1**2*sinb**4)/(cosb**2*vev**2) - (complex(0,1)*MS**2*RA3x1**2*sinb**4)/(cosb**2*vev**2) + (complex(0,1)*m12**2*sinb**5)/(cosb**3*vev**2)',
                 order = {'QED':2})

GC_71 = Coupling(name = 'GC_71',
                 value = '(2*cosb**5*complex(0,1)*m12**2)/(sinb**3*vev**2) - (2*cosb**4*complex(0,1)*Mh1**2*RA1x2**2)/(sinb**2*vev**2) - (2*cosb**4*complex(0,1)*Mh2**2*RA2x2**2)/(sinb**2*vev**2) - (2*cosb**4*complex(0,1)*MS**2*RA3x2**2)/(sinb**2*vev**2) - (4*cosb*complex(0,1)*m12**2*sinb)/vev**2 - (4*cosb*complex(0,1)*Mh1**2*RA1x1*RA1x2*sinb)/vev**2 - (4*cosb*complex(0,1)*Mh2**2*RA2x1*RA2x2*sinb)/vev**2 - (4*cosb*complex(0,1)*MS**2*RA3x1*RA3x2*sinb)/vev**2 - (2*complex(0,1)*Mh1**2*RA1x1**2*sinb**4)/(cosb**2*vev**2) - (2*complex(0,1)*Mh2**2*RA2x1**2*sinb**4)/(cosb**2*vev**2) - (2*complex(0,1)*MS**2*RA3x1**2*sinb**4)/(cosb**2*vev**2) + (2*complex(0,1)*m12**2*sinb**5)/(cosb**3*vev**2)',
                 order = {'QED':2})

GC_72 = Coupling(name = 'GC_72',
                 value = '(3*cosb**5*complex(0,1)*m12**2)/(sinb**3*vev**2) - (3*cosb**4*complex(0,1)*Mh1**2*RA1x2**2)/(sinb**2*vev**2) - (3*cosb**4*complex(0,1)*Mh2**2*RA2x2**2)/(sinb**2*vev**2) - (3*cosb**4*complex(0,1)*MS**2*RA3x2**2)/(sinb**2*vev**2) - (6*cosb*complex(0,1)*m12**2*sinb)/vev**2 - (6*cosb*complex(0,1)*Mh1**2*RA1x1*RA1x2*sinb)/vev**2 - (6*cosb*complex(0,1)*Mh2**2*RA2x1*RA2x2*sinb)/vev**2 - (6*cosb*complex(0,1)*MS**2*RA3x1*RA3x2*sinb)/vev**2 - (3*complex(0,1)*Mh1**2*RA1x1**2*sinb**4)/(cosb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA2x1**2*sinb**4)/(cosb**2*vev**2) - (3*complex(0,1)*MS**2*RA3x1**2*sinb**4)/(cosb**2*vev**2) + (3*complex(0,1)*m12**2*sinb**5)/(cosb**3*vev**2)',
                 order = {'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '(-2*cosb**3*complex(0,1)*MA0**2*RA1x1)/vev + (2*cosb*complex(0,1)*m12**2*RA1x2)/vev + (cosb**3*complex(0,1)*m12**2*RA1x2)/(sinb**2*vev) + (cosb**2*complex(0,1)*m12**2*RA1x1)/(sinb*vev) - (cosb**2*complex(0,1)*Mh1**2*RA1x1**2*RA1x2)/(sinb*vev) - (cosb**2*complex(0,1)*Mh1**2*RA1x2**3)/(sinb*vev) - (cosb**2*complex(0,1)*Mh1**2*RA1x2*RA1x3**2)/(sinb*vev) - (cosb**2*complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x2)/(sinb*vev) - (cosb**2*complex(0,1)*Mh2**2*RA1x2*RA2x2**2)/(sinb*vev) - (cosb**2*complex(0,1)*Mh2**2*RA1x3*RA2x2*RA2x3)/(sinb*vev) - (cosb**2*complex(0,1)*MS**2*RA1x1*RA3x1*RA3x2)/(sinb*vev) - (cosb**2*complex(0,1)*MS**2*RA1x2*RA3x2**2)/(sinb*vev) - (cosb**2*complex(0,1)*MS**2*RA1x3*RA3x2*RA3x3)/(sinb*vev) + (2*complex(0,1)*m12**2*RA1x1*sinb)/vev - (2*cosb**2*complex(0,1)*MA0**2*RA1x2*sinb)/vev - (2*cosb*complex(0,1)*MA0**2*RA1x1*sinb**2)/vev - (complex(0,1)*Mh1**2*RA1x1**3*sinb**2)/(cosb*vev) + (complex(0,1)*m12**2*RA1x2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x3**2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x1*RA2x1**2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x2*RA2x1*RA2x2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x3*RA2x1*RA2x3*sinb**2)/(cosb*vev) - (complex(0,1)*MS**2*RA1x1*RA3x1**2*sinb**2)/(cosb*vev) - (complex(0,1)*MS**2*RA1x2*RA3x1*RA3x2*sinb**2)/(cosb*vev) - (complex(0,1)*MS**2*RA1x3*RA3x1*RA3x3*sinb**2)/(cosb*vev) + (complex(0,1)*m12**2*RA1x1*sinb**3)/(cosb**2*vev) - (2*complex(0,1)*MA0**2*RA1x2*sinb**3)/vev',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '(-2*cosb**3*complex(0,1)*MHP**2*RA1x1)/vev + (2*cosb*complex(0,1)*m12**2*RA1x2)/vev + (cosb**3*complex(0,1)*m12**2*RA1x2)/(sinb**2*vev) + (cosb**2*complex(0,1)*m12**2*RA1x1)/(sinb*vev) - (cosb**2*complex(0,1)*Mh1**2*RA1x1**2*RA1x2)/(sinb*vev) - (cosb**2*complex(0,1)*Mh1**2*RA1x2**3)/(sinb*vev) - (cosb**2*complex(0,1)*Mh1**2*RA1x2*RA1x3**2)/(sinb*vev) - (cosb**2*complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x2)/(sinb*vev) - (cosb**2*complex(0,1)*Mh2**2*RA1x2*RA2x2**2)/(sinb*vev) - (cosb**2*complex(0,1)*Mh2**2*RA1x3*RA2x2*RA2x3)/(sinb*vev) - (cosb**2*complex(0,1)*MS**2*RA1x1*RA3x1*RA3x2)/(sinb*vev) - (cosb**2*complex(0,1)*MS**2*RA1x2*RA3x2**2)/(sinb*vev) - (cosb**2*complex(0,1)*MS**2*RA1x3*RA3x2*RA3x3)/(sinb*vev) + (2*complex(0,1)*m12**2*RA1x1*sinb)/vev - (2*cosb**2*complex(0,1)*MHP**2*RA1x2*sinb)/vev - (2*cosb*complex(0,1)*MHP**2*RA1x1*sinb**2)/vev - (complex(0,1)*Mh1**2*RA1x1**3*sinb**2)/(cosb*vev) + (complex(0,1)*m12**2*RA1x2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x3**2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x1*RA2x1**2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x2*RA2x1*RA2x2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x3*RA2x1*RA2x3*sinb**2)/(cosb*vev) - (complex(0,1)*MS**2*RA1x1*RA3x1**2*sinb**2)/(cosb*vev) - (complex(0,1)*MS**2*RA1x2*RA3x1*RA3x2*sinb**2)/(cosb*vev) - (complex(0,1)*MS**2*RA1x3*RA3x1*RA3x3*sinb**2)/(cosb*vev) + (complex(0,1)*m12**2*RA1x1*sinb**3)/(cosb**2*vev) - (2*complex(0,1)*MHP**2*RA1x2*sinb**3)/vev',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '(-2*cosb**3*complex(0,1)*MA0**2*RA2x1)/vev + (2*cosb*complex(0,1)*m12**2*RA2x2)/vev + (cosb**3*complex(0,1)*m12**2*RA2x2)/(sinb**2*vev) + (cosb**2*complex(0,1)*m12**2*RA2x1)/(sinb*vev) - (cosb**2*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1)/(sinb*vev) - (cosb**2*complex(0,1)*Mh1**2*RA1x2**2*RA2x2)/(sinb*vev) - (cosb**2*complex(0,1)*Mh2**2*RA2x1**2*RA2x2)/(sinb*vev) - (cosb**2*complex(0,1)*Mh2**2*RA2x2**3)/(sinb*vev) - (cosb**2*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x3)/(sinb*vev) - (cosb**2*complex(0,1)*Mh2**2*RA2x2*RA2x3**2)/(sinb*vev) - (cosb**2*complex(0,1)*MS**2*RA2x1*RA3x1*RA3x2)/(sinb*vev) - (cosb**2*complex(0,1)*MS**2*RA2x2*RA3x2**2)/(sinb*vev) - (cosb**2*complex(0,1)*MS**2*RA2x3*RA3x2*RA3x3)/(sinb*vev) + (2*complex(0,1)*m12**2*RA2x1*sinb)/vev - (2*cosb**2*complex(0,1)*MA0**2*RA2x2*sinb)/vev - (2*cosb*complex(0,1)*MA0**2*RA2x1*sinb**2)/vev - (complex(0,1)*Mh1**2*RA1x1**2*RA2x1*sinb**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA2x1**3*sinb**2)/(cosb*vev) + (complex(0,1)*m12**2*RA2x2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA2x1*RA2x2**2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x3*sinb**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA2x1*RA2x3**2*sinb**2)/(cosb*vev) - (complex(0,1)*MS**2*RA2x1*RA3x1**2*sinb**2)/(cosb*vev) - (complex(0,1)*MS**2*RA2x2*RA3x1*RA3x2*sinb**2)/(cosb*vev) - (complex(0,1)*MS**2*RA2x3*RA3x1*RA3x3*sinb**2)/(cosb*vev) + (complex(0,1)*m12**2*RA2x1*sinb**3)/(cosb**2*vev) - (2*complex(0,1)*MA0**2*RA2x2*sinb**3)/vev',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '(-2*cosb**3*complex(0,1)*MHP**2*RA2x1)/vev + (2*cosb*complex(0,1)*m12**2*RA2x2)/vev + (cosb**3*complex(0,1)*m12**2*RA2x2)/(sinb**2*vev) + (cosb**2*complex(0,1)*m12**2*RA2x1)/(sinb*vev) - (cosb**2*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1)/(sinb*vev) - (cosb**2*complex(0,1)*Mh1**2*RA1x2**2*RA2x2)/(sinb*vev) - (cosb**2*complex(0,1)*Mh2**2*RA2x1**2*RA2x2)/(sinb*vev) - (cosb**2*complex(0,1)*Mh2**2*RA2x2**3)/(sinb*vev) - (cosb**2*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x3)/(sinb*vev) - (cosb**2*complex(0,1)*Mh2**2*RA2x2*RA2x3**2)/(sinb*vev) - (cosb**2*complex(0,1)*MS**2*RA2x1*RA3x1*RA3x2)/(sinb*vev) - (cosb**2*complex(0,1)*MS**2*RA2x2*RA3x2**2)/(sinb*vev) - (cosb**2*complex(0,1)*MS**2*RA2x3*RA3x2*RA3x3)/(sinb*vev) + (2*complex(0,1)*m12**2*RA2x1*sinb)/vev - (2*cosb**2*complex(0,1)*MHP**2*RA2x2*sinb)/vev - (2*cosb*complex(0,1)*MHP**2*RA2x1*sinb**2)/vev - (complex(0,1)*Mh1**2*RA1x1**2*RA2x1*sinb**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA2x1**3*sinb**2)/(cosb*vev) + (complex(0,1)*m12**2*RA2x2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA2x1*RA2x2**2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x3*sinb**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA2x1*RA2x3**2*sinb**2)/(cosb*vev) - (complex(0,1)*MS**2*RA2x1*RA3x1**2*sinb**2)/(cosb*vev) - (complex(0,1)*MS**2*RA2x2*RA3x1*RA3x2*sinb**2)/(cosb*vev) - (complex(0,1)*MS**2*RA2x3*RA3x1*RA3x3*sinb**2)/(cosb*vev) + (complex(0,1)*m12**2*RA2x1*sinb**3)/(cosb**2*vev) - (2*complex(0,1)*MHP**2*RA2x2*sinb**3)/vev',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '(-2*cosb**3*complex(0,1)*MA0**2*RA3x1)/vev + (2*cosb*complex(0,1)*m12**2*RA3x2)/vev + (cosb**3*complex(0,1)*m12**2*RA3x2)/(sinb**2*vev) + (cosb**2*complex(0,1)*m12**2*RA3x1)/(sinb*vev) - (cosb**2*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA3x1)/(sinb*vev) - (cosb**2*complex(0,1)*Mh2**2*RA2x1*RA2x2*RA3x1)/(sinb*vev) - (cosb**2*complex(0,1)*Mh1**2*RA1x2**2*RA3x2)/(sinb*vev) - (cosb**2*complex(0,1)*Mh2**2*RA2x2**2*RA3x2)/(sinb*vev) - (cosb**2*complex(0,1)*MS**2*RA3x1**2*RA3x2)/(sinb*vev) - (cosb**2*complex(0,1)*MS**2*RA3x2**3)/(sinb*vev) - (cosb**2*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA3x3)/(sinb*vev) - (cosb**2*complex(0,1)*Mh2**2*RA2x2*RA2x3*RA3x3)/(sinb*vev) - (cosb**2*complex(0,1)*MS**2*RA3x2*RA3x3**2)/(sinb*vev) + (2*complex(0,1)*m12**2*RA3x1*sinb)/vev - (2*cosb**2*complex(0,1)*MA0**2*RA3x2*sinb)/vev - (2*cosb*complex(0,1)*MA0**2*RA3x1*sinb**2)/vev - (complex(0,1)*Mh1**2*RA1x1**2*RA3x1*sinb**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA2x1**2*RA3x1*sinb**2)/(cosb*vev) - (complex(0,1)*MS**2*RA3x1**3*sinb**2)/(cosb*vev) + (complex(0,1)*m12**2*RA3x2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x2*RA3x2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA2x1*RA2x2*RA3x2*sinb**2)/(cosb*vev) - (complex(0,1)*MS**2*RA3x1*RA3x2**2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x3*RA3x3*sinb**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA2x1*RA2x3*RA3x3*sinb**2)/(cosb*vev) - (complex(0,1)*MS**2*RA3x1*RA3x3**2*sinb**2)/(cosb*vev) + (complex(0,1)*m12**2*RA3x1*sinb**3)/(cosb**2*vev) - (2*complex(0,1)*MA0**2*RA3x2*sinb**3)/vev',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '(-2*cosb**3*complex(0,1)*MHP**2*RA3x1)/vev + (2*cosb*complex(0,1)*m12**2*RA3x2)/vev + (cosb**3*complex(0,1)*m12**2*RA3x2)/(sinb**2*vev) + (cosb**2*complex(0,1)*m12**2*RA3x1)/(sinb*vev) - (cosb**2*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA3x1)/(sinb*vev) - (cosb**2*complex(0,1)*Mh2**2*RA2x1*RA2x2*RA3x1)/(sinb*vev) - (cosb**2*complex(0,1)*Mh1**2*RA1x2**2*RA3x2)/(sinb*vev) - (cosb**2*complex(0,1)*Mh2**2*RA2x2**2*RA3x2)/(sinb*vev) - (cosb**2*complex(0,1)*MS**2*RA3x1**2*RA3x2)/(sinb*vev) - (cosb**2*complex(0,1)*MS**2*RA3x2**3)/(sinb*vev) - (cosb**2*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA3x3)/(sinb*vev) - (cosb**2*complex(0,1)*Mh2**2*RA2x2*RA2x3*RA3x3)/(sinb*vev) - (cosb**2*complex(0,1)*MS**2*RA3x2*RA3x3**2)/(sinb*vev) + (2*complex(0,1)*m12**2*RA3x1*sinb)/vev - (2*cosb**2*complex(0,1)*MHP**2*RA3x2*sinb)/vev - (2*cosb*complex(0,1)*MHP**2*RA3x1*sinb**2)/vev - (complex(0,1)*Mh1**2*RA1x1**2*RA3x1*sinb**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA2x1**2*RA3x1*sinb**2)/(cosb*vev) - (complex(0,1)*MS**2*RA3x1**3*sinb**2)/(cosb*vev) + (complex(0,1)*m12**2*RA3x2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x2*RA3x2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA2x1*RA2x2*RA3x2*sinb**2)/(cosb*vev) - (complex(0,1)*MS**2*RA3x1*RA3x2**2*sinb**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x3*RA3x3*sinb**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA2x1*RA2x3*RA3x3*sinb**2)/(cosb*vev) - (complex(0,1)*MS**2*RA3x1*RA3x3**2*sinb**2)/(cosb*vev) + (complex(0,1)*m12**2*RA3x1*sinb**3)/(cosb**2*vev) - (2*complex(0,1)*MHP**2*RA3x2*sinb**3)/vev',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '(cosb*ee**2*complex(0,1)*RA1x1*vev)/(2.*sw**2) + (ee**2*complex(0,1)*RA1x2*sinb*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '(cosb*ee**2*complex(0,1)*RA2x1*vev)/(2.*sw**2) + (ee**2*complex(0,1)*RA2x2*sinb*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '(cosb*ee**2*complex(0,1)*RA3x1*vev)/(2.*sw**2) + (ee**2*complex(0,1)*RA3x2*sinb*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = 'cosb*ee**2*complex(0,1)*RA1x1*vev + ee**2*complex(0,1)*RA1x2*sinb*vev + (cosb*cw**2*ee**2*complex(0,1)*RA1x1*vev)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*RA1x2*sinb*vev)/(2.*sw**2) + (cosb*ee**2*complex(0,1)*RA1x1*sw**2*vev)/(2.*cw**2) + (ee**2*complex(0,1)*RA1x2*sinb*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = 'cosb*ee**2*complex(0,1)*RA2x1*vev + ee**2*complex(0,1)*RA2x2*sinb*vev + (cosb*cw**2*ee**2*complex(0,1)*RA2x1*vev)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*RA2x2*sinb*vev)/(2.*sw**2) + (cosb*ee**2*complex(0,1)*RA2x1*sw**2*vev)/(2.*cw**2) + (ee**2*complex(0,1)*RA2x2*sinb*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = 'cosb*ee**2*complex(0,1)*RA3x1*vev + ee**2*complex(0,1)*RA3x2*sinb*vev + (cosb*cw**2*ee**2*complex(0,1)*RA3x1*vev)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*RA3x2*sinb*vev)/(2.*sw**2) + (cosb*ee**2*complex(0,1)*RA3x1*sw**2*vev)/(2.*cw**2) + (ee**2*complex(0,1)*RA3x2*sinb*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '(-3*complex(0,1)*Mh1**2*RA1x1**5)/(cosb*vev) - (3*complex(0,1)*m12**2*RA1x1**2*RA1x2)/(cosb*vev) - (3*complex(0,1)*Mh1**2*RA1x1**3*RA1x2**2)/(cosb*vev) - (3*complex(0,1)*Mh1**2*RA1x1**3*RA1x3**2)/(cosb*vev) - (3*complex(0,1)*Mh2**2*RA1x1**3*RA2x1**2)/(cosb*vev) - (3*complex(0,1)*Mh2**2*RA1x1**2*RA1x2*RA2x1*RA2x2)/(cosb*vev) - (3*complex(0,1)*Mh2**2*RA1x1**2*RA1x3*RA2x1*RA2x3)/(cosb*vev) - (3*complex(0,1)*MS**2*RA1x1**3*RA3x1**2)/(cosb*vev) - (3*complex(0,1)*MS**2*RA1x1**2*RA1x2*RA3x1*RA3x2)/(cosb*vev) - (3*complex(0,1)*MS**2*RA1x1**2*RA1x3*RA3x1*RA3x3)/(cosb*vev) + (3*cosb*complex(0,1)*m12**2*RA1x2**3)/(sinb**2*vev) - (3*complex(0,1)*m12**2*RA1x1*RA1x2**2)/(sinb*vev) - (3*complex(0,1)*Mh1**2*RA1x1**2*RA1x2**3)/(sinb*vev) - (3*complex(0,1)*Mh1**2*RA1x2**5)/(sinb*vev) - (3*complex(0,1)*Mh1**2*RA1x2**3*RA1x3**2)/(sinb*vev) - (3*complex(0,1)*Mh2**2*RA1x1*RA1x2**2*RA2x1*RA2x2)/(sinb*vev) - (3*complex(0,1)*Mh2**2*RA1x2**3*RA2x2**2)/(sinb*vev) - (3*complex(0,1)*Mh2**2*RA1x2**2*RA1x3*RA2x2*RA2x3)/(sinb*vev) - (3*complex(0,1)*MS**2*RA1x1*RA1x2**2*RA3x1*RA3x2)/(sinb*vev) - (3*complex(0,1)*MS**2*RA1x2**3*RA3x2**2)/(sinb*vev) - (3*complex(0,1)*MS**2*RA1x2**2*RA1x3*RA3x2*RA3x3)/(sinb*vev) + (3*complex(0,1)*m12**2*RA1x1**3*sinb)/(cosb**2*vev) - (3*complex(0,1)*Mh1**2*RA1x1**2*RA1x3**3)/vev3 - (3*complex(0,1)*Mh1**2*RA1x2**2*RA1x3**3)/vev3 - (3*complex(0,1)*Mh1**2*RA1x3**5)/vev3 - (3*complex(0,1)*Mh2**2*RA1x1*RA1x3**2*RA2x1*RA2x3)/vev3 - (3*complex(0,1)*Mh2**2*RA1x2*RA1x3**2*RA2x2*RA2x3)/vev3 - (3*complex(0,1)*Mh2**2*RA1x3**3*RA2x3**2)/vev3 - (3*complex(0,1)*MS**2*RA1x1*RA1x3**2*RA3x1*RA3x3)/vev3 - (3*complex(0,1)*MS**2*RA1x2*RA1x3**2*RA3x2*RA3x3)/vev3 - (3*complex(0,1)*MS**2*RA1x3**3*RA3x3**2)/vev3',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '(-3*complex(0,1)*Mh1**2*RA1x1**4*RA2x1)/(cosb*vev) - (2*complex(0,1)*m12**2*RA1x1*RA1x2*RA2x1)/(cosb*vev) - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x2**2*RA2x1)/(cosb*vev) - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x3**2*RA2x1)/(cosb*vev) - (3*complex(0,1)*Mh2**2*RA1x1**2*RA2x1**3)/(cosb*vev) - (complex(0,1)*m12**2*RA1x1**2*RA2x2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1**3*RA1x2*RA2x2)/(cosb*vev) - (2*complex(0,1)*Mh2**2*RA1x1*RA1x2*RA2x1**2*RA2x2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x1**2*RA2x1*RA2x2**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1**3*RA1x3*RA2x3)/(cosb*vev) - (2*complex(0,1)*Mh2**2*RA1x1*RA1x3*RA2x1**2*RA2x3)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x1**2*RA2x1*RA2x3**2)/(cosb*vev) - (3*complex(0,1)*MS**2*RA1x1**2*RA2x1*RA3x1**2)/(cosb*vev) - (2*complex(0,1)*MS**2*RA1x1*RA1x2*RA2x1*RA3x1*RA3x2)/(cosb*vev) - (complex(0,1)*MS**2*RA1x1**2*RA2x2*RA3x1*RA3x2)/(cosb*vev) - (2*complex(0,1)*MS**2*RA1x1*RA1x3*RA2x1*RA3x1*RA3x3)/(cosb*vev) - (complex(0,1)*MS**2*RA1x1**2*RA2x3*RA3x1*RA3x3)/(cosb*vev) + (3*cosb*complex(0,1)*m12**2*RA1x2**2*RA2x2)/(sinb**2*vev) - (complex(0,1)*m12**2*RA1x2**2*RA2x1)/(sinb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**3*RA2x1)/(sinb*vev) - (2*complex(0,1)*m12**2*RA1x1*RA1x2*RA2x2)/(sinb*vev) - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x2**2*RA2x2)/(sinb*vev) - (3*complex(0,1)*Mh1**2*RA1x2**4*RA2x2)/(sinb*vev) - (2*complex(0,1)*Mh1**2*RA1x2**2*RA1x3**2*RA2x2)/(sinb*vev) - (complex(0,1)*Mh2**2*RA1x2**2*RA2x1**2*RA2x2)/(sinb*vev) - (2*complex(0,1)*Mh2**2*RA1x1*RA1x2*RA2x1*RA2x2**2)/(sinb*vev) - (3*complex(0,1)*Mh2**2*RA1x2**2*RA2x2**3)/(sinb*vev) - (complex(0,1)*Mh1**2*RA1x2**3*RA1x3*RA2x3)/(sinb*vev) - (2*complex(0,1)*Mh2**2*RA1x2*RA1x3*RA2x2**2*RA2x3)/(sinb*vev) - (complex(0,1)*Mh2**2*RA1x2**2*RA2x2*RA2x3**2)/(sinb*vev) - (complex(0,1)*MS**2*RA1x2**2*RA2x1*RA3x1*RA3x2)/(sinb*vev) - (2*complex(0,1)*MS**2*RA1x1*RA1x2*RA2x2*RA3x1*RA3x2)/(sinb*vev) - (3*complex(0,1)*MS**2*RA1x2**2*RA2x2*RA3x2**2)/(sinb*vev) - (2*complex(0,1)*MS**2*RA1x2*RA1x3*RA2x2*RA3x2*RA3x3)/(sinb*vev) - (complex(0,1)*MS**2*RA1x2**2*RA2x3*RA3x2*RA3x3)/(sinb*vev) + (3*complex(0,1)*m12**2*RA1x1**2*RA2x1*sinb)/(cosb**2*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x3**3*RA2x1)/vev3 - (complex(0,1)*Mh1**2*RA1x2*RA1x3**3*RA2x2)/vev3 - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x3**2*RA2x3)/vev3 - (2*complex(0,1)*Mh1**2*RA1x2**2*RA1x3**2*RA2x3)/vev3 - (3*complex(0,1)*Mh1**2*RA1x3**4*RA2x3)/vev3 - (complex(0,1)*Mh2**2*RA1x3**2*RA2x1**2*RA2x3)/vev3 - (complex(0,1)*Mh2**2*RA1x3**2*RA2x2**2*RA2x3)/vev3 - (2*complex(0,1)*Mh2**2*RA1x1*RA1x3*RA2x1*RA2x3**2)/vev3 - (2*complex(0,1)*Mh2**2*RA1x2*RA1x3*RA2x2*RA2x3**2)/vev3 - (3*complex(0,1)*Mh2**2*RA1x3**2*RA2x3**3)/vev3 - (complex(0,1)*MS**2*RA1x3**2*RA2x1*RA3x1*RA3x3)/vev3 - (2*complex(0,1)*MS**2*RA1x1*RA1x3*RA2x3*RA3x1*RA3x3)/vev3 - (complex(0,1)*MS**2*RA1x3**2*RA2x2*RA3x2*RA3x3)/vev3 - (2*complex(0,1)*MS**2*RA1x2*RA1x3*RA2x3*RA3x2*RA3x3)/vev3 - (3*complex(0,1)*MS**2*RA1x3**2*RA2x3*RA3x3**2)/vev3',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '(-3*complex(0,1)*Mh1**2*RA1x1**3*RA2x1**2)/(cosb*vev) - (complex(0,1)*m12**2*RA1x2*RA2x1**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**2*RA2x1**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x3**2*RA2x1**2)/(cosb*vev) - (3*complex(0,1)*Mh2**2*RA1x1*RA2x1**4)/(cosb*vev) - (2*complex(0,1)*m12**2*RA1x1*RA2x1*RA2x2)/(cosb*vev) - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x2*RA2x1*RA2x2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x2*RA2x1**3*RA2x2)/(cosb*vev) - (2*complex(0,1)*Mh2**2*RA1x1*RA2x1**2*RA2x2**2)/(cosb*vev) - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x3*RA2x1*RA2x3)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x3*RA2x1**3*RA2x3)/(cosb*vev) - (2*complex(0,1)*Mh2**2*RA1x1*RA2x1**2*RA2x3**2)/(cosb*vev) - (3*complex(0,1)*MS**2*RA1x1*RA2x1**2*RA3x1**2)/(cosb*vev) - (complex(0,1)*MS**2*RA1x2*RA2x1**2*RA3x1*RA3x2)/(cosb*vev) - (2*complex(0,1)*MS**2*RA1x1*RA2x1*RA2x2*RA3x1*RA3x2)/(cosb*vev) - (complex(0,1)*MS**2*RA1x3*RA2x1**2*RA3x1*RA3x3)/(cosb*vev) - (2*complex(0,1)*MS**2*RA1x1*RA2x1*RA2x3*RA3x1*RA3x3)/(cosb*vev) + (3*cosb*complex(0,1)*m12**2*RA1x2*RA2x2**2)/(sinb**2*vev) - (2*complex(0,1)*m12**2*RA1x2*RA2x1*RA2x2)/(sinb*vev) - (2*complex(0,1)*Mh1**2*RA1x1*RA1x2**2*RA2x1*RA2x2)/(sinb*vev) - (complex(0,1)*m12**2*RA1x1*RA2x2**2)/(sinb*vev) - (complex(0,1)*Mh1**2*RA1x1**2*RA1x2*RA2x2**2)/(sinb*vev) - (3*complex(0,1)*Mh1**2*RA1x2**3*RA2x2**2)/(sinb*vev) - (complex(0,1)*Mh1**2*RA1x2*RA1x3**2*RA2x2**2)/(sinb*vev) - (2*complex(0,1)*Mh2**2*RA1x2*RA2x1**2*RA2x2**2)/(sinb*vev) - (complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x2**3)/(sinb*vev) - (3*complex(0,1)*Mh2**2*RA1x2*RA2x2**4)/(sinb*vev) - (2*complex(0,1)*Mh1**2*RA1x2**2*RA1x3*RA2x2*RA2x3)/(sinb*vev) - (complex(0,1)*Mh2**2*RA1x3*RA2x2**3*RA2x3)/(sinb*vev) - (2*complex(0,1)*Mh2**2*RA1x2*RA2x2**2*RA2x3**2)/(sinb*vev) - (2*complex(0,1)*MS**2*RA1x2*RA2x1*RA2x2*RA3x1*RA3x2)/(sinb*vev) - (complex(0,1)*MS**2*RA1x1*RA2x2**2*RA3x1*RA3x2)/(sinb*vev) - (3*complex(0,1)*MS**2*RA1x2*RA2x2**2*RA3x2**2)/(sinb*vev) - (complex(0,1)*MS**2*RA1x3*RA2x2**2*RA3x2*RA3x3)/(sinb*vev) - (2*complex(0,1)*MS**2*RA1x2*RA2x2*RA2x3*RA3x2*RA3x3)/(sinb*vev) + (3*complex(0,1)*m12**2*RA1x1*RA2x1**2*sinb)/(cosb**2*vev) - (2*complex(0,1)*Mh1**2*RA1x1*RA1x3**2*RA2x1*RA2x3)/vev3 - (2*complex(0,1)*Mh1**2*RA1x2*RA1x3**2*RA2x2*RA2x3)/vev3 - (complex(0,1)*Mh1**2*RA1x1**2*RA1x3*RA2x3**2)/vev3 - (complex(0,1)*Mh1**2*RA1x2**2*RA1x3*RA2x3**2)/vev3 - (3*complex(0,1)*Mh1**2*RA1x3**3*RA2x3**2)/vev3 - (2*complex(0,1)*Mh2**2*RA1x3*RA2x1**2*RA2x3**2)/vev3 - (2*complex(0,1)*Mh2**2*RA1x3*RA2x2**2*RA2x3**2)/vev3 - (complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x3**3)/vev3 - (complex(0,1)*Mh2**2*RA1x2*RA2x2*RA2x3**3)/vev3 - (3*complex(0,1)*Mh2**2*RA1x3*RA2x3**4)/vev3 - (2*complex(0,1)*MS**2*RA1x3*RA2x1*RA2x3*RA3x1*RA3x3)/vev3 - (complex(0,1)*MS**2*RA1x1*RA2x3**2*RA3x1*RA3x3)/vev3 - (2*complex(0,1)*MS**2*RA1x3*RA2x2*RA2x3*RA3x2*RA3x3)/vev3 - (complex(0,1)*MS**2*RA1x2*RA2x3**2*RA3x2*RA3x3)/vev3 - (3*complex(0,1)*MS**2*RA1x3*RA2x3**2*RA3x3**2)/vev3',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '(-3*complex(0,1)*Mh1**2*RA1x1**2*RA2x1**3)/(cosb*vev) - (3*complex(0,1)*Mh2**2*RA2x1**5)/(cosb*vev) - (3*complex(0,1)*m12**2*RA2x1**2*RA2x2)/(cosb*vev) - (3*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1**2*RA2x2)/(cosb*vev) - (3*complex(0,1)*Mh2**2*RA2x1**3*RA2x2**2)/(cosb*vev) - (3*complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x1**2*RA2x3)/(cosb*vev) - (3*complex(0,1)*Mh2**2*RA2x1**3*RA2x3**2)/(cosb*vev) - (3*complex(0,1)*MS**2*RA2x1**3*RA3x1**2)/(cosb*vev) - (3*complex(0,1)*MS**2*RA2x1**2*RA2x2*RA3x1*RA3x2)/(cosb*vev) - (3*complex(0,1)*MS**2*RA2x1**2*RA2x3*RA3x1*RA3x3)/(cosb*vev) + (3*cosb*complex(0,1)*m12**2*RA2x2**3)/(sinb**2*vev) - (3*complex(0,1)*m12**2*RA2x1*RA2x2**2)/(sinb*vev) - (3*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1*RA2x2**2)/(sinb*vev) - (3*complex(0,1)*Mh1**2*RA1x2**2*RA2x2**3)/(sinb*vev) - (3*complex(0,1)*Mh2**2*RA2x1**2*RA2x2**3)/(sinb*vev) - (3*complex(0,1)*Mh2**2*RA2x2**5)/(sinb*vev) - (3*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x2**2*RA2x3)/(sinb*vev) - (3*complex(0,1)*Mh2**2*RA2x2**3*RA2x3**2)/(sinb*vev) - (3*complex(0,1)*MS**2*RA2x1*RA2x2**2*RA3x1*RA3x2)/(sinb*vev) - (3*complex(0,1)*MS**2*RA2x2**3*RA3x2**2)/(sinb*vev) - (3*complex(0,1)*MS**2*RA2x2**2*RA2x3*RA3x2*RA3x3)/(sinb*vev) + (3*complex(0,1)*m12**2*RA2x1**3*sinb)/(cosb**2*vev) - (3*complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x1*RA2x3**2)/vev3 - (3*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x2*RA2x3**2)/vev3 - (3*complex(0,1)*Mh1**2*RA1x3**2*RA2x3**3)/vev3 - (3*complex(0,1)*Mh2**2*RA2x1**2*RA2x3**3)/vev3 - (3*complex(0,1)*Mh2**2*RA2x2**2*RA2x3**3)/vev3 - (3*complex(0,1)*Mh2**2*RA2x3**5)/vev3 - (3*complex(0,1)*MS**2*RA2x1*RA2x3**2*RA3x1*RA3x3)/vev3 - (3*complex(0,1)*MS**2*RA2x2*RA2x3**2*RA3x2*RA3x3)/vev3 - (3*complex(0,1)*MS**2*RA2x3**3*RA3x3**2)/vev3',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '(-3*complex(0,1)*Mh1**2*RA1x1**4*RA3x1)/(cosb*vev) - (2*complex(0,1)*m12**2*RA1x1*RA1x2*RA3x1)/(cosb*vev) - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x2**2*RA3x1)/(cosb*vev) - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x3**2*RA3x1)/(cosb*vev) - (3*complex(0,1)*Mh2**2*RA1x1**2*RA2x1**2*RA3x1)/(cosb*vev) - (2*complex(0,1)*Mh2**2*RA1x1*RA1x2*RA2x1*RA2x2*RA3x1)/(cosb*vev) - (2*complex(0,1)*Mh2**2*RA1x1*RA1x3*RA2x1*RA2x3*RA3x1)/(cosb*vev) - (3*complex(0,1)*MS**2*RA1x1**2*RA3x1**3)/(cosb*vev) - (complex(0,1)*m12**2*RA1x1**2*RA3x2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1**3*RA1x2*RA3x2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x1**2*RA2x1*RA2x2*RA3x2)/(cosb*vev) - (2*complex(0,1)*MS**2*RA1x1*RA1x2*RA3x1**2*RA3x2)/(cosb*vev) - (complex(0,1)*MS**2*RA1x1**2*RA3x1*RA3x2**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1**3*RA1x3*RA3x3)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x1**2*RA2x1*RA2x3*RA3x3)/(cosb*vev) - (2*complex(0,1)*MS**2*RA1x1*RA1x3*RA3x1**2*RA3x3)/(cosb*vev) - (complex(0,1)*MS**2*RA1x1**2*RA3x1*RA3x3**2)/(cosb*vev) + (3*cosb*complex(0,1)*m12**2*RA1x2**2*RA3x2)/(sinb**2*vev) - (complex(0,1)*m12**2*RA1x2**2*RA3x1)/(sinb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**3*RA3x1)/(sinb*vev) - (complex(0,1)*Mh2**2*RA1x2**2*RA2x1*RA2x2*RA3x1)/(sinb*vev) - (2*complex(0,1)*m12**2*RA1x1*RA1x2*RA3x2)/(sinb*vev) - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x2**2*RA3x2)/(sinb*vev) - (3*complex(0,1)*Mh1**2*RA1x2**4*RA3x2)/(sinb*vev) - (2*complex(0,1)*Mh1**2*RA1x2**2*RA1x3**2*RA3x2)/(sinb*vev) - (2*complex(0,1)*Mh2**2*RA1x1*RA1x2*RA2x1*RA2x2*RA3x2)/(sinb*vev) - (3*complex(0,1)*Mh2**2*RA1x2**2*RA2x2**2*RA3x2)/(sinb*vev) - (2*complex(0,1)*Mh2**2*RA1x2*RA1x3*RA2x2*RA2x3*RA3x2)/(sinb*vev) - (complex(0,1)*MS**2*RA1x2**2*RA3x1**2*RA3x2)/(sinb*vev) - (2*complex(0,1)*MS**2*RA1x1*RA1x2*RA3x1*RA3x2**2)/(sinb*vev) - (3*complex(0,1)*MS**2*RA1x2**2*RA3x2**3)/(sinb*vev) - (complex(0,1)*Mh1**2*RA1x2**3*RA1x3*RA3x3)/(sinb*vev) - (complex(0,1)*Mh2**2*RA1x2**2*RA2x2*RA2x3*RA3x3)/(sinb*vev) - (2*complex(0,1)*MS**2*RA1x2*RA1x3*RA3x2**2*RA3x3)/(sinb*vev) - (complex(0,1)*MS**2*RA1x2**2*RA3x2*RA3x3**2)/(sinb*vev) + (3*complex(0,1)*m12**2*RA1x1**2*RA3x1*sinb)/(cosb**2*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x3**3*RA3x1)/vev3 - (complex(0,1)*Mh2**2*RA1x3**2*RA2x1*RA2x3*RA3x1)/vev3 - (complex(0,1)*Mh1**2*RA1x2*RA1x3**3*RA3x2)/vev3 - (complex(0,1)*Mh2**2*RA1x3**2*RA2x2*RA2x3*RA3x2)/vev3 - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x3**2*RA3x3)/vev3 - (2*complex(0,1)*Mh1**2*RA1x2**2*RA1x3**2*RA3x3)/vev3 - (3*complex(0,1)*Mh1**2*RA1x3**4*RA3x3)/vev3 - (2*complex(0,1)*Mh2**2*RA1x1*RA1x3*RA2x1*RA2x3*RA3x3)/vev3 - (2*complex(0,1)*Mh2**2*RA1x2*RA1x3*RA2x2*RA2x3*RA3x3)/vev3 - (3*complex(0,1)*Mh2**2*RA1x3**2*RA2x3**2*RA3x3)/vev3 - (complex(0,1)*MS**2*RA1x3**2*RA3x1**2*RA3x3)/vev3 - (complex(0,1)*MS**2*RA1x3**2*RA3x2**2*RA3x3)/vev3 - (2*complex(0,1)*MS**2*RA1x1*RA1x3*RA3x1*RA3x3**2)/vev3 - (2*complex(0,1)*MS**2*RA1x2*RA1x3*RA3x2*RA3x3**2)/vev3 - (3*complex(0,1)*MS**2*RA1x3**2*RA3x3**3)/vev3',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '(-3*complex(0,1)*Mh1**2*RA1x1**3*RA2x1*RA3x1)/(cosb*vev) - (complex(0,1)*m12**2*RA1x2*RA2x1*RA3x1)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**2*RA2x1*RA3x1)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x3**2*RA2x1*RA3x1)/(cosb*vev) - (3*complex(0,1)*Mh2**2*RA1x1*RA2x1**3*RA3x1)/(cosb*vev) - (complex(0,1)*m12**2*RA1x1*RA2x2*RA3x1)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1**2*RA1x2*RA2x2*RA3x1)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x2*RA2x1**2*RA2x2*RA3x1)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x2**2*RA3x1)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1**2*RA1x3*RA2x3*RA3x1)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x3*RA2x1**2*RA2x3*RA3x1)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x3**2*RA3x1)/(cosb*vev) - (3*complex(0,1)*MS**2*RA1x1*RA2x1*RA3x1**3)/(cosb*vev) - (complex(0,1)*m12**2*RA1x1*RA2x1*RA3x2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1**2*RA1x2*RA2x1*RA3x2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x1*RA2x1**2*RA2x2*RA3x2)/(cosb*vev) - (complex(0,1)*MS**2*RA1x2*RA2x1*RA3x1**2*RA3x2)/(cosb*vev) - (complex(0,1)*MS**2*RA1x1*RA2x2*RA3x1**2*RA3x2)/(cosb*vev) - (complex(0,1)*MS**2*RA1x1*RA2x1*RA3x1*RA3x2**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1**2*RA1x3*RA2x1*RA3x3)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x1*RA2x1**2*RA2x3*RA3x3)/(cosb*vev) - (complex(0,1)*MS**2*RA1x3*RA2x1*RA3x1**2*RA3x3)/(cosb*vev) - (complex(0,1)*MS**2*RA1x1*RA2x3*RA3x1**2*RA3x3)/(cosb*vev) - (complex(0,1)*MS**2*RA1x1*RA2x1*RA3x1*RA3x3**2)/(cosb*vev) + (3*cosb*complex(0,1)*m12**2*RA1x2*RA2x2*RA3x2)/(sinb**2*vev) - (complex(0,1)*m12**2*RA1x2*RA2x2*RA3x1)/(sinb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**2*RA2x2*RA3x1)/(sinb*vev) - (complex(0,1)*Mh2**2*RA1x2*RA2x1*RA2x2**2*RA3x1)/(sinb*vev) - (complex(0,1)*m12**2*RA1x2*RA2x1*RA3x2)/(sinb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**2*RA2x1*RA3x2)/(sinb*vev) - (complex(0,1)*m12**2*RA1x1*RA2x2*RA3x2)/(sinb*vev) - (complex(0,1)*Mh1**2*RA1x1**2*RA1x2*RA2x2*RA3x2)/(sinb*vev) - (3*complex(0,1)*Mh1**2*RA1x2**3*RA2x2*RA3x2)/(sinb*vev) - (complex(0,1)*Mh1**2*RA1x2*RA1x3**2*RA2x2*RA3x2)/(sinb*vev) - (complex(0,1)*Mh2**2*RA1x2*RA2x1**2*RA2x2*RA3x2)/(sinb*vev) - (complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x2**2*RA3x2)/(sinb*vev) - (3*complex(0,1)*Mh2**2*RA1x2*RA2x2**3*RA3x2)/(sinb*vev) - (complex(0,1)*Mh1**2*RA1x2**2*RA1x3*RA2x3*RA3x2)/(sinb*vev) - (complex(0,1)*Mh2**2*RA1x3*RA2x2**2*RA2x3*RA3x2)/(sinb*vev) - (complex(0,1)*Mh2**2*RA1x2*RA2x2*RA2x3**2*RA3x2)/(sinb*vev) - (complex(0,1)*MS**2*RA1x2*RA2x2*RA3x1**2*RA3x2)/(sinb*vev) - (complex(0,1)*MS**2*RA1x2*RA2x1*RA3x1*RA3x2**2)/(sinb*vev) - (complex(0,1)*MS**2*RA1x1*RA2x2*RA3x1*RA3x2**2)/(sinb*vev) - (3*complex(0,1)*MS**2*RA1x2*RA2x2*RA3x2**3)/(sinb*vev) - (complex(0,1)*Mh1**2*RA1x2**2*RA1x3*RA2x2*RA3x3)/(sinb*vev) - (complex(0,1)*Mh2**2*RA1x2*RA2x2**2*RA2x3*RA3x3)/(sinb*vev) - (complex(0,1)*MS**2*RA1x3*RA2x2*RA3x2**2*RA3x3)/(sinb*vev) - (complex(0,1)*MS**2*RA1x2*RA2x3*RA3x2**2*RA3x3)/(sinb*vev) - (complex(0,1)*MS**2*RA1x2*RA2x2*RA3x2*RA3x3**2)/(sinb*vev) + (3*complex(0,1)*m12**2*RA1x1*RA2x1*RA3x1*sinb)/(cosb**2*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x3**2*RA2x3*RA3x1)/vev3 - (complex(0,1)*Mh2**2*RA1x3*RA2x1*RA2x3**2*RA3x1)/vev3 - (complex(0,1)*Mh1**2*RA1x2*RA1x3**2*RA2x3*RA3x2)/vev3 - (complex(0,1)*Mh2**2*RA1x3*RA2x2*RA2x3**2*RA3x2)/vev3 - (complex(0,1)*Mh1**2*RA1x1*RA1x3**2*RA2x1*RA3x3)/vev3 - (complex(0,1)*Mh1**2*RA1x2*RA1x3**2*RA2x2*RA3x3)/vev3 - (complex(0,1)*Mh1**2*RA1x1**2*RA1x3*RA2x3*RA3x3)/vev3 - (complex(0,1)*Mh1**2*RA1x2**2*RA1x3*RA2x3*RA3x3)/vev3 - (3*complex(0,1)*Mh1**2*RA1x3**3*RA2x3*RA3x3)/vev3 - (complex(0,1)*Mh2**2*RA1x3*RA2x1**2*RA2x3*RA3x3)/vev3 - (complex(0,1)*Mh2**2*RA1x3*RA2x2**2*RA2x3*RA3x3)/vev3 - (complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x3**2*RA3x3)/vev3 - (complex(0,1)*Mh2**2*RA1x2*RA2x2*RA2x3**2*RA3x3)/vev3 - (3*complex(0,1)*Mh2**2*RA1x3*RA2x3**3*RA3x3)/vev3 - (complex(0,1)*MS**2*RA1x3*RA2x3*RA3x1**2*RA3x3)/vev3 - (complex(0,1)*MS**2*RA1x3*RA2x3*RA3x2**2*RA3x3)/vev3 - (complex(0,1)*MS**2*RA1x3*RA2x1*RA3x1*RA3x3**2)/vev3 - (complex(0,1)*MS**2*RA1x1*RA2x3*RA3x1*RA3x3**2)/vev3 - (complex(0,1)*MS**2*RA1x3*RA2x2*RA3x2*RA3x3**2)/vev3 - (complex(0,1)*MS**2*RA1x2*RA2x3*RA3x2*RA3x3**2)/vev3 - (3*complex(0,1)*MS**2*RA1x3*RA2x3*RA3x3**3)/vev3',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '(-3*complex(0,1)*Mh1**2*RA1x1**2*RA2x1**2*RA3x1)/(cosb*vev) - (3*complex(0,1)*Mh2**2*RA2x1**4*RA3x1)/(cosb*vev) - (2*complex(0,1)*m12**2*RA2x1*RA2x2*RA3x1)/(cosb*vev) - (2*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1*RA2x2*RA3x1)/(cosb*vev) - (2*complex(0,1)*Mh2**2*RA2x1**2*RA2x2**2*RA3x1)/(cosb*vev) - (2*complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x1*RA2x3*RA3x1)/(cosb*vev) - (2*complex(0,1)*Mh2**2*RA2x1**2*RA2x3**2*RA3x1)/(cosb*vev) - (3*complex(0,1)*MS**2*RA2x1**2*RA3x1**3)/(cosb*vev) - (complex(0,1)*m12**2*RA2x1**2*RA3x2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1**2*RA3x2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA2x1**3*RA2x2*RA3x2)/(cosb*vev) - (2*complex(0,1)*MS**2*RA2x1*RA2x2*RA3x1**2*RA3x2)/(cosb*vev) - (complex(0,1)*MS**2*RA2x1**2*RA3x1*RA3x2**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x1**2*RA3x3)/(cosb*vev) - (complex(0,1)*Mh2**2*RA2x1**3*RA2x3*RA3x3)/(cosb*vev) - (2*complex(0,1)*MS**2*RA2x1*RA2x3*RA3x1**2*RA3x3)/(cosb*vev) - (complex(0,1)*MS**2*RA2x1**2*RA3x1*RA3x3**2)/(cosb*vev) + (3*cosb*complex(0,1)*m12**2*RA2x2**2*RA3x2)/(sinb**2*vev) - (complex(0,1)*m12**2*RA2x2**2*RA3x1)/(sinb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x2**2*RA3x1)/(sinb*vev) - (complex(0,1)*Mh2**2*RA2x1*RA2x2**3*RA3x1)/(sinb*vev) - (2*complex(0,1)*m12**2*RA2x1*RA2x2*RA3x2)/(sinb*vev) - (2*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1*RA2x2*RA3x2)/(sinb*vev) - (3*complex(0,1)*Mh1**2*RA1x2**2*RA2x2**2*RA3x2)/(sinb*vev) - (2*complex(0,1)*Mh2**2*RA2x1**2*RA2x2**2*RA3x2)/(sinb*vev) - (3*complex(0,1)*Mh2**2*RA2x2**4*RA3x2)/(sinb*vev) - (2*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x2*RA2x3*RA3x2)/(sinb*vev) - (2*complex(0,1)*Mh2**2*RA2x2**2*RA2x3**2*RA3x2)/(sinb*vev) - (complex(0,1)*MS**2*RA2x2**2*RA3x1**2*RA3x2)/(sinb*vev) - (2*complex(0,1)*MS**2*RA2x1*RA2x2*RA3x1*RA3x2**2)/(sinb*vev) - (3*complex(0,1)*MS**2*RA2x2**2*RA3x2**3)/(sinb*vev) - (complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x2**2*RA3x3)/(sinb*vev) - (complex(0,1)*Mh2**2*RA2x2**3*RA2x3*RA3x3)/(sinb*vev) - (2*complex(0,1)*MS**2*RA2x2*RA2x3*RA3x2**2*RA3x3)/(sinb*vev) - (complex(0,1)*MS**2*RA2x2**2*RA3x2*RA3x3**2)/(sinb*vev) + (3*complex(0,1)*m12**2*RA2x1**2*RA3x1*sinb)/(cosb**2*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x3**2*RA3x1)/vev3 - (complex(0,1)*Mh2**2*RA2x1*RA2x3**3*RA3x1)/vev3 - (complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x3**2*RA3x2)/vev3 - (complex(0,1)*Mh2**2*RA2x2*RA2x3**3*RA3x2)/vev3 - (2*complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x1*RA2x3*RA3x3)/vev3 - (2*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x2*RA2x3*RA3x3)/vev3 - (3*complex(0,1)*Mh1**2*RA1x3**2*RA2x3**2*RA3x3)/vev3 - (2*complex(0,1)*Mh2**2*RA2x1**2*RA2x3**2*RA3x3)/vev3 - (2*complex(0,1)*Mh2**2*RA2x2**2*RA2x3**2*RA3x3)/vev3 - (3*complex(0,1)*Mh2**2*RA2x3**4*RA3x3)/vev3 - (complex(0,1)*MS**2*RA2x3**2*RA3x1**2*RA3x3)/vev3 - (complex(0,1)*MS**2*RA2x3**2*RA3x2**2*RA3x3)/vev3 - (2*complex(0,1)*MS**2*RA2x1*RA2x3*RA3x1*RA3x3**2)/vev3 - (2*complex(0,1)*MS**2*RA2x2*RA2x3*RA3x2*RA3x3**2)/vev3 - (3*complex(0,1)*MS**2*RA2x3**2*RA3x3**3)/vev3',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '(-3*complex(0,1)*Mh1**2*RA1x1**3*RA3x1**2)/(cosb*vev) - (complex(0,1)*m12**2*RA1x2*RA3x1**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**2*RA3x1**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x3**2*RA3x1**2)/(cosb*vev) - (3*complex(0,1)*Mh2**2*RA1x1*RA2x1**2*RA3x1**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x2*RA2x1*RA2x2*RA3x1**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA1x3*RA2x1*RA2x3*RA3x1**2)/(cosb*vev) - (3*complex(0,1)*MS**2*RA1x1*RA3x1**4)/(cosb*vev) - (2*complex(0,1)*m12**2*RA1x1*RA3x1*RA3x2)/(cosb*vev) - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x2*RA3x1*RA3x2)/(cosb*vev) - (2*complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x2*RA3x1*RA3x2)/(cosb*vev) - (complex(0,1)*MS**2*RA1x2*RA3x1**3*RA3x2)/(cosb*vev) - (2*complex(0,1)*MS**2*RA1x1*RA3x1**2*RA3x2**2)/(cosb*vev) - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x3*RA3x1*RA3x3)/(cosb*vev) - (2*complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x3*RA3x1*RA3x3)/(cosb*vev) - (complex(0,1)*MS**2*RA1x3*RA3x1**3*RA3x3)/(cosb*vev) - (2*complex(0,1)*MS**2*RA1x1*RA3x1**2*RA3x3**2)/(cosb*vev) + (3*cosb*complex(0,1)*m12**2*RA1x2*RA3x2**2)/(sinb**2*vev) - (2*complex(0,1)*m12**2*RA1x2*RA3x1*RA3x2)/(sinb*vev) - (2*complex(0,1)*Mh1**2*RA1x1*RA1x2**2*RA3x1*RA3x2)/(sinb*vev) - (2*complex(0,1)*Mh2**2*RA1x2*RA2x1*RA2x2*RA3x1*RA3x2)/(sinb*vev) - (complex(0,1)*m12**2*RA1x1*RA3x2**2)/(sinb*vev) - (complex(0,1)*Mh1**2*RA1x1**2*RA1x2*RA3x2**2)/(sinb*vev) - (3*complex(0,1)*Mh1**2*RA1x2**3*RA3x2**2)/(sinb*vev) - (complex(0,1)*Mh1**2*RA1x2*RA1x3**2*RA3x2**2)/(sinb*vev) - (complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x2*RA3x2**2)/(sinb*vev) - (3*complex(0,1)*Mh2**2*RA1x2*RA2x2**2*RA3x2**2)/(sinb*vev) - (complex(0,1)*Mh2**2*RA1x3*RA2x2*RA2x3*RA3x2**2)/(sinb*vev) - (2*complex(0,1)*MS**2*RA1x2*RA3x1**2*RA3x2**2)/(sinb*vev) - (complex(0,1)*MS**2*RA1x1*RA3x1*RA3x2**3)/(sinb*vev) - (3*complex(0,1)*MS**2*RA1x2*RA3x2**4)/(sinb*vev) - (2*complex(0,1)*Mh1**2*RA1x2**2*RA1x3*RA3x2*RA3x3)/(sinb*vev) - (2*complex(0,1)*Mh2**2*RA1x2*RA2x2*RA2x3*RA3x2*RA3x3)/(sinb*vev) - (complex(0,1)*MS**2*RA1x3*RA3x2**3*RA3x3)/(sinb*vev) - (2*complex(0,1)*MS**2*RA1x2*RA3x2**2*RA3x3**2)/(sinb*vev) + (3*complex(0,1)*m12**2*RA1x1*RA3x1**2*sinb)/(cosb**2*vev) - (2*complex(0,1)*Mh1**2*RA1x1*RA1x3**2*RA3x1*RA3x3)/vev3 - (2*complex(0,1)*Mh2**2*RA1x3*RA2x1*RA2x3*RA3x1*RA3x3)/vev3 - (2*complex(0,1)*Mh1**2*RA1x2*RA1x3**2*RA3x2*RA3x3)/vev3 - (2*complex(0,1)*Mh2**2*RA1x3*RA2x2*RA2x3*RA3x2*RA3x3)/vev3 - (complex(0,1)*Mh1**2*RA1x1**2*RA1x3*RA3x3**2)/vev3 - (complex(0,1)*Mh1**2*RA1x2**2*RA1x3*RA3x3**2)/vev3 - (3*complex(0,1)*Mh1**2*RA1x3**3*RA3x3**2)/vev3 - (complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x3*RA3x3**2)/vev3 - (complex(0,1)*Mh2**2*RA1x2*RA2x2*RA2x3*RA3x3**2)/vev3 - (3*complex(0,1)*Mh2**2*RA1x3*RA2x3**2*RA3x3**2)/vev3 - (2*complex(0,1)*MS**2*RA1x3*RA3x1**2*RA3x3**2)/vev3 - (2*complex(0,1)*MS**2*RA1x3*RA3x2**2*RA3x3**2)/vev3 - (complex(0,1)*MS**2*RA1x1*RA3x1*RA3x3**3)/vev3 - (complex(0,1)*MS**2*RA1x2*RA3x2*RA3x3**3)/vev3 - (3*complex(0,1)*MS**2*RA1x3*RA3x3**4)/vev3',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '(-3*complex(0,1)*Mh1**2*RA1x1**2*RA2x1*RA3x1**2)/(cosb*vev) - (3*complex(0,1)*Mh2**2*RA2x1**3*RA3x1**2)/(cosb*vev) - (complex(0,1)*m12**2*RA2x2*RA3x1**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x2*RA3x1**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA2x1*RA2x2**2*RA3x1**2)/(cosb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x3*RA3x1**2)/(cosb*vev) - (complex(0,1)*Mh2**2*RA2x1*RA2x3**2*RA3x1**2)/(cosb*vev) - (3*complex(0,1)*MS**2*RA2x1*RA3x1**4)/(cosb*vev) - (2*complex(0,1)*m12**2*RA2x1*RA3x1*RA3x2)/(cosb*vev) - (2*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1*RA3x1*RA3x2)/(cosb*vev) - (2*complex(0,1)*Mh2**2*RA2x1**2*RA2x2*RA3x1*RA3x2)/(cosb*vev) - (complex(0,1)*MS**2*RA2x2*RA3x1**3*RA3x2)/(cosb*vev) - (2*complex(0,1)*MS**2*RA2x1*RA3x1**2*RA3x2**2)/(cosb*vev) - (2*complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x1*RA3x1*RA3x3)/(cosb*vev) - (2*complex(0,1)*Mh2**2*RA2x1**2*RA2x3*RA3x1*RA3x3)/(cosb*vev) - (complex(0,1)*MS**2*RA2x3*RA3x1**3*RA3x3)/(cosb*vev) - (2*complex(0,1)*MS**2*RA2x1*RA3x1**2*RA3x3**2)/(cosb*vev) + (3*cosb*complex(0,1)*m12**2*RA2x2*RA3x2**2)/(sinb**2*vev) - (2*complex(0,1)*m12**2*RA2x2*RA3x1*RA3x2)/(sinb*vev) - (2*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x2*RA3x1*RA3x2)/(sinb*vev) - (2*complex(0,1)*Mh2**2*RA2x1*RA2x2**2*RA3x1*RA3x2)/(sinb*vev) - (complex(0,1)*m12**2*RA2x1*RA3x2**2)/(sinb*vev) - (complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1*RA3x2**2)/(sinb*vev) - (3*complex(0,1)*Mh1**2*RA1x2**2*RA2x2*RA3x2**2)/(sinb*vev) - (complex(0,1)*Mh2**2*RA2x1**2*RA2x2*RA3x2**2)/(sinb*vev) - (3*complex(0,1)*Mh2**2*RA2x2**3*RA3x2**2)/(sinb*vev) - (complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x3*RA3x2**2)/(sinb*vev) - (complex(0,1)*Mh2**2*RA2x2*RA2x3**2*RA3x2**2)/(sinb*vev) - (2*complex(0,1)*MS**2*RA2x2*RA3x1**2*RA3x2**2)/(sinb*vev) - (complex(0,1)*MS**2*RA2x1*RA3x1*RA3x2**3)/(sinb*vev) - (3*complex(0,1)*MS**2*RA2x2*RA3x2**4)/(sinb*vev) - (2*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x2*RA3x2*RA3x3)/(sinb*vev) - (2*complex(0,1)*Mh2**2*RA2x2**2*RA2x3*RA3x2*RA3x3)/(sinb*vev) - (complex(0,1)*MS**2*RA2x3*RA3x2**3*RA3x3)/(sinb*vev) - (2*complex(0,1)*MS**2*RA2x2*RA3x2**2*RA3x3**2)/(sinb*vev) + (3*complex(0,1)*m12**2*RA2x1*RA3x1**2*sinb)/(cosb**2*vev) - (2*complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x3*RA3x1*RA3x3)/vev3 - (2*complex(0,1)*Mh2**2*RA2x1*RA2x3**2*RA3x1*RA3x3)/vev3 - (2*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x3*RA3x2*RA3x3)/vev3 - (2*complex(0,1)*Mh2**2*RA2x2*RA2x3**2*RA3x2*RA3x3)/vev3 - (complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x1*RA3x3**2)/vev3 - (complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x2*RA3x3**2)/vev3 - (3*complex(0,1)*Mh1**2*RA1x3**2*RA2x3*RA3x3**2)/vev3 - (complex(0,1)*Mh2**2*RA2x1**2*RA2x3*RA3x3**2)/vev3 - (complex(0,1)*Mh2**2*RA2x2**2*RA2x3*RA3x3**2)/vev3 - (3*complex(0,1)*Mh2**2*RA2x3**3*RA3x3**2)/vev3 - (2*complex(0,1)*MS**2*RA2x3*RA3x1**2*RA3x3**2)/vev3 - (2*complex(0,1)*MS**2*RA2x3*RA3x2**2*RA3x3**2)/vev3 - (complex(0,1)*MS**2*RA2x1*RA3x1*RA3x3**3)/vev3 - (complex(0,1)*MS**2*RA2x2*RA3x2*RA3x3**3)/vev3 - (3*complex(0,1)*MS**2*RA2x3*RA3x3**4)/vev3',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '(-3*complex(0,1)*Mh1**2*RA1x1**2*RA3x1**3)/(cosb*vev) - (3*complex(0,1)*Mh2**2*RA2x1**2*RA3x1**3)/(cosb*vev) - (3*complex(0,1)*MS**2*RA3x1**5)/(cosb*vev) - (3*complex(0,1)*m12**2*RA3x1**2*RA3x2)/(cosb*vev) - (3*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA3x1**2*RA3x2)/(cosb*vev) - (3*complex(0,1)*Mh2**2*RA2x1*RA2x2*RA3x1**2*RA3x2)/(cosb*vev) - (3*complex(0,1)*MS**2*RA3x1**3*RA3x2**2)/(cosb*vev) - (3*complex(0,1)*Mh1**2*RA1x1*RA1x3*RA3x1**2*RA3x3)/(cosb*vev) - (3*complex(0,1)*Mh2**2*RA2x1*RA2x3*RA3x1**2*RA3x3)/(cosb*vev) - (3*complex(0,1)*MS**2*RA3x1**3*RA3x3**2)/(cosb*vev) + (3*cosb*complex(0,1)*m12**2*RA3x2**3)/(sinb**2*vev) - (3*complex(0,1)*m12**2*RA3x1*RA3x2**2)/(sinb*vev) - (3*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA3x1*RA3x2**2)/(sinb*vev) - (3*complex(0,1)*Mh2**2*RA2x1*RA2x2*RA3x1*RA3x2**2)/(sinb*vev) - (3*complex(0,1)*Mh1**2*RA1x2**2*RA3x2**3)/(sinb*vev) - (3*complex(0,1)*Mh2**2*RA2x2**2*RA3x2**3)/(sinb*vev) - (3*complex(0,1)*MS**2*RA3x1**2*RA3x2**3)/(sinb*vev) - (3*complex(0,1)*MS**2*RA3x2**5)/(sinb*vev) - (3*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA3x2**2*RA3x3)/(sinb*vev) - (3*complex(0,1)*Mh2**2*RA2x2*RA2x3*RA3x2**2*RA3x3)/(sinb*vev) - (3*complex(0,1)*MS**2*RA3x2**3*RA3x3**2)/(sinb*vev) + (3*complex(0,1)*m12**2*RA3x1**3*sinb)/(cosb**2*vev) - (3*complex(0,1)*Mh1**2*RA1x1*RA1x3*RA3x1*RA3x3**2)/vev3 - (3*complex(0,1)*Mh2**2*RA2x1*RA2x3*RA3x1*RA3x3**2)/vev3 - (3*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA3x2*RA3x3**2)/vev3 - (3*complex(0,1)*Mh2**2*RA2x2*RA2x3*RA3x2*RA3x3**2)/vev3 - (3*complex(0,1)*Mh1**2*RA1x3**2*RA3x3**3)/vev3 - (3*complex(0,1)*Mh2**2*RA2x3**2*RA3x3**3)/vev3 - (3*complex(0,1)*MS**2*RA3x1**2*RA3x3**3)/vev3 - (3*complex(0,1)*MS**2*RA3x2**2*RA3x3**3)/vev3 - (3*complex(0,1)*MS**2*RA3x3**5)/vev3',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '(-3*complex(0,1)*Mh1**2*RA1x1**6)/(cosb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x1**4*RA2x1**2)/(cosb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x1**4*RA3x1**2)/(cosb**2*vev**2) + (3*cosb*complex(0,1)*m12**2*RA1x2**4)/(sinb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x2**6)/(sinb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x2**4*RA2x2**2)/(sinb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x2**4*RA3x2**2)/(sinb**2*vev**2) - (6*complex(0,1)*m12**2*RA1x1**2*RA1x2**2)/(cosb*sinb*vev**2) - (6*complex(0,1)*Mh1**2*RA1x1**3*RA1x2**3)/(cosb*sinb*vev**2) - (6*complex(0,1)*Mh2**2*RA1x1**2*RA1x2**2*RA2x1*RA2x2)/(cosb*sinb*vev**2) - (6*complex(0,1)*MS**2*RA1x1**2*RA1x2**2*RA3x1*RA3x2)/(cosb*sinb*vev**2) + (3*complex(0,1)*m12**2*RA1x1**4*sinb)/(cosb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x3**6)/vev3**2 - (3*complex(0,1)*Mh2**2*RA1x3**4*RA2x3**2)/vev3**2 - (3*complex(0,1)*MS**2*RA1x3**4*RA3x3**2)/vev3**2 - (6*complex(0,1)*Mh1**2*RA1x1**3*RA1x3**3)/(cosb*vev*vev3) - (6*complex(0,1)*Mh2**2*RA1x1**2*RA1x3**2*RA2x1*RA2x3)/(cosb*vev*vev3) - (6*complex(0,1)*MS**2*RA1x1**2*RA1x3**2*RA3x1*RA3x3)/(cosb*vev*vev3) - (6*complex(0,1)*Mh1**2*RA1x2**3*RA1x3**3)/(sinb*vev*vev3) - (6*complex(0,1)*Mh2**2*RA1x2**2*RA1x3**2*RA2x2*RA2x3)/(sinb*vev*vev3) - (6*complex(0,1)*MS**2*RA1x2**2*RA1x3**2*RA3x2*RA3x3)/(sinb*vev*vev3)',
                 order = {'QED':2})

GC_96 = Coupling(name = 'GC_96',
                 value = '(-3*complex(0,1)*Mh1**2*RA1x1**5*RA2x1)/(cosb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x1**3*RA2x1**3)/(cosb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x1**3*RA2x1*RA3x1**2)/(cosb**2*vev**2) + (3*cosb*complex(0,1)*m12**2*RA1x2**3*RA2x2)/(sinb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x2**5*RA2x2)/(sinb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x2**3*RA2x2**3)/(sinb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x2**3*RA2x2*RA3x2**2)/(sinb**2*vev**2) - (3*complex(0,1)*m12**2*RA1x1*RA1x2**2*RA2x1)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh1**2*RA1x1**2*RA1x2**3*RA2x1)/(cosb*sinb*vev**2) - (3*complex(0,1)*m12**2*RA1x1**2*RA1x2*RA2x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh1**2*RA1x1**3*RA1x2**2*RA2x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh2**2*RA1x1*RA1x2**2*RA2x1**2*RA2x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh2**2*RA1x1**2*RA1x2*RA2x1*RA2x2**2)/(cosb*sinb*vev**2) - (3*complex(0,1)*MS**2*RA1x1*RA1x2**2*RA2x1*RA3x1*RA3x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*MS**2*RA1x1**2*RA1x2*RA2x2*RA3x1*RA3x2)/(cosb*sinb*vev**2) + (3*complex(0,1)*m12**2*RA1x1**3*RA2x1*sinb)/(cosb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x3**5*RA2x3)/vev3**2 - (3*complex(0,1)*Mh2**2*RA1x3**3*RA2x3**3)/vev3**2 - (3*complex(0,1)*MS**2*RA1x3**3*RA2x3*RA3x3**2)/vev3**2 - (3*complex(0,1)*Mh1**2*RA1x1**2*RA1x3**3*RA2x1)/(cosb*vev*vev3) - (3*complex(0,1)*Mh1**2*RA1x1**3*RA1x3**2*RA2x3)/(cosb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA1x1*RA1x3**2*RA2x1**2*RA2x3)/(cosb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA1x1**2*RA1x3*RA2x1*RA2x3**2)/(cosb*vev*vev3) - (3*complex(0,1)*MS**2*RA1x1*RA1x3**2*RA2x1*RA3x1*RA3x3)/(cosb*vev*vev3) - (3*complex(0,1)*MS**2*RA1x1**2*RA1x3*RA2x3*RA3x1*RA3x3)/(cosb*vev*vev3) - (3*complex(0,1)*Mh1**2*RA1x2**2*RA1x3**3*RA2x2)/(sinb*vev*vev3) - (3*complex(0,1)*Mh1**2*RA1x2**3*RA1x3**2*RA2x3)/(sinb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA1x2*RA1x3**2*RA2x2**2*RA2x3)/(sinb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA1x2**2*RA1x3*RA2x2*RA2x3**2)/(sinb*vev*vev3) - (3*complex(0,1)*MS**2*RA1x2*RA1x3**2*RA2x2*RA3x2*RA3x3)/(sinb*vev*vev3) - (3*complex(0,1)*MS**2*RA1x2**2*RA1x3*RA2x3*RA3x2*RA3x3)/(sinb*vev*vev3)',
                 order = {'QED':2})

GC_97 = Coupling(name = 'GC_97',
                 value = '(-3*complex(0,1)*Mh1**2*RA1x1**4*RA2x1**2)/(cosb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x1**2*RA2x1**4)/(cosb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x1**2*RA2x1**2*RA3x1**2)/(cosb**2*vev**2) + (3*cosb*complex(0,1)*m12**2*RA1x2**2*RA2x2**2)/(sinb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x2**4*RA2x2**2)/(sinb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x2**2*RA2x2**4)/(sinb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x2**2*RA2x2**2*RA3x2**2)/(sinb**2*vev**2) - (complex(0,1)*m12**2*RA1x2**2*RA2x1**2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**3*RA2x1**2)/(cosb*sinb*vev**2) - (4*complex(0,1)*m12**2*RA1x1*RA1x2*RA2x1*RA2x2)/(cosb*sinb*vev**2) - (4*complex(0,1)*Mh1**2*RA1x1**2*RA1x2**2*RA2x1*RA2x2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh2**2*RA1x2**2*RA2x1**3*RA2x2)/(cosb*sinb*vev**2) - (complex(0,1)*m12**2*RA1x1**2*RA2x2**2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh1**2*RA1x1**3*RA1x2*RA2x2**2)/(cosb*sinb*vev**2) - (4*complex(0,1)*Mh2**2*RA1x1*RA1x2*RA2x1**2*RA2x2**2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh2**2*RA1x1**2*RA2x1*RA2x2**3)/(cosb*sinb*vev**2) - (complex(0,1)*MS**2*RA1x2**2*RA2x1**2*RA3x1*RA3x2)/(cosb*sinb*vev**2) - (4*complex(0,1)*MS**2*RA1x1*RA1x2*RA2x1*RA2x2*RA3x1*RA3x2)/(cosb*sinb*vev**2) - (complex(0,1)*MS**2*RA1x1**2*RA2x2**2*RA3x1*RA3x2)/(cosb*sinb*vev**2) + (3*complex(0,1)*m12**2*RA1x1**2*RA2x1**2*sinb)/(cosb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x3**4*RA2x3**2)/vev3**2 - (3*complex(0,1)*Mh2**2*RA1x3**2*RA2x3**4)/vev3**2 - (3*complex(0,1)*MS**2*RA1x3**2*RA2x3**2*RA3x3**2)/vev3**2 - (complex(0,1)*Mh1**2*RA1x1*RA1x3**3*RA2x1**2)/(cosb*vev*vev3) - (4*complex(0,1)*Mh1**2*RA1x1**2*RA1x3**2*RA2x1*RA2x3)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x3**2*RA2x1**3*RA2x3)/(cosb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1**3*RA1x3*RA2x3**2)/(cosb*vev*vev3) - (4*complex(0,1)*Mh2**2*RA1x1*RA1x3*RA2x1**2*RA2x3**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x1**2*RA2x1*RA2x3**3)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA1x3**2*RA2x1**2*RA3x1*RA3x3)/(cosb*vev*vev3) - (4*complex(0,1)*MS**2*RA1x1*RA1x3*RA2x1*RA2x3*RA3x1*RA3x3)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA1x1**2*RA2x3**2*RA3x1*RA3x3)/(cosb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x2*RA1x3**3*RA2x2**2)/(sinb*vev*vev3) - (4*complex(0,1)*Mh1**2*RA1x2**2*RA1x3**2*RA2x2*RA2x3)/(sinb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x3**2*RA2x2**3*RA2x3)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x2**3*RA1x3*RA2x3**2)/(sinb*vev*vev3) - (4*complex(0,1)*Mh2**2*RA1x2*RA1x3*RA2x2**2*RA2x3**2)/(sinb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x2**2*RA2x2*RA2x3**3)/(sinb*vev*vev3) - (complex(0,1)*MS**2*RA1x3**2*RA2x2**2*RA3x2*RA3x3)/(sinb*vev*vev3) - (4*complex(0,1)*MS**2*RA1x2*RA1x3*RA2x2*RA2x3*RA3x2*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*MS**2*RA1x2**2*RA2x3**2*RA3x2*RA3x3)/(sinb*vev*vev3)',
                 order = {'QED':2})

GC_98 = Coupling(name = 'GC_98',
                 value = '(-3*complex(0,1)*Mh1**2*RA1x1**3*RA2x1**3)/(cosb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x1*RA2x1**5)/(cosb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x1*RA2x1**3*RA3x1**2)/(cosb**2*vev**2) + (3*cosb*complex(0,1)*m12**2*RA1x2*RA2x2**3)/(sinb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x2**3*RA2x2**3)/(sinb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x2*RA2x2**5)/(sinb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x2*RA2x2**3*RA3x2**2)/(sinb**2*vev**2) - (3*complex(0,1)*m12**2*RA1x2*RA2x1**2*RA2x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh1**2*RA1x1*RA1x2**2*RA2x1**2*RA2x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*m12**2*RA1x1*RA2x1*RA2x2**2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh1**2*RA1x1**2*RA1x2*RA2x1*RA2x2**2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh2**2*RA1x2*RA2x1**3*RA2x2**2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh2**2*RA1x1*RA2x1**2*RA2x2**3)/(cosb*sinb*vev**2) - (3*complex(0,1)*MS**2*RA1x2*RA2x1**2*RA2x2*RA3x1*RA3x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*MS**2*RA1x1*RA2x1*RA2x2**2*RA3x1*RA3x2)/(cosb*sinb*vev**2) + (3*complex(0,1)*m12**2*RA1x1*RA2x1**3*sinb)/(cosb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x3**3*RA2x3**3)/vev3**2 - (3*complex(0,1)*Mh2**2*RA1x3*RA2x3**5)/vev3**2 - (3*complex(0,1)*MS**2*RA1x3*RA2x3**3*RA3x3**2)/vev3**2 - (3*complex(0,1)*Mh1**2*RA1x1*RA1x3**2*RA2x1**2*RA2x3)/(cosb*vev*vev3) - (3*complex(0,1)*Mh1**2*RA1x1**2*RA1x3*RA2x1*RA2x3**2)/(cosb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA1x3*RA2x1**3*RA2x3**2)/(cosb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA1x1*RA2x1**2*RA2x3**3)/(cosb*vev*vev3) - (3*complex(0,1)*MS**2*RA1x3*RA2x1**2*RA2x3*RA3x1*RA3x3)/(cosb*vev*vev3) - (3*complex(0,1)*MS**2*RA1x1*RA2x1*RA2x3**2*RA3x1*RA3x3)/(cosb*vev*vev3) - (3*complex(0,1)*Mh1**2*RA1x2*RA1x3**2*RA2x2**2*RA2x3)/(sinb*vev*vev3) - (3*complex(0,1)*Mh1**2*RA1x2**2*RA1x3*RA2x2*RA2x3**2)/(sinb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA1x3*RA2x2**3*RA2x3**2)/(sinb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA1x2*RA2x2**2*RA2x3**3)/(sinb*vev*vev3) - (3*complex(0,1)*MS**2*RA1x3*RA2x2**2*RA2x3*RA3x2*RA3x3)/(sinb*vev*vev3) - (3*complex(0,1)*MS**2*RA1x2*RA2x2*RA2x3**2*RA3x2*RA3x3)/(sinb*vev*vev3)',
                 order = {'QED':2})

GC_99 = Coupling(name = 'GC_99',
                 value = '(-3*complex(0,1)*Mh1**2*RA1x1**2*RA2x1**4)/(cosb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA2x1**6)/(cosb**2*vev**2) - (3*complex(0,1)*MS**2*RA2x1**4*RA3x1**2)/(cosb**2*vev**2) + (3*cosb*complex(0,1)*m12**2*RA2x2**4)/(sinb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x2**2*RA2x2**4)/(sinb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA2x2**6)/(sinb**2*vev**2) - (3*complex(0,1)*MS**2*RA2x2**4*RA3x2**2)/(sinb**2*vev**2) - (6*complex(0,1)*m12**2*RA2x1**2*RA2x2**2)/(cosb*sinb*vev**2) - (6*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1**2*RA2x2**2)/(cosb*sinb*vev**2) - (6*complex(0,1)*Mh2**2*RA2x1**3*RA2x2**3)/(cosb*sinb*vev**2) - (6*complex(0,1)*MS**2*RA2x1**2*RA2x2**2*RA3x1*RA3x2)/(cosb*sinb*vev**2) + (3*complex(0,1)*m12**2*RA2x1**4*sinb)/(cosb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x3**2*RA2x3**4)/vev3**2 - (3*complex(0,1)*Mh2**2*RA2x3**6)/vev3**2 - (3*complex(0,1)*MS**2*RA2x3**4*RA3x3**2)/vev3**2 - (6*complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x1**2*RA2x3**2)/(cosb*vev*vev3) - (6*complex(0,1)*Mh2**2*RA2x1**3*RA2x3**3)/(cosb*vev*vev3) - (6*complex(0,1)*MS**2*RA2x1**2*RA2x3**2*RA3x1*RA3x3)/(cosb*vev*vev3) - (6*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x2**2*RA2x3**2)/(sinb*vev*vev3) - (6*complex(0,1)*Mh2**2*RA2x2**3*RA2x3**3)/(sinb*vev*vev3) - (6*complex(0,1)*MS**2*RA2x2**2*RA2x3**2*RA3x2*RA3x3)/(sinb*vev*vev3)',
                 order = {'QED':2})

GC_100 = Coupling(name = 'GC_100',
                  value = '(-3*complex(0,1)*Mh1**2*RA1x1**5*RA3x1)/(cosb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x1**3*RA2x1**2*RA3x1)/(cosb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x1**3*RA3x1**3)/(cosb**2*vev**2) + (3*cosb*complex(0,1)*m12**2*RA1x2**3*RA3x2)/(sinb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x2**5*RA3x2)/(sinb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x2**3*RA2x2**2*RA3x2)/(sinb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x2**3*RA3x2**3)/(sinb**2*vev**2) - (3*complex(0,1)*m12**2*RA1x1*RA1x2**2*RA3x1)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh1**2*RA1x1**2*RA1x2**3*RA3x1)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh2**2*RA1x1*RA1x2**2*RA2x1*RA2x2*RA3x1)/(cosb*sinb*vev**2) - (3*complex(0,1)*m12**2*RA1x1**2*RA1x2*RA3x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh1**2*RA1x1**3*RA1x2**2*RA3x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh2**2*RA1x1**2*RA1x2*RA2x1*RA2x2*RA3x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*MS**2*RA1x1*RA1x2**2*RA3x1**2*RA3x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*MS**2*RA1x1**2*RA1x2*RA3x1*RA3x2**2)/(cosb*sinb*vev**2) + (3*complex(0,1)*m12**2*RA1x1**3*RA3x1*sinb)/(cosb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x3**5*RA3x3)/vev3**2 - (3*complex(0,1)*Mh2**2*RA1x3**3*RA2x3**2*RA3x3)/vev3**2 - (3*complex(0,1)*MS**2*RA1x3**3*RA3x3**3)/vev3**2 - (3*complex(0,1)*Mh1**2*RA1x1**2*RA1x3**3*RA3x1)/(cosb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA1x1*RA1x3**2*RA2x1*RA2x3*RA3x1)/(cosb*vev*vev3) - (3*complex(0,1)*Mh1**2*RA1x1**3*RA1x3**2*RA3x3)/(cosb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA1x1**2*RA1x3*RA2x1*RA2x3*RA3x3)/(cosb*vev*vev3) - (3*complex(0,1)*MS**2*RA1x1*RA1x3**2*RA3x1**2*RA3x3)/(cosb*vev*vev3) - (3*complex(0,1)*MS**2*RA1x1**2*RA1x3*RA3x1*RA3x3**2)/(cosb*vev*vev3) - (3*complex(0,1)*Mh1**2*RA1x2**2*RA1x3**3*RA3x2)/(sinb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA1x2*RA1x3**2*RA2x2*RA2x3*RA3x2)/(sinb*vev*vev3) - (3*complex(0,1)*Mh1**2*RA1x2**3*RA1x3**2*RA3x3)/(sinb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA1x2**2*RA1x3*RA2x2*RA2x3*RA3x3)/(sinb*vev*vev3) - (3*complex(0,1)*MS**2*RA1x2*RA1x3**2*RA3x2**2*RA3x3)/(sinb*vev*vev3) - (3*complex(0,1)*MS**2*RA1x2**2*RA1x3*RA3x2*RA3x3**2)/(sinb*vev*vev3)',
                  order = {'QED':2})

GC_101 = Coupling(name = 'GC_101',
                  value = '(-3*complex(0,1)*Mh1**2*RA1x1**4*RA2x1*RA3x1)/(cosb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x1**2*RA2x1**3*RA3x1)/(cosb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x1**2*RA2x1*RA3x1**3)/(cosb**2*vev**2) + (3*cosb*complex(0,1)*m12**2*RA1x2**2*RA2x2*RA3x2)/(sinb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x2**4*RA2x2*RA3x2)/(sinb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x2**2*RA2x2**3*RA3x2)/(sinb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x2**2*RA2x2*RA3x2**3)/(sinb**2*vev**2) - (complex(0,1)*m12**2*RA1x2**2*RA2x1*RA3x1)/(cosb*sinb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**3*RA2x1*RA3x1)/(cosb*sinb*vev**2) - (2*complex(0,1)*m12**2*RA1x1*RA1x2*RA2x2*RA3x1)/(cosb*sinb*vev**2) - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x2**2*RA2x2*RA3x1)/(cosb*sinb*vev**2) - (complex(0,1)*Mh2**2*RA1x2**2*RA2x1**2*RA2x2*RA3x1)/(cosb*sinb*vev**2) - (2*complex(0,1)*Mh2**2*RA1x1*RA1x2*RA2x1*RA2x2**2*RA3x1)/(cosb*sinb*vev**2) - (2*complex(0,1)*m12**2*RA1x1*RA1x2*RA2x1*RA3x2)/(cosb*sinb*vev**2) - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x2**2*RA2x1*RA3x2)/(cosb*sinb*vev**2) - (complex(0,1)*m12**2*RA1x1**2*RA2x2*RA3x2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh1**2*RA1x1**3*RA1x2*RA2x2*RA3x2)/(cosb*sinb*vev**2) - (2*complex(0,1)*Mh2**2*RA1x1*RA1x2*RA2x1**2*RA2x2*RA3x2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh2**2*RA1x1**2*RA2x1*RA2x2**2*RA3x2)/(cosb*sinb*vev**2) - (complex(0,1)*MS**2*RA1x2**2*RA2x1*RA3x1**2*RA3x2)/(cosb*sinb*vev**2) - (2*complex(0,1)*MS**2*RA1x1*RA1x2*RA2x2*RA3x1**2*RA3x2)/(cosb*sinb*vev**2) - (2*complex(0,1)*MS**2*RA1x1*RA1x2*RA2x1*RA3x1*RA3x2**2)/(cosb*sinb*vev**2) - (complex(0,1)*MS**2*RA1x1**2*RA2x2*RA3x1*RA3x2**2)/(cosb*sinb*vev**2) + (3*complex(0,1)*m12**2*RA1x1**2*RA2x1*RA3x1*sinb)/(cosb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x3**4*RA2x3*RA3x3)/vev3**2 - (3*complex(0,1)*Mh2**2*RA1x3**2*RA2x3**3*RA3x3)/vev3**2 - (3*complex(0,1)*MS**2*RA1x3**2*RA2x3*RA3x3**3)/vev3**2 - (complex(0,1)*Mh1**2*RA1x1*RA1x3**3*RA2x1*RA3x1)/(cosb*vev*vev3) - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x3**2*RA2x3*RA3x1)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x3**2*RA2x1**2*RA2x3*RA3x1)/(cosb*vev*vev3) - (2*complex(0,1)*Mh2**2*RA1x1*RA1x3*RA2x1*RA2x3**2*RA3x1)/(cosb*vev*vev3) - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x3**2*RA2x1*RA3x3)/(cosb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1**3*RA1x3*RA2x3*RA3x3)/(cosb*vev*vev3) - (2*complex(0,1)*Mh2**2*RA1x1*RA1x3*RA2x1**2*RA2x3*RA3x3)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x1**2*RA2x1*RA2x3**2*RA3x3)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA1x3**2*RA2x1*RA3x1**2*RA3x3)/(cosb*vev*vev3) - (2*complex(0,1)*MS**2*RA1x1*RA1x3*RA2x3*RA3x1**2*RA3x3)/(cosb*vev*vev3) - (2*complex(0,1)*MS**2*RA1x1*RA1x3*RA2x1*RA3x1*RA3x3**2)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA1x1**2*RA2x3*RA3x1*RA3x3**2)/(cosb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x2*RA1x3**3*RA2x2*RA3x2)/(sinb*vev*vev3) - (2*complex(0,1)*Mh1**2*RA1x2**2*RA1x3**2*RA2x3*RA3x2)/(sinb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x3**2*RA2x2**2*RA2x3*RA3x2)/(sinb*vev*vev3) - (2*complex(0,1)*Mh2**2*RA1x2*RA1x3*RA2x2*RA2x3**2*RA3x2)/(sinb*vev*vev3) - (2*complex(0,1)*Mh1**2*RA1x2**2*RA1x3**2*RA2x2*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x2**3*RA1x3*RA2x3*RA3x3)/(sinb*vev*vev3) - (2*complex(0,1)*Mh2**2*RA1x2*RA1x3*RA2x2**2*RA2x3*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x2**2*RA2x2*RA2x3**2*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*MS**2*RA1x3**2*RA2x2*RA3x2**2*RA3x3)/(sinb*vev*vev3) - (2*complex(0,1)*MS**2*RA1x2*RA1x3*RA2x3*RA3x2**2*RA3x3)/(sinb*vev*vev3) - (2*complex(0,1)*MS**2*RA1x2*RA1x3*RA2x2*RA3x2*RA3x3**2)/(sinb*vev*vev3) - (complex(0,1)*MS**2*RA1x2**2*RA2x3*RA3x2*RA3x3**2)/(sinb*vev*vev3)',
                  order = {'QED':2})

GC_102 = Coupling(name = 'GC_102',
                  value = '(-3*complex(0,1)*Mh1**2*RA1x1**3*RA2x1**2*RA3x1)/(cosb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x1*RA2x1**4*RA3x1)/(cosb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x1*RA2x1**2*RA3x1**3)/(cosb**2*vev**2) + (3*cosb*complex(0,1)*m12**2*RA1x2*RA2x2**2*RA3x2)/(sinb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x2**3*RA2x2**2*RA3x2)/(sinb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x2*RA2x2**4*RA3x2)/(sinb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x2*RA2x2**2*RA3x2**3)/(sinb**2*vev**2) - (2*complex(0,1)*m12**2*RA1x2*RA2x1*RA2x2*RA3x1)/(cosb*sinb*vev**2) - (2*complex(0,1)*Mh1**2*RA1x1*RA1x2**2*RA2x1*RA2x2*RA3x1)/(cosb*sinb*vev**2) - (complex(0,1)*m12**2*RA1x1*RA2x2**2*RA3x1)/(cosb*sinb*vev**2) - (complex(0,1)*Mh1**2*RA1x1**2*RA1x2*RA2x2**2*RA3x1)/(cosb*sinb*vev**2) - (2*complex(0,1)*Mh2**2*RA1x2*RA2x1**2*RA2x2**2*RA3x1)/(cosb*sinb*vev**2) - (complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x2**3*RA3x1)/(cosb*sinb*vev**2) - (complex(0,1)*m12**2*RA1x2*RA2x1**2*RA3x2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**2*RA2x1**2*RA3x2)/(cosb*sinb*vev**2) - (2*complex(0,1)*m12**2*RA1x1*RA2x1*RA2x2*RA3x2)/(cosb*sinb*vev**2) - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x2*RA2x1*RA2x2*RA3x2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh2**2*RA1x2*RA2x1**3*RA2x2*RA3x2)/(cosb*sinb*vev**2) - (2*complex(0,1)*Mh2**2*RA1x1*RA2x1**2*RA2x2**2*RA3x2)/(cosb*sinb*vev**2) - (2*complex(0,1)*MS**2*RA1x2*RA2x1*RA2x2*RA3x1**2*RA3x2)/(cosb*sinb*vev**2) - (complex(0,1)*MS**2*RA1x1*RA2x2**2*RA3x1**2*RA3x2)/(cosb*sinb*vev**2) - (complex(0,1)*MS**2*RA1x2*RA2x1**2*RA3x1*RA3x2**2)/(cosb*sinb*vev**2) - (2*complex(0,1)*MS**2*RA1x1*RA2x1*RA2x2*RA3x1*RA3x2**2)/(cosb*sinb*vev**2) + (3*complex(0,1)*m12**2*RA1x1*RA2x1**2*RA3x1*sinb)/(cosb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x3**3*RA2x3**2*RA3x3)/vev3**2 - (3*complex(0,1)*Mh2**2*RA1x3*RA2x3**4*RA3x3)/vev3**2 - (3*complex(0,1)*MS**2*RA1x3*RA2x3**2*RA3x3**3)/vev3**2 - (2*complex(0,1)*Mh1**2*RA1x1*RA1x3**2*RA2x1*RA2x3*RA3x1)/(cosb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1**2*RA1x3*RA2x3**2*RA3x1)/(cosb*vev*vev3) - (2*complex(0,1)*Mh2**2*RA1x3*RA2x1**2*RA2x3**2*RA3x1)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x3**3*RA3x1)/(cosb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1*RA1x3**2*RA2x1**2*RA3x3)/(cosb*vev*vev3) - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x3*RA2x1*RA2x3*RA3x3)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x3*RA2x1**3*RA2x3*RA3x3)/(cosb*vev*vev3) - (2*complex(0,1)*Mh2**2*RA1x1*RA2x1**2*RA2x3**2*RA3x3)/(cosb*vev*vev3) - (2*complex(0,1)*MS**2*RA1x3*RA2x1*RA2x3*RA3x1**2*RA3x3)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA1x1*RA2x3**2*RA3x1**2*RA3x3)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA1x3*RA2x1**2*RA3x1*RA3x3**2)/(cosb*vev*vev3) - (2*complex(0,1)*MS**2*RA1x1*RA2x1*RA2x3*RA3x1*RA3x3**2)/(cosb*vev*vev3) - (2*complex(0,1)*Mh1**2*RA1x2*RA1x3**2*RA2x2*RA2x3*RA3x2)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x2**2*RA1x3*RA2x3**2*RA3x2)/(sinb*vev*vev3) - (2*complex(0,1)*Mh2**2*RA1x3*RA2x2**2*RA2x3**2*RA3x2)/(sinb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x2*RA2x2*RA2x3**3*RA3x2)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x2*RA1x3**2*RA2x2**2*RA3x3)/(sinb*vev*vev3) - (2*complex(0,1)*Mh1**2*RA1x2**2*RA1x3*RA2x2*RA2x3*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x3*RA2x2**3*RA2x3*RA3x3)/(sinb*vev*vev3) - (2*complex(0,1)*Mh2**2*RA1x2*RA2x2**2*RA2x3**2*RA3x3)/(sinb*vev*vev3) - (2*complex(0,1)*MS**2*RA1x3*RA2x2*RA2x3*RA3x2**2*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*MS**2*RA1x2*RA2x3**2*RA3x2**2*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*MS**2*RA1x3*RA2x2**2*RA3x2*RA3x3**2)/(sinb*vev*vev3) - (2*complex(0,1)*MS**2*RA1x2*RA2x2*RA2x3*RA3x2*RA3x3**2)/(sinb*vev*vev3)',
                  order = {'QED':2})

GC_103 = Coupling(name = 'GC_103',
                  value = '(-3*complex(0,1)*Mh1**2*RA1x1**2*RA2x1**3*RA3x1)/(cosb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA2x1**5*RA3x1)/(cosb**2*vev**2) - (3*complex(0,1)*MS**2*RA2x1**3*RA3x1**3)/(cosb**2*vev**2) + (3*cosb*complex(0,1)*m12**2*RA2x2**3*RA3x2)/(sinb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x2**2*RA2x2**3*RA3x2)/(sinb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA2x2**5*RA3x2)/(sinb**2*vev**2) - (3*complex(0,1)*MS**2*RA2x2**3*RA3x2**3)/(sinb**2*vev**2) - (3*complex(0,1)*m12**2*RA2x1*RA2x2**2*RA3x1)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1*RA2x2**2*RA3x1)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh2**2*RA2x1**2*RA2x2**3*RA3x1)/(cosb*sinb*vev**2) - (3*complex(0,1)*m12**2*RA2x1**2*RA2x2*RA3x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1**2*RA2x2*RA3x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh2**2*RA2x1**3*RA2x2**2*RA3x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*MS**2*RA2x1*RA2x2**2*RA3x1**2*RA3x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*MS**2*RA2x1**2*RA2x2*RA3x1*RA3x2**2)/(cosb*sinb*vev**2) + (3*complex(0,1)*m12**2*RA2x1**3*RA3x1*sinb)/(cosb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x3**2*RA2x3**3*RA3x3)/vev3**2 - (3*complex(0,1)*Mh2**2*RA2x3**5*RA3x3)/vev3**2 - (3*complex(0,1)*MS**2*RA2x3**3*RA3x3**3)/vev3**2 - (3*complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x1*RA2x3**2*RA3x1)/(cosb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA2x1**2*RA2x3**3*RA3x1)/(cosb*vev*vev3) - (3*complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x1**2*RA2x3*RA3x3)/(cosb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA2x1**3*RA2x3**2*RA3x3)/(cosb*vev*vev3) - (3*complex(0,1)*MS**2*RA2x1*RA2x3**2*RA3x1**2*RA3x3)/(cosb*vev*vev3) - (3*complex(0,1)*MS**2*RA2x1**2*RA2x3*RA3x1*RA3x3**2)/(cosb*vev*vev3) - (3*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x2*RA2x3**2*RA3x2)/(sinb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA2x2**2*RA2x3**3*RA3x2)/(sinb*vev*vev3) - (3*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x2**2*RA2x3*RA3x3)/(sinb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA2x2**3*RA2x3**2*RA3x3)/(sinb*vev*vev3) - (3*complex(0,1)*MS**2*RA2x2*RA2x3**2*RA3x2**2*RA3x3)/(sinb*vev*vev3) - (3*complex(0,1)*MS**2*RA2x2**2*RA2x3*RA3x2*RA3x3**2)/(sinb*vev*vev3)',
                  order = {'QED':2})

GC_104 = Coupling(name = 'GC_104',
                  value = '(-3*complex(0,1)*Mh1**2*RA1x1**4*RA3x1**2)/(cosb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x1**2*RA2x1**2*RA3x1**2)/(cosb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x1**2*RA3x1**4)/(cosb**2*vev**2) + (3*cosb*complex(0,1)*m12**2*RA1x2**2*RA3x2**2)/(sinb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x2**4*RA3x2**2)/(sinb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x2**2*RA2x2**2*RA3x2**2)/(sinb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x2**2*RA3x2**4)/(sinb**2*vev**2) - (complex(0,1)*m12**2*RA1x2**2*RA3x1**2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**3*RA3x1**2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh2**2*RA1x2**2*RA2x1*RA2x2*RA3x1**2)/(cosb*sinb*vev**2) - (4*complex(0,1)*m12**2*RA1x1*RA1x2*RA3x1*RA3x2)/(cosb*sinb*vev**2) - (4*complex(0,1)*Mh1**2*RA1x1**2*RA1x2**2*RA3x1*RA3x2)/(cosb*sinb*vev**2) - (4*complex(0,1)*Mh2**2*RA1x1*RA1x2*RA2x1*RA2x2*RA3x1*RA3x2)/(cosb*sinb*vev**2) - (complex(0,1)*MS**2*RA1x2**2*RA3x1**3*RA3x2)/(cosb*sinb*vev**2) - (complex(0,1)*m12**2*RA1x1**2*RA3x2**2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh1**2*RA1x1**3*RA1x2*RA3x2**2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh2**2*RA1x1**2*RA2x1*RA2x2*RA3x2**2)/(cosb*sinb*vev**2) - (4*complex(0,1)*MS**2*RA1x1*RA1x2*RA3x1**2*RA3x2**2)/(cosb*sinb*vev**2) - (complex(0,1)*MS**2*RA1x1**2*RA3x1*RA3x2**3)/(cosb*sinb*vev**2) + (3*complex(0,1)*m12**2*RA1x1**2*RA3x1**2*sinb)/(cosb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x3**4*RA3x3**2)/vev3**2 - (3*complex(0,1)*Mh2**2*RA1x3**2*RA2x3**2*RA3x3**2)/vev3**2 - (3*complex(0,1)*MS**2*RA1x3**2*RA3x3**4)/vev3**2 - (complex(0,1)*Mh1**2*RA1x1*RA1x3**3*RA3x1**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x3**2*RA2x1*RA2x3*RA3x1**2)/(cosb*vev*vev3) - (4*complex(0,1)*Mh1**2*RA1x1**2*RA1x3**2*RA3x1*RA3x3)/(cosb*vev*vev3) - (4*complex(0,1)*Mh2**2*RA1x1*RA1x3*RA2x1*RA2x3*RA3x1*RA3x3)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA1x3**2*RA3x1**3*RA3x3)/(cosb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1**3*RA1x3*RA3x3**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x1**2*RA2x1*RA2x3*RA3x3**2)/(cosb*vev*vev3) - (4*complex(0,1)*MS**2*RA1x1*RA1x3*RA3x1**2*RA3x3**2)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA1x1**2*RA3x1*RA3x3**3)/(cosb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x2*RA1x3**3*RA3x2**2)/(sinb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x3**2*RA2x2*RA2x3*RA3x2**2)/(sinb*vev*vev3) - (4*complex(0,1)*Mh1**2*RA1x2**2*RA1x3**2*RA3x2*RA3x3)/(sinb*vev*vev3) - (4*complex(0,1)*Mh2**2*RA1x2*RA1x3*RA2x2*RA2x3*RA3x2*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*MS**2*RA1x3**2*RA3x2**3*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x2**3*RA1x3*RA3x3**2)/(sinb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x2**2*RA2x2*RA2x3*RA3x3**2)/(sinb*vev*vev3) - (4*complex(0,1)*MS**2*RA1x2*RA1x3*RA3x2**2*RA3x3**2)/(sinb*vev*vev3) - (complex(0,1)*MS**2*RA1x2**2*RA3x2*RA3x3**3)/(sinb*vev*vev3)',
                  order = {'QED':2})

GC_105 = Coupling(name = 'GC_105',
                  value = '(-3*complex(0,1)*Mh1**2*RA1x1**3*RA2x1*RA3x1**2)/(cosb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x1*RA2x1**3*RA3x1**2)/(cosb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x1*RA2x1*RA3x1**4)/(cosb**2*vev**2) + (3*cosb*complex(0,1)*m12**2*RA1x2*RA2x2*RA3x2**2)/(sinb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x2**3*RA2x2*RA3x2**2)/(sinb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x2*RA2x2**3*RA3x2**2)/(sinb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x2*RA2x2*RA3x2**4)/(sinb**2*vev**2) - (complex(0,1)*m12**2*RA1x2*RA2x2*RA3x1**2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**2*RA2x2*RA3x1**2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh2**2*RA1x2*RA2x1*RA2x2**2*RA3x1**2)/(cosb*sinb*vev**2) - (2*complex(0,1)*m12**2*RA1x2*RA2x1*RA3x1*RA3x2)/(cosb*sinb*vev**2) - (2*complex(0,1)*Mh1**2*RA1x1*RA1x2**2*RA2x1*RA3x1*RA3x2)/(cosb*sinb*vev**2) - (2*complex(0,1)*m12**2*RA1x1*RA2x2*RA3x1*RA3x2)/(cosb*sinb*vev**2) - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x2*RA2x2*RA3x1*RA3x2)/(cosb*sinb*vev**2) - (2*complex(0,1)*Mh2**2*RA1x2*RA2x1**2*RA2x2*RA3x1*RA3x2)/(cosb*sinb*vev**2) - (2*complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x2**2*RA3x1*RA3x2)/(cosb*sinb*vev**2) - (complex(0,1)*MS**2*RA1x2*RA2x2*RA3x1**3*RA3x2)/(cosb*sinb*vev**2) - (complex(0,1)*m12**2*RA1x1*RA2x1*RA3x2**2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh1**2*RA1x1**2*RA1x2*RA2x1*RA3x2**2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh2**2*RA1x1*RA2x1**2*RA2x2*RA3x2**2)/(cosb*sinb*vev**2) - (2*complex(0,1)*MS**2*RA1x2*RA2x1*RA3x1**2*RA3x2**2)/(cosb*sinb*vev**2) - (2*complex(0,1)*MS**2*RA1x1*RA2x2*RA3x1**2*RA3x2**2)/(cosb*sinb*vev**2) - (complex(0,1)*MS**2*RA1x1*RA2x1*RA3x1*RA3x2**3)/(cosb*sinb*vev**2) + (3*complex(0,1)*m12**2*RA1x1*RA2x1*RA3x1**2*sinb)/(cosb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x3**3*RA2x3*RA3x3**2)/vev3**2 - (3*complex(0,1)*Mh2**2*RA1x3*RA2x3**3*RA3x3**2)/vev3**2 - (3*complex(0,1)*MS**2*RA1x3*RA2x3*RA3x3**4)/vev3**2 - (complex(0,1)*Mh1**2*RA1x1*RA1x3**2*RA2x3*RA3x1**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x3*RA2x1*RA2x3**2*RA3x1**2)/(cosb*vev*vev3) - (2*complex(0,1)*Mh1**2*RA1x1*RA1x3**2*RA2x1*RA3x1*RA3x3)/(cosb*vev*vev3) - (2*complex(0,1)*Mh1**2*RA1x1**2*RA1x3*RA2x3*RA3x1*RA3x3)/(cosb*vev*vev3) - (2*complex(0,1)*Mh2**2*RA1x3*RA2x1**2*RA2x3*RA3x1*RA3x3)/(cosb*vev*vev3) - (2*complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x3**2*RA3x1*RA3x3)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA1x3*RA2x3*RA3x1**3*RA3x3)/(cosb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1**2*RA1x3*RA2x1*RA3x3**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x1*RA2x1**2*RA2x3*RA3x3**2)/(cosb*vev*vev3) - (2*complex(0,1)*MS**2*RA1x3*RA2x1*RA3x1**2*RA3x3**2)/(cosb*vev*vev3) - (2*complex(0,1)*MS**2*RA1x1*RA2x3*RA3x1**2*RA3x3**2)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA1x1*RA2x1*RA3x1*RA3x3**3)/(cosb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x2*RA1x3**2*RA2x3*RA3x2**2)/(sinb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x3*RA2x2*RA2x3**2*RA3x2**2)/(sinb*vev*vev3) - (2*complex(0,1)*Mh1**2*RA1x2*RA1x3**2*RA2x2*RA3x2*RA3x3)/(sinb*vev*vev3) - (2*complex(0,1)*Mh1**2*RA1x2**2*RA1x3*RA2x3*RA3x2*RA3x3)/(sinb*vev*vev3) - (2*complex(0,1)*Mh2**2*RA1x3*RA2x2**2*RA2x3*RA3x2*RA3x3)/(sinb*vev*vev3) - (2*complex(0,1)*Mh2**2*RA1x2*RA2x2*RA2x3**2*RA3x2*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*MS**2*RA1x3*RA2x3*RA3x2**3*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x2**2*RA1x3*RA2x2*RA3x3**2)/(sinb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x2*RA2x2**2*RA2x3*RA3x3**2)/(sinb*vev*vev3) - (2*complex(0,1)*MS**2*RA1x3*RA2x2*RA3x2**2*RA3x3**2)/(sinb*vev*vev3) - (2*complex(0,1)*MS**2*RA1x2*RA2x3*RA3x2**2*RA3x3**2)/(sinb*vev*vev3) - (complex(0,1)*MS**2*RA1x2*RA2x2*RA3x2*RA3x3**3)/(sinb*vev*vev3)',
                  order = {'QED':2})

GC_106 = Coupling(name = 'GC_106',
                  value = '(-3*complex(0,1)*Mh1**2*RA1x1**2*RA2x1**2*RA3x1**2)/(cosb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA2x1**4*RA3x1**2)/(cosb**2*vev**2) - (3*complex(0,1)*MS**2*RA2x1**2*RA3x1**4)/(cosb**2*vev**2) + (3*cosb*complex(0,1)*m12**2*RA2x2**2*RA3x2**2)/(sinb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x2**2*RA2x2**2*RA3x2**2)/(sinb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA2x2**4*RA3x2**2)/(sinb**2*vev**2) - (3*complex(0,1)*MS**2*RA2x2**2*RA3x2**4)/(sinb**2*vev**2) - (complex(0,1)*m12**2*RA2x2**2*RA3x1**2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x2**2*RA3x1**2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh2**2*RA2x1*RA2x2**3*RA3x1**2)/(cosb*sinb*vev**2) - (4*complex(0,1)*m12**2*RA2x1*RA2x2*RA3x1*RA3x2)/(cosb*sinb*vev**2) - (4*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1*RA2x2*RA3x1*RA3x2)/(cosb*sinb*vev**2) - (4*complex(0,1)*Mh2**2*RA2x1**2*RA2x2**2*RA3x1*RA3x2)/(cosb*sinb*vev**2) - (complex(0,1)*MS**2*RA2x2**2*RA3x1**3*RA3x2)/(cosb*sinb*vev**2) - (complex(0,1)*m12**2*RA2x1**2*RA3x2**2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1**2*RA3x2**2)/(cosb*sinb*vev**2) - (complex(0,1)*Mh2**2*RA2x1**3*RA2x2*RA3x2**2)/(cosb*sinb*vev**2) - (4*complex(0,1)*MS**2*RA2x1*RA2x2*RA3x1**2*RA3x2**2)/(cosb*sinb*vev**2) - (complex(0,1)*MS**2*RA2x1**2*RA3x1*RA3x2**3)/(cosb*sinb*vev**2) + (3*complex(0,1)*m12**2*RA2x1**2*RA3x1**2*sinb)/(cosb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x3**2*RA2x3**2*RA3x3**2)/vev3**2 - (3*complex(0,1)*Mh2**2*RA2x3**4*RA3x3**2)/vev3**2 - (3*complex(0,1)*MS**2*RA2x3**2*RA3x3**4)/vev3**2 - (complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x3**2*RA3x1**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA2x1*RA2x3**3*RA3x1**2)/(cosb*vev*vev3) - (4*complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x1*RA2x3*RA3x1*RA3x3)/(cosb*vev*vev3) - (4*complex(0,1)*Mh2**2*RA2x1**2*RA2x3**2*RA3x1*RA3x3)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA2x3**2*RA3x1**3*RA3x3)/(cosb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x1**2*RA3x3**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA2x1**3*RA2x3*RA3x3**2)/(cosb*vev*vev3) - (4*complex(0,1)*MS**2*RA2x1*RA2x3*RA3x1**2*RA3x3**2)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA2x1**2*RA3x1*RA3x3**3)/(cosb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x3**2*RA3x2**2)/(sinb*vev*vev3) - (complex(0,1)*Mh2**2*RA2x2*RA2x3**3*RA3x2**2)/(sinb*vev*vev3) - (4*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x2*RA2x3*RA3x2*RA3x3)/(sinb*vev*vev3) - (4*complex(0,1)*Mh2**2*RA2x2**2*RA2x3**2*RA3x2*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*MS**2*RA2x3**2*RA3x2**3*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x2**2*RA3x3**2)/(sinb*vev*vev3) - (complex(0,1)*Mh2**2*RA2x2**3*RA2x3*RA3x3**2)/(sinb*vev*vev3) - (4*complex(0,1)*MS**2*RA2x2*RA2x3*RA3x2**2*RA3x3**2)/(sinb*vev*vev3) - (complex(0,1)*MS**2*RA2x2**2*RA3x2*RA3x3**3)/(sinb*vev*vev3)',
                  order = {'QED':2})

GC_107 = Coupling(name = 'GC_107',
                  value = '(-3*complex(0,1)*Mh1**2*RA1x1**3*RA3x1**3)/(cosb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x1*RA2x1**2*RA3x1**3)/(cosb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x1*RA3x1**5)/(cosb**2*vev**2) + (3*cosb*complex(0,1)*m12**2*RA1x2*RA3x2**3)/(sinb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x2**3*RA3x2**3)/(sinb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA1x2*RA2x2**2*RA3x2**3)/(sinb**2*vev**2) - (3*complex(0,1)*MS**2*RA1x2*RA3x2**5)/(sinb**2*vev**2) - (3*complex(0,1)*m12**2*RA1x2*RA3x1**2*RA3x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh1**2*RA1x1*RA1x2**2*RA3x1**2*RA3x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh2**2*RA1x2*RA2x1*RA2x2*RA3x1**2*RA3x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*m12**2*RA1x1*RA3x1*RA3x2**2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh1**2*RA1x1**2*RA1x2*RA3x1*RA3x2**2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x2*RA3x1*RA3x2**2)/(cosb*sinb*vev**2) - (3*complex(0,1)*MS**2*RA1x2*RA3x1**3*RA3x2**2)/(cosb*sinb*vev**2) - (3*complex(0,1)*MS**2*RA1x1*RA3x1**2*RA3x2**3)/(cosb*sinb*vev**2) + (3*complex(0,1)*m12**2*RA1x1*RA3x1**3*sinb)/(cosb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x3**3*RA3x3**3)/vev3**2 - (3*complex(0,1)*Mh2**2*RA1x3*RA2x3**2*RA3x3**3)/vev3**2 - (3*complex(0,1)*MS**2*RA1x3*RA3x3**5)/vev3**2 - (3*complex(0,1)*Mh1**2*RA1x1*RA1x3**2*RA3x1**2*RA3x3)/(cosb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA1x3*RA2x1*RA2x3*RA3x1**2*RA3x3)/(cosb*vev*vev3) - (3*complex(0,1)*Mh1**2*RA1x1**2*RA1x3*RA3x1*RA3x3**2)/(cosb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x3*RA3x1*RA3x3**2)/(cosb*vev*vev3) - (3*complex(0,1)*MS**2*RA1x3*RA3x1**3*RA3x3**2)/(cosb*vev*vev3) - (3*complex(0,1)*MS**2*RA1x1*RA3x1**2*RA3x3**3)/(cosb*vev*vev3) - (3*complex(0,1)*Mh1**2*RA1x2*RA1x3**2*RA3x2**2*RA3x3)/(sinb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA1x3*RA2x2*RA2x3*RA3x2**2*RA3x3)/(sinb*vev*vev3) - (3*complex(0,1)*Mh1**2*RA1x2**2*RA1x3*RA3x2*RA3x3**2)/(sinb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA1x2*RA2x2*RA2x3*RA3x2*RA3x3**2)/(sinb*vev*vev3) - (3*complex(0,1)*MS**2*RA1x3*RA3x2**3*RA3x3**2)/(sinb*vev*vev3) - (3*complex(0,1)*MS**2*RA1x2*RA3x2**2*RA3x3**3)/(sinb*vev*vev3)',
                  order = {'QED':2})

GC_108 = Coupling(name = 'GC_108',
                  value = '(-3*complex(0,1)*Mh1**2*RA1x1**2*RA2x1*RA3x1**3)/(cosb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA2x1**3*RA3x1**3)/(cosb**2*vev**2) - (3*complex(0,1)*MS**2*RA2x1*RA3x1**5)/(cosb**2*vev**2) + (3*cosb*complex(0,1)*m12**2*RA2x2*RA3x2**3)/(sinb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x2**2*RA2x2*RA3x2**3)/(sinb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA2x2**3*RA3x2**3)/(sinb**2*vev**2) - (3*complex(0,1)*MS**2*RA2x2*RA3x2**5)/(sinb**2*vev**2) - (3*complex(0,1)*m12**2*RA2x2*RA3x1**2*RA3x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x2*RA3x1**2*RA3x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh2**2*RA2x1*RA2x2**2*RA3x1**2*RA3x2)/(cosb*sinb*vev**2) - (3*complex(0,1)*m12**2*RA2x1*RA3x1*RA3x2**2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1*RA3x1*RA3x2**2)/(cosb*sinb*vev**2) - (3*complex(0,1)*Mh2**2*RA2x1**2*RA2x2*RA3x1*RA3x2**2)/(cosb*sinb*vev**2) - (3*complex(0,1)*MS**2*RA2x2*RA3x1**3*RA3x2**2)/(cosb*sinb*vev**2) - (3*complex(0,1)*MS**2*RA2x1*RA3x1**2*RA3x2**3)/(cosb*sinb*vev**2) + (3*complex(0,1)*m12**2*RA2x1*RA3x1**3*sinb)/(cosb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x3**2*RA2x3*RA3x3**3)/vev3**2 - (3*complex(0,1)*Mh2**2*RA2x3**3*RA3x3**3)/vev3**2 - (3*complex(0,1)*MS**2*RA2x3*RA3x3**5)/vev3**2 - (3*complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x3*RA3x1**2*RA3x3)/(cosb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA2x1*RA2x3**2*RA3x1**2*RA3x3)/(cosb*vev*vev3) - (3*complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x1*RA3x1*RA3x3**2)/(cosb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA2x1**2*RA2x3*RA3x1*RA3x3**2)/(cosb*vev*vev3) - (3*complex(0,1)*MS**2*RA2x3*RA3x1**3*RA3x3**2)/(cosb*vev*vev3) - (3*complex(0,1)*MS**2*RA2x1*RA3x1**2*RA3x3**3)/(cosb*vev*vev3) - (3*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x3*RA3x2**2*RA3x3)/(sinb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA2x2*RA2x3**2*RA3x2**2*RA3x3)/(sinb*vev*vev3) - (3*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x2*RA3x2*RA3x3**2)/(sinb*vev*vev3) - (3*complex(0,1)*Mh2**2*RA2x2**2*RA2x3*RA3x2*RA3x3**2)/(sinb*vev*vev3) - (3*complex(0,1)*MS**2*RA2x3*RA3x2**3*RA3x3**2)/(sinb*vev*vev3) - (3*complex(0,1)*MS**2*RA2x2*RA3x2**2*RA3x3**3)/(sinb*vev*vev3)',
                  order = {'QED':2})

GC_109 = Coupling(name = 'GC_109',
                  value = '(-3*complex(0,1)*Mh1**2*RA1x1**2*RA3x1**4)/(cosb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA2x1**2*RA3x1**4)/(cosb**2*vev**2) - (3*complex(0,1)*MS**2*RA3x1**6)/(cosb**2*vev**2) + (3*cosb*complex(0,1)*m12**2*RA3x2**4)/(sinb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x2**2*RA3x2**4)/(sinb**2*vev**2) - (3*complex(0,1)*Mh2**2*RA2x2**2*RA3x2**4)/(sinb**2*vev**2) - (3*complex(0,1)*MS**2*RA3x2**6)/(sinb**2*vev**2) - (6*complex(0,1)*m12**2*RA3x1**2*RA3x2**2)/(cosb*sinb*vev**2) - (6*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA3x1**2*RA3x2**2)/(cosb*sinb*vev**2) - (6*complex(0,1)*Mh2**2*RA2x1*RA2x2*RA3x1**2*RA3x2**2)/(cosb*sinb*vev**2) - (6*complex(0,1)*MS**2*RA3x1**3*RA3x2**3)/(cosb*sinb*vev**2) + (3*complex(0,1)*m12**2*RA3x1**4*sinb)/(cosb**3*vev**2) - (3*complex(0,1)*Mh1**2*RA1x3**2*RA3x3**4)/vev3**2 - (3*complex(0,1)*Mh2**2*RA2x3**2*RA3x3**4)/vev3**2 - (3*complex(0,1)*MS**2*RA3x3**6)/vev3**2 - (6*complex(0,1)*Mh1**2*RA1x1*RA1x3*RA3x1**2*RA3x3**2)/(cosb*vev*vev3) - (6*complex(0,1)*Mh2**2*RA2x1*RA2x3*RA3x1**2*RA3x3**2)/(cosb*vev*vev3) - (6*complex(0,1)*MS**2*RA3x1**3*RA3x3**3)/(cosb*vev*vev3) - (6*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA3x2**2*RA3x3**2)/(sinb*vev*vev3) - (6*complex(0,1)*Mh2**2*RA2x2*RA2x3*RA3x2**2*RA3x3**2)/(sinb*vev*vev3) - (6*complex(0,1)*MS**2*RA3x2**3*RA3x3**3)/(sinb*vev*vev3)',
                  order = {'QED':2})

GC_110 = Coupling(name = 'GC_110',
                  value = '(-2*cosb**2*complex(0,1)*MA0**2*RA1x1**2)/vev**2 + (4*complex(0,1)*m12**2*RA1x1*RA1x2)/vev**2 + (cosb**3*complex(0,1)*m12**2*RA1x2**2)/(sinb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2**4)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*Mh2**2*RA1x2**2*RA2x2**2)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*MS**2*RA1x2**2*RA3x2**2)/(sinb**2*vev**2) + (cosb*complex(0,1)*m12**2*RA1x1**2)/(sinb*vev**2) - (cosb*complex(0,1)*Mh1**2*RA1x1**3*RA1x2)/(sinb*vev**2) - (cosb*complex(0,1)*Mh2**2*RA1x1**2*RA2x1*RA2x2)/(sinb*vev**2) - (cosb*complex(0,1)*MS**2*RA1x1**2*RA3x1*RA3x2)/(sinb*vev**2) - (4*cosb*complex(0,1)*MA0**2*RA1x1*RA1x2*sinb)/vev**2 + (complex(0,1)*m12**2*RA1x2**2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**3*sinb)/(cosb*vev**2) - (complex(0,1)*Mh2**2*RA1x2**2*RA2x1*RA2x2*sinb)/(cosb*vev**2) - (complex(0,1)*MS**2*RA1x2**2*RA3x1*RA3x2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1**4*sinb**2)/(cosb**2*vev**2) - (2*complex(0,1)*MA0**2*RA1x2**2*sinb**2)/vev**2 - (complex(0,1)*Mh2**2*RA1x1**2*RA2x1**2*sinb**2)/(cosb**2*vev**2) - (complex(0,1)*MS**2*RA1x1**2*RA3x1**2*sinb**2)/(cosb**2*vev**2) + (complex(0,1)*m12**2*RA1x1**2*sinb**3)/(cosb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2*RA1x3**3)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*Mh2**2*RA1x3**2*RA2x2*RA2x3)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*MS**2*RA1x3**2*RA3x2*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1*RA1x3**3*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x3**2*RA2x1*RA2x3*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA1x3**2*RA3x1*RA3x3*sinb**2)/(cosb*vev*vev3)',
                  order = {'QED':2})

GC_111 = Coupling(name = 'GC_111',
                  value = '(-2*cosb**2*complex(0,1)*MHP**2*RA1x1**2)/vev**2 + (4*complex(0,1)*m12**2*RA1x1*RA1x2)/vev**2 + (cosb**3*complex(0,1)*m12**2*RA1x2**2)/(sinb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2**4)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*Mh2**2*RA1x2**2*RA2x2**2)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*MS**2*RA1x2**2*RA3x2**2)/(sinb**2*vev**2) + (cosb*complex(0,1)*m12**2*RA1x1**2)/(sinb*vev**2) - (cosb*complex(0,1)*Mh1**2*RA1x1**3*RA1x2)/(sinb*vev**2) - (cosb*complex(0,1)*Mh2**2*RA1x1**2*RA2x1*RA2x2)/(sinb*vev**2) - (cosb*complex(0,1)*MS**2*RA1x1**2*RA3x1*RA3x2)/(sinb*vev**2) - (4*cosb*complex(0,1)*MHP**2*RA1x1*RA1x2*sinb)/vev**2 + (complex(0,1)*m12**2*RA1x2**2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**3*sinb)/(cosb*vev**2) - (complex(0,1)*Mh2**2*RA1x2**2*RA2x1*RA2x2*sinb)/(cosb*vev**2) - (complex(0,1)*MS**2*RA1x2**2*RA3x1*RA3x2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1**4*sinb**2)/(cosb**2*vev**2) - (2*complex(0,1)*MHP**2*RA1x2**2*sinb**2)/vev**2 - (complex(0,1)*Mh2**2*RA1x1**2*RA2x1**2*sinb**2)/(cosb**2*vev**2) - (complex(0,1)*MS**2*RA1x1**2*RA3x1**2*sinb**2)/(cosb**2*vev**2) + (complex(0,1)*m12**2*RA1x1**2*sinb**3)/(cosb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2*RA1x3**3)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*Mh2**2*RA1x3**2*RA2x2*RA2x3)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*MS**2*RA1x3**2*RA3x2*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1*RA1x3**3*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x3**2*RA2x1*RA2x3*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA1x3**2*RA3x1*RA3x3*sinb**2)/(cosb*vev*vev3)',
                  order = {'QED':2})

GC_112 = Coupling(name = 'GC_112',
                  value = '(-2*cosb**2*complex(0,1)*MA0**2*RA1x1*RA2x1)/vev**2 + (2*complex(0,1)*m12**2*RA1x2*RA2x1)/vev**2 + (2*complex(0,1)*m12**2*RA1x1*RA2x2)/vev**2 + (cosb**3*complex(0,1)*m12**2*RA1x2*RA2x2)/(sinb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2**3*RA2x2)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*Mh2**2*RA1x2*RA2x2**3)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*MS**2*RA1x2*RA2x2*RA3x2**2)/(sinb**2*vev**2) + (cosb*complex(0,1)*m12**2*RA1x1*RA2x1)/(sinb*vev**2) - (cosb*complex(0,1)*Mh1**2*RA1x1**2*RA1x2*RA2x1)/(sinb*vev**2) - (cosb*complex(0,1)*Mh2**2*RA1x1*RA2x1**2*RA2x2)/(sinb*vev**2) - (cosb*complex(0,1)*MS**2*RA1x1*RA2x1*RA3x1*RA3x2)/(sinb*vev**2) - (2*cosb*complex(0,1)*MA0**2*RA1x2*RA2x1*sinb)/vev**2 - (2*cosb*complex(0,1)*MA0**2*RA1x1*RA2x2*sinb)/vev**2 + (complex(0,1)*m12**2*RA1x2*RA2x2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**2*RA2x2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh2**2*RA1x2*RA2x1*RA2x2**2*sinb)/(cosb*vev**2) - (complex(0,1)*MS**2*RA1x2*RA2x2*RA3x1*RA3x2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1**3*RA2x1*sinb**2)/(cosb**2*vev**2) - (complex(0,1)*Mh2**2*RA1x1*RA2x1**3*sinb**2)/(cosb**2*vev**2) - (2*complex(0,1)*MA0**2*RA1x2*RA2x2*sinb**2)/vev**2 - (complex(0,1)*MS**2*RA1x1*RA2x1*RA3x1**2*sinb**2)/(cosb**2*vev**2) + (complex(0,1)*m12**2*RA1x1*RA2x1*sinb**3)/(cosb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2*RA1x3**2*RA2x3)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*Mh2**2*RA1x3*RA2x2*RA2x3**2)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*MS**2*RA1x3*RA2x3*RA3x2*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1*RA1x3**2*RA2x3*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x3*RA2x1*RA2x3**2*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA1x3*RA2x3*RA3x1*RA3x3*sinb**2)/(cosb*vev*vev3)',
                  order = {'QED':2})

GC_113 = Coupling(name = 'GC_113',
                  value = '(-2*cosb**2*complex(0,1)*MHP**2*RA1x1*RA2x1)/vev**2 + (2*complex(0,1)*m12**2*RA1x2*RA2x1)/vev**2 + (2*complex(0,1)*m12**2*RA1x1*RA2x2)/vev**2 + (cosb**3*complex(0,1)*m12**2*RA1x2*RA2x2)/(sinb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2**3*RA2x2)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*Mh2**2*RA1x2*RA2x2**3)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*MS**2*RA1x2*RA2x2*RA3x2**2)/(sinb**2*vev**2) + (cosb*complex(0,1)*m12**2*RA1x1*RA2x1)/(sinb*vev**2) - (cosb*complex(0,1)*Mh1**2*RA1x1**2*RA1x2*RA2x1)/(sinb*vev**2) - (cosb*complex(0,1)*Mh2**2*RA1x1*RA2x1**2*RA2x2)/(sinb*vev**2) - (cosb*complex(0,1)*MS**2*RA1x1*RA2x1*RA3x1*RA3x2)/(sinb*vev**2) - (2*cosb*complex(0,1)*MHP**2*RA1x2*RA2x1*sinb)/vev**2 - (2*cosb*complex(0,1)*MHP**2*RA1x1*RA2x2*sinb)/vev**2 + (complex(0,1)*m12**2*RA1x2*RA2x2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**2*RA2x2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh2**2*RA1x2*RA2x1*RA2x2**2*sinb)/(cosb*vev**2) - (complex(0,1)*MS**2*RA1x2*RA2x2*RA3x1*RA3x2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1**3*RA2x1*sinb**2)/(cosb**2*vev**2) - (complex(0,1)*Mh2**2*RA1x1*RA2x1**3*sinb**2)/(cosb**2*vev**2) - (2*complex(0,1)*MHP**2*RA1x2*RA2x2*sinb**2)/vev**2 - (complex(0,1)*MS**2*RA1x1*RA2x1*RA3x1**2*sinb**2)/(cosb**2*vev**2) + (complex(0,1)*m12**2*RA1x1*RA2x1*sinb**3)/(cosb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2*RA1x3**2*RA2x3)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*Mh2**2*RA1x3*RA2x2*RA2x3**2)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*MS**2*RA1x3*RA2x3*RA3x2*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1*RA1x3**2*RA2x3*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x3*RA2x1*RA2x3**2*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA1x3*RA2x3*RA3x1*RA3x3*sinb**2)/(cosb*vev*vev3)',
                  order = {'QED':2})

GC_114 = Coupling(name = 'GC_114',
                  value = '(-2*cosb**2*complex(0,1)*MA0**2*RA2x1**2)/vev**2 + (4*complex(0,1)*m12**2*RA2x1*RA2x2)/vev**2 + (cosb**3*complex(0,1)*m12**2*RA2x2**2)/(sinb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2**2*RA2x2**2)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*Mh2**2*RA2x2**4)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*MS**2*RA2x2**2*RA3x2**2)/(sinb**2*vev**2) + (cosb*complex(0,1)*m12**2*RA2x1**2)/(sinb*vev**2) - (cosb*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1**2)/(sinb*vev**2) - (cosb*complex(0,1)*Mh2**2*RA2x1**3*RA2x2)/(sinb*vev**2) - (cosb*complex(0,1)*MS**2*RA2x1**2*RA3x1*RA3x2)/(sinb*vev**2) - (4*cosb*complex(0,1)*MA0**2*RA2x1*RA2x2*sinb)/vev**2 + (complex(0,1)*m12**2*RA2x2**2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x2**2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh2**2*RA2x1*RA2x2**3*sinb)/(cosb*vev**2) - (complex(0,1)*MS**2*RA2x2**2*RA3x1*RA3x2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1**2*RA2x1**2*sinb**2)/(cosb**2*vev**2) - (complex(0,1)*Mh2**2*RA2x1**4*sinb**2)/(cosb**2*vev**2) - (2*complex(0,1)*MA0**2*RA2x2**2*sinb**2)/vev**2 - (complex(0,1)*MS**2*RA2x1**2*RA3x1**2*sinb**2)/(cosb**2*vev**2) + (complex(0,1)*m12**2*RA2x1**2*sinb**3)/(cosb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x3**2)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*Mh2**2*RA2x2*RA2x3**3)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*MS**2*RA2x3**2*RA3x2*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x3**2*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA2x1*RA2x3**3*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA2x3**2*RA3x1*RA3x3*sinb**2)/(cosb*vev*vev3)',
                  order = {'QED':2})

GC_115 = Coupling(name = 'GC_115',
                  value = '(-2*cosb**2*complex(0,1)*MHP**2*RA2x1**2)/vev**2 + (4*complex(0,1)*m12**2*RA2x1*RA2x2)/vev**2 + (cosb**3*complex(0,1)*m12**2*RA2x2**2)/(sinb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2**2*RA2x2**2)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*Mh2**2*RA2x2**4)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*MS**2*RA2x2**2*RA3x2**2)/(sinb**2*vev**2) + (cosb*complex(0,1)*m12**2*RA2x1**2)/(sinb*vev**2) - (cosb*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1**2)/(sinb*vev**2) - (cosb*complex(0,1)*Mh2**2*RA2x1**3*RA2x2)/(sinb*vev**2) - (cosb*complex(0,1)*MS**2*RA2x1**2*RA3x1*RA3x2)/(sinb*vev**2) - (4*cosb*complex(0,1)*MHP**2*RA2x1*RA2x2*sinb)/vev**2 + (complex(0,1)*m12**2*RA2x2**2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x2**2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh2**2*RA2x1*RA2x2**3*sinb)/(cosb*vev**2) - (complex(0,1)*MS**2*RA2x2**2*RA3x1*RA3x2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1**2*RA2x1**2*sinb**2)/(cosb**2*vev**2) - (complex(0,1)*Mh2**2*RA2x1**4*sinb**2)/(cosb**2*vev**2) - (2*complex(0,1)*MHP**2*RA2x2**2*sinb**2)/vev**2 - (complex(0,1)*MS**2*RA2x1**2*RA3x1**2*sinb**2)/(cosb**2*vev**2) + (complex(0,1)*m12**2*RA2x1**2*sinb**3)/(cosb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x3**2)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*Mh2**2*RA2x2*RA2x3**3)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*MS**2*RA2x3**2*RA3x2*RA3x3)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x3**2*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA2x1*RA2x3**3*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA2x3**2*RA3x1*RA3x3*sinb**2)/(cosb*vev*vev3)',
                  order = {'QED':2})

GC_116 = Coupling(name = 'GC_116',
                  value = '(-2*cosb**2*complex(0,1)*MA0**2*RA1x1*RA3x1)/vev**2 + (2*complex(0,1)*m12**2*RA1x2*RA3x1)/vev**2 + (2*complex(0,1)*m12**2*RA1x1*RA3x2)/vev**2 + (cosb**3*complex(0,1)*m12**2*RA1x2*RA3x2)/(sinb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2**3*RA3x2)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*Mh2**2*RA1x2*RA2x2**2*RA3x2)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*MS**2*RA1x2*RA3x2**3)/(sinb**2*vev**2) + (cosb*complex(0,1)*m12**2*RA1x1*RA3x1)/(sinb*vev**2) - (cosb*complex(0,1)*Mh1**2*RA1x1**2*RA1x2*RA3x1)/(sinb*vev**2) - (cosb*complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x2*RA3x1)/(sinb*vev**2) - (cosb*complex(0,1)*MS**2*RA1x1*RA3x1**2*RA3x2)/(sinb*vev**2) - (2*cosb*complex(0,1)*MA0**2*RA1x2*RA3x1*sinb)/vev**2 - (2*cosb*complex(0,1)*MA0**2*RA1x1*RA3x2*sinb)/vev**2 + (complex(0,1)*m12**2*RA1x2*RA3x2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**2*RA3x2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh2**2*RA1x2*RA2x1*RA2x2*RA3x2*sinb)/(cosb*vev**2) - (complex(0,1)*MS**2*RA1x2*RA3x1*RA3x2**2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1**3*RA3x1*sinb**2)/(cosb**2*vev**2) - (complex(0,1)*Mh2**2*RA1x1*RA2x1**2*RA3x1*sinb**2)/(cosb**2*vev**2) - (complex(0,1)*MS**2*RA1x1*RA3x1**3*sinb**2)/(cosb**2*vev**2) - (2*complex(0,1)*MA0**2*RA1x2*RA3x2*sinb**2)/vev**2 + (complex(0,1)*m12**2*RA1x1*RA3x1*sinb**3)/(cosb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2*RA1x3**2*RA3x3)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*Mh2**2*RA1x3*RA2x2*RA2x3*RA3x3)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*MS**2*RA1x3*RA3x2*RA3x3**2)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1*RA1x3**2*RA3x3*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x3*RA2x1*RA2x3*RA3x3*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA1x3*RA3x1*RA3x3**2*sinb**2)/(cosb*vev*vev3)',
                  order = {'QED':2})

GC_117 = Coupling(name = 'GC_117',
                  value = '(-2*cosb**2*complex(0,1)*MHP**2*RA1x1*RA3x1)/vev**2 + (2*complex(0,1)*m12**2*RA1x2*RA3x1)/vev**2 + (2*complex(0,1)*m12**2*RA1x1*RA3x2)/vev**2 + (cosb**3*complex(0,1)*m12**2*RA1x2*RA3x2)/(sinb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2**3*RA3x2)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*Mh2**2*RA1x2*RA2x2**2*RA3x2)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*MS**2*RA1x2*RA3x2**3)/(sinb**2*vev**2) + (cosb*complex(0,1)*m12**2*RA1x1*RA3x1)/(sinb*vev**2) - (cosb*complex(0,1)*Mh1**2*RA1x1**2*RA1x2*RA3x1)/(sinb*vev**2) - (cosb*complex(0,1)*Mh2**2*RA1x1*RA2x1*RA2x2*RA3x1)/(sinb*vev**2) - (cosb*complex(0,1)*MS**2*RA1x1*RA3x1**2*RA3x2)/(sinb*vev**2) - (2*cosb*complex(0,1)*MHP**2*RA1x2*RA3x1*sinb)/vev**2 - (2*cosb*complex(0,1)*MHP**2*RA1x1*RA3x2*sinb)/vev**2 + (complex(0,1)*m12**2*RA1x2*RA3x2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2**2*RA3x2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh2**2*RA1x2*RA2x1*RA2x2*RA3x2*sinb)/(cosb*vev**2) - (complex(0,1)*MS**2*RA1x2*RA3x1*RA3x2**2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1**3*RA3x1*sinb**2)/(cosb**2*vev**2) - (complex(0,1)*Mh2**2*RA1x1*RA2x1**2*RA3x1*sinb**2)/(cosb**2*vev**2) - (complex(0,1)*MS**2*RA1x1*RA3x1**3*sinb**2)/(cosb**2*vev**2) - (2*complex(0,1)*MHP**2*RA1x2*RA3x2*sinb**2)/vev**2 + (complex(0,1)*m12**2*RA1x1*RA3x1*sinb**3)/(cosb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2*RA1x3**2*RA3x3)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*Mh2**2*RA1x3*RA2x2*RA2x3*RA3x3)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*MS**2*RA1x3*RA3x2*RA3x3**2)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1*RA1x3**2*RA3x3*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA1x3*RA2x1*RA2x3*RA3x3*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA1x3*RA3x1*RA3x3**2*sinb**2)/(cosb*vev*vev3)',
                  order = {'QED':2})

GC_118 = Coupling(name = 'GC_118',
                  value = '(-2*cosb**2*complex(0,1)*MA0**2*RA2x1*RA3x1)/vev**2 + (2*complex(0,1)*m12**2*RA2x2*RA3x1)/vev**2 + (2*complex(0,1)*m12**2*RA2x1*RA3x2)/vev**2 + (cosb**3*complex(0,1)*m12**2*RA2x2*RA3x2)/(sinb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2**2*RA2x2*RA3x2)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*Mh2**2*RA2x2**3*RA3x2)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*MS**2*RA2x2*RA3x2**3)/(sinb**2*vev**2) + (cosb*complex(0,1)*m12**2*RA2x1*RA3x1)/(sinb*vev**2) - (cosb*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1*RA3x1)/(sinb*vev**2) - (cosb*complex(0,1)*Mh2**2*RA2x1**2*RA2x2*RA3x1)/(sinb*vev**2) - (cosb*complex(0,1)*MS**2*RA2x1*RA3x1**2*RA3x2)/(sinb*vev**2) - (2*cosb*complex(0,1)*MA0**2*RA2x2*RA3x1*sinb)/vev**2 - (2*cosb*complex(0,1)*MA0**2*RA2x1*RA3x2*sinb)/vev**2 + (complex(0,1)*m12**2*RA2x2*RA3x2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x2*RA3x2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh2**2*RA2x1*RA2x2**2*RA3x2*sinb)/(cosb*vev**2) - (complex(0,1)*MS**2*RA2x2*RA3x1*RA3x2**2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1**2*RA2x1*RA3x1*sinb**2)/(cosb**2*vev**2) - (complex(0,1)*Mh2**2*RA2x1**3*RA3x1*sinb**2)/(cosb**2*vev**2) - (complex(0,1)*MS**2*RA2x1*RA3x1**3*sinb**2)/(cosb**2*vev**2) - (2*complex(0,1)*MA0**2*RA2x2*RA3x2*sinb**2)/vev**2 + (complex(0,1)*m12**2*RA2x1*RA3x1*sinb**3)/(cosb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x3*RA3x3)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*Mh2**2*RA2x2*RA2x3**2*RA3x3)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*MS**2*RA2x3*RA3x2*RA3x3**2)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x3*RA3x3*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA2x1*RA2x3**2*RA3x3*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA2x3*RA3x1*RA3x3**2*sinb**2)/(cosb*vev*vev3)',
                  order = {'QED':2})

GC_119 = Coupling(name = 'GC_119',
                  value = '(-2*cosb**2*complex(0,1)*MHP**2*RA2x1*RA3x1)/vev**2 + (2*complex(0,1)*m12**2*RA2x2*RA3x1)/vev**2 + (2*complex(0,1)*m12**2*RA2x1*RA3x2)/vev**2 + (cosb**3*complex(0,1)*m12**2*RA2x2*RA3x2)/(sinb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2**2*RA2x2*RA3x2)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*Mh2**2*RA2x2**3*RA3x2)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*MS**2*RA2x2*RA3x2**3)/(sinb**2*vev**2) + (cosb*complex(0,1)*m12**2*RA2x1*RA3x1)/(sinb*vev**2) - (cosb*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x1*RA3x1)/(sinb*vev**2) - (cosb*complex(0,1)*Mh2**2*RA2x1**2*RA2x2*RA3x1)/(sinb*vev**2) - (cosb*complex(0,1)*MS**2*RA2x1*RA3x1**2*RA3x2)/(sinb*vev**2) - (2*cosb*complex(0,1)*MHP**2*RA2x2*RA3x1*sinb)/vev**2 - (2*cosb*complex(0,1)*MHP**2*RA2x1*RA3x2*sinb)/vev**2 + (complex(0,1)*m12**2*RA2x2*RA3x2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2*RA2x2*RA3x2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh2**2*RA2x1*RA2x2**2*RA3x2*sinb)/(cosb*vev**2) - (complex(0,1)*MS**2*RA2x2*RA3x1*RA3x2**2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1**2*RA2x1*RA3x1*sinb**2)/(cosb**2*vev**2) - (complex(0,1)*Mh2**2*RA2x1**3*RA3x1*sinb**2)/(cosb**2*vev**2) - (complex(0,1)*MS**2*RA2x1*RA3x1**3*sinb**2)/(cosb**2*vev**2) - (2*complex(0,1)*MHP**2*RA2x2*RA3x2*sinb**2)/vev**2 + (complex(0,1)*m12**2*RA2x1*RA3x1*sinb**3)/(cosb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA2x3*RA3x3)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*Mh2**2*RA2x2*RA2x3**2*RA3x3)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*MS**2*RA2x3*RA3x2*RA3x3**2)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1*RA1x3*RA2x3*RA3x3*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA2x1*RA2x3**2*RA3x3*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA2x3*RA3x1*RA3x3**2*sinb**2)/(cosb*vev*vev3)',
                  order = {'QED':2})

GC_120 = Coupling(name = 'GC_120',
                  value = '(-2*cosb**2*complex(0,1)*MA0**2*RA3x1**2)/vev**2 + (4*complex(0,1)*m12**2*RA3x1*RA3x2)/vev**2 + (cosb**3*complex(0,1)*m12**2*RA3x2**2)/(sinb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2**2*RA3x2**2)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*Mh2**2*RA2x2**2*RA3x2**2)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*MS**2*RA3x2**4)/(sinb**2*vev**2) + (cosb*complex(0,1)*m12**2*RA3x1**2)/(sinb*vev**2) - (cosb*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA3x1**2)/(sinb*vev**2) - (cosb*complex(0,1)*Mh2**2*RA2x1*RA2x2*RA3x1**2)/(sinb*vev**2) - (cosb*complex(0,1)*MS**2*RA3x1**3*RA3x2)/(sinb*vev**2) - (4*cosb*complex(0,1)*MA0**2*RA3x1*RA3x2*sinb)/vev**2 + (complex(0,1)*m12**2*RA3x2**2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2*RA3x2**2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh2**2*RA2x1*RA2x2*RA3x2**2*sinb)/(cosb*vev**2) - (complex(0,1)*MS**2*RA3x1*RA3x2**3*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1**2*RA3x1**2*sinb**2)/(cosb**2*vev**2) - (complex(0,1)*Mh2**2*RA2x1**2*RA3x1**2*sinb**2)/(cosb**2*vev**2) - (complex(0,1)*MS**2*RA3x1**4*sinb**2)/(cosb**2*vev**2) - (2*complex(0,1)*MA0**2*RA3x2**2*sinb**2)/vev**2 + (complex(0,1)*m12**2*RA3x1**2*sinb**3)/(cosb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA3x3**2)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*Mh2**2*RA2x2*RA2x3*RA3x3**2)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*MS**2*RA3x2*RA3x3**3)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1*RA1x3*RA3x3**2*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA2x1*RA2x3*RA3x3**2*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA3x1*RA3x3**3*sinb**2)/(cosb*vev*vev3)',
                  order = {'QED':2})

GC_121 = Coupling(name = 'GC_121',
                  value = '(-2*cosb**2*complex(0,1)*MHP**2*RA3x1**2)/vev**2 + (4*complex(0,1)*m12**2*RA3x1*RA3x2)/vev**2 + (cosb**3*complex(0,1)*m12**2*RA3x2**2)/(sinb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2**2*RA3x2**2)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*Mh2**2*RA2x2**2*RA3x2**2)/(sinb**2*vev**2) - (cosb**2*complex(0,1)*MS**2*RA3x2**4)/(sinb**2*vev**2) + (cosb*complex(0,1)*m12**2*RA3x1**2)/(sinb*vev**2) - (cosb*complex(0,1)*Mh1**2*RA1x1*RA1x2*RA3x1**2)/(sinb*vev**2) - (cosb*complex(0,1)*Mh2**2*RA2x1*RA2x2*RA3x1**2)/(sinb*vev**2) - (cosb*complex(0,1)*MS**2*RA3x1**3*RA3x2)/(sinb*vev**2) - (4*cosb*complex(0,1)*MHP**2*RA3x1*RA3x2*sinb)/vev**2 + (complex(0,1)*m12**2*RA3x2**2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1*RA1x2*RA3x2**2*sinb)/(cosb*vev**2) - (complex(0,1)*Mh2**2*RA2x1*RA2x2*RA3x2**2*sinb)/(cosb*vev**2) - (complex(0,1)*MS**2*RA3x1*RA3x2**3*sinb)/(cosb*vev**2) - (complex(0,1)*Mh1**2*RA1x1**2*RA3x1**2*sinb**2)/(cosb**2*vev**2) - (complex(0,1)*Mh2**2*RA2x1**2*RA3x1**2*sinb**2)/(cosb**2*vev**2) - (complex(0,1)*MS**2*RA3x1**4*sinb**2)/(cosb**2*vev**2) - (2*complex(0,1)*MHP**2*RA3x2**2*sinb**2)/vev**2 + (complex(0,1)*m12**2*RA3x1**2*sinb**3)/(cosb**3*vev**2) - (cosb**2*complex(0,1)*Mh1**2*RA1x2*RA1x3*RA3x3**2)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*Mh2**2*RA2x2*RA2x3*RA3x3**2)/(sinb*vev*vev3) - (cosb**2*complex(0,1)*MS**2*RA3x2*RA3x3**3)/(sinb*vev*vev3) - (complex(0,1)*Mh1**2*RA1x1*RA1x3*RA3x3**2*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*Mh2**2*RA2x1*RA2x3*RA3x3**2*sinb**2)/(cosb*vev*vev3) - (complex(0,1)*MS**2*RA3x1*RA3x3**3*sinb**2)/(cosb*vev*vev3)',
                  order = {'QED':2})

GC_122 = Coupling(name = 'GC_122',
                  value = '-((complex(0,1)*RA1x1*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '-((complex(0,1)*RA1x2*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '-((complex(0,1)*RA1x3*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '-((complex(0,1)*RA2x1*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '-((complex(0,1)*RA3x1*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '(sinb*yb)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '-((complex(0,1)*RA1x1*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '-((complex(0,1)*RA1x2*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '-((complex(0,1)*RA1x3*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '-((complex(0,1)*RA2x1*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '-((complex(0,1)*RA3x1*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '-((sinb*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '-((complex(0,1)*RA1x1*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '-((complex(0,1)*RA1x2*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '-((complex(0,1)*RA1x3*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '-((complex(0,1)*RA2x1*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '-((complex(0,1)*RA3x1*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_139 = Coupling(name = 'GC_139',
                  value = '(sinb*ydo)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '-((complex(0,1)*RA1x1*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '-((complex(0,1)*RA1x2*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '-((complex(0,1)*RA1x3*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '-((complex(0,1)*RA2x1*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '-((complex(0,1)*RA3x1*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = 'complex(0,1)*sinb*ye',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '(sinb*ye)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '-((complex(0,1)*RA1x1*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '-((complex(0,1)*RA1x2*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '-((complex(0,1)*RA1x3*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '-((complex(0,1)*RA2x1*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '-((complex(0,1)*RA3x1*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = 'complex(0,1)*sinb*ym',
                  order = {'QED':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '(sinb*ym)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '-((complex(0,1)*RA1x1*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '-((complex(0,1)*RA1x2*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '-((complex(0,1)*RA1x3*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '-((complex(0,1)*RA2x1*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '-((complex(0,1)*RA3x1*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_159 = Coupling(name = 'GC_159',
                  value = '(sinb*ys)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '-((complex(0,1)*RA1x1*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_161 = Coupling(name = 'GC_161',
                  value = '-((complex(0,1)*RA1x2*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_162 = Coupling(name = 'GC_162',
                  value = '-((complex(0,1)*RA1x3*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_163 = Coupling(name = 'GC_163',
                  value = '-((complex(0,1)*RA2x1*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_164 = Coupling(name = 'GC_164',
                  value = '-((complex(0,1)*RA3x1*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '-((sinb*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '-((complex(0,1)*RA1x1*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_167 = Coupling(name = 'GC_167',
                  value = '-((complex(0,1)*RA1x2*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '-((complex(0,1)*RA1x3*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_169 = Coupling(name = 'GC_169',
                  value = '-((complex(0,1)*RA2x1*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '-((complex(0,1)*RA3x1*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_171 = Coupling(name = 'GC_171',
                  value = 'complex(0,1)*sinb*ytau',
                  order = {'QED':1})

GC_172 = Coupling(name = 'GC_172',
                  value = '(sinb*ytau)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_173 = Coupling(name = 'GC_173',
                  value = '-((complex(0,1)*RA1x1*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_174 = Coupling(name = 'GC_174',
                  value = '-((complex(0,1)*RA1x2*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_175 = Coupling(name = 'GC_175',
                  value = '-((complex(0,1)*RA1x3*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_176 = Coupling(name = 'GC_176',
                  value = '-((complex(0,1)*RA2x1*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_177 = Coupling(name = 'GC_177',
                  value = '-((complex(0,1)*RA3x1*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_178 = Coupling(name = 'GC_178',
                  value = '-((sinb*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

