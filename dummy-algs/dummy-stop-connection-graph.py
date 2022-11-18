#!/bin/python3

import argparse

parser = argparse.ArgumentParser(
    prog='dummy-stop-connection-graph',
    description='Outputs a stop connection graph for Coventry.')

parser.add_argument("-e", "--empty-output", action="store_true",
                    help="Output a blank file instead of the json", dest="empty_output")
parser.add_argument("-o", dest="output", type=argparse.FileType("w"),
                    action="store", required=False, metavar="outputfile", help="The filename of the output json file. Defaults to out.json", default="out.json")
parser.add_argument("map", type=argparse.FileType("r"), help="A json file containing the map.")
parser.add_argument("stops", type=argparse.FileType("r"), help="A json file containing the bus stops.")

args = parser.parse_args()
if not args.empty_output:
    args.output.write("""{
  "links": [
    {
      "id": 1,
      "name": "Birmingham Rd / Brickhill Lane => Birmingham Rd / Brickhill Lane",
      "length": 0.0006062756633735554,
      "speed": {
        "0:00": 30
      },
      "startid": 370819527,
      "endid": 370819530
    },
    {
      "id": 2,
      "name": "Birmingham Rd / Brickhill Lane => Birmingham Rd / Windmill Farm",
      "length": 0.012881388064957972,
      "speed": {
        "0:00": 30
      },
      "startid": 370819530,
      "endid": 370819525
    },
    {
      "id": 3,
      "name": "Birmingham Rd / Windmill Farm => Parkhill Dr / Parkhill Estate Terminus",
      "length": 0.008745833371377748,
      "speed": {
        "0:00": 30
      },
      "startid": 370819525,
      "endid": 370818229
    },
    {
      "id": 4,
      "name": "Parkhill Dr / Parkhill Estate Terminus => Birmingham Rd / Neale Avenue",
      "length": 0.006306014482219508,
      "speed": {
        "0:00": 30
      },
      "startid": 370818229,
      "endid": 370819493
    },
    {
      "id": 5,
      "name": "Birmingham Rd / Neale Avenue => Birmingham Rd / Neale Avenue",
      "length": 0.0014933214590289524,
      "speed": {
        "0:00": 30
      },
      "startid": 370819493,
      "endid": 370819494
    },
    {
      "id": 6,
      "name": "Birmingham Rd / Neale Avenue => Birmingham Rd / Allesley Post Office",
      "length": 0.0015646175379312936,
      "speed": {
        "0:00": 30
      },
      "startid": 370819494,
      "endid": 370819489
    },
    {
      "id": 7,
      "name": "Birmingham Rd / Allesley Post Office => Birmingham Rd / Allesley Post Office",
      "length": 0.0008820798716671872,
      "speed": {
        "0:00": 30
      },
      "startid": 370819489,
      "endid": 370819490
    },
    {
      "id": 8,
      "name": "Birmingham Rd / Allesley Post Office => Birmingham Rd / Butchers Lane",
      "length": 0.002760424034455538,
      "speed": {
        "0:00": 30
      },
      "startid": 370819490,
      "endid": 370819486
    },
    {
      "id": 9,
      "name": "Birmingham Rd / Butchers Lane => Birmingham Rd / Butchers Lane",
      "length": 0.002666668160832974,
      "speed": {
        "0:00": 30
      },
      "startid": 370819486,
      "endid": 370819484
    },
    {
      "id": 10,
      "name": "Birmingham Rd / Butchers Lane => Birmingham Rd / Norton Grange",
      "length": 0.0032394266313661847,
      "speed": {
        "0:00": 30
      },
      "startid": 370819484,
      "endid": 370819481
    },
    {
      "id": 11,
      "name": "Birmingham Rd / Norton Grange => Birmingham Rd / Norton Grange",
      "length": 0.00018735042033075414,
      "speed": {
        "0:00": 30
      },
      "startid": 370819481,
      "endid": 370819482
    },
    {
      "id": 12,
      "name": "Birmingham Rd / Norton Grange => Holyhead Rd / Dulverton Avenue",
      "length": 0.005333658446132934,
      "speed": {
        "0:00": 30
      },
      "startid": 370819482,
      "endid": 370819479
    },
    {
      "id": 13,
      "name": "Holyhead Rd / Dulverton Avenue => Holyhead Rd / Dulverton Avenue",
      "length": 0.0004808124894384671,
      "speed": {
        "0:00": 30
      },
      "startid": 370819479,
      "endid": 370819480
    },
    {
      "id": 14,
      "name": "Holyhead Rd / Dulverton Avenue => Holyhead Rd / Grayswood Avenue",
      "length": 0.005298354314313946,
      "speed": {
        "0:00": 30
      },
      "startid": 370819480,
      "endid": 370819453
    },
    {
      "id": 15,
      "name": "Holyhead Rd / Grayswood Avenue => Holyhead Rd / Grayswood Avenue",
      "length": 0.0015367593988653307,
      "speed": {
        "0:00": 30
      },
      "startid": 370819453,
      "endid": 370819454
    },
    {
      "id": 16,
      "name": "Holyhead Rd / Grayswood Avenue => Holyhead Rd / Southbank Rd",
      "length": 0.0018399552304324976,
      "speed": {
        "0:00": 30
      },
      "startid": 370819454,
      "endid": 370819450
    },
    {
      "id": 17,
      "name": "Holyhead Rd / Southbank Rd => Holyhead Rd / Southbank Rd",
      "length": 0.0020147104010257858,
      "speed": {
        "0:00": 30
      },
      "startid": 370819450,
      "endid": 370819452
    },
    {
      "id": 18,
      "name": "Holyhead Rd / Southbank Rd => Holyhead Rd / Redesdale Avenue",
      "length": 0.0032341260334133653,
      "speed": {
        "0:00": 30
      },
      "startid": 370819452,
      "endid": 370819398
    },
    {
      "id": 19,
      "name": "Holyhead Rd / Redesdale Avenue => Holyhead Rd / Redesdale Avenue",
      "length": 0.0006598299856777957,
      "speed": {
        "0:00": 30
      },
      "startid": 370819398,
      "endid": 370819399
    },
    {
      "id": 20,
      "name": "Holyhead Rd / Redesdale Avenue => Holyhead Rd / Moseley Avenue",
      "length": 0.003837463750968571,
      "speed": {
        "0:00": 30
      },
      "startid": 370819399,
      "endid": 370819395
    },
    {
      "id": 21,
      "name": "Holyhead Rd / Moseley Avenue => Holyhead Rd / Moseley Avenue",
      "length": 0.0008869628740820093,
      "speed": {
        "0:00": 30
      },
      "startid": 370819395,
      "endid": 370819397
    },
    {
      "id": 22,
      "name": "Holyhead Rd / Moseley Avenue => Holyhead Rd / Alvis Retail Park",
      "length": 0.0043102225893796985,
      "speed": {
        "0:00": 30
      },
      "startid": 370819397,
      "endid": 370819361
    },
    {
      "id": 23,
      "name": "Holyhead Rd / Alvis Retail Park => Holyhead Rd / Alvis Retail Park",
      "length": 0.0002442421953716176,
      "speed": {
        "0:00": 30
      },
      "startid": 370819361,
      "endid": 370819363
    },
    {
      "id": 24,
      "name": "Holyhead Rd / Alvis Retail Park => Holyhead Rd / Meriden St",
      "length": 0.006867083871630511,
      "speed": {
        "0:00": 30
      },
      "startid": 370819363,
      "endid": 370819360
    },
    {
      "id": 25,
      "name": "Holyhead Rd / Meriden St => Holyhead Rd / Meriden St",
      "length": 0.0008530438792932072,
      "speed": {
        "0:00": 30
      },
      "startid": 370819360,
      "endid": 370819359
    },
    {
      "id": 26,
      "name": "Holyhead Rd / Meriden St => Holyhead Rd / Ringway",
      "length": 0.0034018527613649606,
      "speed": {
        "0:00": 30
      },
      "startid": 370819359,
      "endid": 370819355
    },
    {
      "id": 27,
      "name": "Holyhead Rd / Ringway => Holyhead Rd / Ringway",
      "length": 0.0001523425416673504,
      "speed": {
        "0:00": 30
      },
      "startid": 370819355,
      "endid": 370819357
    },
    {
      "id": 28,
      "name": "Holyhead Rd / Ringway => UL3",
      "length": 0.0059757926938607455,
      "speed": {
        "0:00": 30
      },
      "startid": 370819357,
      "endid": 370817723
    },
    {
      "id": 29,
      "name": "UL4 => BS3",
      "length": 0.002031303665137189,
      "speed": {
        "0:00": 30
      },
      "startid": 370817719,
      "endid": 370817695
    },
    {
      "id": 30,
      "name": "GH1 => Gibbet Hill Rd / Kirby Corner Rd",
      "length": 0.00028726186659678205,
      "speed": {
        "0:00": 30
      },
      "startid": 370817946,
      "endid": 370817948
    },
    {
      "id": 31,
      "name": "Gibbet Hill Rd / Kirby Corner Rd => WR5",
      "length": 0.05383669593892193,
      "speed": {
        "0:00": 30
      },
      "startid": 370817948,
      "endid": 370817793
    },
    {
      "id": 32,
      "name": "WR5 => WR6",
      "length": 0.0004939037153162216,
      "speed": {
        "0:00": 30
      },
      "startid": 370817793,
      "endid": 370817791
    },
    {
      "id": 33,
      "name": "Crackley => Kenilworth Rd / Cryfield Grange Rd",
      "length": 0.011246090378880294,
      "speed": {
        "0:00": 30
      },
      "startid": 487161622,
      "endid": 370819558
    },
    {
      "id": 34,
      "name": "Kenilworth Rd / Cryfield Grange Rd => Kenilworth Rd / Cryfield Grange Rd",
      "length": 0.000620335473758559,
      "speed": {
        "0:00": 30
      },
      "startid": 370819558,
      "endid": 370819556
    },
    {
      "id": 35,
      "name": "Kenilworth Rd / Cryfield Grange Rd => Kenilworth Rd / Gibbet Hill Rd",
      "length": 0.0036430279782063376,
      "speed": {
        "0:00": 30
      },
      "startid": 370819556,
      "endid": 370819763
    },
    {
      "id": 36,
      "name": "Kenilworth Rd / Gibbet Hill Rd => GH5",
      "length": 0.0043060810965434085,
      "speed": {
        "0:00": 30
      },
      "startid": 370819763,
      "endid": 370819587
    },
    {
      "id": 37,
      "name": "GH5 => GH6",
      "length": 0.003083086677340662,
      "speed": {
        "0:00": 30
      },
      "startid": 370819587,
      "endid": 370819586
    },
    {
      "id": 38,
      "name": "GH6 => Kirby Corner Rd / Gibbet Hill Rd",
      "length": 0.01508304399582899,
      "speed": {
        "0:00": 30
      },
      "startid": 370819586,
      "endid": 370819749
    },
    {
      "id": 39,
      "name": "Kirby Corner Rd / Gibbet Hill Rd => Kirby Corner Rd / University Westwood Site",
      "length": 0.004738827116489978,
      "speed": {
        "0:00": 30
      },
      "startid": 370819749,
      "endid": 370817931
    },
    {
      "id": 40,
      "name": "Kirby Corner Rd / University Westwood Site => Kirby Corner Rd / University Westwood Site",
      "length": 0.0008440280208634823,
      "speed": {
        "0:00": 30
      },
      "startid": 370817931,
      "endid": 370817930
    },
    {
      "id": 41,
      "name": "Kirby Corner Rd / University Westwood Site => Kirby Corner Rd / Lynchgate Rd",
      "length": 0.005184185461573927,
      "speed": {
        "0:00": 30
      },
      "startid": 370817930,
      "endid": 370817929
    },
    {
      "id": 42,
      "name": "Kirby Corner Rd / Lynchgate Rd => Kirby Corner Rd / Lynchgate Rd",
      "length": 0.00029797681117596606,
      "speed": {
        "0:00": 30
      },
      "startid": 370817929,
      "endid": 370817927
    },
    {
      "id": 43,
      "name": "Kirby Corner Rd / Lynchgate Rd => Sir Henry Parkes Rd / Centenary Rd",
      "length": 0.004740845448860625,
      "speed": {
        "0:00": 30
      },
      "startid": 370817927,
      "endid": 370817913
    },
    {
      "id": 44,
      "name": "Sir Henry Parkes Rd / Centenary Rd => Sir Henry Parkes Rd / Centenary Rd",
      "length": 0.00046643209580508546,
      "speed": {
        "0:00": 30
      },
      "startid": 370817913,
      "endid": 370817911
    },
    {
      "id": 45,
      "name": "Sir Henry Parkes Rd / Centenary Rd => Fletchamstead Highway / Torrington Avenue",
      "length": 0.009913927022121799,
      "speed": {
        "0:00": 30
      },
      "startid": 370817911,
      "endid": 370818204
    },
    {
      "id": 46,
      "name": "Fletchamstead Highway / Torrington Avenue => Herald Avenue / Vanguard Avenue",
      "length": 0.0040187881519201775,
      "speed": {
        "0:00": 30
      },
      "startid": 370818204,
      "endid": 370817405
    },
    {
      "id": 47,
      "name": "Herald Avenue / Vanguard Avenue => Herald Avenue / Vanguard Avenue",
      "length": 0.0006769428336276444,
      "speed": {
        "0:00": 30
      },
      "startid": 370817405,
      "endid": 370817403
    },
    {
      "id": 48,
      "name": "Herald Avenue / Vanguard Avenue => Herald Avenue / Business Park",
      "length": 0.003840197032705414,
      "speed": {
        "0:00": 30
      },
      "startid": 370817403,
      "endid": 370817716
    },
    {
      "id": 49,
      "name": "Herald Avenue / Business Park => Herald Avenue / Business Park",
      "length": 0.00012615902663344223,
      "speed": {
        "0:00": 30
      },
      "startid": 370817716,
      "endid": 370817713
    },
    {
      "id": 50,
      "name": "Herald Avenue / Business Park => Tile Hill Lane / Brd Lane",
      "length": 0.0038903780407555204,
      "speed": {
        "0:00": 30
      },
      "startid": 370817713,
      "endid": 370818159
    },
    {
      "id": 51,
      "name": "Tile Hill Lane / Brd Lane => Tile Hill Lane / Broad Lane",
      "length": 0.00033008995743662075,
      "speed": {
        "0:00": 30
      },
      "startid": 370818159,
      "endid": 370818157
    },
    {
      "id": 52,
      "name": "Tile Hill Lane / Broad Lane => Tile Hill Lane / Hearsall Common",
      "length": 0.005069562744458173,
      "speed": {
        "0:00": 30
      },
      "startid": 370818157,
      "endid": 370818853
    },
    {
      "id": 53,
      "name": "Tile Hill Lane / Hearsall Common => Tile Hill Lane / Hearsall Common",
      "length": 0.0010889620838209612,
      "speed": {
        "0:00": 30
      },
      "startid": 370818853,
      "endid": 370818854
    },
    {
      "id": 54,
      "name": "Tile Hill Lane / Hearsall Common => Earlsdon Ave Nth / Hearsall Common",
      "length": 0.006721247135018954,
      "speed": {
        "0:00": 30
      },
      "startid": 370818854,
      "endid": 370819669
    },
    {
      "id": 55,
      "name": "Earlsdon Ave Nth / Hearsall Common => Earlsdon Ave Nth / Kensington Rd",
      "length": 0.003008462286617318,
      "speed": {
        "0:00": 30
      },
      "startid": 370819669,
      "endid": 370818041
    },
    {
      "id": 56,
      "name": "Earlsdon Ave Nth / Kensington Rd => Earlsdon Ave Nth / Kensington Rd",
      "length": 0.0006666035178424757,
      "speed": {
        "0:00": 30
      },
      "startid": 370818041,
      "endid": 370818040
    },
    {
      "id": 57,
      "name": "Earlsdon Ave Nth / Kensington Rd => Earlsdon Ave Nth / Earlsdon St",
      "length": 0.002565598663084612,
      "speed": {
        "0:00": 30
      },
      "startid": 370818040,
      "endid": 370819666
    },
    {
      "id": 58,
      "name": "Earlsdon Ave Nth / Earlsdon St => Earlsdon Ave Sth / Earlsdon St",
      "length": 0.0007956032805336548,
      "speed": {
        "0:00": 30
      },
      "startid": 370819666,
      "endid": 370819665
    },
    {
      "id": 59,
      "name": "Earlsdon Ave Sth / Earlsdon St => Earlsdon Ave Sth / Warwick Avenue",
      "length": 0.0038277053870416837,
      "speed": {
        "0:00": 30
      },
      "startid": 370819665,
      "endid": 370817899
    },
    {
      "id": 60,
      "name": "Earlsdon Ave Sth / Warwick Avenue => Earlsdon Ave Sth / Warwick Avenue",
      "length": 0.0012502755736241162,
      "speed": {
        "0:00": 30
      },
      "startid": 370817899,
      "endid": 370817896
    },
    {
      "id": 61,
      "name": "Earlsdon Ave Sth / Warwick Avenue => Belvedere Rd / Mickleton Rd",
      "length": 0.0022720180677081175,
      "speed": {
        "0:00": 30
      },
      "startid": 370817896,
      "endid": 370819110
    },
    {
      "id": 62,
      "name": "Belvedere Rd / Mickleton Rd => Belvedere Rd / Mickleton Rd",
      "length": 0.00019824825346114047,
      "speed": {
        "0:00": 30
      },
      "startid": 370819110,
      "endid": 370819111
    },
    {
      "id": 63,
      "name": "Belvedere Rd / Mickleton Rd => Belvedere Rd / Huntingdon Rd",
      "length": 0.0014042509640373464,
      "speed": {
        "0:00": 30
      },
      "startid": 370819111,
      "endid": 370817905
    },
    {
      "id": 64,
      "name": "Belvedere Rd / Huntingdon Rd => Belvedere Rd / Huntingdon Rd",
      "length": 0.00033854076563888706,
      "speed": {
        "0:00": 30
      },
      "startid": 370817905,
      "endid": 370817903
    },
    {
      "id": 65,
      "name": "Belvedere Rd / Huntingdon Rd => Dalton Rd / Spencer Rd",
      "length": 0.002033681698301944,
      "speed": {
        "0:00": 30
      },
      "startid": 370817903,
      "endid": 370819753
    },
    {
      "id": 66,
      "name": "Dalton Rd / Spencer Rd => Spencer Rd / Spencer Park",
      "length": 0.0005607090243606053,
      "speed": {
        "0:00": 30
      },
      "startid": 370819753,
      "endid": 370819109
    },
    {
      "id": 67,
      "name": "Spencer Rd / Spencer Park => Spencer Rd / King Henry Viii School",
      "length": 0.0027027300013129398,
      "speed": {
        "0:00": 30
      },
      "startid": 370819109,
      "endid": 370818563
    },
    {
      "id": 68,
      "name": "Spencer Rd / King Henry Viii School => Spencer Rd / King Henry Viii School",
      "length": 0.0006269117960272998,
      "speed": {
        "0:00": 30
      },
      "startid": 370818563,
      "endid": 370818565
    },
    {
      "id": 69,
      "name": "Spencer Rd / King Henry Viii School => LP1",
      "length": 0.012188156356478122,
      "speed": {
        "0:00": 30
      },
      "startid": 370818565,
      "endid": 370817776
    },
    {
      "id": 70,
      "name": "LP1 => ES1",
      "length": 0.0016872650799448009,
      "speed": {
        "0:00": 30
      },
      "startid": 370817776,
      "endid": 370817774
    },
    {
      "id": 71,
      "name": "ES1 => CU5",
      "length": 0.003415736749225697,
      "speed": {
        "0:00": 30
      },
      "startid": 370817774,
      "endid": 370819676
    },
    {
      "id": 72,
      "name": "CU5 => FX1",
      "length": 0.001435590516124241,
      "speed": {
        "0:00": 30
      },
      "startid": 370819676,
      "endid": 370817768
    },
    {
      "id": 73,
      "name": "Earlsdon Avenue South, Earlsdon Street => 3177370283",
      "length": 0.0010256624834710454,
      "speed": {
        "0:00": 30
      },
      "startid": 3177370284,
      "endid": 3177370283
    },
    {
      "id": 74,
      "name": "3177370283 => UW4",
      "length": 0.03793017631833587,
      "speed": {
        "0:00": 30
      },
      "startid": 3177370283,
      "endid": 3731158214
    },
    {
      "id": 75,
      "name": "UW4 => Gibbet Hill Rd / Scarman Rd",
      "length": 0.00502250535290999,
      "speed": {
        "0:00": 30
      },
      "startid": 3731158214,
      "endid": 3731548201
    },
    {
      "id": 76,
      "name": "Gibbet Hill Rd / Scarman Rd => Gibbet Hill Rd / Scarman Rd",
      "length": 0.0013853324113731547,
      "speed": {
        "0:00": 30
      },
      "startid": 3731548201,
      "endid": 3731548192
    },
    {
      "id": 77,
      "name": "Gibbet Hill Rd / Scarman Rd => UW1",
      "length": 0.003383814895939169,
      "speed": {
        "0:00": 30
      },
      "startid": 3731548192,
      "endid": 3731158223
    },
    {
      "id": 78,
      "name": "UW1 => L",
      "length": 0.06403549141062287,
      "speed": {
        "0:00": 30
      },
      "startid": 3731158223,
      "endid": 370817744
    },
    {
      "id": 79,
      "name": "L => BY2",
      "length": 0.006856440596255099,
      "speed": {
        "0:00": 30
      },
      "startid": 370817744,
      "endid": 370817685
    },
    {
      "id": 80,
      "name": "BY2 => TS5",
      "length": 0.0036580004264603057,
      "speed": {
        "0:00": 30
      },
      "startid": 370817685,
      "endid": 1769864769
    },
    {
      "id": 81,
      "name": "TS5 => CS2",
      "length": 0.004111900311291662,
      "speed": {
        "0:00": 30
      },
      "startid": 1769864769,
      "endid": 370817700
    },
    {
      "id": 82,
      "name": "CS2 => GR2",
      "length": 0.0038800846099024252,
      "speed": {
        "0:00": 30
      },
      "startid": 370817700,
      "endid": 370817796
    },
    {
      "id": 83,
      "name": "GR2 => VR2",
      "length": 0.0020745281728630723,
      "speed": {
        "0:00": 30
      },
      "startid": 370817796,
      "endid": 370817717
    },
    {
      "id": 84,
      "name": "VR2 => Hearsall Common / Earlsdon Ave North",
      "length": 0.02044196191391665,
      "speed": {
        "0:00": 30
      },
      "startid": 370817717,
      "endid": 4815880384
    },
    {
      "id": 85,
      "name": "Hearsall Common / Earlsdon Ave North => WR4",
      "length": 0.01964434682675884,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880384,
      "endid": 9416517352
    },
    {
      "id": 86,
      "name": "WR4 => WR2",
      "length": 0.0005154336814760899,
      "speed": {
        "0:00": 30
      },
      "startid": 9416517352,
      "endid": 9416517350
    },
    {
      "id": 87,
      "name": "GR2 => Quinton Rd / Park Rd",
      "length": 0.006841491489435623,
      "speed": {
        "0:00": 30
      },
      "startid": 370817796,
      "endid": 370817761
    },
    {
      "id": 88,
      "name": "Quinton Rd / Park Rd => Quinton Rd / Park Rd",
      "length": 0.00028927594092737423,
      "speed": {
        "0:00": 30
      },
      "startid": 370817761,
      "endid": 370817762
    },
    {
      "id": 89,
      "name": "Quinton Rd / Park Rd => Quinton Rd / Stoney Rd",
      "length": 0.0013972925427406058,
      "speed": {
        "0:00": 30
      },
      "startid": 370817762,
      "endid": 370818291
    },
    {
      "id": 90,
      "name": "Quinton Rd / Stoney Rd => Quinton Rd / Stoney Rd",
      "length": 0.0004313330267910657,
      "speed": {
        "0:00": 30
      },
      "startid": 370818291,
      "endid": 370818294
    },
    {
      "id": 91,
      "name": "Quinton Rd / Stoney Rd => Quinton Rd / The Martyrs Close",
      "length": 0.0030395899542527307,
      "speed": {
        "0:00": 30
      },
      "startid": 370818294,
      "endid": 370818506
    },
    {
      "id": 92,
      "name": "Quinton Rd / The Martyrs Close => Quinton Rd / The Martyrs Close",
      "length": 0.0005721483111920976,
      "speed": {
        "0:00": 30
      },
      "startid": 370818506,
      "endid": 370818505
    },
    {
      "id": 93,
      "name": "Quinton Rd / The Martyrs Close => Quinton Rd / Lichfield Rd",
      "length": 0.002933190121697732,
      "speed": {
        "0:00": 30
      },
      "startid": 370818505,
      "endid": 370818507
    },
    {
      "id": 94,
      "name": "Quinton Rd / Lichfield Rd => Quinton Park / Blondvil St",
      "length": 0.0010224467761226605,
      "speed": {
        "0:00": 30
      },
      "startid": 370818507,
      "endid": 370818556
    },
    {
      "id": 95,
      "name": "Quinton Park / Blondvil St => Quinton Park / Blondvil St",
      "length": 0.0005186051484463979,
      "speed": {
        "0:00": 30
      },
      "startid": 370818556,
      "endid": 370818558
    },
    {
      "id": 96,
      "name": "Quinton Park / Blondvil St => Quinton Park / Brightwalton Rd",
      "length": 0.001443511846164078,
      "speed": {
        "0:00": 30
      },
      "startid": 370818558,
      "endid": 370818533
    },
    {
      "id": 97,
      "name": "Quinton Park / Brightwalton Rd => Quinton Park / Brightwalton Rd",
      "length": 0.00032683006287288844,
      "speed": {
        "0:00": 30
      },
      "startid": 370818533,
      "endid": 370818534
    },
    {
      "id": 98,
      "name": "Quinton Park / Brightwalton Rd => Black Prince Ave / Mary Herbert St",
      "length": 0.003686555207779806,
      "speed": {
        "0:00": 30
      },
      "startid": 370818534,
      "endid": 370818536
    },
    {
      "id": 99,
      "name": "Black Prince Ave / Mary Herbert St => Black Prince Ave / Mary Herbert St",
      "length": 0.000678884828230006,
      "speed": {
        "0:00": 30
      },
      "startid": 370818536,
      "endid": 370818537
    },
    {
      "id": 100,
      "name": "Black Prince Ave / Mary Herbert St => Black Prince Ave / Arundel Rd",
      "length": 0.0036360066474085254,
      "speed": {
        "0:00": 30
      },
      "startid": 370818537,
      "endid": 370818538
    },
    {
      "id": 101,
      "name": "Black Prince Ave / Arundel Rd => Black Prince Ave / Arundel Rd",
      "length": 0.0008693496247180646,
      "speed": {
        "0:00": 30
      },
      "startid": 370818538,
      "endid": 370818540
    },
    {
      "id": 102,
      "name": "Black Prince Ave / Arundel Rd => Dillotford Avenue / Black Prince Avenue",
      "length": 0.001258461091971772,
      "speed": {
        "0:00": 30
      },
      "startid": 370818540,
      "endid": 370819084
    },
    {
      "id": 103,
      "name": "Dillotford Avenue / Black Prince Avenue => Dillotford Avenue / Black Prince Avenue",
      "length": 0.0005969073629957522,
      "speed": {
        "0:00": 30
      },
      "startid": 370819084,
      "endid": 370819082
    },
    {
      "id": 104,
      "name": "Dillotford Avenue / Black Prince Avenue => Dillotford Avenue / Croydon Close",
      "length": 0.002201432490448783,
      "speed": {
        "0:00": 30
      },
      "startid": 370819082,
      "endid": 370819080
    },
    {
      "id": 105,
      "name": "Dillotford Avenue / Croydon Close => Dillotford Avenue / Croydon Close",
      "length": 0.0001267713690071976,
      "speed": {
        "0:00": 30
      },
      "startid": 370819080,
      "endid": 370819079
    },
    {
      "id": 106,
      "name": "Dillotford Avenue / Croydon Close => Dillotford Avenue / Campion Close",
      "length": 0.0030203818252002063,
      "speed": {
        "0:00": 30
      },
      "startid": 370819079,
      "endid": 794487694
    },
    {
      "id": 107,
      "name": "Dillotford Avenue / Campion Close => Dillotford Avenue / Campion Close",
      "length": 0.0003078202397511282,
      "speed": {
        "0:00": 30
      },
      "startid": 794487694,
      "endid": 794487697
    },
    {
      "id": 108,
      "name": "Dillotford Avenue / Campion Close => Dillotford Avenue / Calvert Close",
      "length": 0.001712667591800295,
      "speed": {
        "0:00": 30
      },
      "startid": 794487697,
      "endid": 370819076
    },
    {
      "id": 109,
      "name": "Dillotford Avenue / Calvert Close => Dillotford Avenue / Calvert Close",
      "length": 0.0004958452379519306,
      "speed": {
        "0:00": 30
      },
      "startid": 370819076,
      "endid": 370819077
    },
    {
      "id": 110,
      "name": "Dillotford Avenue / Calvert Close => Dillotford Avenue / Watercall Avenue",
      "length": 0.0016537586341424403,
      "speed": {
        "0:00": 30
      },
      "startid": 370819077,
      "endid": 370819726
    },
    {
      "id": 111,
      "name": "Dillotford Avenue / Watercall Avenue => Dillotford Avenue / Watercall Avenue",
      "length": 0.0003545620397071383,
      "speed": {
        "0:00": 30
      },
      "startid": 370819726,
      "endid": 370819724
    },
    {
      "id": 112,
      "name": "Dillotford Avenue / Watercall Avenue => The Chesils / Dillotford Avenue",
      "length": 0.0016609479763073677,
      "speed": {
        "0:00": 30
      },
      "startid": 370819724,
      "endid": 370819074
    },
    {
      "id": 113,
      "name": "The Chesils / Dillotford Avenue => The Chesils / Dillotford Avenue",
      "length": 0.0014154314183323813,
      "speed": {
        "0:00": 30
      },
      "startid": 370819074,
      "endid": 370819075
    },
    {
      "id": 114,
      "name": "The Chesils / Dillotford Avenue => The Chesils / Knoll Drive",
      "length": 0.0015665817086885734,
      "speed": {
        "0:00": 30
      },
      "startid": 370819075,
      "endid": 370819071
    },
    {
      "id": 115,
      "name": "The Chesils / Knoll Drive => The Chesils / Ridgeway Avenue",
      "length": 0.0029390753988287432,
      "speed": {
        "0:00": 30
      },
      "startid": 370819071,
      "endid": 370819727
    },
    {
      "id": 116,
      "name": "The Chesils / Ridgeway Avenue => Baginton Rd / Maidavale Crescent",
      "length": 0.0007259159455490091,
      "speed": {
        "0:00": 30
      },
      "startid": 370819727,
      "endid": 370818586
    },
    {
      "id": 117,
      "name": "Baginton Rd / Maidavale Crescent => Baginton Rd / Watercall Avenue",
      "length": 0.002694697563734998,
      "speed": {
        "0:00": 30
      },
      "startid": 370818586,
      "endid": 370818582
    },
    {
      "id": 118,
      "name": "Baginton Rd / Watercall Avenue => Baginton Rd / Dawlish Drive",
      "length": 0.002106127085434133,
      "speed": {
        "0:00": 30
      },
      "startid": 370818582,
      "endid": 370818583
    },
    {
      "id": 119,
      "name": "Baginton Rd / Dawlish Drive => Fenside Ave / Arnold Avenue",
      "length": 0.0017087627629384663,
      "speed": {
        "0:00": 30
      },
      "startid": 370818583,
      "endid": 370818930
    },
    {
      "id": 120,
      "name": "Fenside Ave / Arnold Avenue => VR2",
      "length": 0.02811382267017802,
      "speed": {
        "0:00": 30
      },
      "startid": 370818930,
      "endid": 370817717
    },
    {
      "id": 121,
      "name": "VR2 => CS3",
      "length": 0.0021289177156473215,
      "speed": {
        "0:00": 30
      },
      "startid": 370817717,
      "endid": 370817701
    },
    {
      "id": 122,
      "name": "CS3 => Charminster Dr / Fenside Avenue",
      "length": 0.030497311483146695,
      "speed": {
        "0:00": 30
      },
      "startid": 370817701,
      "endid": 2335471014
    },
    {
      "id": 123,
      "name": "Charminster Dr / Fenside Avenue => The Chesils / Knoll Drive",
      "length": 0.008682946051310397,
      "speed": {
        "0:00": 30
      },
      "startid": 2335471014,
      "endid": 370819072
    },
    {
      "id": 124,
      "name": "The Chesils / Knoll Drive => The Chesils / Ridgeway Avenue",
      "length": 0.002191582008503791,
      "speed": {
        "0:00": 30
      },
      "startid": 370819072,
      "endid": 370819729
    },
    {
      "id": 125,
      "name": "The Chesils / Ridgeway Avenue => Baginton Rd / Maidavale Crescent",
      "length": 0.0008747257627390072,
      "speed": {
        "0:00": 30
      },
      "startid": 370819729,
      "endid": 370818585
    },
    {
      "id": 126,
      "name": "Baginton Rd / Maidavale Crescent => Baginton Rd / Watercall Avenue",
      "length": 0.003319466390853321,
      "speed": {
        "0:00": 30
      },
      "startid": 370818585,
      "endid": 370818580
    },
    {
      "id": 127,
      "name": "Baginton Rd / Watercall Avenue => Baginton Rd / Dawlish Drive",
      "length": 0.0018580554485794652,
      "speed": {
        "0:00": 30
      },
      "startid": 370818580,
      "endid": 370818584
    },
    {
      "id": 128,
      "name": "Baginton Rd / Dawlish Drive => Fenside Ave / Arnold Avenue",
      "length": 0.002609816545277147,
      "speed": {
        "0:00": 30
      },
      "startid": 370818584,
      "endid": 370818932
    },
    {
      "id": 129,
      "name": "Fenside Ave / Arnold Avenue => BY1",
      "length": 0.02623643255094176,
      "speed": {
        "0:00": 30
      },
      "startid": 370818932,
      "endid": 370817684
    },
    {
      "id": 130,
      "name": "BY1 => White St / Bus Garage",
      "length": 0.009747790942051603,
      "speed": {
        "0:00": 30
      },
      "startid": 370817684,
      "endid": 370817758
    },
    {
      "id": 131,
      "name": "White St / Bus Garage => TS2",
      "length": 0.005213860014422566,
      "speed": {
        "0:00": 30
      },
      "startid": 370817758,
      "endid": 370817660
    },
    {
      "id": 132,
      "name": "TS2 => BS3",
      "length": 0.0025764621421626955,
      "speed": {
        "0:00": 30
      },
      "startid": 370817660,
      "endid": 370817695
    },
    {
      "id": 133,
      "name": "BS3 => VR3",
      "length": 0.005259339564050662,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 370817718
    },
    {
      "id": 134,
      "name": "VR3 => GR1",
      "length": 0.002224508586183148,
      "speed": {
        "0:00": 30
      },
      "startid": 370817718,
      "endid": 370817794
    },
    {
      "id": 135,
      "name": "GR1 => BY5",
      "length": 0.0031498880630907375,
      "speed": {
        "0:00": 30
      },
      "startid": 370817794,
      "endid": 370817679
    },
    {
      "id": 136,
      "name": "BY5 => N",
      "length": 0.006724098430274631,
      "speed": {
        "0:00": 30
      },
      "startid": 370817679,
      "endid": 370817746
    },
    {
      "id": 137,
      "name": "N => S",
      "length": 0.0005991124769199075,
      "speed": {
        "0:00": 30
      },
      "startid": 370817746,
      "endid": 370817751
    },
    {
      "id": 138,
      "name": "S => White St / Bus Garage",
      "length": 0.0024134042512565564,
      "speed": {
        "0:00": 30
      },
      "startid": 370817751,
      "endid": 370817757
    },
    {
      "id": 139,
      "name": "White St / Bus Garage => Victoria St / Vine St",
      "length": 0.003888743563157784,
      "speed": {
        "0:00": 30
      },
      "startid": 370817757,
      "endid": 370817453
    },
    {
      "id": 140,
      "name": "Victoria St / Vine St => Victoria St / Vine St",
      "length": 0.0007354850440354118,
      "speed": {
        "0:00": 30
      },
      "startid": 370817453,
      "endid": 370817454
    },
    {
      "id": 141,
      "name": "Victoria St / Vine St => King William St / St Benedicts School",
      "length": 0.003619327810519606,
      "speed": {
        "0:00": 30
      },
      "startid": 370817454,
      "endid": 370817456
    },
    {
      "id": 142,
      "name": "King William St / St Benedicts School => King William St / St Benedicts School",
      "length": 0.0004073053891133307,
      "speed": {
        "0:00": 30
      },
      "startid": 370817456,
      "endid": 370817455
    },
    {
      "id": 143,
      "name": "King William St / St Benedicts School => Berry St / Vauxhall St",
      "length": 0.0032078499871399328,
      "speed": {
        "0:00": 30
      },
      "startid": 370817455,
      "endid": 370817459
    },
    {
      "id": 144,
      "name": "Berry St / Vauxhall St => Berry St / Vauxhall St",
      "length": 0.00015018511910524452,
      "speed": {
        "0:00": 30
      },
      "startid": 370817459,
      "endid": 370817458
    },
    {
      "id": 145,
      "name": "Berry St / Vauxhall St => Paynes Lane / Days Lane",
      "length": 0.0021721072095999775,
      "speed": {
        "0:00": 30
      },
      "startid": 370817458,
      "endid": 370817460
    },
    {
      "id": 146,
      "name": "Paynes Lane / Days Lane => Paynes Lane / Days Lane",
      "length": 0.00018780718835871655,
      "speed": {
        "0:00": 30
      },
      "startid": 370817460,
      "endid": 370817462
    },
    {
      "id": 147,
      "name": "Paynes Lane / Days Lane => Walsgrave Rd / Swan Lane",
      "length": 0.005192963008727335,
      "speed": {
        "0:00": 30
      },
      "startid": 370817462,
      "endid": 370817463
    },
    {
      "id": 148,
      "name": "Walsgrave Rd / Swan Lane => Walsgrave Rd / Clements St",
      "length": 0.0030988222827398773,
      "speed": {
        "0:00": 30
      },
      "startid": 370817463,
      "endid": 370817467
    },
    {
      "id": 149,
      "name": "Walsgrave Rd / Clements St => Walsgrave Rd / Clements St",
      "length": 0.0005896212004330483,
      "speed": {
        "0:00": 30
      },
      "startid": 370817467,
      "endid": 370817465
    },
    {
      "id": 150,
      "name": "Walsgrave Rd / Clements St => Walsgrave Rd / Harefield Rd",
      "length": 0.00521431387624442,
      "speed": {
        "0:00": 30
      },
      "startid": 370817465,
      "endid": 370817501
    },
    {
      "id": 151,
      "name": "Walsgrave Rd / Harefield Rd => Walsgrave Rd / Harefield Rd",
      "length": 0.0006063554485614267,
      "speed": {
        "0:00": 30
      },
      "startid": 370817501,
      "endid": 370817500
    },
    {
      "id": 152,
      "name": "Walsgrave Rd / Harefield Rd => Walsgrave Rd / Burns Rd",
      "length": 0.0036222750930872813,
      "speed": {
        "0:00": 30
      },
      "startid": 370817500,
      "endid": 370817504
    },
    {
      "id": 153,
      "name": "Walsgrave Rd / Burns Rd => Walsgrave Rd / Burns Rd",
      "length": 0.0015216241651606255,
      "speed": {
        "0:00": 30
      },
      "startid": 370817504,
      "endid": 370817502
    },
    {
      "id": 154,
      "name": "Walsgrave Rd / Burns Rd => Longfellow Rd / Coleridge Rd",
      "length": 0.003106956911513569,
      "speed": {
        "0:00": 30
      },
      "startid": 370817502,
      "endid": 370818337
    },
    {
      "id": 155,
      "name": "Longfellow Rd / Coleridge Rd => Longfellow Rd / Coleridge Rd",
      "length": 0.0008177070685765369,
      "speed": {
        "0:00": 30
      },
      "startid": 370818337,
      "endid": 370818336
    },
    {
      "id": 156,
      "name": "Longfellow Rd / Coleridge Rd => Longfellow Rd / Mellowdew Rd",
      "length": 0.002345184926610366,
      "speed": {
        "0:00": 30
      },
      "startid": 370818336,
      "endid": 370817507
    },
    {
      "id": 157,
      "name": "Longfellow Rd / Mellowdew Rd => Longfellow Rd / Mellowdew Rd",
      "length": 0.0009740439517803643,
      "speed": {
        "0:00": 30
      },
      "startid": 370817507,
      "endid": 370817505
    },
    {
      "id": 158,
      "name": "Longfellow Rd / Mellowdew Rd => Longfellow Rd / Morris Ave",
      "length": 0.0029103147269665982,
      "speed": {
        "0:00": 30
      },
      "startid": 370817505,
      "endid": 370817512
    },
    {
      "id": 159,
      "name": "Longfellow Rd / Morris Ave => Longfellow Rd / Morris Ave",
      "length": 0.0009356046707877733,
      "speed": {
        "0:00": 30
      },
      "startid": 370817512,
      "endid": 370817510
    },
    {
      "id": 160,
      "name": "Longfellow Rd / Morris Ave => Longfellow Rd / Hipswell Highway",
      "length": 0.002224853581700198,
      "speed": {
        "0:00": 30
      },
      "startid": 370817510,
      "endid": 370817703
    },
    {
      "id": 161,
      "name": "Longfellow Rd / Hipswell Highway => Longfellow Rd / Hipswell Highway",
      "length": 0.0003073880446606868,
      "speed": {
        "0:00": 30
      },
      "startid": 370817703,
      "endid": 370817705
    },
    {
      "id": 162,
      "name": "Longfellow Rd / Hipswell Highway => Hipswell Highway / Longfellow Rd",
      "length": 0.0013628606164965294,
      "speed": {
        "0:00": 30
      },
      "startid": 370817705,
      "endid": 370817430
    },
    {
      "id": 163,
      "name": "Hipswell Highway / Longfellow Rd => Hipswell Highway / Meredith Rd",
      "length": 0.0014559813529020406,
      "speed": {
        "0:00": 30
      },
      "startid": 370817430,
      "endid": 370818376
    },
    {
      "id": 164,
      "name": "Hipswell Highway / Meredith Rd => Hipswell Highway / Meredith Rd",
      "length": 0.00048271595167421127,
      "speed": {
        "0:00": 30
      },
      "startid": 370818376,
      "endid": 370818375
    },
    {
      "id": 165,
      "name": "Hipswell Highway / Meredith Rd => Mayflower Dr / Allerton Close",
      "length": 0.003259330570836959,
      "speed": {
        "0:00": 30
      },
      "startid": 370818375,
      "endid": 370818365
    },
    {
      "id": 166,
      "name": "Mayflower Dr / Allerton Close => Mayflower Dr / Allerton Close",
      "length": 0.0008543406873121222,
      "speed": {
        "0:00": 30
      },
      "startid": 370818365,
      "endid": 370818364
    },
    {
      "id": 167,
      "name": "Mayflower Dr / Allerton Close => Harry Rose Rd / Lloyd Crescent",
      "length": 0.003015470797404941,
      "speed": {
        "0:00": 30
      },
      "startid": 370818364,
      "endid": 370818369
    },
    {
      "id": 168,
      "name": "Harry Rose Rd / Lloyd Crescent => Harry Rose Rd / Lloyd Crescent",
      "length": 0.000690972712923798,
      "speed": {
        "0:00": 30
      },
      "startid": 370818369,
      "endid": 370818367
    },
    {
      "id": 169,
      "name": "Harry Rose Rd / Lloyd Crescent => Attoxhall Rd / Hopedale Close",
      "length": 0.002773932320731819,
      "speed": {
        "0:00": 30
      },
      "startid": 370818367,
      "endid": 370818370
    },
    {
      "id": 170,
      "name": "Attoxhall Rd / Hopedale Close => Attoxhall Rd / Hopedale Close",
      "length": 0.0002227371994051731,
      "speed": {
        "0:00": 30
      },
      "startid": 370818370,
      "endid": 370818371
    },
    {
      "id": 171,
      "name": "Attoxhall Rd / Hopedale Close => Attoxhall Rd / Belgrave Lodge",
      "length": 0.0014797770440169876,
      "speed": {
        "0:00": 30
      },
      "startid": 370818371,
      "endid": 370818372
    },
    {
      "id": 172,
      "name": "Attoxhall Rd / Belgrave Lodge => Attoxhall Rd / Belgrave Lodge",
      "length": 0.00024058582668387877,
      "speed": {
        "0:00": 30
      },
      "startid": 370818372,
      "endid": 370818373
    },
    {
      "id": 173,
      "name": "Attoxhall Rd / Belgrave Lodge => Attoxhall Rd / Axholme Rd",
      "length": 0.001724253948808374,
      "speed": {
        "0:00": 30
      },
      "startid": 370818373,
      "endid": 370818495
    },
    {
      "id": 174,
      "name": "Attoxhall Rd / Axholme Rd => Belgrave Rd / Attoxhall Rd",
      "length": 0.0013658181797013085,
      "speed": {
        "0:00": 30
      },
      "startid": 370818495,
      "endid": 370819303
    },
    {
      "id": 175,
      "name": "Belgrave Rd / Attoxhall Rd => Belgrave Rd / Arch Rd",
      "length": 0.0035260788207304087,
      "speed": {
        "0:00": 30
      },
      "startid": 370819303,
      "endid": 370817571
    },
    {
      "id": 176,
      "name": "Belgrave Rd / Arch Rd => Belgrave Rd / Arch Rd",
      "length": 0.00045216626366826956,
      "speed": {
        "0:00": 30
      },
      "startid": 370817571,
      "endid": 370817572
    },
    {
      "id": 177,
      "name": "Belgrave Rd / Arch Rd => Belgrave Rd / Westmorland Rd",
      "length": 0.003083393536349537,
      "speed": {
        "0:00": 30
      },
      "startid": 370817572,
      "endid": 370817627
    },
    {
      "id": 178,
      "name": "Belgrave Rd / Westmorland Rd => Belgrave Rd / Westmorland Rd",
      "length": 0.0001048001908401134,
      "speed": {
        "0:00": 30
      },
      "startid": 370817627,
      "endid": 370817625
    },
    {
      "id": 179,
      "name": "Belgrave Rd / Westmorland Rd => Belgrave Rd / Clifford Bridge Rd",
      "length": 0.0021349345118752226,
      "speed": {
        "0:00": 30
      },
      "startid": 370817625,
      "endid": 370817709
    },
    {
      "id": 180,
      "name": "Belgrave Rd / Clifford Bridge Rd => Belgrave Rd / Clifford Bridge Rd",
      "length": 0.000413697050992378,
      "speed": {
        "0:00": 30
      },
      "startid": 370817709,
      "endid": 370817707
    },
    {
      "id": 181,
      "name": "Belgrave Rd / Clifford Bridge Rd => Clifford Bridge Rd / Dorchester Way",
      "length": 0.0028021035544781208,
      "speed": {
        "0:00": 30
      },
      "startid": 370817707,
      "endid": 370817578
    },
    {
      "id": 182,
      "name": "Clifford Bridge Rd / Dorchester Way => UH6",
      "length": 0.008406966828171356,
      "speed": {
        "0:00": 30
      },
      "startid": 370817578,
      "endid": 4062225929
    },
    {
      "id": 183,
      "name": "UH6 => WH",
      "length": 0.005721260320069507,
      "speed": {
        "0:00": 30
      },
      "startid": 4062225929,
      "endid": 370817732
    },
    {
      "id": 184,
      "name": "WH => WG",
      "length": 0.000278365084014834,
      "speed": {
        "0:00": 30
      },
      "startid": 370817732,
      "endid": 370817730
    },
    {
      "id": 185,
      "name": "WG => WF",
      "length": 0.003325900281127788,
      "speed": {
        "0:00": 30
      },
      "startid": 370817730,
      "endid": 370817729
    },
    {
      "id": 186,
      "name": "WF => CS4",
      "length": 0.07458682604374647,
      "speed": {
        "0:00": 30
      },
      "startid": 370817729,
      "endid": 370817702
    },
    {
      "id": 187,
      "name": "CS4 => Britannia Street / Wren Street",
      "length": 0.023480313232152696,
      "speed": {
        "0:00": 30
      },
      "startid": 370817702,
      "endid": 7857415187
    },
    {
      "id": 188,
      "name": "Britannia Street / Wren Street => Swan Lane / Britannia Street",
      "length": 0.0021032121552519,
      "speed": {
        "0:00": 30
      },
      "startid": 7857415187,
      "endid": 7857415186
    },
    {
      "id": 189,
      "name": "GH5 => GH6",
      "length": 0.003083086677340662,
      "speed": {
        "0:00": 30
      },
      "startid": 370819587,
      "endid": 370819586
    },
    {
      "id": 190,
      "name": "GH6 => UW5",
      "length": 0.007892891592441185,
      "speed": {
        "0:00": 30
      },
      "startid": 370819586,
      "endid": 3731158219
    },
    {
      "id": 191,
      "name": "Terry Rd / Humber Rd => Terry Rd / Humber Rd",
      "length": 0.00027649117526620104,
      "speed": {
        "0:00": 30
      },
      "startid": 370818321,
      "endid": 370818320
    },
    {
      "id": 192,
      "name": "Terry Rd / Humber Rd => Terry Rd / Bluecoat School",
      "length": 0.002631594486238174,
      "speed": {
        "0:00": 30
      },
      "startid": 370818320,
      "endid": 370818318
    },
    {
      "id": 193,
      "name": "Terry Rd / Bluecoat School => Terry Rd / Bluecoat School",
      "length": 0.00034314617876286287,
      "speed": {
        "0:00": 30
      },
      "startid": 370818318,
      "endid": 370818319
    },
    {
      "id": 194,
      "name": "Terry Rd / Bluecoat School => Terry Rd / Humber Avenue",
      "length": 0.002196148250915689,
      "speed": {
        "0:00": 30
      },
      "startid": 370818319,
      "endid": 370818315
    },
    {
      "id": 195,
      "name": "Terry Rd / Humber Avenue => Terry Rd / Humber Avenue",
      "length": 0.00019683439739761187,
      "speed": {
        "0:00": 30
      },
      "startid": 370818315,
      "endid": 370818317
    },
    {
      "id": 196,
      "name": "Terry Rd / Humber Avenue => Terry Rd / Northfield Rd",
      "length": 0.0014850931014554283,
      "speed": {
        "0:00": 30
      },
      "startid": 370818317,
      "endid": 370818314
    },
    {
      "id": 197,
      "name": "Terry Rd / Northfield Rd => Northfield Rd / Terry Rd",
      "length": 0.0006312836763309971,
      "speed": {
        "0:00": 30
      },
      "startid": 370818314,
      "endid": 370817819
    },
    {
      "id": 198,
      "name": "Northfield Rd / Terry Rd => CU1",
      "length": 0.00803948599165289,
      "speed": {
        "0:00": 30
      },
      "startid": 370817819,
      "endid": 370817766
    },
    {
      "id": 199,
      "name": "CU1 => CU5",
      "length": 0.0021117262535691986,
      "speed": {
        "0:00": 30
      },
      "startid": 370817766,
      "endid": 370819676
    },
    {
      "id": 200,
      "name": "CU5 => CU4",
      "length": 0.0005253710783815626,
      "speed": {
        "0:00": 30
      },
      "startid": 370819676,
      "endid": 370819679
    },
    {
      "id": 201,
      "name": "CU4 => FX1",
      "length": 0.001230879766667563,
      "speed": {
        "0:00": 30
      },
      "startid": 370819679,
      "endid": 370817768
    },
    {
      "id": 202,
      "name": "FX1 => The Moorfield / Roundhouse Rd",
      "length": 0.02622364753423666,
      "speed": {
        "0:00": 30
      },
      "startid": 370817768,
      "endid": 370819646
    },
    {
      "id": 203,
      "name": "The Moorfield / Roundhouse Rd => The Moorfield / Mitchell Close",
      "length": 0.0032425831246094368,
      "speed": {
        "0:00": 30
      },
      "startid": 370819646,
      "endid": 370818342
    },
    {
      "id": 204,
      "name": "The Moorfield / Mitchell Close => The Moorfield / Mitchell Close",
      "length": 0.0003398316053587813,
      "speed": {
        "0:00": 30
      },
      "startid": 370818342,
      "endid": 370818341
    },
    {
      "id": 205,
      "name": "The Moorfield / Mitchell Close => The Moorfield / The Barley Lea",
      "length": 0.00159517961684649,
      "speed": {
        "0:00": 30
      },
      "startid": 370818341,
      "endid": 370818343
    },
    {
      "id": 206,
      "name": "The Moorfield / The Barley Lea => The Moorfield / The Barley Lea",
      "length": 0.00010193061365211741,
      "speed": {
        "0:00": 30
      },
      "startid": 370818343,
      "endid": 370818345
    },
    {
      "id": 207,
      "name": "The Moorfield / The Barley Lea => The Barley Lea / Acorn St",
      "length": 0.0026489428570675194,
      "speed": {
        "0:00": 30
      },
      "startid": 370818345,
      "endid": 370818351
    },
    {
      "id": 208,
      "name": "The Barley Lea / Acorn St => The Barley Lea / Acorn St",
      "length": 0.0000782143848705695,
      "speed": {
        "0:00": 30
      },
      "startid": 370818351,
      "endid": 370818352
    },
    {
      "id": 209,
      "name": "The Barley Lea / Acorn St => The Barley Lea / The Farmstead",
      "length": 0.0030359720634418716,
      "speed": {
        "0:00": 30
      },
      "startid": 370818352,
      "endid": 370818349
    },
    {
      "id": 210,
      "name": "The Barley Lea / The Farmstead => The Barley Lea / The Farmstead",
      "length": 0.00044790456572747816,
      "speed": {
        "0:00": 30
      },
      "startid": 370818349,
      "endid": 370818348
    },
    {
      "id": 211,
      "name": "The Barley Lea / The Farmstead => The Barley Lea / Jasmine Grove",
      "length": 0.0021675044659732615,
      "speed": {
        "0:00": 30
      },
      "startid": 370818348,
      "endid": 370818346
    },
    {
      "id": 212,
      "name": "The Barley Lea / Jasmine Grove => The Barley Lea / Jasmine Grove",
      "length": 0.000917275062346183,
      "speed": {
        "0:00": 30
      },
      "startid": 370818346,
      "endid": 370818347
    },
    {
      "id": 213,
      "name": "The Barley Lea / Jasmine Grove => Langbank Ave / Garth Crescent",
      "length": 0.0055576533914954065,
      "speed": {
        "0:00": 30
      },
      "startid": 370818347,
      "endid": 370818397
    },
    {
      "id": 214,
      "name": "Langbank Ave / Garth Crescent => Langbank Ave / Garth Crescent",
      "length": 0.0009164919257691167,
      "speed": {
        "0:00": 30
      },
      "startid": 370818397,
      "endid": 370818399
    },
    {
      "id": 215,
      "name": "Langbank Ave / Garth Crescent => Langbank Ave / Corpus Christi School",
      "length": 0.0031430964430025727,
      "speed": {
        "0:00": 30
      },
      "startid": 370818399,
      "endid": 370818395
    },
    {
      "id": 216,
      "name": "Langbank Ave / Corpus Christi School => Princethorpe Way / Nene Close",
      "length": 0.0017608009825073538,
      "speed": {
        "0:00": 30
      },
      "startid": 370818395,
      "endid": 370817799
    },
    {
      "id": 217,
      "name": "Princethorpe Way / Nene Close => Princethorpe Way / Sowe Valley School",
      "length": 0.0022779536430768983,
      "speed": {
        "0:00": 30
      },
      "startid": 370817799,
      "endid": 370818392
    },
    {
      "id": 218,
      "name": "Princethorpe Way / Sowe Valley School => Princethorpe Way / Sowe Valley School",
      "length": 0.0005965104190185192,
      "speed": {
        "0:00": 30
      },
      "startid": 370818392,
      "endid": 370818393
    },
    {
      "id": 219,
      "name": "Princethorpe Way / Sowe Valley School => Princethorpe Way / Ernesford Grange School",
      "length": 0.001363655649350504,
      "speed": {
        "0:00": 30
      },
      "startid": 370818393,
      "endid": 370818390
    },
    {
      "id": 220,
      "name": "Princethorpe Way / Ernesford Grange School => Princethorpe Way / Ernesford Grange School",
      "length": 0.000379486297506172,
      "speed": {
        "0:00": 30
      },
      "startid": 370818390,
      "endid": 370818391
    },
    {
      "id": 221,
      "name": "Princethorpe Way / Ernesford Grange School => Princethorpe Way / Bruntingthorpe Way",
      "length": 0.001274435043462188,
      "speed": {
        "0:00": 30
      },
      "startid": 370818391,
      "endid": 370818387
    },
    {
      "id": 222,
      "name": "Princethorpe Way / Bruntingthorpe Way => Princethorpe Way / Bruntingthorpe Way",
      "length": 0.0006148991787308028,
      "speed": {
        "0:00": 30
      },
      "startid": 370818387,
      "endid": 370818388
    },
    {
      "id": 223,
      "name": "Princethorpe Way / Bruntingthorpe Way => Princethorpe Way / Lawford Close",
      "length": 0.0014845882459456768,
      "speed": {
        "0:00": 30
      },
      "startid": 370818388,
      "endid": 370818386
    },
    {
      "id": 224,
      "name": "Princethorpe Way / Lawford Close => Princethorpe Way / Lawford Close",
      "length": 0.002886085106158579,
      "speed": {
        "0:00": 30
      },
      "startid": 370818386,
      "endid": 370818385
    },
    {
      "id": 225,
      "name": "Princethorpe Way / Lawford Close => Princethorpe Way / Oxenden Way",
      "length": 0.0020516730538776974,
      "speed": {
        "0:00": 30
      },
      "startid": 370818385,
      "endid": 370818383
    },
    {
      "id": 226,
      "name": "Princethorpe Way / Oxenden Way => Princethorpe Way / Bowden Way",
      "length": 0.0013931490264829877,
      "speed": {
        "0:00": 30
      },
      "startid": 370818383,
      "endid": 370817802
    },
    {
      "id": 227,
      "name": "Princethorpe Way / Bowden Way => Princethorpe Way / Bowden Way",
      "length": 0.0002296836955479753,
      "speed": {
        "0:00": 30
      },
      "startid": 370817802,
      "endid": 370817805
    },
    {
      "id": 228,
      "name": "Princethorpe Way / Bowden Way => Binley Rd / Princethorpe Way",
      "length": 0.0012088057329451315,
      "speed": {
        "0:00": 30
      },
      "startid": 370817805,
      "endid": 370818381
    },
    {
      "id": 229,
      "name": "Binley Rd / Princethorpe Way => Binley Rd / Ebro Crescent",
      "length": 0.0016824441090271,
      "speed": {
        "0:00": 30
      },
      "startid": 370818381,
      "endid": 370817807
    },
    {
      "id": 230,
      "name": "Binley Rd / Ebro Crescent => Brandon Rd / Binley Park Inn",
      "length": 0.0017650665284913514,
      "speed": {
        "0:00": 30
      },
      "startid": 370817807,
      "endid": 370818456
    },
    {
      "id": 231,
      "name": "Brandon Rd / Binley Park Inn => Brandon Rd / Binley Park Inn",
      "length": 0.0005661131512307444,
      "speed": {
        "0:00": 30
      },
      "startid": 370818456,
      "endid": 370818453
    },
    {
      "id": 232,
      "name": "Brandon Rd / Binley Park Inn => Brandon Rd / Willenhall Lane",
      "length": 0.004328036512094069,
      "speed": {
        "0:00": 30
      },
      "startid": 370818453,
      "endid": 370818463
    },
    {
      "id": 233,
      "name": "Brandon Rd / Willenhall Lane => Brandon Rd / Willenhall Lane",
      "length": 0.0003965726289091613,
      "speed": {
        "0:00": 30
      },
      "startid": 370818463,
      "endid": 370818461
    },
    {
      "id": 234,
      "name": "Brandon Rd / Willenhall Lane => Brandon Rd / Herald Way",
      "length": 0.0031462295927036322,
      "speed": {
        "0:00": 30
      },
      "startid": 370818461,
      "endid": 370817408
    },
    {
      "id": 235,
      "name": "Brandon Rd / Herald Way => Brandon Rd / Herald Way",
      "length": 0.00024123619131873235,
      "speed": {
        "0:00": 30
      },
      "startid": 370817408,
      "endid": 370817407
    },
    {
      "id": 236,
      "name": "Brandon Rd / Herald Way => Kynner Way / Kynner Way",
      "length": 0.006696544246848425,
      "speed": {
        "0:00": 30
      },
      "startid": 370817407,
      "endid": 2190110490
    },
    {
      "id": 237,
      "name": "Kynner Way / Kynner Way => The Moorfield / Roundhouse Rd",
      "length": 0.0476237912663407,
      "speed": {
        "0:00": 30
      },
      "startid": 2190110490,
      "endid": 2196422942
    },
    {
      "id": 238,
      "name": "The Moorfield / Roundhouse Rd => Kynner Way / Skipworth Rd",
      "length": 0.04503078404158648,
      "speed": {
        "0:00": 30
      },
      "startid": 2196422942,
      "endid": 4318890427
    },
    {
      "id": 239,
      "name": "Kynner Way / Skipworth Rd => Kynner Way / Skipworth Rd",
      "length": 0.00012467128778715364,
      "speed": {
        "0:00": 30
      },
      "startid": 4318890427,
      "endid": 4318890428
    },
    {
      "id": 240,
      "name": "Kynner Way / Skipworth Rd => CU2",
      "length": 0.06683456652855647,
      "speed": {
        "0:00": 30
      },
      "startid": 4318890428,
      "endid": 370819680
    },
    {
      "id": 241,
      "name": "CU2 => Vecqueray St / Far Gosford St",
      "length": 0.004965666426573402,
      "speed": {
        "0:00": 30
      },
      "startid": 370819680,
      "endid": 370817798
    },
    {
      "id": 242,
      "name": "Vecqueray St / Far Gosford St => WF",
      "length": 0.058258733949598455,
      "speed": {
        "0:00": 30
      },
      "startid": 370817798,
      "endid": 370817729
    },
    {
      "id": 243,
      "name": "WF => WH",
      "length": 0.00313308919119921,
      "speed": {
        "0:00": 30
      },
      "startid": 370817729,
      "endid": 370817732
    },
    {
      "id": 244,
      "name": "WH => WG",
      "length": 0.000278365084014834,
      "speed": {
        "0:00": 30
      },
      "startid": 370817732,
      "endid": 370817730
    },
    {
      "id": 245,
      "name": "WG => Clifford Bridge Rd / Dorchester Way",
      "length": 0.002886836431110773,
      "speed": {
        "0:00": 30
      },
      "startid": 370817730,
      "endid": 370817578
    },
    {
      "id": 246,
      "name": "Clifford Bridge Rd / Dorchester Way => Skipworth Rd / Middlefield Drive",
      "length": 0.021365490239407117,
      "speed": {
        "0:00": 30
      },
      "startid": 370817578,
      "endid": 4815880367
    },
    {
      "id": 247,
      "name": "Skipworth Rd / Middlefield Drive => Skipworth Rd / Middlefield Drive",
      "length": 0.00032619848252193114,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880367,
      "endid": 4815880366
    },
    {
      "id": 248,
      "name": "Skipworth Rd / Middlefield Drive => Skipworth Rd / Camville",
      "length": 0.0037980871883099327,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880366,
      "endid": 4815880369
    },
    {
      "id": 249,
      "name": "Skipworth Rd / Camville => Skipworth Rd / Camville",
      "length": 0.0009197065238434087,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880369,
      "endid": 4815880368
    },
    {
      "id": 250,
      "name": "Skipworth Rd / Camville => Brinklow Rd / Coombe Court",
      "length": 0.001508797961958801,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880368,
      "endid": 370819174
    },
    {
      "id": 251,
      "name": "Brinklow Rd / Coombe Court => Brinklow Rd / Porchester Close",
      "length": 0.0018598436923576822,
      "speed": {
        "0:00": 30
      },
      "startid": 370819174,
      "endid": 370818428
    },
    {
      "id": 252,
      "name": "Brinklow Rd / Porchester Close => Brinklow Rd / Porchester Close",
      "length": 0.0019948509367861797,
      "speed": {
        "0:00": 30
      },
      "startid": 370818428,
      "endid": 370818424
    },
    {
      "id": 253,
      "name": "Brinklow Rd / Porchester Close => Brinklow Rd / Coombe Social Club",
      "length": 0.0015390668666434438,
      "speed": {
        "0:00": 30
      },
      "startid": 370818424,
      "endid": 4815880370
    },
    {
      "id": 254,
      "name": "Brinklow Rd / Coombe Social Club => Brinklow Rd / Rannock Close",
      "length": 0.0007116764222595206,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880370,
      "endid": 4815876529
    },
    {
      "id": 255,
      "name": "Brinklow Rd / Rannock Close => Clifford Bridge Rd / Coombe Park Rd",
      "length": 0.0017539331942797824,
      "speed": {
        "0:00": 30
      },
      "startid": 4815876529,
      "endid": 370818409
    },
    {
      "id": 256,
      "name": "Clifford Bridge Rd / Coombe Park Rd => Clifford Bridge Rd / Coombe Park Rd",
      "length": 0.0005575986459799535,
      "speed": {
        "0:00": 30
      },
      "startid": 370818409,
      "endid": 370818406
    },
    {
      "id": 257,
      "name": "Clifford Bridge Rd / Coombe Park Rd => Clifford Bridge Rd / Bridgeacre Gardens",
      "length": 0.0028369323802329267,
      "speed": {
        "0:00": 30
      },
      "startid": 370818406,
      "endid": 370818412
    },
    {
      "id": 258,
      "name": "Clifford Bridge Rd / Bridgeacre Gardens => Clifford Bridge Rd / Bridgeacre Gardens",
      "length": 0.00034793569808658665,
      "speed": {
        "0:00": 30
      },
      "startid": 370818412,
      "endid": 370818410
    },
    {
      "id": 259,
      "name": "Clifford Bridge Rd / Bridgeacre Gardens => Clifford Bridge Rd / Gainford Rise",
      "length": 0.0012607908192880967,
      "speed": {
        "0:00": 30
      },
      "startid": 370818410,
      "endid": 370818415
    },
    {
      "id": 260,
      "name": "Clifford Bridge Rd / Gainford Rise => Clifford Bridge Rd / Gainford Rise",
      "length": 0.0007986141120735769,
      "speed": {
        "0:00": 30
      },
      "startid": 370818415,
      "endid": 370818418
    },
    {
      "id": 261,
      "name": "Clifford Bridge Rd / Gainford Rise => Clifford Bridge Rd / Tesco",
      "length": 0.003019325462746543,
      "speed": {
        "0:00": 30
      },
      "startid": 370818418,
      "endid": 370817575
    },
    {
      "id": 262,
      "name": "Clifford Bridge Rd / Tesco => Clifford Bridge Rd / Tesco",
      "length": 0.0011893140922393406,
      "speed": {
        "0:00": 30
      },
      "startid": 370817575,
      "endid": 370817577
    },
    {
      "id": 263,
      "name": "Clifford Bridge Rd / Tesco => Dorchester Way / Tesco",
      "length": 0.0021675169803289625,
      "speed": {
        "0:00": 30
      },
      "startid": 370817577,
      "endid": 370818285
    },
    {
      "id": 264,
      "name": "Dorchester Way / Tesco => Dorchester Way / Tesco",
      "length": 0.0006983372036497266,
      "speed": {
        "0:00": 30
      },
      "startid": 370818285,
      "endid": 370818283
    },
    {
      "id": 265,
      "name": "Dorchester Way / Tesco => Dorchester Way / Pearl Hyde School",
      "length": 0.0035059223508221693,
      "speed": {
        "0:00": 30
      },
      "startid": 370818283,
      "endid": 370818442
    },
    {
      "id": 266,
      "name": "Dorchester Way / Pearl Hyde School => Dorchester Way / Pearl Hyde School",
      "length": 0.00016052146274156856,
      "speed": {
        "0:00": 30
      },
      "startid": 370818442,
      "endid": 370818438
    },
    {
      "id": 267,
      "name": "Dorchester Way / Pearl Hyde School => Dorchester Way / Blandford Drive",
      "length": 0.002317581008291228,
      "speed": {
        "0:00": 30
      },
      "startid": 370818438,
      "endid": 370818282
    },
    {
      "id": 268,
      "name": "Dorchester Way / Blandford Drive => Dorchester Way / Blandford Drive",
      "length": 0.001223701957177531,
      "speed": {
        "0:00": 30
      },
      "startid": 370818282,
      "endid": 370818281
    },
    {
      "id": 269,
      "name": "Dorchester Way / Blandford Drive => Far Gosford St / Bramble St",
      "length": 0.05567181082486922,
      "speed": {
        "0:00": 30
      },
      "startid": 370818281,
      "endid": 4815880407
    },
    {
      "id": 270,
      "name": "Far Gosford St / Bramble St => Humber Rd / Bolingbroke Rd",
      "length": 0.011196603238928553,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880407,
      "endid": 370819596
    },
    {
      "id": 271,
      "name": "Humber Rd / Bolingbroke Rd => Bolingbroke Rd / Humber Rd",
      "length": 0.0007172932803261293,
      "speed": {
        "0:00": 30
      },
      "startid": 370819596,
      "endid": 370818324
    },
    {
      "id": 272,
      "name": "Bolingbroke Rd / Humber Rd => Bolingbroke Rd / Middle",
      "length": 0.0015910248269594637,
      "speed": {
        "0:00": 30
      },
      "startid": 370818324,
      "endid": 370818326
    },
    {
      "id": 273,
      "name": "Bolingbroke Rd / Middle => Bolingbroke Rd / Middle",
      "length": 0.0006007741672208405,
      "speed": {
        "0:00": 30
      },
      "startid": 370818326,
      "endid": 3672600325
    },
    {
      "id": 274,
      "name": "Bolingbroke Rd / Middle => Bolingbroke Rd / Stoke Green",
      "length": 0.0032601802480847902,
      "speed": {
        "0:00": 30
      },
      "startid": 3672600325,
      "endid": 370817822
    },
    {
      "id": 275,
      "name": "Bolingbroke Rd / Stoke Green => Aldermoor Lane / Bulls Head Lane",
      "length": 0.0007466517930085684,
      "speed": {
        "0:00": 30
      },
      "startid": 370817822,
      "endid": 370818327
    },
    {
      "id": 276,
      "name": "Aldermoor Lane / Bulls Head Lane => Aldermoor Lane / Ernsford Avenue",
      "length": 0.0013172830561394716,
      "speed": {
        "0:00": 30
      },
      "startid": 370818327,
      "endid": 370818328
    },
    {
      "id": 277,
      "name": "Aldermoor Lane / Ernsford Avenue => Aldermoor Lane / Ernsford Avenue",
      "length": 0.0008524917125722084,
      "speed": {
        "0:00": 30
      },
      "startid": 370818328,
      "endid": 370818329
    },
    {
      "id": 278,
      "name": "Aldermoor Lane / Ernsford Avenue => Aldermoor Lane / Roundhouse Rd",
      "length": 0.0008634073488209599,
      "speed": {
        "0:00": 30
      },
      "startid": 370818329,
      "endid": 370818340
    },
    {
      "id": 279,
      "name": "Aldermoor Lane / Roundhouse Rd => Aldermoor Lane / Roundhouse Rd",
      "length": 0.0016563330130134925,
      "speed": {
        "0:00": 30
      },
      "startid": 370818340,
      "endid": 370818338
    },
    {
      "id": 280,
      "name": "Aldermoor Lane / Roundhouse Rd => Princethorpe Way / Oxenden Way",
      "length": 0.02932725652528692,
      "speed": {
        "0:00": 30
      },
      "startid": 370818338,
      "endid": 4815880401
    },
    {
      "id": 281,
      "name": "Princethorpe Way / Oxenden Way => Charterhouse Rd / Gulson Rd",
      "length": 0.04367627762218334,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880401,
      "endid": 4815880403
    },
    {
      "id": 282,
      "name": "Charterhouse Rd / Gulson Rd => Charterhouse Rd / Gulson Rd",
      "length": 0.0001246011637182185,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880403,
      "endid": 4815880402
    },
    {
      "id": 283,
      "name": "Charterhouse Rd / Gulson Rd => TS3",
      "length": 0.014146804742061201,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880402,
      "endid": 370817661
    },
    {
      "id": 284,
      "name": "TS3 => HS4",
      "length": 0.0016821347627367477,
      "speed": {
        "0:00": 30
      },
      "startid": 370817661,
      "endid": 7620250857
    },
    {
      "id": 285,
      "name": "HS4 => White St / Bus Garage",
      "length": 0.003797063460094171,
      "speed": {
        "0:00": 30
      },
      "startid": 7620250857,
      "endid": 370817758
    },
    {
      "id": 286,
      "name": "White St / Bus Garage => Stoney Stanton Rd / Swanswell St",
      "length": 0.0019552979363815543,
      "speed": {
        "0:00": 30
      },
      "startid": 370817758,
      "endid": 370817782
    },
    {
      "id": 287,
      "name": "Stoney Stanton Rd / Swanswell St => Swanswell St / City College",
      "length": 0.0012525744129577283,
      "speed": {
        "0:00": 30
      },
      "startid": 370817782,
      "endid": 370817756
    },
    {
      "id": 288,
      "name": "Eagle St / Foleshill Rd => Eagle St / Foleshill Rd",
      "length": 0.00020139545674834492,
      "speed": {
        "0:00": 30
      },
      "startid": 370817778,
      "endid": 370817779
    },
    {
      "id": 289,
      "name": "Eagle St / Foleshill Rd => Foleshill Rd / Eagle St",
      "length": 0.0013301184082687178,
      "speed": {
        "0:00": 30
      },
      "startid": 370817779,
      "endid": 370818765
    },
    {
      "id": 290,
      "name": "Foleshill Rd / Eagle St => Foleshill Rd / Cashs Lane",
      "length": 0.0011237341055589636,
      "speed": {
        "0:00": 30
      },
      "startid": 370818765,
      "endid": 370818774
    },
    {
      "id": 291,
      "name": "Foleshill Rd / Cashs Lane => Foleshill Rd / Cashs Lane",
      "length": 0.00022125555360341274,
      "speed": {
        "0:00": 30
      },
      "startid": 370818774,
      "endid": 370818776
    },
    {
      "id": 292,
      "name": "Foleshill Rd / Cashs Lane => Foleshill Rd / Courtaulds Way",
      "length": 0.003993401069262629,
      "speed": {
        "0:00": 30
      },
      "startid": 370818776,
      "endid": 370818780
    },
    {
      "id": 293,
      "name": "Foleshill Rd / Courtaulds Way => Foleshill Rd / Courtaulds Way",
      "length": 0.00035180778843009035,
      "speed": {
        "0:00": 30
      },
      "startid": 370818780,
      "endid": 370818784
    },
    {
      "id": 294,
      "name": "Foleshill Rd / Courtaulds Way => Lockhurst Lane / Drake St",
      "length": 0.0027313134441142107,
      "speed": {
        "0:00": 30
      },
      "startid": 370818784,
      "endid": 370818817
    },
    {
      "id": 295,
      "name": "Lockhurst Lane / Drake St => Lockhurst Lane / Drake St",
      "length": 0.00037055855137838625,
      "speed": {
        "0:00": 30
      },
      "startid": 370818817,
      "endid": 370818819
    },
    {
      "id": 296,
      "name": "Lockhurst Lane / Drake St => Lockhurst Lane / Livingstone Rd",
      "length": 0.0016633556444744144,
      "speed": {
        "0:00": 30
      },
      "startid": 370818819,
      "endid": 370818821
    },
    {
      "id": 297,
      "name": "Lockhurst Lane / Livingstone Rd => Lockhurst Lane / Livingstone Rd",
      "length": 0.0006372397508020465,
      "speed": {
        "0:00": 30
      },
      "startid": 370818821,
      "endid": 370818820
    },
    {
      "id": 298,
      "name": "Lockhurst Lane / Livingstone Rd => Lockhurst Lane / Northey Rd",
      "length": 0.00218892646061737,
      "speed": {
        "0:00": 30
      },
      "startid": 370818820,
      "endid": 370818824
    },
    {
      "id": 299,
      "name": "Lockhurst Lane / Northey Rd => Lockhurst Lane / Northey Rd",
      "length": 0.0005499946545192443,
      "speed": {
        "0:00": 30
      },
      "startid": 370818824,
      "endid": 370818822
    },
    {
      "id": 300,
      "name": "Lockhurst Lane / Northey Rd => Holbrook Lane / Burnaby Rd",
      "length": 0.003404003121325636,
      "speed": {
        "0:00": 30
      },
      "startid": 370818822,
      "endid": 370818641
    },
    {
      "id": 301,
      "name": "Holbrook Lane / Burnaby Rd => Holbrook Lane / Burnaby Rd",
      "length": 0.0012164446637656114,
      "speed": {
        "0:00": 30
      },
      "startid": 370818641,
      "endid": 370818639
    },
    {
      "id": 302,
      "name": "Holbrook Lane / Burnaby Rd => Holbrook Lane / Jackson Rd",
      "length": 0.002138914960905445,
      "speed": {
        "0:00": 30
      },
      "startid": 370818639,
      "endid": 370818644
    },
    {
      "id": 303,
      "name": "Holbrook Lane / Jackson Rd => Holbrook Lane / Jackson Rd",
      "length": 0.00034841498245982087,
      "speed": {
        "0:00": 30
      },
      "startid": 370818644,
      "endid": 370818643
    },
    {
      "id": 304,
      "name": "Holbrook Lane / Jackson Rd => Holbrook Lane / Sunningdale Avenue",
      "length": 0.0021165109874502672,
      "speed": {
        "0:00": 30
      },
      "startid": 370818643,
      "endid": 370818695
    },
    {
      "id": 305,
      "name": "Holbrook Lane / Sunningdale Avenue => Holbrook Lane / Sunningdale Avenue",
      "length": 0.0005816921522595038,
      "speed": {
        "0:00": 30
      },
      "startid": 370818695,
      "endid": 370818694
    },
    {
      "id": 306,
      "name": "Holbrook Lane / Sunningdale Avenue => Holbrook Lane / Lythalls Lane",
      "length": 0.00219085827930567,
      "speed": {
        "0:00": 30
      },
      "startid": 370818694,
      "endid": 370818696
    },
    {
      "id": 307,
      "name": "Holbrook Lane / Lythalls Lane => Holbrook Lane / Lythalls Lane",
      "length": 0.0008457769504993159,
      "speed": {
        "0:00": 30
      },
      "startid": 370818696,
      "endid": 370818698
    },
    {
      "id": 308,
      "name": "Holbrook Lane / Lythalls Lane => Holbrook Lane / Beacon Rd",
      "length": 0.0011527133641974214,
      "speed": {
        "0:00": 30
      },
      "startid": 370818698,
      "endid": 370818701
    },
    {
      "id": 309,
      "name": "Holbrook Lane / Beacon Rd => Holbrook Lane / Beacon Rd",
      "length": 0.000484708675391857,
      "speed": {
        "0:00": 30
      },
      "startid": 370818701,
      "endid": 370818700
    },
    {
      "id": 310,
      "name": "Holbrook Lane / Beacon Rd => Wheelwright Lane / Roland Ave",
      "length": 0.0017179598714730875,
      "speed": {
        "0:00": 30
      },
      "startid": 370818700,
      "endid": 370818706
    },
    {
      "id": 311,
      "name": "Wheelwright Lane / Roland Ave => Hen Lane / Wheelwright Lane",
      "length": 0.0010379589201904241,
      "speed": {
        "0:00": 30
      },
      "startid": 370818706,
      "endid": 370817759
    },
    {
      "id": 312,
      "name": "Hen Lane / Wheelwright Lane => Hen Lane / Briscoe Rd",
      "length": 0.002743569538029189,
      "speed": {
        "0:00": 30
      },
      "startid": 370817759,
      "endid": 370818710
    },
    {
      "id": 313,
      "name": "Hen Lane / Lauderdale Avenue => 1493268140",
      "length": 0.007862329060145059,
      "speed": {
        "0:00": 30
      },
      "startid": 370818719,
      "endid": 1493268140
    },
    {
      "id": 314,
      "name": "1493268140 => AJ",
      "length": 0.0016239715822634923,
      "speed": {
        "0:00": 30
      },
      "startid": 1493268140,
      "endid": 4085310603
    },
    {
      "id": 315,
      "name": "AJ => AD",
      "length": 0.004517590748397498,
      "speed": {
        "0:00": 30
      },
      "startid": 4085310603,
      "endid": 370819739
    },
    {
      "id": 316,
      "name": "AD => BS6",
      "length": 0.0397801644855828,
      "speed": {
        "0:00": 30
      },
      "startid": 370819739,
      "endid": 370817664
    },
    {
      "id": 317,
      "name": "BS6 => UH4",
      "length": 0.07271595329692092,
      "speed": {
        "0:00": 30
      },
      "startid": 370817664,
      "endid": 370818279
    },
    {
      "id": 318,
      "name": "UW1 => Gibbet Hill Rd / Scarman Rd",
      "length": 0.004707836464871993,
      "speed": {
        "0:00": 30
      },
      "startid": 3731158223,
      "endid": 3731548201
    },
    {
      "id": 319,
      "name": "Gibbet Hill Rd / Scarman Rd => GH1",
      "length": 0.001683870553218648,
      "speed": {
        "0:00": 30
      },
      "startid": 3731548201,
      "endid": 370817946
    },
    {
      "id": 320,
      "name": "GH1 => Gibbet Hill Rd / Kirby Corner Rd",
      "length": 0.00028726186659678205,
      "speed": {
        "0:00": 30
      },
      "startid": 370817946,
      "endid": 370817948
    },
    {
      "id": 321,
      "name": "Gibbet Hill Rd / Kirby Corner Rd => Kirby Corner Rd / Gibbet Hill Rd",
      "length": 0.0012235206945547885,
      "speed": {
        "0:00": 30
      },
      "startid": 370817948,
      "endid": 370819749
    },
    {
      "id": 322,
      "name": "Kirby Corner Rd / Gibbet Hill Rd => Kirby Corner Rd / University Westwood Site",
      "length": 0.004738827116489978,
      "speed": {
        "0:00": 30
      },
      "startid": 370819749,
      "endid": 370817931
    },
    {
      "id": 323,
      "name": "Kirby Corner Rd / University Westwood Site => Kirby Corner Rd / University Westwood Site",
      "length": 0.0008440280208634823,
      "speed": {
        "0:00": 30
      },
      "startid": 370817931,
      "endid": 370817930
    },
    {
      "id": 324,
      "name": "Kirby Corner Rd / University Westwood Site => Kirby Corner Rd / Lynchgate Rd",
      "length": 0.004906978463372993,
      "speed": {
        "0:00": 30
      },
      "startid": 370817930,
      "endid": 370817927
    },
    {
      "id": 325,
      "name": "Kirby Corner Rd / Lynchgate Rd => Kirby Corner Rd / Lynchgate Rd",
      "length": 0.00029797681117596606,
      "speed": {
        "0:00": 30
      },
      "startid": 370817927,
      "endid": 370817929
    },
    {
      "id": 326,
      "name": "Kirby Corner Rd / Lynchgate Rd => Lynchgate Rd / Leeming Close",
      "length": 0.004009206591087638,
      "speed": {
        "0:00": 30
      },
      "startid": 370817929,
      "endid": 370819152
    },
    {
      "id": 327,
      "name": "Lynchgate Rd / Leeming Close => De Montfort Way / Cannon Park Shops",
      "length": 0.0023546683949164826,
      "speed": {
        "0:00": 30
      },
      "startid": 370819152,
      "endid": 370817920
    },
    {
      "id": 328,
      "name": "De Montfort Way / Cannon Park Shops => Sir Henry Parkes Rd / Centenary Rd",
      "length": 0.004222512670197375,
      "speed": {
        "0:00": 30
      },
      "startid": 370817920,
      "endid": 370817913
    },
    {
      "id": 329,
      "name": "Sir Henry Parkes Rd / Centenary Rd => Fletchamstead Highway / Canley Rd",
      "length": 0.0052666385228150306,
      "speed": {
        "0:00": 30
      },
      "startid": 370817913,
      "endid": 370819754
    },
    {
      "id": 330,
      "name": "Fletchamstead Highway / Canley Rd => Kenpas Highway / Leamington Rd",
      "length": 0.032448214264116364,
      "speed": {
        "0:00": 30
      },
      "startid": 370819754,
      "endid": 370818958
    },
    {
      "id": 331,
      "name": "Kenpas Highway / Leamington Rd => Kenpas Highway / Bathway Rd",
      "length": 0.007177886753773176,
      "speed": {
        "0:00": 30
      },
      "startid": 370818958,
      "endid": 370818955
    },
    {
      "id": 332,
      "name": "Kenpas Highway / Bathway Rd => Kenpas Highway / Bathway Rd",
      "length": 0.0003065698289125855,
      "speed": {
        "0:00": 30
      },
      "startid": 370818955,
      "endid": 370818956
    },
    {
      "id": 333,
      "name": "Kenpas Highway / Bathway Rd => Kenpas Highway / Green Lane",
      "length": 0.005219613098687893,
      "speed": {
        "0:00": 30
      },
      "startid": 370818956,
      "endid": 370819756
    },
    {
      "id": 334,
      "name": "Kenpas Highway / Green Lane => Kenpas Highway / Wainbody Avenue",
      "length": 0.0018871993482405607,
      "speed": {
        "0:00": 30
      },
      "startid": 370819756,
      "endid": 370817883
    },
    {
      "id": 335,
      "name": "Kenpas Highway / Wainbody Avenue => Kenpas Highway / Wainbody Avenue",
      "length": 0.0014131731457975225,
      "speed": {
        "0:00": 30
      },
      "startid": 370817883,
      "endid": 370817880
    },
    {
      "id": 336,
      "name": "Kenpas Highway / Wainbody Avenue => Fletchamstead Highway / Cannon Park Rd",
      "length": 0.005509793529706021,
      "speed": {
        "0:00": 30
      },
      "startid": 370817880,
      "endid": 370817894
    },
    {
      "id": 337,
      "name": "Fletchamstead Highway / Cannon Park Rd => Fletchamstead Highway / Cannon Park Rd",
      "length": 0.0025635280942480913,
      "speed": {
        "0:00": 30
      },
      "startid": 370817894,
      "endid": 370817893
    },
    {
      "id": 338,
      "name": "Fletchamstead Highway / Cannon Park Rd => Leamington Rd / Stonebridge Highway",
      "length": 0.023871319688068434,
      "speed": {
        "0:00": 30
      },
      "startid": 370817893,
      "endid": 370818933
    },
    {
      "id": 339,
      "name": "Leamington Rd / Stonebridge Highway => Leamington Rd / Stonebridge Highway",
      "length": 0.00028445586652267,
      "speed": {
        "0:00": 30
      },
      "startid": 370818933,
      "endid": 370818935
    },
    {
      "id": 340,
      "name": "Leamington Rd / Stonebridge Highway => Leamington Rd / Dewsbury Avenue",
      "length": 0.002528549546679714,
      "speed": {
        "0:00": 30
      },
      "startid": 370818935,
      "endid": 370818579
    },
    {
      "id": 341,
      "name": "Leamington Rd / Dewsbury Avenue => Leamington Rd / Dewsbury Avenue",
      "length": 0.00026672916975609856,
      "speed": {
        "0:00": 30
      },
      "startid": 370818579,
      "endid": 370818578
    },
    {
      "id": 342,
      "name": "Leamington Rd / Dewsbury Avenue => Leamington Rd / Baginton Rd",
      "length": 0.0008850576478397776,
      "speed": {
        "0:00": 30
      },
      "startid": 370818578,
      "endid": 370818575
    },
    {
      "id": 343,
      "name": "Leamington Rd / Baginton Rd => Baginton Rd / The Chesils",
      "length": 0.001279121640033208,
      "speed": {
        "0:00": 30
      },
      "startid": 370818575,
      "endid": 370819161
    },
    {
      "id": 344,
      "name": "Baginton Rd / The Chesils => The Chesils / Ridgeway Avenue",
      "length": 0.0011475752219346775,
      "speed": {
        "0:00": 30
      },
      "startid": 370819161,
      "endid": 370819727
    },
    {
      "id": 345,
      "name": "The Chesils / Ridgeway Avenue => The Chesils / Ridgeway Avenue",
      "length": 0.0003339799395154415,
      "speed": {
        "0:00": 30
      },
      "startid": 370819727,
      "endid": 370819729
    },
    {
      "id": 346,
      "name": "The Chesils / Ridgeway Avenue => The Chesils / Knoll Drive",
      "length": 0.002191582008503791,
      "speed": {
        "0:00": 30
      },
      "startid": 370819729,
      "endid": 370819072
    },
    {
      "id": 347,
      "name": "The Chesils / Knoll Drive => The Chesils / Knoll Drive",
      "length": 0.00043950893051316464,
      "speed": {
        "0:00": 30
      },
      "startid": 370819072,
      "endid": 370819071
    },
    {
      "id": 348,
      "name": "The Chesils / Knoll Drive => The Chesils / Dillotford Avenue",
      "length": 0.0015665817086885734,
      "speed": {
        "0:00": 30
      },
      "startid": 370819071,
      "endid": 370819075
    },
    {
      "id": 349,
      "name": "The Chesils / Dillotford Avenue => The Chesils / Dillotford Avenue",
      "length": 0.0014154314183323813,
      "speed": {
        "0:00": 30
      },
      "startid": 370819075,
      "endid": 370819074
    },
    {
      "id": 350,
      "name": "The Chesils / Dillotford Avenue => The Chesils / Ulverscroft Rd",
      "length": 0.0026621070395426417,
      "speed": {
        "0:00": 30
      },
      "startid": 370819074,
      "endid": 370819810
    },
    {
      "id": 351,
      "name": "The Chesils / Ulverscroft Rd => The Chesils / Ulverscroft Rd",
      "length": 0.00016712345735921276,
      "speed": {
        "0:00": 30
      },
      "startid": 370819810,
      "endid": 370819811
    },
    {
      "id": 352,
      "name": "The Chesils / Ulverscroft Rd => Black Prince Ave / Mary Herbert St",
      "length": 0.0036517707047401047,
      "speed": {
        "0:00": 30
      },
      "startid": 370819811,
      "endid": 370818536
    },
    {
      "id": 353,
      "name": "Black Prince Ave / Mary Herbert St => Black Prince Ave / Mary Herbert St",
      "length": 0.000678884828230006,
      "speed": {
        "0:00": 30
      },
      "startid": 370818536,
      "endid": 370818537
    },
    {
      "id": 354,
      "name": "Black Prince Ave / Mary Herbert St => Black Prince Ave / Arundel Rd",
      "length": 0.0036360066474085254,
      "speed": {
        "0:00": 30
      },
      "startid": 370818537,
      "endid": 370818538
    },
    {
      "id": 355,
      "name": "Black Prince Ave / Arundel Rd => William Bristow Rd / Seneschal Rd",
      "length": 0.0005686934938977226,
      "speed": {
        "0:00": 30
      },
      "startid": 370818538,
      "endid": 370819743
    },
    {
      "id": 356,
      "name": "William Bristow Rd / Seneschal Rd => William Bristow Rd / Esher Drive",
      "length": 0.0012883850666645397,
      "speed": {
        "0:00": 30
      },
      "startid": 370819743,
      "endid": 370819807
    },
    {
      "id": 357,
      "name": "William Bristow Rd / Esher Drive => William Bristow Rd / Esher Drive",
      "length": 0.0002832698360217084,
      "speed": {
        "0:00": 30
      },
      "startid": 370819807,
      "endid": 370819809
    },
    {
      "id": 358,
      "name": "William Bristow Rd / Esher Drive => William Bristow Rd / Cecily Rd",
      "length": 0.001797233012158026,
      "speed": {
        "0:00": 30
      },
      "startid": 370819809,
      "endid": 370819742
    },
    {
      "id": 359,
      "name": "William Bristow Rd / Cecily Rd => William Bristow Rd / Cecily Rd",
      "length": 0.0004280925250451224,
      "speed": {
        "0:00": 30
      },
      "startid": 370819742,
      "endid": 370819741
    },
    {
      "id": 360,
      "name": "William Bristow Rd / Cecily Rd => Daventry Rd / The Mount",
      "length": 0.0011595657506181585,
      "speed": {
        "0:00": 30
      },
      "startid": 370819741,
      "endid": 370818519
    },
    {
      "id": 361,
      "name": "Daventry Rd / The Mount => Daventry Rd / London Rd",
      "length": 0.002846572003304803,
      "speed": {
        "0:00": 30
      },
      "startid": 370818519,
      "endid": 370818524
    },
    {
      "id": 362,
      "name": "Daventry Rd / London Rd => Daventry Rd / London Rd",
      "length": 0.00033666725412569983,
      "speed": {
        "0:00": 30
      },
      "startid": 370818524,
      "endid": 370818522
    },
    {
      "id": 363,
      "name": "Daventry Rd / London Rd => Leaf Lane / Jaguar Works",
      "length": 0.008123091175777721,
      "speed": {
        "0:00": 30
      },
      "startid": 370818522,
      "endid": 4815874903
    },
    {
      "id": 364,
      "name": "Leaf Lane / Jaguar Works => London Rd / Riverside Close",
      "length": 0.006798259524320715,
      "speed": {
        "0:00": 30
      },
      "startid": 4815874903,
      "endid": 370818598
    },
    {
      "id": 365,
      "name": "London Rd / Riverside Close => London Rd / Riverside Close",
      "length": 0.0011431498676901016,
      "speed": {
        "0:00": 30
      },
      "startid": 370818598,
      "endid": 370818597
    },
    {
      "id": 366,
      "name": "London Rd / Riverside Close => London Rd / Tonbridge Rd",
      "length": 0.0056439592707584075,
      "speed": {
        "0:00": 30
      },
      "startid": 370818597,
      "endid": 370818601
    },
    {
      "id": 367,
      "name": "London Rd / Tonbridge Rd => London Rd / Tonbridge Rd",
      "length": 0.0003229243409830427,
      "speed": {
        "0:00": 30
      },
      "startid": 370818601,
      "endid": 370818600
    },
    {
      "id": 368,
      "name": "London Rd / Tonbridge Rd => London Rd / Abbey Rd",
      "length": 0.0027695408716981364,
      "speed": {
        "0:00": 30
      },
      "startid": 370818600,
      "endid": 370818602
    },
    {
      "id": 369,
      "name": "London Rd / Abbey Rd => London Rd / Abbey Rd",
      "length": 0.0013384568203700501,
      "speed": {
        "0:00": 30
      },
      "startid": 370818602,
      "endid": 370818604
    },
    {
      "id": 370,
      "name": "London Rd / Abbey Rd => London Rd / Chace Avenue",
      "length": 0.0026914786512259497,
      "speed": {
        "0:00": 30
      },
      "startid": 370818604,
      "endid": 4248964910
    },
    {
      "id": 371,
      "name": "London Rd / Chace Avenue => London Rd / St James Lane",
      "length": 0.002023270664047027,
      "speed": {
        "0:00": 30
      },
      "startid": 4248964910,
      "endid": 370818985
    },
    {
      "id": 372,
      "name": "London Rd / St James Lane => St James Lane / London Rd",
      "length": 0.0022078424762651877,
      "speed": {
        "0:00": 30
      },
      "startid": 370818985,
      "endid": 370819723
    },
    {
      "id": 373,
      "name": "St James Lane / London Rd => St James Lane / Cedric Close",
      "length": 0.004031236182612137,
      "speed": {
        "0:00": 30
      },
      "startid": 370819723,
      "endid": 370818990
    },
    {
      "id": 374,
      "name": "St James Lane / Cedric Close => St James Lane / Cedric Close",
      "length": 0.0005462948013669836,
      "speed": {
        "0:00": 30
      },
      "startid": 370818990,
      "endid": 370818995
    },
    {
      "id": 375,
      "name": "St James Lane / Cedric Close => St James Lane / Dunsmore Avenue",
      "length": 0.0022731797817127104,
      "speed": {
        "0:00": 30
      },
      "startid": 370818995,
      "endid": 370818997
    },
    {
      "id": 376,
      "name": "St James Lane / Dunsmore Avenue => St James Lane / Dunsmore Avenue",
      "length": 0.0009609037933145949,
      "speed": {
        "0:00": 30
      },
      "startid": 370818997,
      "endid": 370818999
    },
    {
      "id": 377,
      "name": "St James Lane / Dunsmore Avenue => Robin Hood Rd / Willenhall Social Club",
      "length": 0.0014634688243968337,
      "speed": {
        "0:00": 30
      },
      "startid": 370818999,
      "endid": 370819060
    },
    {
      "id": 378,
      "name": "Robin Hood Rd / Willenhall Social Club => Remembrance Rd / Robin Hood Rd",
      "length": 0.0013364006323022468,
      "speed": {
        "0:00": 30
      },
      "startid": 370819060,
      "endid": 370819018
    },
    {
      "id": 379,
      "name": "Remembrance Rd / Robin Hood Rd => Remembrance Rd / Robin Hood Rd",
      "length": 0.0002497812843251117,
      "speed": {
        "0:00": 30
      },
      "startid": 370819018,
      "endid": 370819020
    },
    {
      "id": 380,
      "name": "Remembrance Rd / Robin Hood Rd => Remembrance Rd / Meadfoot Rd",
      "length": 0.004700035016889503,
      "speed": {
        "0:00": 30
      },
      "startid": 370819020,
      "endid": 370819011
    },
    {
      "id": 381,
      "name": "Remembrance Rd / Meadfoot Rd => Remembrance Rd / Meadfoot Rd",
      "length": 0.00021900020547924723,
      "speed": {
        "0:00": 30
      },
      "startid": 370819011,
      "endid": 370819015
    },
    {
      "id": 382,
      "name": "Remembrance Rd / Meadfoot Rd => St James Lane / Remembrance Rd",
      "length": 0.0023430831141896718,
      "speed": {
        "0:00": 30
      },
      "startid": 370819015,
      "endid": 370819030
    },
    {
      "id": 383,
      "name": "St James Lane / Remembrance Rd => St James Lane / Remembrance Rd",
      "length": 0.0006869756618688374,
      "speed": {
        "0:00": 30
      },
      "startid": 370819030,
      "endid": 370819024
    },
    {
      "id": 384,
      "name": "St James Lane / Remembrance Rd => St James Lane / Middle Ride",
      "length": 0.0034330742272778163,
      "speed": {
        "0:00": 30
      },
      "startid": 370819024,
      "endid": 370819037
    },
    {
      "id": 385,
      "name": "St James Lane / Middle Ride => St James Lane / Middle Ride",
      "length": 0.0009964726589326248,
      "speed": {
        "0:00": 30
      },
      "startid": 370819037,
      "endid": 370819033
    },
    {
      "id": 386,
      "name": "St James Lane / Middle Ride => Willenhall Lane / Craigends Avenue",
      "length": 0.004659450239030234,
      "speed": {
        "0:00": 30
      },
      "startid": 370819033,
      "endid": 370818483
    },
    {
      "id": 387,
      "name": "Willenhall Lane / Craigends Avenue => Willenhall Lane / Craigends Avenue",
      "length": 0.0001938537593170669,
      "speed": {
        "0:00": 30
      },
      "startid": 370818483,
      "endid": 370818485
    },
    {
      "id": 388,
      "name": "Willenhall Lane / Craigends Avenue => Quorn Way / William Mckee Close",
      "length": 0.002202882883856658,
      "speed": {
        "0:00": 30
      },
      "startid": 370818485,
      "endid": 370818481
    },
    {
      "id": 389,
      "name": "Quorn Way / William Mckee Close => Quorn Way / William Mckee Close",
      "length": 0.00033093233447511073,
      "speed": {
        "0:00": 30
      },
      "startid": 370818481,
      "endid": 370818482
    },
    {
      "id": 390,
      "name": "Quorn Way / William Mckee Close => Bredon Avenue / Ashby Close",
      "length": 0.001413791091355694,
      "speed": {
        "0:00": 30
      },
      "startid": 370818482,
      "endid": 370818479
    },
    {
      "id": 391,
      "name": "Bredon Avenue / Ashby Close => Bredon Avenue / Ashby Close",
      "length": 0.0005371153041952862,
      "speed": {
        "0:00": 30
      },
      "startid": 370818479,
      "endid": 370818478
    },
    {
      "id": 392,
      "name": "Bredon Avenue / Ashby Close => Bredon Avenue / Invicta Rd",
      "length": 0.0017172689043927207,
      "speed": {
        "0:00": 30
      },
      "startid": 370818478,
      "endid": 370818474
    },
    {
      "id": 393,
      "name": "Bredon Avenue / Invicta Rd => Bredon Avenue / Invicta Rd",
      "length": 0.0013760327030977414,
      "speed": {
        "0:00": 30
      },
      "startid": 370818474,
      "endid": 370818475
    },
    {
      "id": 394,
      "name": "Bredon Avenue / Invicta Rd => Bredon Avenue / Sandwick Close",
      "length": 0.001335234391409192,
      "speed": {
        "0:00": 30
      },
      "startid": 370818475,
      "endid": 370818472
    },
    {
      "id": 395,
      "name": "Bredon Avenue / Sandwick Close => Bredon Avenue / Sandwick Close",
      "length": 0.0002288041302067782,
      "speed": {
        "0:00": 30
      },
      "startid": 370818472,
      "endid": 370818471
    },
    {
      "id": 396,
      "name": "Bredon Avenue / Sandwick Close => Deerdale Way / Willenhall Lane",
      "length": 0.004044732185200675,
      "speed": {
        "0:00": 30
      },
      "startid": 370818471,
      "endid": 370818400
    },
    {
      "id": 397,
      "name": "Deerdale Way / Willenhall Lane => Deerdale Way / Willenhall Lane",
      "length": 0.0007129659879684774,
      "speed": {
        "0:00": 30
      },
      "startid": 370818400,
      "endid": 370818402
    },
    {
      "id": 398,
      "name": "Deerdale Way / Willenhall Lane => Willenhall Lane / Industrial Estate",
      "length": 0.001456776413868924,
      "speed": {
        "0:00": 30
      },
      "startid": 370818402,
      "endid": 370818470
    },
    {
      "id": 399,
      "name": "Willenhall Lane / Industrial Estate => Brandon Rd / Willenhall Lane",
      "length": 0.0017606169486793033,
      "speed": {
        "0:00": 30
      },
      "startid": 370818470,
      "endid": 370818463
    },
    {
      "id": 400,
      "name": "Brandon Rd / Willenhall Lane => Brandon Rd / Willenhall Lane",
      "length": 0.0003965726289091613,
      "speed": {
        "0:00": 30
      },
      "startid": 370818463,
      "endid": 370818461
    },
    {
      "id": 401,
      "name": "Brandon Rd / Willenhall Lane => Brandon Rd / Binley Park Inn",
      "length": 0.0039827592570996434,
      "speed": {
        "0:00": 30
      },
      "startid": 370818461,
      "endid": 370818453
    },
    {
      "id": 402,
      "name": "Brandon Rd / Binley Park Inn => Brandon Rd / Binley Park Inn",
      "length": 0.0005661131512307444,
      "speed": {
        "0:00": 30
      },
      "startid": 370818453,
      "endid": 370818456
    },
    {
      "id": 403,
      "name": "Brandon Rd / Binley Park Inn => Brinklow Rd / Binley Church",
      "length": 0.0009995471474615672,
      "speed": {
        "0:00": 30
      },
      "startid": 370818456,
      "endid": 370818403
    },
    {
      "id": 404,
      "name": "Brinklow Rd / Binley Church => Brinklow Rd / Binley Church",
      "length": 0.00043138813150249373,
      "speed": {
        "0:00": 30
      },
      "startid": 370818403,
      "endid": 370818404
    },
    {
      "id": 405,
      "name": "Brinklow Rd / Binley Church => Clifford Bridge Rd / Coombe Park Rd",
      "length": 0.0019197100432089239,
      "speed": {
        "0:00": 30
      },
      "startid": 370818404,
      "endid": 370818409
    },
    {
      "id": 406,
      "name": "Clifford Bridge Rd / Coombe Park Rd => Clifford Bridge Rd / Coombe Park Rd",
      "length": 0.0005575986459799535,
      "speed": {
        "0:00": 30
      },
      "startid": 370818409,
      "endid": 370818406
    },
    {
      "id": 407,
      "name": "Clifford Bridge Rd / Coombe Park Rd => Clifford Bridge Rd / Bridgeacre Gardens",
      "length": 0.0025707344942616124,
      "speed": {
        "0:00": 30
      },
      "startid": 370818406,
      "endid": 370818410
    },
    {
      "id": 408,
      "name": "Clifford Bridge Rd / Bridgeacre Gardens => Clifford Bridge Rd / Bridgeacre Gardens",
      "length": 0.00034793569808658665,
      "speed": {
        "0:00": 30
      },
      "startid": 370818410,
      "endid": 370818412
    },
    {
      "id": 409,
      "name": "Clifford Bridge Rd / Bridgeacre Gardens => Clifford Bridge Rd / Gainford Rise",
      "length": 0.0010103507608701986,
      "speed": {
        "0:00": 30
      },
      "startid": 370818412,
      "endid": 370818415
    },
    {
      "id": 410,
      "name": "Clifford Bridge Rd / Gainford Rise => Clifford Bridge Rd / Gainford Rise",
      "length": 0.0007986141120735769,
      "speed": {
        "0:00": 30
      },
      "startid": 370818415,
      "endid": 370818418
    },
    {
      "id": 411,
      "name": "Clifford Bridge Rd / Gainford Rise => Clifford Bridge Rd / Tesco",
      "length": 0.0022040893856635595,
      "speed": {
        "0:00": 30
      },
      "startid": 370818418,
      "endid": 370817577
    },
    {
      "id": 412,
      "name": "Clifford Bridge Rd / Tesco => Clifford Bridge Rd / Tesco",
      "length": 0.0011893140922393406,
      "speed": {
        "0:00": 30
      },
      "startid": 370817577,
      "endid": 370817575
    },
    {
      "id": 413,
      "name": "Clifford Bridge Rd / Tesco => Clifford Bridge Rd / Dorchester Way",
      "length": 0.006370308992510571,
      "speed": {
        "0:00": 30
      },
      "startid": 370817575,
      "endid": 370817578
    },
    {
      "id": 414,
      "name": "Clifford Bridge Rd / Dorchester Way => WH",
      "length": 0.0031459014129458303,
      "speed": {
        "0:00": 30
      },
      "startid": 370817578,
      "endid": 370817732
    },
    {
      "id": 415,
      "name": "WH => WG",
      "length": 0.000278365084014834,
      "speed": {
        "0:00": 30
      },
      "startid": 370817732,
      "endid": 370817730
    },
    {
      "id": 416,
      "name": "WG => WF",
      "length": 0.003325900281127788,
      "speed": {
        "0:00": 30
      },
      "startid": 370817730,
      "endid": 370817729
    },
    {
      "id": 417,
      "name": "WF => UH3",
      "length": 0.0023002886797094564,
      "speed": {
        "0:00": 30
      },
      "startid": 370817729,
      "endid": 370817649
    },
    {
      "id": 418,
      "name": "UH3 => Belgrave Rd / Clifford Bridge Rd",
      "length": 0.009598382082937746,
      "speed": {
        "0:00": 30
      },
      "startid": 370817649,
      "endid": 370817709
    },
    {
      "id": 419,
      "name": "Belgrave Rd / Clifford Bridge Rd => Belgrave Rd / Clifford Bridge Rd",
      "length": 0.000413697050992378,
      "speed": {
        "0:00": 30
      },
      "startid": 370817709,
      "endid": 370817707
    },
    {
      "id": 420,
      "name": "Belgrave Rd / Clifford Bridge Rd => Belgrave Rd / Westmorland Rd",
      "length": 0.002525399184286982,
      "speed": {
        "0:00": 30
      },
      "startid": 370817707,
      "endid": 370817625
    },
    {
      "id": 421,
      "name": "Belgrave Rd / Westmorland Rd => Belgrave Rd / Westmorland Rd",
      "length": 0.0001048001908401134,
      "speed": {
        "0:00": 30
      },
      "startid": 370817625,
      "endid": 370817627
    },
    {
      "id": 422,
      "name": "Belgrave Rd / Westmorland Rd => Belgrave Rd / Arch Rd",
      "length": 0.003083393536349537,
      "speed": {
        "0:00": 30
      },
      "startid": 370817627,
      "endid": 370817572
    },
    {
      "id": 423,
      "name": "Belgrave Rd / Arch Rd => Belgrave Rd / Arch Rd",
      "length": 0.00045216626366826956,
      "speed": {
        "0:00": 30
      },
      "startid": 370817572,
      "endid": 370817571
    },
    {
      "id": 424,
      "name": "Belgrave Rd / Arch Rd => Belgrave Rd / Attoxhall Rd",
      "length": 0.0036362293230761656,
      "speed": {
        "0:00": 30
      },
      "startid": 370817571,
      "endid": 370819304
    },
    {
      "id": 425,
      "name": "Belgrave Rd / Attoxhall Rd => Belgrave Rd / Attoxhall Rd",
      "length": 0.00013086252328456342,
      "speed": {
        "0:00": 30
      },
      "startid": 370819304,
      "endid": 370819303
    },
    {
      "id": 426,
      "name": "Belgrave Rd / Attoxhall Rd => Belgrave Rd / St Ives Rd",
      "length": 0.0023936576614048783,
      "speed": {
        "0:00": 30
      },
      "startid": 370819303,
      "endid": 370817706
    },
    {
      "id": 427,
      "name": "Belgrave Rd / St Ives Rd => Hipswell Highway / Belgrave Rd",
      "length": 0.000789897436380245,
      "speed": {
        "0:00": 30
      },
      "startid": 370817706,
      "endid": 370817519
    },
    {
      "id": 428,
      "name": "Hipswell Highway / Belgrave Rd => Hipswell Highway / The Wyken Pippin",
      "length": 0.00231997310545036,
      "speed": {
        "0:00": 30
      },
      "startid": 370817519,
      "endid": 370819636
    },
    {
      "id": 429,
      "name": "Hipswell Highway / The Wyken Pippin => Sewall Highway / Wyken Avenue",
      "length": 0.0015969225560444162,
      "speed": {
        "0:00": 30
      },
      "startid": 370819636,
      "endid": 370819160
    },
    {
      "id": 430,
      "name": "Sewall Highway / Wyken Avenue => Sewall Highway / Tiverton Rd",
      "length": 0.00479852285291905,
      "speed": {
        "0:00": 30
      },
      "startid": 370819160,
      "endid": 370819157
    },
    {
      "id": 431,
      "name": "Sewall Highway / Tiverton Rd => Sewall Highway / Tiverton Rd",
      "length": 0.00011073301224297402,
      "speed": {
        "0:00": 30
      },
      "startid": 370819157,
      "endid": 370819159
    },
    {
      "id": 432,
      "name": "Sewall Highway / Tiverton Rd => Sewall Highway / Torcross Avenue",
      "length": 0.0030247192018421384,
      "speed": {
        "0:00": 30
      },
      "startid": 370819159,
      "endid": 370819594
    },
    {
      "id": 433,
      "name": "Sewall Highway / Torcross Avenue => Torcross Ave / Sewall Highway",
      "length": 0.0007732489443898928,
      "speed": {
        "0:00": 30
      },
      "startid": 370819594,
      "endid": 370817486
    },
    {
      "id": 434,
      "name": "Torcross Ave / Sewall Highway => Sewall Highway / Middle",
      "length": 0.003031260175240516,
      "speed": {
        "0:00": 30
      },
      "startid": 370817486,
      "endid": 370819641
    },
    {
      "id": 435,
      "name": "Sewall Highway / Middle => Sewall Highway / Dennis Rd",
      "length": 0.002706378391876186,
      "speed": {
        "0:00": 30
      },
      "startid": 370819641,
      "endid": 370819640
    },
    {
      "id": 436,
      "name": "Sewall Highway / Dennis Rd => Sewall Highway / Dennis Rd",
      "length": 0.0006107787897418022,
      "speed": {
        "0:00": 30
      },
      "startid": 370819640,
      "endid": 370819639
    },
    {
      "id": 437,
      "name": "Sewall Highway / Dennis Rd => Sewall Highway / Blackberry Lane",
      "length": 0.0014448067033318197,
      "speed": {
        "0:00": 30
      },
      "startid": 370819639,
      "endid": 370819637
    },
    {
      "id": 438,
      "name": "Sewall Highway / Blackberry Lane => Sewall Highway / Stoke Heath",
      "length": 0.002495324269508649,
      "speed": {
        "0:00": 30
      },
      "startid": 370819637,
      "endid": 370817496
    },
    {
      "id": 439,
      "name": "Sewall Highway / Stoke Heath => Sewall Highway / Stoke Heath",
      "length": 0.00032229107961597293,
      "speed": {
        "0:00": 30
      },
      "startid": 370817496,
      "endid": 370817495
    },
    {
      "id": 440,
      "name": "Sewall Highway / Stoke Heath => Sewall Highway / Purcell Rd",
      "length": 0.003023914881411909,
      "speed": {
        "0:00": 30
      },
      "startid": 370817495,
      "endid": 370817498
    },
    {
      "id": 441,
      "name": "Sewall Highway / Purcell Rd => Sewall Highway / Purcell Rd",
      "length": 0.0013855523808202221,
      "speed": {
        "0:00": 30
      },
      "startid": 370817498,
      "endid": 370817497
    },
    {
      "id": 442,
      "name": "Sewall Highway / Purcell Rd => Sewall Highway / Courthouse Green School",
      "length": 0.0020618558363773173,
      "speed": {
        "0:00": 30
      },
      "startid": 370817497,
      "endid": 370817783
    },
    {
      "id": 443,
      "name": "Sewall Highway / Courthouse Green School => Sewall Highway / Courthouse Green School",
      "length": 0.00023345074426964503,
      "speed": {
        "0:00": 30
      },
      "startid": 370817783,
      "endid": 370817785
    },
    {
      "id": 444,
      "name": "Sewall Highway / Courthouse Green School => Proffitt Ave / Elkington St",
      "length": 0.0032346073795722816,
      "speed": {
        "0:00": 30
      },
      "startid": 370817785,
      "endid": 370817391
    },
    {
      "id": 445,
      "name": "Proffitt Ave / Elkington St => Proffitt Ave / Elkington St",
      "length": 0.0004867998048474009,
      "speed": {
        "0:00": 30
      },
      "startid": 370817391,
      "endid": 370817392
    },
    {
      "id": 446,
      "name": "Proffitt Ave / Elkington St => Proffitt Ave / Dudley St",
      "length": 0.0018428503927375834,
      "speed": {
        "0:00": 30
      },
      "startid": 370817392,
      "endid": 370818496
    },
    {
      "id": 447,
      "name": "Proffitt Ave / Dudley St => Proffitt Ave / Gayer St",
      "length": 0.0006167980301511341,
      "speed": {
        "0:00": 30
      },
      "startid": 370818496,
      "endid": 370817355
    },
    {
      "id": 448,
      "name": "Proffitt Ave / Gayer St => Proffitt Ave / Thomas Lane St",
      "length": 0.001899254814393909,
      "speed": {
        "0:00": 30
      },
      "startid": 370817355,
      "endid": 370817358
    },
    {
      "id": 449,
      "name": "Proffitt Ave / Thomas Lane St => Proffitt Ave / Thomas Lane St",
      "length": 0.0002484673016722097,
      "speed": {
        "0:00": 30
      },
      "startid": 370817358,
      "endid": 370817357
    },
    {
      "id": 450,
      "name": "Proffitt Ave / Thomas Lane St => Old Church Rd / Old Church Rd",
      "length": 0.0033300960001174064,
      "speed": {
        "0:00": 30
      },
      "startid": 370817357,
      "endid": 4340167903
    },
    {
      "id": 451,
      "name": "Old Church Rd / Old Church Rd => Old Church Rd / Old Church Rd",
      "length": 0.0003017998343275688,
      "speed": {
        "0:00": 30
      },
      "startid": 4340167903,
      "endid": 4340167904
    },
    {
      "id": 452,
      "name": "Old Church Rd / Old Church Rd => Old Church Rd / Foleshill Rd",
      "length": 0.005627819116674061,
      "speed": {
        "0:00": 30
      },
      "startid": 4340167904,
      "endid": 370819598
    },
    {
      "id": 453,
      "name": "Old Church Rd / Foleshill Rd => Old Church Rd / Foleshill Rd",
      "length": 0.00016866324436543354,
      "speed": {
        "0:00": 30
      },
      "startid": 370819598,
      "endid": 370819599
    },
    {
      "id": 454,
      "name": "Old Church Rd / Foleshill Rd => AE",
      "length": 0.005769502312159234,
      "speed": {
        "0:00": 30
      },
      "startid": 370819599,
      "endid": 370819740
    },
    {
      "id": 455,
      "name": "AE => AG",
      "length": 0.0013163040112380477,
      "speed": {
        "0:00": 30
      },
      "startid": 370819740,
      "endid": 370818869
    },
    {
      "id": 456,
      "name": "AG => AF",
      "length": 0.0008466729474816734,
      "speed": {
        "0:00": 30
      },
      "startid": 370818869,
      "endid": 370818867
    },
    {
      "id": 457,
      "name": "AF => Foleshill Rd / The Wheatsheaf",
      "length": 0.001456813598235208,
      "speed": {
        "0:00": 30
      },
      "startid": 370818867,
      "endid": 370818864
    },
    {
      "id": 458,
      "name": "Foleshill Rd / The Wheatsheaf => Foleshill Rd / The Wheatsheaf",
      "length": 0.00031738230889481126,
      "speed": {
        "0:00": 30
      },
      "startid": 370818864,
      "endid": 370818865
    },
    {
      "id": 459,
      "name": "Foleshill Rd / The Wheatsheaf => Charter Ave / Sir Henry Parkes Rd",
      "length": 0.0797750719539018,
      "speed": {
        "0:00": 30
      },
      "startid": 370818865,
      "endid": 370817940
    },
    {
      "id": 460,
      "name": "Charter Ave / Sir Henry Parkes Rd => Gibbet Hill Rd / Scarman Rd",
      "length": 0.013421368197395624,
      "speed": {
        "0:00": 30
      },
      "startid": 370817940,
      "endid": 3731548192
    },
    {
      "id": 461,
      "name": "Gibbet Hill Rd / Scarman Rd => Charter Ave / Fletchamstead Highway",
      "length": 0.018131450801854694,
      "speed": {
        "0:00": 30
      },
      "startid": 3731548192,
      "endid": 466384984
    },
    {
      "id": 462,
      "name": "Charter Ave / Fletchamstead Highway => Charter Ave / Centenary Rd",
      "length": 0.0031323945361338627,
      "speed": {
        "0:00": 30
      },
      "startid": 466384984,
      "endid": 370817918
    },
    {
      "id": 463,
      "name": "Charter Ave / Centenary Rd => UH9",
      "length": 0.11668956344819315,
      "speed": {
        "0:00": 30
      },
      "startid": 370817918,
      "endid": 4062225927
    },
    {
      "id": 464,
      "name": "Cedars Road => Cedars Road",
      "length": 0.00009587251952832346,
      "speed": {
        "0:00": 30
      },
      "startid": 487166699,
      "endid": 487166701
    },
    {
      "id": 465,
      "name": "Cedars Road => Field View Close",
      "length": 0.002068134205025566,
      "speed": {
        "0:00": 30
      },
      "startid": 487166701,
      "endid": 487169363
    },
    {
      "id": 466,
      "name": "Field View Close => Field View Close",
      "length": 0.0005728722894345266,
      "speed": {
        "0:00": 30
      },
      "startid": 487169363,
      "endid": 487169354
    },
    {
      "id": 467,
      "name": "Field View Close => Hayes Lane",
      "length": 0.0008336227264145015,
      "speed": {
        "0:00": 30
      },
      "startid": 487169354,
      "endid": 487174464
    },
    {
      "id": 468,
      "name": "Hayes Lane => Hayes Lane",
      "length": 0.0007126821732062443,
      "speed": {
        "0:00": 30
      },
      "startid": 487174464,
      "endid": 487169359
    },
    {
      "id": 469,
      "name": "Hayes Lane => Heckley Road",
      "length": 0.0019734361149991134,
      "speed": {
        "0:00": 30
      },
      "startid": 487169359,
      "endid": 487174461
    },
    {
      "id": 470,
      "name": "Heckley Road => Trelawney Road",
      "length": 0.0009165142933970633,
      "speed": {
        "0:00": 30
      },
      "startid": 487174461,
      "endid": 487169366
    },
    {
      "id": 471,
      "name": "Trelawney Road => Lord Raglan",
      "length": 0.0008222157867605711,
      "speed": {
        "0:00": 30
      },
      "startid": 487169366,
      "endid": 487174457
    },
    {
      "id": 472,
      "name": "Lord Raglan => Blackhorse Road",
      "length": 0.001911582135301548,
      "speed": {
        "0:00": 30
      },
      "startid": 487174457,
      "endid": 487169369
    },
    {
      "id": 473,
      "name": "Blackhorse Road => Black Horse",
      "length": 0.001370454088983439,
      "speed": {
        "0:00": 30
      },
      "startid": 487169369,
      "endid": 487169349
    },
    {
      "id": 474,
      "name": "Black Horse => Black Horse",
      "length": 0.00041012888217990085,
      "speed": {
        "0:00": 30
      },
      "startid": 487169349,
      "endid": 487169388
    },
    {
      "id": 475,
      "name": "Black Horse => Bedworth Rd / Oban Rd",
      "length": 0.007028217129543348,
      "speed": {
        "0:00": 30
      },
      "startid": 487169388,
      "endid": 370818876
    },
    {
      "id": 476,
      "name": "Bedworth Rd / Oban Rd => Bedworth Rd / Ibstock Rd",
      "length": 0.002246773317446427,
      "speed": {
        "0:00": 30
      },
      "startid": 370818876,
      "endid": 370818878
    },
    {
      "id": 477,
      "name": "Bedworth Rd / Ibstock Rd => Bedworth Rd / Ibstock Rd",
      "length": 0.00033837257572197685,
      "speed": {
        "0:00": 30
      },
      "startid": 370818878,
      "endid": 370818879
    },
    {
      "id": 478,
      "name": "Bedworth Rd / Ibstock Rd => Bedworth Rd / Oban Rd",
      "length": 0.0033466396594159123,
      "speed": {
        "0:00": 30
      },
      "startid": 370818879,
      "endid": 370818877
    },
    {
      "id": 479,
      "name": "Bedworth Rd / Oban Rd => Longford Rd / Longford Square",
      "length": 0.0026911415013017555,
      "speed": {
        "0:00": 30
      },
      "startid": 370818877,
      "endid": 370818874
    },
    {
      "id": 480,
      "name": "Longford Rd / Longford Square => Longford Rd / Longford Square",
      "length": 0.0003155618639778003,
      "speed": {
        "0:00": 30
      },
      "startid": 370818874,
      "endid": 370818873
    },
    {
      "id": 481,
      "name": "Longford Rd / Longford Square => Longford Rd / Vinecote Rd",
      "length": 0.0027949190256651227,
      "speed": {
        "0:00": 30
      },
      "startid": 370818873,
      "endid": 370818872
    },
    {
      "id": 482,
      "name": "Longford Rd / Vinecote Rd => Longford Rd / Oakmoor Rd",
      "length": 0.0011475531403839034,
      "speed": {
        "0:00": 30
      },
      "startid": 370818872,
      "endid": 370818871
    },
    {
      "id": 483,
      "name": "Longford Rd / Oakmoor Rd => Longford Rd / Longford Bridge",
      "length": 0.0032066862163273296,
      "speed": {
        "0:00": 30
      },
      "startid": 370818871,
      "endid": 370819748
    },
    {
      "id": 484,
      "name": "Longford Rd / Longford Bridge => Longford Rd / Windmill Rd",
      "length": 0.0014970952808711533,
      "speed": {
        "0:00": 30
      },
      "startid": 370819748,
      "endid": 370819732
    },
    {
      "id": 485,
      "name": "Longford Rd / Windmill Rd => Longford Rd / Dovedale Avenue",
      "length": 0.0010496597639259562,
      "speed": {
        "0:00": 30
      },
      "startid": 370819732,
      "endid": 370818870
    },
    {
      "id": 486,
      "name": "Longford Rd / Dovedale Avenue => AG",
      "length": 0.0021072323103976083,
      "speed": {
        "0:00": 30
      },
      "startid": 370818870,
      "endid": 370818869
    },
    {
      "id": 487,
      "name": "AG => AF",
      "length": 0.0008466729474816734,
      "speed": {
        "0:00": 30
      },
      "startid": 370818869,
      "endid": 370818867
    },
    {
      "id": 488,
      "name": "AF => Foleshill Rd / The Wheatsheaf",
      "length": 0.001456813598235208,
      "speed": {
        "0:00": 30
      },
      "startid": 370818867,
      "endid": 370818864
    },
    {
      "id": 489,
      "name": "Foleshill Rd / The Wheatsheaf => Foleshill Rd / The Wheatsheaf",
      "length": 0.00031738230889481126,
      "speed": {
        "0:00": 30
      },
      "startid": 370818864,
      "endid": 370818865
    },
    {
      "id": 490,
      "name": "Foleshill Rd / The Wheatsheaf => Foleshill Rd / Old Church Rd",
      "length": 0.0031598401984935013,
      "speed": {
        "0:00": 30
      },
      "startid": 370818865,
      "endid": 370818863
    },
    {
      "id": 491,
      "name": "Foleshill Rd / Old Church Rd => Foleshill Rd / Old Church Rd",
      "length": 0.0003347000000000211,
      "speed": {
        "0:00": 30
      },
      "startid": 370818863,
      "endid": 370818862
    },
    {
      "id": 492,
      "name": "Foleshill Rd / Old Church Rd => Foleshill Rd / Phoenix Way",
      "length": 0.0035533042270538776,
      "speed": {
        "0:00": 30
      },
      "startid": 370818862,
      "endid": 370818832
    },
    {
      "id": 493,
      "name": "Foleshill Rd / Phoenix Way => Foleshill Rd / Phoenix Way",
      "length": 0.0002803520108717694,
      "speed": {
        "0:00": 30
      },
      "startid": 370818832,
      "endid": 370818834
    },
    {
      "id": 494,
      "name": "Foleshill Rd / Phoenix Way => Foleshill Rd / Cross Rd",
      "length": 0.0016837137820924367,
      "speed": {
        "0:00": 30
      },
      "startid": 370818834,
      "endid": 370818830
    },
    {
      "id": 495,
      "name": "Foleshill Rd / Cross Rd => Foleshill Rd / Cross Rd",
      "length": 0.0004945206264681952,
      "speed": {
        "0:00": 30
      },
      "startid": 370818830,
      "endid": 370818831
    },
    {
      "id": 496,
      "name": "Foleshill Rd / Cross Rd => Foleshill Rd / Family Centre",
      "length": 0.0026930447174148245,
      "speed": {
        "0:00": 30
      },
      "startid": 370818831,
      "endid": 370819702
    },
    {
      "id": 497,
      "name": "Foleshill Rd / Family Centre => Foleshill Rd / Family Centre",
      "length": 0.00016455625178377943,
      "speed": {
        "0:00": 30
      },
      "startid": 370819702,
      "endid": 370819703
    },
    {
      "id": 498,
      "name": "Foleshill Rd / Family Centre => Foleshill Rd / Station St",
      "length": 0.0014088894953136236,
      "speed": {
        "0:00": 30
      },
      "startid": 370819703,
      "endid": 370818829
    },
    {
      "id": 499,
      "name": "Foleshill Rd / Station St => Foleshill Rd / Station St",
      "length": 0.0013386575364890566,
      "speed": {
        "0:00": 30
      },
      "startid": 370818829,
      "endid": 370818827
    },
    {
      "id": 500,
      "name": "Foleshill Rd / Station St => Foleshill Rd / Broad St",
      "length": 0.0028052413532526385,
      "speed": {
        "0:00": 30
      },
      "startid": 370818827,
      "endid": 370818825
    },
    {
      "id": 501,
      "name": "Foleshill Rd / Broad St => Foleshill Rd / Broad St",
      "length": 0.00038016818646532426,
      "speed": {
        "0:00": 30
      },
      "startid": 370818825,
      "endid": 370818826
    },
    {
      "id": 502,
      "name": "Foleshill Rd / Broad St => Foleshill Rd / Courtaulds Way",
      "length": 0.004239609710810101,
      "speed": {
        "0:00": 30
      },
      "startid": 370818826,
      "endid": 370818780
    },
    {
      "id": 503,
      "name": "Foleshill Rd / Courtaulds Way => Foleshill Rd / Courtaulds Way",
      "length": 0.00035180778843009035,
      "speed": {
        "0:00": 30
      },
      "startid": 370818780,
      "endid": 370818784
    },
    {
      "id": 504,
      "name": "Foleshill Rd / Courtaulds Way => Foleshill Rd / Cashs Lane",
      "length": 0.004273169018420262,
      "speed": {
        "0:00": 30
      },
      "startid": 370818784,
      "endid": 370818776
    },
    {
      "id": 505,
      "name": "Foleshill Rd / Cashs Lane => Foleshill Rd / Cashs Lane",
      "length": 0.00022125555360341274,
      "speed": {
        "0:00": 30
      },
      "startid": 370818776,
      "endid": 370818774
    },
    {
      "id": 506,
      "name": "Foleshill Rd / Cashs Lane => Foleshill Rd / Eagle St",
      "length": 0.0011237341055589636,
      "speed": {
        "0:00": 30
      },
      "startid": 370818774,
      "endid": 370818765
    },
    {
      "id": 507,
      "name": "Foleshill Rd / Eagle St => Foleshill Rd / Eagle St",
      "length": 0.001522061907418469,
      "speed": {
        "0:00": 30
      },
      "startid": 370818765,
      "endid": 370818766
    },
    {
      "id": 508,
      "name": "Foleshill Rd / Eagle St => Foleshill Rd / City Engineers",
      "length": 0.0027907170565999295,
      "speed": {
        "0:00": 30
      },
      "startid": 370818766,
      "endid": 370818762
    },
    {
      "id": 509,
      "name": "Foleshill Rd / City Engineers => Foleshill Rd / City Engineers",
      "length": 0.00022393115013730707,
      "speed": {
        "0:00": 30
      },
      "startid": 370818762,
      "endid": 370818764
    },
    {
      "id": 510,
      "name": "Foleshill Rd / City Engineers => Foleshill Rd / Leicester Row",
      "length": 0.0016005044017478598,
      "speed": {
        "0:00": 30
      },
      "startid": 370818764,
      "endid": 370818761
    },
    {
      "id": 511,
      "name": "Foleshill Rd / Leicester Row => Foleshill Rd / Leicester Row",
      "length": 0.00040428367515873303,
      "speed": {
        "0:00": 30
      },
      "startid": 370818761,
      "endid": 370818758
    },
    {
      "id": 512,
      "name": "Foleshill Rd / Leicester Row => BS1",
      "length": 0.003915537353925627,
      "speed": {
        "0:00": 30
      },
      "startid": 370818758,
      "endid": 370817728
    },
    {
      "id": 513,
      "name": "BS1 => BS2",
      "length": 0.0006854744707142306,
      "speed": {
        "0:00": 30
      },
      "startid": 370817728,
      "endid": 370817727
    },
    {
      "id": 514,
      "name": "BS2 => TS4",
      "length": 0.002139564165897073,
      "speed": {
        "0:00": 30
      },
      "startid": 370817727,
      "endid": 370817662
    },
    {
      "id": 515,
      "name": "Mitchell Avenue / Westwood School => Westwood Way / Business Park",
      "length": 0.004981516062404504,
      "speed": {
        "0:00": 30
      },
      "startid": 370819688,
      "endid": 370817953
    },
    {
      "id": 516,
      "name": "Westwood Way / Business Park => Westwood Way / Business Park",
      "length": 0.00020864326013591357,
      "speed": {
        "0:00": 30
      },
      "startid": 370817953,
      "endid": 370817954
    },
    {
      "id": 517,
      "name": "Westwood Way / Business Park => Westwood Way / Longwood Close",
      "length": 0.004476377174680815,
      "speed": {
        "0:00": 30
      },
      "startid": 370817954,
      "endid": 370817955
    },
    {
      "id": 518,
      "name": "Westwood Way / Longwood Close => Charter Ave / Mitchell Ave",
      "length": 0.010938311718451948,
      "speed": {
        "0:00": 30
      },
      "startid": 370817955,
      "endid": 370817984
    },
    {
      "id": 519,
      "name": "Charter Ave / Mitchell Ave => Charter Ave / John Rous Ave",
      "length": 0.0029593990014863333,
      "speed": {
        "0:00": 30
      },
      "startid": 370817984,
      "endid": 370817981
    },
    {
      "id": 520,
      "name": "Charter Ave / John Rous Ave => Fletchamstead Highway / Torrington Avenue",
      "length": 0.010974969308838838,
      "speed": {
        "0:00": 30
      },
      "startid": 370817981,
      "endid": 370818204
    },
    {
      "id": 521,
      "name": "Fletchamstead Highway / Torrington Avenue => Herald Avenue / Vanguard Avenue",
      "length": 0.0040187881519201775,
      "speed": {
        "0:00": 30
      },
      "startid": 370818204,
      "endid": 370817405
    },
    {
      "id": 522,
      "name": "Herald Avenue / Vanguard Avenue => Herald Avenue / Vanguard Avenue",
      "length": 0.0006769428336276444,
      "speed": {
        "0:00": 30
      },
      "startid": 370817405,
      "endid": 370817403
    },
    {
      "id": 523,
      "name": "Herald Avenue / Vanguard Avenue => Herald Avenue / Business Park",
      "length": 0.0039010029902577913,
      "speed": {
        "0:00": 30
      },
      "startid": 370817403,
      "endid": 370817713
    },
    {
      "id": 524,
      "name": "Herald Avenue / Business Park => Herald Avenue / Business Park",
      "length": 0.00012615902663344223,
      "speed": {
        "0:00": 30
      },
      "startid": 370817713,
      "endid": 370817716
    },
    {
      "id": 525,
      "name": "Herald Avenue / Business Park => Tile Hill Lane / Brd Lane",
      "length": 0.003972316140490556,
      "speed": {
        "0:00": 30
      },
      "startid": 370817716,
      "endid": 370818159
    },
    {
      "id": 526,
      "name": "Tile Hill Lane / Brd Lane => Tile Hill Lane / Broad Lane",
      "length": 0.00033008995743662075,
      "speed": {
        "0:00": 30
      },
      "startid": 370818159,
      "endid": 370818157
    },
    {
      "id": 527,
      "name": "Tile Hill Lane / Broad Lane => Tile Hill Lane / Hearsall Common",
      "length": 0.005069562744458173,
      "speed": {
        "0:00": 30
      },
      "startid": 370818157,
      "endid": 370818853
    },
    {
      "id": 528,
      "name": "Tile Hill Lane / Hearsall Common => Tile Hill Lane / Hearsall Common",
      "length": 0.0010889620838209612,
      "speed": {
        "0:00": 30
      },
      "startid": 370818853,
      "endid": 370818854
    },
    {
      "id": 529,
      "name": "Tile Hill Lane / Hearsall Common => Hearsall Lane / Queensland Avenue",
      "length": 0.008118906370933264,
      "speed": {
        "0:00": 30
      },
      "startid": 370818854,
      "endid": 370819672
    },
    {
      "id": 530,
      "name": "Hearsall Lane / Queensland Avenue => Hearsall Lane / Farman Rd",
      "length": 0.002659731702637258,
      "speed": {
        "0:00": 30
      },
      "startid": 370819672,
      "endid": 370818036
    },
    {
      "id": 531,
      "name": "Hearsall Lane / Farman Rd => Hearsall Lane / Farman Rd",
      "length": 0.00020274560414026315,
      "speed": {
        "0:00": 30
      },
      "startid": 370818036,
      "endid": 370818039
    },
    {
      "id": 532,
      "name": "Hearsall Lane / Farman Rd => Spon End / The Arches",
      "length": 0.004305751897173334,
      "speed": {
        "0:00": 30
      },
      "startid": 370818039,
      "endid": 370818021
    },
    {
      "id": 533,
      "name": "Spon End / The Arches => Spon End / The Arches",
      "length": 0.00015506108474010497,
      "speed": {
        "0:00": 30
      },
      "startid": 370818021,
      "endid": 370818019
    },
    {
      "id": 534,
      "name": "Spon End / The Arches => Butts Radial Link / Albany Rd",
      "length": 0.004784828060651391,
      "speed": {
        "0:00": 30
      },
      "startid": 370818019,
      "endid": 370817814
    },
    {
      "id": 535,
      "name": "Butts Radial Link / Albany Rd => Butts Radial Link / Albany Rd",
      "length": 0.0017027777688234339,
      "speed": {
        "0:00": 30
      },
      "startid": 370817814,
      "endid": 370817816
    },
    {
      "id": 536,
      "name": "Butts Radial Link / Albany Rd => CR4",
      "length": 0.004735637618103989,
      "speed": {
        "0:00": 30
      },
      "startid": 370817816,
      "endid": 370817813
    },
    {
      "id": 537,
      "name": "CR4 => CS1",
      "length": 0.0037459906153076926,
      "speed": {
        "0:00": 30
      },
      "startid": 370817813,
      "endid": 370817698
    },
    {
      "id": 538,
      "name": "CS1 => Charter Ave / Mitchell Ave",
      "length": 0.05706596816334411,
      "speed": {
        "0:00": 30
      },
      "startid": 370817698,
      "endid": 370817985
    },
    {
      "id": 539,
      "name": "Charter Ave / Mitchell Ave => BS3",
      "length": 0.0599918679252429,
      "speed": {
        "0:00": 30
      },
      "startid": 370817985,
      "endid": 370817695
    },
    {
      "id": 540,
      "name": "BS3 => CS4",
      "length": 0.003071773762827612,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 370817702
    },
    {
      "id": 541,
      "name": "CS4 => VR3",
      "length": 0.002391225267514317,
      "speed": {
        "0:00": 30
      },
      "startid": 370817702,
      "endid": 370817718
    },
    {
      "id": 542,
      "name": "VR3 => BS7",
      "length": 0.005316306727418198,
      "speed": {
        "0:00": 30
      },
      "startid": 370817718,
      "endid": 7620250858
    },
    {
      "id": 543,
      "name": "BS7 => John Rous Ave / Wendiburgh St",
      "length": 0.05630698470394175,
      "speed": {
        "0:00": 30
      },
      "startid": 7620250858,
      "endid": 370817980
    },
    {
      "id": 544,
      "name": "John Rous Ave / Wendiburgh St => John Rous Ave / Wendiburgh St",
      "length": 0.00015920050251101692,
      "speed": {
        "0:00": 30
      },
      "startid": 370817980,
      "endid": 370817979
    },
    {
      "id": 545,
      "name": "John Rous Ave / Wendiburgh St => Templars Fields / John Ross Avenue",
      "length": 0.0018530347999994171,
      "speed": {
        "0:00": 30
      },
      "startid": 370817979,
      "endid": 370819687
    },
    {
      "id": 546,
      "name": "Templars Fields / John Ross Avenue => Prior Deram Walk / John Ross Ave",
      "length": 0.0005438519743467372,
      "speed": {
        "0:00": 30
      },
      "startid": 370819687,
      "endid": 370819682
    },
    {
      "id": 547,
      "name": "Prior Deram Walk / John Ross Ave => Sheriff Ave / Prior Deram Walk",
      "length": 0.0032020073781933484,
      "speed": {
        "0:00": 30
      },
      "startid": 370819682,
      "endid": 370819155
    },
    {
      "id": 548,
      "name": "Sheriff Ave / Prior Deram Walk => Prior Deram Walk / Fletchamstead Highway",
      "length": 0.005011514505615828,
      "speed": {
        "0:00": 30
      },
      "startid": 370819155,
      "endid": 4815876524
    },
    {
      "id": 549,
      "name": "Prior Deram Walk / Fletchamstead Highway => Prior Deram Walk / Fletchamstead Highway",
      "length": 0.00010448564494865598,
      "speed": {
        "0:00": 30
      },
      "startid": 4815876524,
      "endid": 4815876523
    },
    {
      "id": 550,
      "name": "Prior Deram Walk / Fletchamstead Highway => Charter Ave / Ten Shilling Wood",
      "length": 0.017247467234930803,
      "speed": {
        "0:00": 30
      },
      "startid": 4815876523,
      "endid": 370817987
    },
    {
      "id": 551,
      "name": "Charter Ave / Ten Shilling Wood => Charter Ave / Ten Shilling Wood",
      "length": 0.0008599757264015652,
      "speed": {
        "0:00": 30
      },
      "startid": 370817987,
      "endid": 370817986
    },
    {
      "id": 552,
      "name": "Charter Ave / Ten Shilling Wood => Charter Ave / Wolfe Rd",
      "length": 0.0024701140398776956,
      "speed": {
        "0:00": 30
      },
      "startid": 370817986,
      "endid": 370817991
    },
    {
      "id": 553,
      "name": "Charter Ave / Wolfe Rd => Charter Ave / Wolfe Rd",
      "length": 0.00106623742665507,
      "speed": {
        "0:00": 30
      },
      "startid": 370817991,
      "endid": 370817990
    },
    {
      "id": 554,
      "name": "Charter Ave / Wolfe Rd => Charter Ave / Marler Rd",
      "length": 0.002026663484646584,
      "speed": {
        "0:00": 30
      },
      "startid": 370817990,
      "endid": 370817996
    },
    {
      "id": 555,
      "name": "Charter Ave / Marler Rd => Charter Ave / Marler Rd",
      "length": 0.0005352118552501463,
      "speed": {
        "0:00": 30
      },
      "startid": 370817996,
      "endid": 370817994
    },
    {
      "id": 556,
      "name": "Charter Ave / Marler Rd => Charter Ave / Warren Green",
      "length": 0.0021186995185726062,
      "speed": {
        "0:00": 30
      },
      "startid": 370817994,
      "endid": 370817999
    },
    {
      "id": 557,
      "name": "Charter Ave / Warren Green => Charter Ave / Warren Green",
      "length": 0.0006786605115951983,
      "speed": {
        "0:00": 30
      },
      "startid": 370817999,
      "endid": 370817997
    },
    {
      "id": 558,
      "name": "Charter Ave / Warren Green => Charter Ave / Bradney Green",
      "length": 0.0032953990122594136,
      "speed": {
        "0:00": 30
      },
      "startid": 370817997,
      "endid": 370818000
    },
    {
      "id": 559,
      "name": "Charter Ave / Bradney Green => Charter Ave / Bradney Green",
      "length": 0.0007407507813021757,
      "speed": {
        "0:00": 30
      },
      "startid": 370818000,
      "endid": 370818003
    },
    {
      "id": 560,
      "name": "Charter Ave / Bradney Green => Charter Ave / Marina Close",
      "length": 0.00425260104524283,
      "speed": {
        "0:00": 30
      },
      "startid": 370818003,
      "endid": 370818006
    },
    {
      "id": 561,
      "name": "Charter Ave / Marina Close => Charter Ave / Marina Close",
      "length": 0.0005919281206352491,
      "speed": {
        "0:00": 30
      },
      "startid": 370818006,
      "endid": 370818005
    },
    {
      "id": 562,
      "name": "Charter Ave / Marina Close => Charter Ave / Dalmeny Rd",
      "length": 0.005004857269692999,
      "speed": {
        "0:00": 30
      },
      "startid": 370818005,
      "endid": 370818017
    },
    {
      "id": 563,
      "name": "Charter Ave / Dalmeny Rd => Charter Ave / Dalmeny Rd",
      "length": 0.0014327701281086536,
      "speed": {
        "0:00": 30
      },
      "startid": 370818017,
      "endid": 370818016
    },
    {
      "id": 564,
      "name": "Charter Ave / Dalmeny Rd => Cromwell Lane / Tile Hill Rail Station",
      "length": 0.0010329564608424775,
      "speed": {
        "0:00": 30
      },
      "startid": 370818016,
      "endid": 370818007
    },
    {
      "id": 565,
      "name": "Cromwell Lane / Tile Hill Rail Station => Cromwell Lane / Tile Hill Rail Station",
      "length": 0.00012686378521843434,
      "speed": {
        "0:00": 30
      },
      "startid": 370818007,
      "endid": 370818008
    },
    {
      "id": 566,
      "name": "Cromwell Lane / Tile Hill Rail Station => Torrington Ave / Station Avenue",
      "length": 0.004709245040347451,
      "speed": {
        "0:00": 30
      },
      "startid": 370818008,
      "endid": 370818256
    },
    {
      "id": 567,
      "name": "Torrington Ave / Station Avenue => Station Ave / Torrington Ave",
      "length": 0.0007348293543436731,
      "speed": {
        "0:00": 30
      },
      "startid": 370818256,
      "endid": 4316311353
    },
    {
      "id": 568,
      "name": "Station Ave / Torrington Ave => U",
      "length": 0.089827389177244,
      "speed": {
        "0:00": 30
      },
      "startid": 4316311353,
      "endid": 370817754
    },
    {
      "id": 569,
      "name": "U => Hearsall Common / Earlsdon Ave North",
      "length": 0.030172622940174965,
      "speed": {
        "0:00": 30
      },
      "startid": 370817754,
      "endid": 370818127
    },
    {
      "id": 570,
      "name": "Poole Rd / Banks Road => Poole Rd / Banks Road",
      "length": 0.0005891697633112058,
      "speed": {
        "0:00": 30
      },
      "startid": 370819545,
      "endid": 370819547
    },
    {
      "id": 571,
      "name": "Poole Rd / Banks Road => Christchurch Rd / Scots Lane",
      "length": 0.005403079679220014,
      "speed": {
        "0:00": 30
      },
      "startid": 370819547,
      "endid": 370819524
    },
    {
      "id": 572,
      "name": "Christchurch Rd / Scots Lane => Scots Lane / Christchurch Rd",
      "length": 0.00037228006929701545,
      "speed": {
        "0:00": 30
      },
      "startid": 370819524,
      "endid": 370819170
    },
    {
      "id": 573,
      "name": "Scots Lane / Christchurch Rd => Duncroft Avenue / Scot Lane",
      "length": 0.005780215048773004,
      "speed": {
        "0:00": 30
      },
      "startid": 370819170,
      "endid": 370819783
    },
    {
      "id": 574,
      "name": "Duncroft Avenue / Scot Lane => Duncroft Avenue / Norman Place Rd",
      "length": 0.004387249256652828,
      "speed": {
        "0:00": 30
      },
      "startid": 370819783,
      "endid": 370819549
    },
    {
      "id": 575,
      "name": "Duncroft Avenue / Norman Place Rd => Duncroft Avenue / Norman Place Rd",
      "length": 0.00007853712498450453,
      "speed": {
        "0:00": 30
      },
      "startid": 370819549,
      "endid": 370819550
    },
    {
      "id": 576,
      "name": "Duncroft Avenue / Norman Place Rd => Birchfield Rd / Eversleigh Rd",
      "length": 0.001087368552977933,
      "speed": {
        "0:00": 30
      },
      "startid": 370819550,
      "endid": 370819553
    },
    {
      "id": 577,
      "name": "Birchfield Rd / Eversleigh Rd => Norman Place Rd / Brownshill Green Rd",
      "length": 0.0022706869313053038,
      "speed": {
        "0:00": 30
      },
      "startid": 370819553,
      "endid": 370818811
    },
    {
      "id": 578,
      "name": "Norman Place Rd / Brownshill Green Rd => Brownshill Green Rd / Norman Place Rd",
      "length": 0.00176621131804798,
      "speed": {
        "0:00": 30
      },
      "startid": 370818811,
      "endid": 370819521
    },
    {
      "id": 579,
      "name": "Brownshill Green Rd / Norman Place Rd => Overslade Cres / Eversleigh Road",
      "length": 0.005593968813821559,
      "speed": {
        "0:00": 30
      },
      "startid": 370819521,
      "endid": 370819782
    },
    {
      "id": 580,
      "name": "Overslade Cres / Eversleigh Road => 860387245",
      "length": 0.002129814775983255,
      "speed": {
        "0:00": 30
      },
      "startid": 370819782,
      "endid": 860387245
    },
    {
      "id": 581,
      "name": "860387245 => Birchfield Rd / Brownshill Green Rd",
      "length": 0.0037987804951063737,
      "speed": {
        "0:00": 30
      },
      "startid": 860387245,
      "endid": 370819784
    },
    {
      "id": 582,
      "name": "Birchfield Rd / Brownshill Green Rd => Overslade Cres / Mapleton Road",
      "length": 0.0019083476858264693,
      "speed": {
        "0:00": 30
      },
      "startid": 370819784,
      "endid": 370819522
    },
    {
      "id": 583,
      "name": "Overslade Cres / Mapleton Road => Moseley Ave / Crampers Field",
      "length": 0.01925687558276047,
      "speed": {
        "0:00": 30
      },
      "startid": 370819522,
      "endid": 370819386
    },
    {
      "id": 584,
      "name": "Moseley Ave / Crampers Field => Moseley Ave / Crampers Field",
      "length": 0.0005126478811043996,
      "speed": {
        "0:00": 30
      },
      "startid": 370819386,
      "endid": 370819384
    },
    {
      "id": 585,
      "name": "Moseley Ave / Crampers Field => Moseley Ave / Moseley Junior School",
      "length": 0.0018987457044079773,
      "speed": {
        "0:00": 30
      },
      "startid": 370819384,
      "endid": 370819392
    },
    {
      "id": 586,
      "name": "Moseley Ave / Moseley Junior School => Moseley Ave / Lammas Rd",
      "length": 0.004619589506656326,
      "speed": {
        "0:00": 30
      },
      "startid": 370819392,
      "endid": 370819388
    },
    {
      "id": 587,
      "name": "Moseley Ave / Lammas Rd => Holyhead Rd / Alvis Retail Park",
      "length": 0.0030237352794161435,
      "speed": {
        "0:00": 30
      },
      "startid": 370819388,
      "endid": 370819361
    },
    {
      "id": 588,
      "name": "Holyhead Rd / Alvis Retail Park => Holyhead Rd / Alvis Retail Park",
      "length": 0.0002442421953716176,
      "speed": {
        "0:00": 30
      },
      "startid": 370819361,
      "endid": 370819363
    },
    {
      "id": 589,
      "name": "Holyhead Rd / Alvis Retail Park => Holyhead Rd / Meriden St",
      "length": 0.006018893655815038,
      "speed": {
        "0:00": 30
      },
      "startid": 370819363,
      "endid": 370819359
    },
    {
      "id": 590,
      "name": "Holyhead Rd / Meriden St => Holyhead Rd / Meriden St",
      "length": 0.0008530438792932072,
      "speed": {
        "0:00": 30
      },
      "startid": 370819359,
      "endid": 370819360
    },
    {
      "id": 591,
      "name": "Holyhead Rd / Meriden St => Holyhead Rd / Ringway",
      "length": 0.0025533747413974952,
      "speed": {
        "0:00": 30
      },
      "startid": 370819360,
      "endid": 370819355
    },
    {
      "id": 592,
      "name": "Holyhead Rd / Ringway => Holyhead Rd / Ringway",
      "length": 0.0001523425416673504,
      "speed": {
        "0:00": 30
      },
      "startid": 370819355,
      "endid": 370819357
    },
    {
      "id": 593,
      "name": "Holyhead Rd / Ringway => UL3",
      "length": 0.0059757926938607455,
      "speed": {
        "0:00": 30
      },
      "startid": 370819357,
      "endid": 370817723
    },
    {
      "id": 594,
      "name": "UL3 => Scots Lane / Duncroft Avenue",
      "length": 0.024457412960493228,
      "speed": {
        "0:00": 30
      },
      "startid": 370817723,
      "endid": 370819500
    },
    {
      "id": 595,
      "name": "Scots Lane / Duncroft Avenue => Holloway Field / Thistley Field North",
      "length": 0.0021931768487744798,
      "speed": {
        "0:00": 30
      },
      "startid": 370819500,
      "endid": 370819478
    },
    {
      "id": 596,
      "name": "Holloway Field / Thistley Field North => Holloway Field / Haywards Green",
      "length": 0.001346566515254444,
      "speed": {
        "0:00": 30
      },
      "startid": 370819478,
      "endid": 370819449
    },
    {
      "id": 597,
      "name": "Holloway Field / Haywards Green => Holloway Field / Haywards Green",
      "length": 0.000596924986911296,
      "speed": {
        "0:00": 30
      },
      "startid": 370819449,
      "endid": 370819447
    },
    {
      "id": 598,
      "name": "Holloway Field / Haywards Green => Holloway Field / Scots Lane",
      "length": 0.002387826226926472,
      "speed": {
        "0:00": 30
      },
      "startid": 370819447,
      "endid": 370819559
    },
    {
      "id": 599,
      "name": "Holloway Field / Scots Lane => Holloway Field / Scots Lane",
      "length": 0.0005575004394617002,
      "speed": {
        "0:00": 30
      },
      "startid": 370819559,
      "endid": 370819562
    },
    {
      "id": 600,
      "name": "Holloway Field / Scots Lane => G",
      "length": 0.030148476800164258,
      "speed": {
        "0:00": 30
      },
      "startid": 370819562,
      "endid": 370817740
    },
    {
      "id": 601,
      "name": "G => BS3",
      "length": 0.005308715619620055,
      "speed": {
        "0:00": 30
      },
      "startid": 370817740,
      "endid": 370817695
    },
    {
      "id": 602,
      "name": "BS3 => UL4",
      "length": 0.002031303665137189,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 370817719
    },
    {
      "id": 603,
      "name": "UL4 => BS5",
      "length": 0.0029723583851876648,
      "speed": {
        "0:00": 30
      },
      "startid": 370817719,
      "endid": 370817666
    },
    {
      "id": 604,
      "name": "Lythalls Lane / Bartlett Close => Lythalls Lane / Bartlett Close",
      "length": 0.0013430125315871308,
      "speed": {
        "0:00": 30
      },
      "startid": 370819572,
      "endid": 370819573
    },
    {
      "id": 605,
      "name": "Lythalls Lane / Bartlett Close => Lythalls Lane / Holbrooks Lane",
      "length": 0.009378751876982406,
      "speed": {
        "0:00": 30
      },
      "startid": 370819573,
      "endid": 370819580
    },
    {
      "id": 606,
      "name": "Lythalls Lane / Holbrooks Lane => Holbrook Lane / Lythalls Lane",
      "length": 0.0012410988075082987,
      "speed": {
        "0:00": 30
      },
      "startid": 370819580,
      "endid": 370818696
    },
    {
      "id": 607,
      "name": "Holbrook Lane / Lythalls Lane => Holbrook Lane / Sunningdale Avenue",
      "length": 0.00219085827930567,
      "speed": {
        "0:00": 30
      },
      "startid": 370818696,
      "endid": 370818694
    },
    {
      "id": 608,
      "name": "Holbrook Lane / Sunningdale Avenue => Holbrook Lane / Sunningdale Avenue",
      "length": 0.0005816921522595038,
      "speed": {
        "0:00": 30
      },
      "startid": 370818694,
      "endid": 370818695
    },
    {
      "id": 609,
      "name": "Holbrook Lane / Sunningdale Avenue => Holbrook Lane / Jackson Rd",
      "length": 0.0021165109874502672,
      "speed": {
        "0:00": 30
      },
      "startid": 370818695,
      "endid": 370818643
    },
    {
      "id": 610,
      "name": "Holbrook Lane / Jackson Rd => Holbrook Lane / Jackson Rd",
      "length": 0.00034841498245982087,
      "speed": {
        "0:00": 30
      },
      "startid": 370818643,
      "endid": 370818644
    },
    {
      "id": 611,
      "name": "Holbrook Lane / Jackson Rd => Holbrook Lane / Burnaby Rd",
      "length": 0.002138914960905445,
      "speed": {
        "0:00": 30
      },
      "startid": 370818644,
      "endid": 370818639
    },
    {
      "id": 612,
      "name": "Holbrook Lane / Burnaby Rd => Burnaby Rd / Holbrook Lane",
      "length": 0.001491348882724255,
      "speed": {
        "0:00": 30
      },
      "startid": 370818639,
      "endid": 370817733
    },
    {
      "id": 613,
      "name": "Burnaby Rd / Holbrook Lane => Burnaby Rd / Yelverton Rd",
      "length": 0.0019221106549832405,
      "speed": {
        "0:00": 30
      },
      "startid": 370817733,
      "endid": 370818732
    },
    {
      "id": 614,
      "name": "Burnaby Rd / Yelverton Rd => Burnaby Rd / Yelverton Rd",
      "length": 0.0004544431537595393,
      "speed": {
        "0:00": 30
      },
      "startid": 370818732,
      "endid": 370818731
    },
    {
      "id": 615,
      "name": "Burnaby Rd / Yelverton Rd => Burnaby Rd / Rollason Rd",
      "length": 0.0018422619683421634,
      "speed": {
        "0:00": 30
      },
      "startid": 370818731,
      "endid": 370819584
    },
    {
      "id": 616,
      "name": "Burnaby Rd / Rollason Rd => Burnaby Rd / Rollason Rd",
      "length": 0.0015071672833497306,
      "speed": {
        "0:00": 30
      },
      "startid": 370819584,
      "endid": 370819583
    },
    {
      "id": 617,
      "name": "Burnaby Rd / Rollason Rd => Burnaby Rd / Pilot Hotel",
      "length": 0.0016565227828196697,
      "speed": {
        "0:00": 30
      },
      "startid": 370819583,
      "endid": 370818727
    },
    {
      "id": 618,
      "name": "Burnaby Rd / Pilot Hotel => Catesby Rd / Rollason Rd",
      "length": 0.001839239516756027,
      "speed": {
        "0:00": 30
      },
      "startid": 370818727,
      "endid": 370818628
    },
    {
      "id": 619,
      "name": "Catesby Rd / Rollason Rd => Catesby Rd / Catesby Rd",
      "length": 0.0011654908837110077,
      "speed": {
        "0:00": 30
      },
      "startid": 370818628,
      "endid": 370818722
    },
    {
      "id": 620,
      "name": "Catesby Rd / Catesby Rd => Catesby Rd / Catesby Rd",
      "length": 0.00043126118535944427,
      "speed": {
        "0:00": 30
      },
      "startid": 370818722,
      "endid": 370818720
    },
    {
      "id": 621,
      "name": "Jubilee Cres / Catesby Rd => Jubilee Cres / Cheveral Avenue",
      "length": 0.0016222491115734576,
      "speed": {
        "0:00": 30
      },
      "startid": 370818625,
      "endid": 370818624
    },
    {
      "id": 622,
      "name": "Jubilee Cres / Cheveral Avenue => Links Rd / St Francis Church",
      "length": 0.0021809527757376333,
      "speed": {
        "0:00": 30
      },
      "startid": 370818624,
      "endid": 370819713
    },
    {
      "id": 623,
      "name": "Links Rd / St Francis Church => Links Rd / Sadler Rd",
      "length": 0.004004657298696484,
      "speed": {
        "0:00": 30
      },
      "startid": 370819713,
      "endid": 370818791
    },
    {
      "id": 624,
      "name": "Links Rd / Sadler Rd => Wallace Rd / Dickens Rd",
      "length": 0.0025944287270995778,
      "speed": {
        "0:00": 30
      },
      "startid": 370818791,
      "endid": 370818757
    },
    {
      "id": 625,
      "name": "Wallace Rd / Dickens Rd => Wallace Rd / Dickens Rd",
      "length": 0.0018292782948475788,
      "speed": {
        "0:00": 30
      },
      "startid": 370818757,
      "endid": 370818755
    },
    {
      "id": 626,
      "name": "Wallace Rd / Dickens Rd => Norman Place Rd / Keresley Rd",
      "length": 0.0031413157832349222,
      "speed": {
        "0:00": 30
      },
      "startid": 370818755,
      "endid": 370818793
    },
    {
      "id": 627,
      "name": "Norman Place Rd / Keresley Rd => Norman Place Rd / Keresley Rd",
      "length": 0.00018880871272323826,
      "speed": {
        "0:00": 30
      },
      "startid": 370818793,
      "endid": 370818792
    },
    {
      "id": 628,
      "name": "Norman Place Rd / Keresley Rd => Norman Place Rd / Brownshill Green Rd",
      "length": 0.0030675574599339046,
      "speed": {
        "0:00": 30
      },
      "startid": 370818792,
      "endid": 370818810
    },
    {
      "id": 629,
      "name": "Norman Place Rd / Brownshill Green Rd => Norman Place Rd / Brownshill Green Rd",
      "length": 0.0005544783223886224,
      "speed": {
        "0:00": 30
      },
      "startid": 370818810,
      "endid": 370818811
    },
    {
      "id": 630,
      "name": "Norman Place Rd / Brownshill Green Rd => Norman Place Rd / Duncroft Avenue",
      "length": 0.003237172384967507,
      "speed": {
        "0:00": 30
      },
      "startid": 370818811,
      "endid": 370819467
    },
    {
      "id": 631,
      "name": "Norman Place Rd / Duncroft Avenue => Norman Place Rd / Duncroft Avenue",
      "length": 0.00026087391590686766,
      "speed": {
        "0:00": 30
      },
      "startid": 370819467,
      "endid": 370819465
    },
    {
      "id": 632,
      "name": "Norman Place Rd / Duncroft Avenue => Hollyfast Rd / Norman Place Rd",
      "length": 0.0020127073309346866,
      "speed": {
        "0:00": 30
      },
      "startid": 370819465,
      "endid": 370819464
    },
    {
      "id": 633,
      "name": "Hollyfast Rd / Norman Place Rd => Hollyfast Rd / Norman Place Rd",
      "length": 0.0002063635626770855,
      "speed": {
        "0:00": 30
      },
      "startid": 370819464,
      "endid": 370819463
    },
    {
      "id": 634,
      "name": "Hollyfast Rd / Norman Place Rd => Hollyfast Rd / Haynestone Rd",
      "length": 0.0017291453640445767,
      "speed": {
        "0:00": 30
      },
      "startid": 370819463,
      "endid": 370819461
    },
    {
      "id": 635,
      "name": "Hollyfast Rd / Haynestone Rd => Hollyfast Rd / Haynestone Rd",
      "length": 0.0007994517934222269,
      "speed": {
        "0:00": 30
      },
      "startid": 370819461,
      "endid": 370819459
    },
    {
      "id": 636,
      "name": "Hollyfast Rd / Haynestone Rd => Westhill Rd / Courtland Avenue",
      "length": 0.003698460740629859,
      "speed": {
        "0:00": 30
      },
      "startid": 370819459,
      "endid": 370819458
    },
    {
      "id": 637,
      "name": "Westhill Rd / Courtland Avenue => Westhill Rd / Courtland Avenue",
      "length": 0.0009471797717418264,
      "speed": {
        "0:00": 30
      },
      "startid": 370819458,
      "endid": 370819456
    },
    {
      "id": 638,
      "name": "Westhill Rd / Courtland Avenue => Barkers Butts Lane / Ashwood Avenue",
      "length": 0.003083724833705342,
      "speed": {
        "0:00": 30
      },
      "startid": 370819456,
      "endid": 370819409
    },
    {
      "id": 639,
      "name": "Barkers Butts Lane / Ashwood Avenue => Barkers Butts Lane / Ashwood Avenue",
      "length": 0.0005091038400957758,
      "speed": {
        "0:00": 30
      },
      "startid": 370819409,
      "endid": 370819411
    },
    {
      "id": 640,
      "name": "Barkers Butts Lane / Ashwood Avenue => Barkers Butts Lane / Browett Rd",
      "length": 0.002881217801556623,
      "speed": {
        "0:00": 30
      },
      "startid": 370819411,
      "endid": 370819408
    },
    {
      "id": 641,
      "name": "Barkers Butts Lane / Browett Rd => Barkers Butts Lane / Browett Rd",
      "length": 0.0009830320442389589,
      "speed": {
        "0:00": 30
      },
      "startid": 370819408,
      "endid": 370819407
    },
    {
      "id": 642,
      "name": "Barkers Butts Lane / Browett Rd => Barkers Butts Lane / Moseley Avenue",
      "length": 0.0017103410946331416,
      "speed": {
        "0:00": 30
      },
      "startid": 370819407,
      "endid": 370819382
    },
    {
      "id": 643,
      "name": "Barkers Butts Lane / Moseley Avenue => Barkers Butts Lane / Moseley Avenue",
      "length": 0.0013327606911980824,
      "speed": {
        "0:00": 30
      },
      "startid": 370819382,
      "endid": 370819379
    },
    {
      "id": 644,
      "name": "Barkers Butts Lane / Moseley Avenue => Barkers Butts Lane / Tomson Avenue",
      "length": 0.0033757849516812726,
      "speed": {
        "0:00": 30
      },
      "startid": 370819379,
      "endid": 370819376
    },
    {
      "id": 645,
      "name": "Barkers Butts Lane / Tomson Avenue => Barkers Butts Lane / Tomson Avenue",
      "length": 0.00030290600852587226,
      "speed": {
        "0:00": 30
      },
      "startid": 370819376,
      "endid": 370819377
    },
    {
      "id": 646,
      "name": "Barkers Butts Lane / Tomson Avenue => Coundon Rd / Middleborough Rd",
      "length": 0.004570993845978481,
      "speed": {
        "0:00": 30
      },
      "startid": 370819377,
      "endid": 370819372
    },
    {
      "id": 647,
      "name": "Coundon Rd / Middleborough Rd => Coundon Rd / Middleborough Rd",
      "length": 0.00015459912677892894,
      "speed": {
        "0:00": 30
      },
      "startid": 370819372,
      "endid": 370819375
    },
    {
      "id": 648,
      "name": "Coundon Rd / Middleborough Rd => Holyhead Rd / Ringway",
      "length": 0.0014236819342784428,
      "speed": {
        "0:00": 30
      },
      "startid": 370819375,
      "endid": 370819357
    },
    {
      "id": 649,
      "name": "Holyhead Rd / Ringway => Holyhead Rd / Ringway",
      "length": 0.0001523425416673504,
      "speed": {
        "0:00": 30
      },
      "startid": 370819357,
      "endid": 370819355
    },
    {
      "id": 650,
      "name": "Holyhead Rd / Ringway => UL3",
      "length": 0.005939280506088558,
      "speed": {
        "0:00": 30
      },
      "startid": 370819355,
      "endid": 370817723
    },
    {
      "id": 651,
      "name": "UL3 => G",
      "length": 0.007639622758356647,
      "speed": {
        "0:00": 30
      },
      "startid": 370817723,
      "endid": 370817740
    },
    {
      "id": 652,
      "name": "G => BS3",
      "length": 0.005308715619620055,
      "speed": {
        "0:00": 30
      },
      "startid": 370817740,
      "endid": 370817695
    },
    {
      "id": 653,
      "name": "BS3 => Lythalls Lane / Sunningdale Ave",
      "length": 0.032599032746540524,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 4815880415
    },
    {
      "id": 654,
      "name": "Lythalls Lane / Sunningdale Ave => Lythalls Lane / Sunningdale Ave",
      "length": 0.00016058617624200878,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880415,
      "endid": 4815880414
    },
    {
      "id": 655,
      "name": "Lythalls Lane / Sunningdale Ave => Lythalls Lane / Holbrooks Lane",
      "length": 0.003228648226426197,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880414,
      "endid": 370819581
    },
    {
      "id": 656,
      "name": "Lythalls Lane / Holbrooks Lane => UL4",
      "length": 0.032747128035909165,
      "speed": {
        "0:00": 30
      },
      "startid": 370819581,
      "endid": 370817719
    },
    {
      "id": 657,
      "name": "UL4 => Links Rd / Sadler Rd",
      "length": 0.023113959622056802,
      "speed": {
        "0:00": 30
      },
      "startid": 370817719,
      "endid": 4815880413
    },
    {
      "id": 658,
      "name": "Links Rd / Sadler Rd => Burnaby Rd / Pilot Hotel",
      "length": 0.00841787899651688,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880413,
      "endid": 370818728
    },
    {
      "id": 659,
      "name": "Burnaby Rd / Pilot Hotel => BS5",
      "length": 0.025599039894884,
      "speed": {
        "0:00": 30
      },
      "startid": 370818728,
      "endid": 370817666
    },
    {
      "id": 660,
      "name": "Browns Lane / Hawks Mill Lane => Browns Lane / Freshfield Close",
      "length": 0.003840214827321831,
      "speed": {
        "0:00": 30
      },
      "startid": 370819513,
      "endid": 370819512
    },
    {
      "id": 661,
      "name": "Browns Lane / Freshfield Close => Browns Lane / Freshfield Close",
      "length": 0.00046835419289525314,
      "speed": {
        "0:00": 30
      },
      "startid": 370819512,
      "endid": 370819511
    },
    {
      "id": 662,
      "name": "Browns Lane / Freshfield Close => Browns Lane / Carvell Close",
      "length": 0.0028817391450292862,
      "speed": {
        "0:00": 30
      },
      "startid": 370819511,
      "endid": 370819510
    },
    {
      "id": 663,
      "name": "Browns Lane / Carvell Close => Browns Lane / Carvell Close",
      "length": 0.000657908785470021,
      "speed": {
        "0:00": 30
      },
      "startid": 370819510,
      "endid": 370819508
    },
    {
      "id": 664,
      "name": "Browns Lane / Carvell Close => Browns Lane / Marystow Close",
      "length": 0.0034254773010502174,
      "speed": {
        "0:00": 30
      },
      "startid": 370819508,
      "endid": 370819507
    },
    {
      "id": 665,
      "name": "Browns Lane / Marystow Close => Browns Lane / Marystow Close",
      "length": 0.000430207856736039,
      "speed": {
        "0:00": 30
      },
      "startid": 370819507,
      "endid": 370819506
    },
    {
      "id": 666,
      "name": "Browns Lane / Marystow Close => The Windmill Hill / Butt Lane",
      "length": 0.005477019716050114,
      "speed": {
        "0:00": 30
      },
      "startid": 370819506,
      "endid": 370819499
    },
    {
      "id": 667,
      "name": "The Windmill Hill / Butt Lane => The Windmill Hill / Butt Lane",
      "length": 0.0001540079218738181,
      "speed": {
        "0:00": 30
      },
      "startid": 370819499,
      "endid": 370819498
    },
    {
      "id": 668,
      "name": "The Windmill Hill / Butt Lane => The Windmill Hill / Cameron Close",
      "length": 0.0042461767509170195,
      "speed": {
        "0:00": 30
      },
      "startid": 370819498,
      "endid": 370819495
    },
    {
      "id": 669,
      "name": "The Windmill Hill / Cameron Close => The Windmill Hill / Cameron Close",
      "length": 0.00037310293486017294,
      "speed": {
        "0:00": 30
      },
      "startid": 370819495,
      "endid": 370819497
    },
    {
      "id": 670,
      "name": "The Windmill Hill / Cameron Close => Birmingham Rd / Neale Avenue",
      "length": 0.0038383881057044017,
      "speed": {
        "0:00": 30
      },
      "startid": 370819497,
      "endid": 370819493
    },
    {
      "id": 671,
      "name": "Birmingham Rd / Neale Avenue => Birmingham Rd / Neale Avenue",
      "length": 0.0014933214590289524,
      "speed": {
        "0:00": 30
      },
      "startid": 370819493,
      "endid": 370819494
    },
    {
      "id": 672,
      "name": "Birmingham Rd / Neale Avenue => Birmingham Rd / Allesley Post Office",
      "length": 0.0015646175379312936,
      "speed": {
        "0:00": 30
      },
      "startid": 370819494,
      "endid": 370819489
    },
    {
      "id": 673,
      "name": "Birmingham Rd / Allesley Post Office => Birmingham Rd / Allesley Post Office",
      "length": 0.0008820798716671872,
      "speed": {
        "0:00": 30
      },
      "startid": 370819489,
      "endid": 370819490
    },
    {
      "id": 674,
      "name": "Birmingham Rd / Allesley Post Office => Birmingham Rd / Butchers Lane",
      "length": 0.002760424034455538,
      "speed": {
        "0:00": 30
      },
      "startid": 370819490,
      "endid": 370819486
    },
    {
      "id": 675,
      "name": "Birmingham Rd / Butchers Lane => Birmingham Rd / Butchers Lane",
      "length": 0.002666668160832974,
      "speed": {
        "0:00": 30
      },
      "startid": 370819486,
      "endid": 370819484
    },
    {
      "id": 676,
      "name": "Birmingham Rd / Butchers Lane => Birmingham Rd / Norton Grange",
      "length": 0.0032394266313661847,
      "speed": {
        "0:00": 30
      },
      "startid": 370819484,
      "endid": 370819481
    },
    {
      "id": 677,
      "name": "Birmingham Rd / Norton Grange => Birmingham Rd / Norton Grange",
      "length": 0.00018735042033075414,
      "speed": {
        "0:00": 30
      },
      "startid": 370819481,
      "endid": 370819482
    },
    {
      "id": 678,
      "name": "Birmingham Rd / Norton Grange => Holyhead Rd / Dulverton Avenue",
      "length": 0.005333658446132934,
      "speed": {
        "0:00": 30
      },
      "startid": 370819482,
      "endid": 370819479
    },
    {
      "id": 679,
      "name": "Holyhead Rd / Dulverton Avenue => Holyhead Rd / Dulverton Avenue",
      "length": 0.0004808124894384671,
      "speed": {
        "0:00": 30
      },
      "startid": 370819479,
      "endid": 370819480
    },
    {
      "id": 680,
      "name": "Holyhead Rd / Dulverton Avenue => Holyhead Rd / Grayswood Avenue",
      "length": 0.005298354314313946,
      "speed": {
        "0:00": 30
      },
      "startid": 370819480,
      "endid": 370819453
    },
    {
      "id": 681,
      "name": "Holyhead Rd / Grayswood Avenue => Holyhead Rd / Grayswood Avenue",
      "length": 0.0015367593988653307,
      "speed": {
        "0:00": 30
      },
      "startid": 370819453,
      "endid": 370819454
    },
    {
      "id": 682,
      "name": "Holyhead Rd / Grayswood Avenue => Holyhead Rd / Southbank Rd",
      "length": 0.0038324237148309693,
      "speed": {
        "0:00": 30
      },
      "startid": 370819454,
      "endid": 370819452
    },
    {
      "id": 683,
      "name": "Holyhead Rd / Southbank Rd => Holyhead Rd / Redesdale Avenue",
      "length": 0.0032341260334133653,
      "speed": {
        "0:00": 30
      },
      "startid": 370819452,
      "endid": 370819398
    },
    {
      "id": 684,
      "name": "Holyhead Rd / Redesdale Avenue => Holyhead Rd / Redesdale Avenue",
      "length": 0.0006598299856777957,
      "speed": {
        "0:00": 30
      },
      "startid": 370819398,
      "endid": 370819399
    },
    {
      "id": 685,
      "name": "Holyhead Rd / Redesdale Avenue => Holyhead Rd / Southbank Rd",
      "length": 0.005888709010471048,
      "speed": {
        "0:00": 30
      },
      "startid": 370819399,
      "endid": 370819450
    },
    {
      "id": 686,
      "name": "Holyhead Rd / Southbank Rd => Holyhead Rd / Moseley Avenue",
      "length": 0.010553858034386935,
      "speed": {
        "0:00": 30
      },
      "startid": 370819450,
      "endid": 370819397
    },
    {
      "id": 687,
      "name": "Holyhead Rd / Moseley Avenue => Holyhead Rd / Moseley Avenue",
      "length": 0.0008869628740820093,
      "speed": {
        "0:00": 30
      },
      "startid": 370819397,
      "endid": 370819395
    },
    {
      "id": 688,
      "name": "Holyhead Rd / Moseley Avenue => Holyhead Rd / Alvis Retail Park",
      "length": 0.005177505156925933,
      "speed": {
        "0:00": 30
      },
      "startid": 370819395,
      "endid": 370819361
    },
    {
      "id": 689,
      "name": "Holyhead Rd / Alvis Retail Park => Holyhead Rd / Alvis Retail Park",
      "length": 0.0002442421953716176,
      "speed": {
        "0:00": 30
      },
      "startid": 370819361,
      "endid": 370819363
    },
    {
      "id": 690,
      "name": "Holyhead Rd / Alvis Retail Park => Holyhead Rd / Meriden St",
      "length": 0.006018893655815038,
      "speed": {
        "0:00": 30
      },
      "startid": 370819363,
      "endid": 370819359
    },
    {
      "id": 691,
      "name": "Holyhead Rd / Meriden St => Holyhead Rd / Meriden St",
      "length": 0.0008530438792932072,
      "speed": {
        "0:00": 30
      },
      "startid": 370819359,
      "endid": 370819360
    },
    {
      "id": 692,
      "name": "Holyhead Rd / Meriden St => Holyhead Rd / Ringway",
      "length": 0.0025533747413974952,
      "speed": {
        "0:00": 30
      },
      "startid": 370819360,
      "endid": 370819355
    },
    {
      "id": 693,
      "name": "Holyhead Rd / Ringway => Holyhead Rd / Ringway",
      "length": 0.0001523425416673504,
      "speed": {
        "0:00": 30
      },
      "startid": 370819355,
      "endid": 370819357
    },
    {
      "id": 694,
      "name": "Holyhead Rd / Ringway => UL4",
      "length": 0.0062750762561103,
      "speed": {
        "0:00": 30
      },
      "startid": 370819357,
      "endid": 370817719
    },
    {
      "id": 695,
      "name": "UL4 => UL3",
      "length": 0.00031591698276652307,
      "speed": {
        "0:00": 30
      },
      "startid": 370817719,
      "endid": 370817723
    },
    {
      "id": 696,
      "name": "UL3 => BS3",
      "length": 0.0023332105005764514,
      "speed": {
        "0:00": 30
      },
      "startid": 370817723,
      "endid": 370817695
    },
    {
      "id": 697,
      "name": "BS3 => BS5",
      "length": 0.0010715734832442273,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 370817666
    },
    {
      "id": 698,
      "name": "BS5 => N",
      "length": 0.003582887140281883,
      "speed": {
        "0:00": 30
      },
      "startid": 370817666,
      "endid": 370817746
    },
    {
      "id": 699,
      "name": "N => G",
      "length": 0.0008477681994510137,
      "speed": {
        "0:00": 30
      },
      "startid": 370817746,
      "endid": 370817740
    },
    {
      "id": 700,
      "name": "G => FX1",
      "length": 0.0020614218127312416,
      "speed": {
        "0:00": 30
      },
      "startid": 370817740,
      "endid": 370817768
    },
    {
      "id": 701,
      "name": "FX1 => CU4",
      "length": 0.001230879766667563,
      "speed": {
        "0:00": 30
      },
      "startid": 370817768,
      "endid": 370819679
    },
    {
      "id": 702,
      "name": "CU4 => CU5",
      "length": 0.0005253710783815626,
      "speed": {
        "0:00": 30
      },
      "startid": 370819679,
      "endid": 370819676
    },
    {
      "id": 703,
      "name": "CU5 => CU1",
      "length": 0.0021117262535691986,
      "speed": {
        "0:00": 30
      },
      "startid": 370819676,
      "endid": 370817766
    },
    {
      "id": 704,
      "name": "CU1 => CU2",
      "length": 0.00010206831045847219,
      "speed": {
        "0:00": 30
      },
      "startid": 370817766,
      "endid": 370819680
    },
    {
      "id": 705,
      "name": "CU2 => Sky Blue Way / Walkway To Gosford St",
      "length": 0.006305733683720618,
      "speed": {
        "0:00": 30
      },
      "startid": 370819680,
      "endid": 4815874919
    },
    {
      "id": 706,
      "name": "Sky Blue Way / Walkway To Gosford St => Sky Blue Way / Gosford Green",
      "length": 0.0029580316495925675,
      "speed": {
        "0:00": 30
      },
      "startid": 4815874919,
      "endid": 4815880373
    },
    {
      "id": 707,
      "name": "Sky Blue Way / Gosford Green => Sky Blue Way / Gosford Green",
      "length": 0.0003139044440539605,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880373,
      "endid": 4815880374
    },
    {
      "id": 708,
      "name": "Sky Blue Way / Gosford Green => Walsgrave Rd / Swan Lane",
      "length": 0.0038133658229965737,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880374,
      "endid": 370817464
    },
    {
      "id": 709,
      "name": "Walsgrave Rd / Swan Lane => Walsgrave Rd / Swan Lane",
      "length": 0.0017645372707868672,
      "speed": {
        "0:00": 30
      },
      "startid": 370817464,
      "endid": 370817463
    },
    {
      "id": 710,
      "name": "Walsgrave Rd / Swan Lane => Walsgrave Rd / Clements St",
      "length": 0.0030988222827398773,
      "speed": {
        "0:00": 30
      },
      "startid": 370817463,
      "endid": 370817467
    },
    {
      "id": 711,
      "name": "Walsgrave Rd / Clements St => Walsgrave Rd / Clements St",
      "length": 0.0005896212004330483,
      "speed": {
        "0:00": 30
      },
      "startid": 370817467,
      "endid": 370817465
    },
    {
      "id": 712,
      "name": "Walsgrave Rd / Clements St => Clay Lane / Villiers St",
      "length": 0.002018121963607191,
      "speed": {
        "0:00": 30
      },
      "startid": 370817465,
      "endid": 370817469
    },
    {
      "id": 713,
      "name": "Clay Lane / Villiers St => Clay Lane / Villiers St",
      "length": 0.0004209312770510226,
      "speed": {
        "0:00": 30
      },
      "startid": 370817469,
      "endid": 370817470
    },
    {
      "id": 714,
      "name": "Clay Lane / Villiers St => Clay Lane / Caludon Rd",
      "length": 0.0013332352230586053,
      "speed": {
        "0:00": 30
      },
      "startid": 370817470,
      "endid": 370817472
    },
    {
      "id": 715,
      "name": "Clay Lane / Caludon Rd => Clay Lane / Caludon Rd",
      "length": 0.00023488720697729067,
      "speed": {
        "0:00": 30
      },
      "startid": 370817472,
      "endid": 370817474
    },
    {
      "id": 716,
      "name": "Clay Lane / Caludon Rd => Barras Green / Coventry St",
      "length": 0.0021808694137867867,
      "speed": {
        "0:00": 30
      },
      "startid": 370817474,
      "endid": 370817477
    },
    {
      "id": 717,
      "name": "Barras Green / Coventry St => Barras Green / Coventry St",
      "length": 0.0002759794195227487,
      "speed": {
        "0:00": 30
      },
      "startid": 370817477,
      "endid": 370817479
    },
    {
      "id": 718,
      "name": "Barras Green / Coventry St => Mercer Ave / North St",
      "length": 0.002349813177682842,
      "speed": {
        "0:00": 30
      },
      "startid": 370817479,
      "endid": 370817480
    },
    {
      "id": 719,
      "name": "Mercer Ave / North St => Mercer Ave / North St",
      "length": 0.00022498899973042542,
      "speed": {
        "0:00": 30
      },
      "startid": 370817480,
      "endid": 370817481
    },
    {
      "id": 720,
      "name": "Mercer Ave / North St => Alfall Rd / Stubbs Grove",
      "length": 0.004840595362142863,
      "speed": {
        "0:00": 30
      },
      "startid": 370817481,
      "endid": 370819566
    },
    {
      "id": 721,
      "name": "Alfall Rd / Stubbs Grove => Alfall Rd / Stubbs Grove",
      "length": 0.0005282783830510509,
      "speed": {
        "0:00": 30
      },
      "startid": 370819566,
      "endid": 370819567
    },
    {
      "id": 722,
      "name": "Alfall Rd / Stubbs Grove => Alfall Rd / Dennis Rd",
      "length": 0.002337872400281609,
      "speed": {
        "0:00": 30
      },
      "startid": 370819567,
      "endid": 370819643
    },
    {
      "id": 723,
      "name": "Alfall Rd / Dennis Rd => Alfall Rd / Dennis Rd",
      "length": 0.001948143662567895,
      "speed": {
        "0:00": 30
      },
      "startid": 370819643,
      "endid": 370819644
    },
    {
      "id": 724,
      "name": "Alfall Rd / Dennis Rd => Avon St / Alfall Rd",
      "length": 0.0007244049972218178,
      "speed": {
        "0:00": 30
      },
      "startid": 370819644,
      "endid": 370817483
    },
    {
      "id": 725,
      "name": "Avon St / Alfall Rd => Avon St / Honiton Rd",
      "length": 0.0019748620610052668,
      "speed": {
        "0:00": 30
      },
      "startid": 370817483,
      "endid": 370817485
    },
    {
      "id": 726,
      "name": "Avon St / Honiton Rd => Avon St / Honiton Rd",
      "length": 0.00046808773750384527,
      "speed": {
        "0:00": 30
      },
      "startid": 370817485,
      "endid": 370817484
    },
    {
      "id": 727,
      "name": "Avon St / Honiton Rd => Torcross Ave / Sewall Highway",
      "length": 0.0016491798476805893,
      "speed": {
        "0:00": 30
      },
      "startid": 370817484,
      "endid": 370817488
    },
    {
      "id": 728,
      "name": "Torcross Ave / Sewall Highway => Torcross Ave / Sewall Highway",
      "length": 0.0003655913018657318,
      "speed": {
        "0:00": 30
      },
      "startid": 370817488,
      "endid": 370817486
    },
    {
      "id": 729,
      "name": "Torcross Ave / Sewall Highway => Sewall Highway / Middle",
      "length": 0.003031260175240516,
      "speed": {
        "0:00": 30
      },
      "startid": 370817486,
      "endid": 370819641
    },
    {
      "id": 730,
      "name": "Sewall Highway / Middle => Sewall Highway / Dennis Rd",
      "length": 0.002706378391876186,
      "speed": {
        "0:00": 30
      },
      "startid": 370819641,
      "endid": 370819640
    },
    {
      "id": 731,
      "name": "Sewall Highway / Dennis Rd => Sewall Highway / Dennis Rd",
      "length": 0.0006107787897418022,
      "speed": {
        "0:00": 30
      },
      "startid": 370819640,
      "endid": 370819639
    },
    {
      "id": 732,
      "name": "Sewall Highway / Dennis Rd => Blackberry Lane / Brixham Drive",
      "length": 0.004937185053247094,
      "speed": {
        "0:00": 30
      },
      "startid": 370819639,
      "endid": 370817641
    },
    {
      "id": 733,
      "name": "Blackberry Lane / Brixham Drive => Blackberry Lane / Brixham Drive",
      "length": 0.0001440904229983649,
      "speed": {
        "0:00": 30
      },
      "startid": 370817641,
      "endid": 370817639
    },
    {
      "id": 734,
      "name": "Blackberry Lane / Brixham Drive => Blackberry Lane / Attwood Crescent",
      "length": 0.004738575104395738,
      "speed": {
        "0:00": 30
      },
      "startid": 370817639,
      "endid": 370817651
    },
    {
      "id": 735,
      "name": "Blackberry Lane / Attwood Crescent => Wyken Croft / Blackberry Lane",
      "length": 0.001917655756385987,
      "speed": {
        "0:00": 30
      },
      "startid": 370817651,
      "endid": 370817489
    },
    {
      "id": 736,
      "name": "Wyken Croft / Blackberry Lane => Wyken Croft / Hermes Crescent",
      "length": 0.0011307992969597162,
      "speed": {
        "0:00": 30
      },
      "startid": 370817489,
      "endid": 370817653
    },
    {
      "id": 737,
      "name": "Wyken Croft / Hermes Crescent => Wyken Croft / Hermes Crescent",
      "length": 0.0011230694546673055,
      "speed": {
        "0:00": 30
      },
      "startid": 370817653,
      "endid": 4815881234
    },
    {
      "id": 738,
      "name": "Wyken Croft / Hermes Crescent => Wyken Croft / Doncaster Close",
      "length": 0.0010068258886211014,
      "speed": {
        "0:00": 30
      },
      "startid": 4815881234,
      "endid": 370817533
    },
    {
      "id": 739,
      "name": "Wyken Croft / Doncaster Close => Wyken Croft / Doncaster Close",
      "length": 0.0002922190958847474,
      "speed": {
        "0:00": 30
      },
      "startid": 370817533,
      "endid": 370817535
    },
    {
      "id": 740,
      "name": "Wyken Croft / Doncaster Close => Henley Rd / Broad Park Rd",
      "length": 0.0031911319700053263,
      "speed": {
        "0:00": 30
      },
      "startid": 370817535,
      "endid": 370817560
    },
    {
      "id": 741,
      "name": "Henley Rd / Broad Park Rd => Broad Park Rd / Logan Rd",
      "length": 0.0009178312045262597,
      "speed": {
        "0:00": 30
      },
      "startid": 370817560,
      "endid": 4815876530
    },
    {
      "id": 742,
      "name": "Broad Park Rd / Logan Rd => Broad Park Rd / Broad Park Shops",
      "length": 0.0008362044726040847,
      "speed": {
        "0:00": 30
      },
      "startid": 4815876530,
      "endid": 370817536
    },
    {
      "id": 743,
      "name": "Broad Park Rd / Broad Park Shops => Broad Park Rd / Broad Park Shops",
      "length": 0.000692580103667792,
      "speed": {
        "0:00": 30
      },
      "startid": 370817536,
      "endid": 370817539
    },
    {
      "id": 744,
      "name": "Broad Park Rd / Broad Park Shops => Winston Avenue / Clennon Rise",
      "length": 0.0031214824298725925,
      "speed": {
        "0:00": 30
      },
      "startid": 370817539,
      "endid": 370817543
    },
    {
      "id": 745,
      "name": "Winston Avenue / Clennon Rise => Winston Avenue / Clennon Rise",
      "length": 0.0006219700314324196,
      "speed": {
        "0:00": 30
      },
      "startid": 370817543,
      "endid": 370817541
    },
    {
      "id": 746,
      "name": "Winston Avenue / Clennon Rise => Winston Avenue / Deedmore Rd",
      "length": 0.004886732295717704,
      "speed": {
        "0:00": 30
      },
      "startid": 370817541,
      "endid": 370817545
    },
    {
      "id": 747,
      "name": "Winston Avenue / Deedmore Rd => Winston Avenue / Deedmore Rd",
      "length": 0.0004305618886989429,
      "speed": {
        "0:00": 30
      },
      "startid": 370817545,
      "endid": 370817546
    },
    {
      "id": 748,
      "name": "Winston Avenue / Deedmore Rd => Deedmore Rd / Henley Rd",
      "length": 0.003181467015389691,
      "speed": {
        "0:00": 30
      },
      "startid": 370817546,
      "endid": 370817426
    },
    {
      "id": 749,
      "name": "Deedmore Rd / Henley Rd => Henley Rd / Deedmore Rd",
      "length": 0.0011486461334971625,
      "speed": {
        "0:00": 30
      },
      "startid": 370817426,
      "endid": 370817566
    },
    {
      "id": 750,
      "name": "Henley Rd / Deedmore Rd => Henley Rd / Dame Agnes Grove",
      "length": 0.005039856365016028,
      "speed": {
        "0:00": 30
      },
      "startid": 370817566,
      "endid": 370817365
    },
    {
      "id": 751,
      "name": "Henley Rd / Dame Agnes Grove => Henley Rd / Dame Agnes Grove",
      "length": 0.0008064862057111586,
      "speed": {
        "0:00": 30
      },
      "startid": 370817365,
      "endid": 370817363
    },
    {
      "id": 752,
      "name": "Henley Rd / Dame Agnes Grove => Roseberry Ave / Riley Square",
      "length": 0.00264472129722247,
      "speed": {
        "0:00": 30
      },
      "startid": 370817363,
      "endid": 370817349
    },
    {
      "id": 753,
      "name": "Ansty Rd / Mellowdew Rd => Ansty Rd / Mellowdew Rd",
      "length": 0.0011267458630953426,
      "speed": {
        "0:00": 30
      },
      "startid": 370817524,
      "endid": 370817526
    },
    {
      "id": 754,
      "name": "Ansty Rd / Mellowdew Rd => Ansty Rd / Dane Rd",
      "length": 0.003051524392823839,
      "speed": {
        "0:00": 30
      },
      "startid": 370817526,
      "endid": 370817522
    },
    {
      "id": 755,
      "name": "Ansty Rd / Dane Rd => Ansty Rd / Dane Rd",
      "length": 0.0005844890075955145,
      "speed": {
        "0:00": 30
      },
      "startid": 370817522,
      "endid": 370817521
    },
    {
      "id": 756,
      "name": "Ansty Rd / Dane Rd => Ansty Rd / Morris Avenue",
      "length": 0.0064786340242358985,
      "speed": {
        "0:00": 30
      },
      "startid": 370817521,
      "endid": 370817620
    },
    {
      "id": 757,
      "name": "Ansty Rd / Morris Avenue => Ansty Rd / Morris Avenue",
      "length": 0.000945145517896747,
      "speed": {
        "0:00": 30
      },
      "startid": 370817620,
      "endid": 370817621
    },
    {
      "id": 758,
      "name": "Ansty Rd / Morris Avenue => Ansty Rd / Hipswell Highway",
      "length": 0.0031013986941376545,
      "speed": {
        "0:00": 30
      },
      "startid": 370817621,
      "endid": 370817528
    },
    {
      "id": 759,
      "name": "Ansty Rd / Hipswell Highway => Ansty Rd / Hipswell Highway",
      "length": 0.001124690188452074,
      "speed": {
        "0:00": 30
      },
      "startid": 370817528,
      "endid": 370817527
    },
    {
      "id": 760,
      "name": "Ansty Rd / Hipswell Highway => Ansty Rd / Arch Rd",
      "length": 0.003705011516852265,
      "speed": {
        "0:00": 30
      },
      "startid": 370817527,
      "endid": 370817531
    },
    {
      "id": 761,
      "name": "Ansty Rd / Arch Rd => Ansty Rd / Arch Rd",
      "length": 0.001321381398385821,
      "speed": {
        "0:00": 30
      },
      "startid": 370817531,
      "endid": 370817532
    },
    {
      "id": 762,
      "name": "Ansty Rd / Arch Rd => Ansty Rd / Norton Hill Drive",
      "length": 0.0027710291896699047,
      "speed": {
        "0:00": 30
      },
      "startid": 370817532,
      "endid": 370817581
    },
    {
      "id": 763,
      "name": "Ansty Rd / Norton Hill Drive => Ansty Rd / Norton Hill Drive",
      "length": 0.0008620050695904217,
      "speed": {
        "0:00": 30
      },
      "startid": 370817581,
      "endid": 370817583
    },
    {
      "id": 764,
      "name": "Ansty Rd / Norton Hill Drive => Ansty Rd / Clifford Bridge Rd",
      "length": 0.0027758262787859972,
      "speed": {
        "0:00": 30
      },
      "startid": 370817583,
      "endid": 370817630
    },
    {
      "id": 765,
      "name": "Ansty Rd / Clifford Bridge Rd => Ansty Rd / Clifford Bridge Rd",
      "length": 0.0004618862630562424,
      "speed": {
        "0:00": 30
      },
      "startid": 370817630,
      "endid": 370817629
    },
    {
      "id": 766,
      "name": "Ansty Rd / Clifford Bridge Rd => WH",
      "length": 0.005105841427228393,
      "speed": {
        "0:00": 30
      },
      "startid": 370817629,
      "endid": 370817732
    },
    {
      "id": 767,
      "name": "WH => WG",
      "length": 0.000278365084014834,
      "speed": {
        "0:00": 30
      },
      "startid": 370817732,
      "endid": 370817730
    },
    {
      "id": 768,
      "name": "WG => WF",
      "length": 0.003325900281127788,
      "speed": {
        "0:00": 30
      },
      "startid": 370817730,
      "endid": 370817729
    },
    {
      "id": 769,
      "name": "WF => Walsgrave Rd / Burns Rd",
      "length": 0.03398274814814121,
      "speed": {
        "0:00": 30
      },
      "startid": 370817729,
      "endid": 370817502
    },
    {
      "id": 770,
      "name": "Walsgrave Rd / Burns Rd => Walsgrave Rd / Burns Rd",
      "length": 0.0015216241651606255,
      "speed": {
        "0:00": 30
      },
      "startid": 370817502,
      "endid": 370817504
    },
    {
      "id": 771,
      "name": "Walsgrave Rd / Burns Rd => Walsgrave Rd / Harefield Rd",
      "length": 0.0036222750930872813,
      "speed": {
        "0:00": 30
      },
      "startid": 370817504,
      "endid": 370817500
    },
    {
      "id": 772,
      "name": "Walsgrave Rd / Harefield Rd => Walsgrave Rd / Harefield Rd",
      "length": 0.0006063554485614267,
      "speed": {
        "0:00": 30
      },
      "startid": 370817500,
      "endid": 370817501
    },
    {
      "id": 773,
      "name": "Walsgrave Rd / Harefield Rd => Walsgrave Rd / Clements St",
      "length": 0.00521431387624442,
      "speed": {
        "0:00": 30
      },
      "startid": 370817501,
      "endid": 370817465
    },
    {
      "id": 774,
      "name": "Walsgrave Rd / Clements St => Walsgrave Rd / Clements St",
      "length": 0.0005896212004330483,
      "speed": {
        "0:00": 30
      },
      "startid": 370817465,
      "endid": 370817467
    },
    {
      "id": 775,
      "name": "Walsgrave Rd / Clements St => Walsgrave Rd / Swan Lane",
      "length": 0.0030988222827398773,
      "speed": {
        "0:00": 30
      },
      "startid": 370817467,
      "endid": 370817463
    },
    {
      "id": 776,
      "name": "Walsgrave Rd / Swan Lane => Walsgrave Rd / Swan Lane",
      "length": 0.0017645372707868672,
      "speed": {
        "0:00": 30
      },
      "startid": 370817463,
      "endid": 370817464
    },
    {
      "id": 777,
      "name": "Walsgrave Rd / Swan Lane => CU2",
      "length": 0.013072843649719269,
      "speed": {
        "0:00": 30
      },
      "startid": 370817464,
      "endid": 370819680
    },
    {
      "id": 778,
      "name": "CU2 => CU1",
      "length": 0.00010206831045847219,
      "speed": {
        "0:00": 30
      },
      "startid": 370819680,
      "endid": 370817766
    },
    {
      "id": 779,
      "name": "CU1 => CU5",
      "length": 0.0021117262535691986,
      "speed": {
        "0:00": 30
      },
      "startid": 370817766,
      "endid": 370819676
    },
    {
      "id": 780,
      "name": "CU5 => CU4",
      "length": 0.0005253710783815626,
      "speed": {
        "0:00": 30
      },
      "startid": 370819676,
      "endid": 370819679
    },
    {
      "id": 781,
      "name": "CU4 => VR2",
      "length": 0.012198051477592616,
      "speed": {
        "0:00": 30
      },
      "startid": 370819679,
      "endid": 370817717
    },
    {
      "id": 782,
      "name": "VR2 => Leamington Rd / War Memorial Park",
      "length": 0.0124963034122109,
      "speed": {
        "0:00": 30
      },
      "startid": 370817717,
      "endid": 370818569
    },
    {
      "id": 783,
      "name": "Leamington Rd / War Memorial Park => Leamington Rd / War Memorial Park",
      "length": 0.00032981820750473,
      "speed": {
        "0:00": 30
      },
      "startid": 370818569,
      "endid": 370818570
    },
    {
      "id": 784,
      "name": "Leamington Rd / War Memorial Park => Leamington Rd / Armorial Rd",
      "length": 0.0021197752262931174,
      "speed": {
        "0:00": 30
      },
      "startid": 370818570,
      "endid": 370818562
    },
    {
      "id": 785,
      "name": "Leamington Rd / Armorial Rd => Leamington Rd / Armorial Rd",
      "length": 0.0003211603026512689,
      "speed": {
        "0:00": 30
      },
      "startid": 370818562,
      "endid": 370818559
    },
    {
      "id": 786,
      "name": "Leamington Rd / Armorial Rd => Leamington Rd / Stivichall Croft",
      "length": 0.0023907359808194324,
      "speed": {
        "0:00": 30
      },
      "startid": 370818559,
      "endid": 370818572
    },
    {
      "id": 787,
      "name": "Leamington Rd / Stivichall Croft => Leamington Rd / Baginton Rd",
      "length": 0.0034378628710281943,
      "speed": {
        "0:00": 30
      },
      "startid": 370818572,
      "endid": 370818577
    },
    {
      "id": 788,
      "name": "Leamington Rd / Baginton Rd => Leamington Rd / Stonebridge Highway",
      "length": 0.0051924960635563785,
      "speed": {
        "0:00": 30
      },
      "startid": 370818577,
      "endid": 370818935
    },
    {
      "id": 789,
      "name": "Leamington Rd / Stonebridge Highway => Leamington Rd / Stonebridge Highway",
      "length": 0.00028445586652267,
      "speed": {
        "0:00": 30
      },
      "startid": 370818935,
      "endid": 370818933
    },
    {
      "id": 790,
      "name": "Leamington Rd / Stonebridge Highway => Green Lane / Finham Park School",
      "length": 0.008816016280044034,
      "speed": {
        "0:00": 30
      },
      "startid": 370818933,
      "endid": 1639951952
    },
    {
      "id": 791,
      "name": "Green Lane / Finham Park School => Green Lane / Crossway Rd",
      "length": 0.0031744405806414197,
      "speed": {
        "0:00": 30
      },
      "startid": 1639951952,
      "endid": 370818949
    },
    {
      "id": 792,
      "name": "Green Lane / Crossway Rd => Green Lane / Leasowes Cottages",
      "length": 0.0023223696970973567,
      "speed": {
        "0:00": 30
      },
      "startid": 370818949,
      "endid": 370819040
    },
    {
      "id": 793,
      "name": "Green Lane / Leasowes Cottages => Green Lane / Daleway Rd",
      "length": 0.0019867153042136144,
      "speed": {
        "0:00": 30
      },
      "startid": 370819040,
      "endid": 370818952
    },
    {
      "id": 794,
      "name": "Green Lane / Daleway Rd => Green Lane / Droylesdon Park Rd",
      "length": 0.0024073113737144024,
      "speed": {
        "0:00": 30
      },
      "startid": 370818952,
      "endid": 370819801
    },
    {
      "id": 795,
      "name": "Green Lane / Droylesdon Park Rd => Green Lane / Finham Green Rd",
      "length": 0.004295855663307947,
      "speed": {
        "0:00": 30
      },
      "startid": 370819801,
      "endid": 370818839
    },
    {
      "id": 796,
      "name": "Green Lane / Finham Green Rd => Brentwood Avenue / Alfriston Rd",
      "length": 0.006025984601707754,
      "speed": {
        "0:00": 30
      },
      "startid": 370818839,
      "endid": 370818943
    },
    {
      "id": 797,
      "name": "Brentwood Avenue / Alfriston Rd => Hadleigh Rd / St Martins Rd",
      "length": 0.004375926347642987,
      "speed": {
        "0:00": 30
      },
      "startid": 370818943,
      "endid": 370818940
    },
    {
      "id": 798,
      "name": "Hadleigh Rd / St Martins Rd => St Martins Rd / Erithway Rd",
      "length": 0.0026286467278779095,
      "speed": {
        "0:00": 30
      },
      "startid": 370818940,
      "endid": 370818937
    },
    {
      "id": 799,
      "name": "St Martins Rd / Erithway Rd => CS2",
      "length": 0.030510331812031957,
      "speed": {
        "0:00": 30
      },
      "startid": 370818937,
      "endid": 370817700
    },
    {
      "id": 800,
      "name": "CS2 => Leamington Rd / Stivichall Croft",
      "length": 0.01976032526377148,
      "speed": {
        "0:00": 30
      },
      "startid": 370817700,
      "endid": 370818574
    },
    {
      "id": 801,
      "name": "Leamington Rd / Stivichall Croft => TS5",
      "length": 0.020529397850398375,
      "speed": {
        "0:00": 30
      },
      "startid": 370818574,
      "endid": 1769864769
    },
    {
      "id": 802,
      "name": "TS5 => GR2",
      "length": 0.005847488849923562,
      "speed": {
        "0:00": 30
      },
      "startid": 1769864769,
      "endid": 370817796
    },
    {
      "id": 803,
      "name": "GR2 => St Martins Rd / Erithway Rd",
      "length": 0.027000237456917903,
      "speed": {
        "0:00": 30
      },
      "startid": 370817796,
      "endid": 370818938
    },
    {
      "id": 804,
      "name": "St Martins Rd / Erithway Rd => Hadleigh Rd / St Martins Rd",
      "length": 0.0020704263377444815,
      "speed": {
        "0:00": 30
      },
      "startid": 370818938,
      "endid": 370818942
    },
    {
      "id": 805,
      "name": "Hadleigh Rd / St Martins Rd => Brentwood Avenue / Alfriston Rd",
      "length": 0.004172986332351912,
      "speed": {
        "0:00": 30
      },
      "startid": 370818942,
      "endid": 370818944
    },
    {
      "id": 806,
      "name": "Brentwood Avenue / Alfriston Rd => Green Lane / Finham Green Rd",
      "length": 0.006539108820777424,
      "speed": {
        "0:00": 30
      },
      "startid": 370818944,
      "endid": 370818837
    },
    {
      "id": 807,
      "name": "Green Lane / Finham Green Rd => Green Lane / Daleway Rd",
      "length": 0.0059792764821509714,
      "speed": {
        "0:00": 30
      },
      "startid": 370818837,
      "endid": 370818950
    },
    {
      "id": 808,
      "name": "Green Lane / Daleway Rd => Green Lane / Leasowes Cottages",
      "length": 0.002212384636539533,
      "speed": {
        "0:00": 30
      },
      "startid": 370818950,
      "endid": 370819043
    },
    {
      "id": 809,
      "name": "Green Lane / Leasowes Cottages => Green Lane / Crossway Rd",
      "length": 0.0024999534895654477,
      "speed": {
        "0:00": 30
      },
      "startid": 370819043,
      "endid": 370818947
    },
    {
      "id": 810,
      "name": "Green Lane / Crossway Rd => Green Lane / Finham Park School",
      "length": 0.0034956993992613945,
      "speed": {
        "0:00": 30
      },
      "startid": 370818947,
      "endid": 370819722
    },
    {
      "id": 811,
      "name": "Green Lane / Finham Park School => Bathway Rd / Green Lane",
      "length": 0.000981250233120884,
      "speed": {
        "0:00": 30
      },
      "startid": 370819722,
      "endid": 370818945
    },
    {
      "id": 812,
      "name": "Bathway Rd / Green Lane => Kenpas Highway / Wainbody Avenue",
      "length": 0.0066469708236152085,
      "speed": {
        "0:00": 30
      },
      "startid": 370818945,
      "endid": 370817883
    },
    {
      "id": 813,
      "name": "Kenpas Highway / Wainbody Avenue => Kenpas Highway / Green Lane",
      "length": 0.0018871993482405607,
      "speed": {
        "0:00": 30
      },
      "startid": 370817883,
      "endid": 370819756
    },
    {
      "id": 814,
      "name": "Kenpas Highway / Green Lane => Beanfield Ave / Kenpas Highway",
      "length": 0.001378572003922437,
      "speed": {
        "0:00": 30
      },
      "startid": 370819756,
      "endid": 1639951987
    },
    {
      "id": 815,
      "name": "Beanfield Ave / Kenpas Highway => Beanfield Ave / Medland Avenue",
      "length": 0.0027621376685431575,
      "speed": {
        "0:00": 30
      },
      "startid": 1639951987,
      "endid": 1639951990
    },
    {
      "id": 816,
      "name": "Beanfield Ave / Medland Avenue => Leasowes Avenue / Beanfield Avenue",
      "length": 0.0037465174348980594,
      "speed": {
        "0:00": 30
      },
      "startid": 1639951990,
      "endid": 1639951960
    },
    {
      "id": 817,
      "name": "Leasowes Avenue / Beanfield Avenue => Wainbody Ave South / Leasowes Ave",
      "length": 0.0025156491726731254,
      "speed": {
        "0:00": 30
      },
      "startid": 1639951960,
      "endid": 1639951947
    },
    {
      "id": 818,
      "name": "Wainbody Ave South / Leasowes Ave => Wainbody Ave South / Kenpas Highway",
      "length": 0.002982116650975653,
      "speed": {
        "0:00": 30
      },
      "startid": 1639951947,
      "endid": 1639951993
    },
    {
      "id": 819,
      "name": "Wainbody Ave South / Kenpas Highway => Green Lane / Gretna Rd",
      "length": 0.00449455303339568,
      "speed": {
        "0:00": 30
      },
      "startid": 1639951993,
      "endid": 370817884
    },
    {
      "id": 820,
      "name": "Green Lane / Gretna Rd => UH7",
      "length": 0.09721511581050656,
      "speed": {
        "0:00": 30
      },
      "startid": 370817884,
      "endid": 4062225930
    },
    {
      "id": 821,
      "name": "UH7 => P",
      "length": 0.06992138375068148,
      "speed": {
        "0:00": 30
      },
      "startid": 4062225930,
      "endid": 370817747
    },
    {
      "id": 822,
      "name": "P => J",
      "length": 0.0007430522054331744,
      "speed": {
        "0:00": 30
      },
      "startid": 370817747,
      "endid": 370817742
    },
    {
      "id": 823,
      "name": "J => FX1",
      "length": 0.0026257533414241257,
      "speed": {
        "0:00": 30
      },
      "startid": 370817742,
      "endid": 370817768
    },
    {
      "id": 824,
      "name": "FX1 => GR1",
      "length": 0.01149121375399486,
      "speed": {
        "0:00": 30
      },
      "startid": 370817768,
      "endid": 370817794
    },
    {
      "id": 825,
      "name": "GR1 => VR3",
      "length": 0.002224508586183148,
      "speed": {
        "0:00": 30
      },
      "startid": 370817794,
      "endid": 370817718
    },
    {
      "id": 826,
      "name": "VR3 => CS4",
      "length": 0.002391225267514317,
      "speed": {
        "0:00": 30
      },
      "startid": 370817718,
      "endid": 370817702
    },
    {
      "id": 827,
      "name": "CS4 => BS3",
      "length": 0.003071773762827612,
      "speed": {
        "0:00": 30
      },
      "startid": 370817702,
      "endid": 370817695
    },
    {
      "id": 828,
      "name": "BS3 => Sky Blue Way / Walkway To Gosford St",
      "length": 0.01570945654979733,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 4815874919
    },
    {
      "id": 829,
      "name": "Sky Blue Way / Walkway To Gosford St => Sky Blue Way / Gosford Green",
      "length": 0.002963493080808429,
      "speed": {
        "0:00": 30
      },
      "startid": 4815874919,
      "endid": 4815880374
    },
    {
      "id": 830,
      "name": "Sky Blue Way / Gosford Green => Sky Blue Way / Gosford Green",
      "length": 0.0003139044440539605,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880374,
      "endid": 4815880373
    },
    {
      "id": 831,
      "name": "Sky Blue Way / Gosford Green => Warwick Road / Leamington Rd",
      "length": 0.026267339600728724,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880373,
      "endid": 370818568
    },
    {
      "id": 832,
      "name": "Warwick Road / Leamington Rd => Warwick Road / Leamington Rd",
      "length": 0.000625492965591671,
      "speed": {
        "0:00": 30
      },
      "startid": 370818568,
      "endid": 370818566
    },
    {
      "id": 833,
      "name": "Warwick Road / Leamington Rd => WR5",
      "length": 0.0026801527288538595,
      "speed": {
        "0:00": 30
      },
      "startid": 370818566,
      "endid": 370817793
    },
    {
      "id": 834,
      "name": "WR5 => WR6",
      "length": 0.0004939037153162216,
      "speed": {
        "0:00": 30
      },
      "startid": 370817793,
      "endid": 370817791
    },
    {
      "id": 835,
      "name": "WR6 => Baginton Rd / Barnack Avenue",
      "length": 0.014784280790762376,
      "speed": {
        "0:00": 30
      },
      "startid": 370817791,
      "endid": 1639951970
    },
    {
      "id": 836,
      "name": "Baginton Rd / Barnack Avenue => Mantilla Dr / Baginton Rd",
      "length": 0.0023026927823750847,
      "speed": {
        "0:00": 30
      },
      "startid": 1639951970,
      "endid": 1639951928
    },
    {
      "id": 837,
      "name": "Mantilla Dr / Baginton Rd => Mantilla Dr / Baginton Rd",
      "length": 0.0002361491266124233,
      "speed": {
        "0:00": 30
      },
      "startid": 1639951928,
      "endid": 370819068
    },
    {
      "id": 838,
      "name": "Mantilla Dr / Baginton Rd => Mantilla Dr / Chideock Hill",
      "length": 0.0039657117457036,
      "speed": {
        "0:00": 30
      },
      "startid": 370819068,
      "endid": 1639951964
    },
    {
      "id": 839,
      "name": "Mantilla Dr / Chideock Hill => Mantilla Dr / Chideock Hill",
      "length": 0.00017350922165666941,
      "speed": {
        "0:00": 30
      },
      "startid": 1639951964,
      "endid": 370819067
    },
    {
      "id": 840,
      "name": "Mantilla Dr / Chideock Hill => Mantilla Dr / Peveril Drive",
      "length": 0.0015397212799732193,
      "speed": {
        "0:00": 30
      },
      "startid": 370819067,
      "endid": 1639951983
    },
    {
      "id": 841,
      "name": "Mantilla Dr / Peveril Drive => Mantilla Dr / Peveril Drive",
      "length": 0.0009891249668275356,
      "speed": {
        "0:00": 30
      },
      "startid": 1639951983,
      "endid": 370819066
    },
    {
      "id": 842,
      "name": "Mantilla Dr / Peveril Drive => Mantilla Dr / Hexworthy Ave Shops",
      "length": 0.002384635504641901,
      "speed": {
        "0:00": 30
      },
      "startid": 370819066,
      "endid": 2191394746
    },
    {
      "id": 843,
      "name": "Mantilla Dr / Hexworthy Ave Shops => Mantilla Dr / Hexworthy Ave Shops",
      "length": 0.00019583487942569563,
      "speed": {
        "0:00": 30
      },
      "startid": 2191394746,
      "endid": 370819063
    },
    {
      "id": 844,
      "name": "Mantilla Dr / Hexworthy Ave Shops => Mantilla Dr / Wade Avenue",
      "length": 0.0010745710306932687,
      "speed": {
        "0:00": 30
      },
      "startid": 370819063,
      "endid": 1639951929
    },
    {
      "id": 845,
      "name": "Mantilla Dr / Wade Avenue => Mantilla Dr / Wade Avenue",
      "length": 0.0003569066124355264,
      "speed": {
        "0:00": 30
      },
      "startid": 1639951929,
      "endid": 370819062
    },
    {
      "id": 846,
      "name": "Windmill Rd / St Thomas' Rd => Windmill Rd / St Thomas' Rd",
      "length": 0.0019420495410774708,
      "speed": {
        "0:00": 30
      },
      "startid": 370818859,
      "endid": 370818861
    },
    {
      "id": 847,
      "name": "Windmill Rd / St Thomas' Rd => Windmill Rd / Recreation Rd",
      "length": 0.001029124258775919,
      "speed": {
        "0:00": 30
      },
      "startid": 370818861,
      "endid": 370817401
    },
    {
      "id": 848,
      "name": "Windmill Rd / Recreation Rd => Windmill Rd / Barston Close",
      "length": 0.0026771179372600223,
      "speed": {
        "0:00": 30
      },
      "startid": 370817401,
      "endid": 370818882
    },
    {
      "id": 849,
      "name": "Windmill Rd / Barston Close => Windmill Rd / Barston Close",
      "length": 0.000379546308109366,
      "speed": {
        "0:00": 30
      },
      "startid": 370818882,
      "endid": 370818883
    },
    {
      "id": 850,
      "name": "Windmill Rd / Barston Close => Windmill Rd / Mill Race Lane",
      "length": 0.0023966617199763364,
      "speed": {
        "0:00": 30
      },
      "startid": 370818883,
      "endid": 370817384
    },
    {
      "id": 851,
      "name": "Windmill Rd / Mill Race Lane => Windmill Rd / Mill Race Lane",
      "length": 0.0005935334952651139,
      "speed": {
        "0:00": 30
      },
      "startid": 370817384,
      "endid": 370817386
    },
    {
      "id": 852,
      "name": "Windmill Rd / Mill Race Lane => Hall Green Rd / Dersingham Drive",
      "length": 0.004529617204580371,
      "speed": {
        "0:00": 30
      },
      "startid": 370817386,
      "endid": 370817368
    },
    {
      "id": 853,
      "name": "Hall Green Rd / Dersingham Drive => Hall Green Rd / Dersingham Drive",
      "length": 0.0001453545320973188,
      "speed": {
        "0:00": 30
      },
      "startid": 370817368,
      "endid": 370817369
    },
    {
      "id": 854,
      "name": "Hall Green Rd / Dersingham Drive => Hall Green Rd / Almond Tree Avenue",
      "length": 0.0025275078199727095,
      "speed": {
        "0:00": 30
      },
      "startid": 370817369,
      "endid": 370817362
    },
    {
      "id": 855,
      "name": "Hall Green Rd / Almond Tree Avenue => Hall Green Rd / Almond Tree Avenue",
      "length": 0.000748740449017119,
      "speed": {
        "0:00": 30
      },
      "startid": 370817362,
      "endid": 370817360
    },
    {
      "id": 856,
      "name": "Hall Green Rd / Almond Tree Avenue => Almond Tree Ave / Honeysuckle Drive",
      "length": 0.001228825003814196,
      "speed": {
        "0:00": 30
      },
      "startid": 370817360,
      "endid": 370819301
    },
    {
      "id": 857,
      "name": "Almond Tree Ave / Honeysuckle Drive => Henley Rd / Old Church Rd",
      "length": 0.0034965209966499877,
      "speed": {
        "0:00": 30
      },
      "startid": 370819301,
      "endid": 370819625
    },
    {
      "id": 858,
      "name": "Henley Rd / Old Church Rd => Longford Rd / Dovedale Avenue",
      "length": 0.017272667369284535,
      "speed": {
        "0:00": 30
      },
      "startid": 370819625,
      "endid": 370818870
    },
    {
      "id": 859,
      "name": "Longford Rd / Dovedale Avenue => AG",
      "length": 0.0021072323103976083,
      "speed": {
        "0:00": 30
      },
      "startid": 370818870,
      "endid": 370818869
    },
    {
      "id": 860,
      "name": "AG => AF",
      "length": 0.0008466729474816734,
      "speed": {
        "0:00": 30
      },
      "startid": 370818869,
      "endid": 370818867
    },
    {
      "id": 861,
      "name": "AF => Foleshill Rd / The Wheatsheaf",
      "length": 0.001456813598235208,
      "speed": {
        "0:00": 30
      },
      "startid": 370818867,
      "endid": 370818864
    },
    {
      "id": 862,
      "name": "Foleshill Rd / The Wheatsheaf => Foleshill Rd / The Wheatsheaf",
      "length": 0.00031738230889481126,
      "speed": {
        "0:00": 30
      },
      "startid": 370818864,
      "endid": 370818865
    },
    {
      "id": 863,
      "name": "Foleshill Rd / The Wheatsheaf => Foleshill Rd / Old Church Rd",
      "length": 0.0031598401984935013,
      "speed": {
        "0:00": 30
      },
      "startid": 370818865,
      "endid": 370818863
    },
    {
      "id": 864,
      "name": "Foleshill Rd / Old Church Rd => Foleshill Rd / Old Church Rd",
      "length": 0.0003347000000000211,
      "speed": {
        "0:00": 30
      },
      "startid": 370818863,
      "endid": 370818862
    },
    {
      "id": 865,
      "name": "Foleshill Rd / Old Church Rd => Foleshill Rd / Phoenix Way",
      "length": 0.0035533042270538776,
      "speed": {
        "0:00": 30
      },
      "startid": 370818862,
      "endid": 370818832
    },
    {
      "id": 866,
      "name": "Foleshill Rd / Phoenix Way => Foleshill Rd / Phoenix Way",
      "length": 0.0002803520108717694,
      "speed": {
        "0:00": 30
      },
      "startid": 370818832,
      "endid": 370818834
    },
    {
      "id": 867,
      "name": "Foleshill Rd / Phoenix Way => Foleshill Rd / Cross Rd",
      "length": 0.0016837137820924367,
      "speed": {
        "0:00": 30
      },
      "startid": 370818834,
      "endid": 370818830
    },
    {
      "id": 868,
      "name": "Foleshill Rd / Cross Rd => Foleshill Rd / Cross Rd",
      "length": 0.0004945206264681952,
      "speed": {
        "0:00": 30
      },
      "startid": 370818830,
      "endid": 370818831
    },
    {
      "id": 869,
      "name": "Foleshill Rd / Cross Rd => Foleshill Rd / Family Centre",
      "length": 0.0026930447174148245,
      "speed": {
        "0:00": 30
      },
      "startid": 370818831,
      "endid": 370819702
    },
    {
      "id": 870,
      "name": "Foleshill Rd / Family Centre => Foleshill Rd / Family Centre",
      "length": 0.00016455625178377943,
      "speed": {
        "0:00": 30
      },
      "startid": 370819702,
      "endid": 370819703
    },
    {
      "id": 871,
      "name": "Foleshill Rd / Family Centre => Foleshill Rd / Station St",
      "length": 0.0014088894953136236,
      "speed": {
        "0:00": 30
      },
      "startid": 370819703,
      "endid": 370818829
    },
    {
      "id": 872,
      "name": "Foleshill Rd / Station St => Foleshill Rd / Station St",
      "length": 0.0013386575364890566,
      "speed": {
        "0:00": 30
      },
      "startid": 370818829,
      "endid": 370818827
    },
    {
      "id": 873,
      "name": "Foleshill Rd / Station St => Foleshill Rd / Broad St",
      "length": 0.0028052413532526385,
      "speed": {
        "0:00": 30
      },
      "startid": 370818827,
      "endid": 370818825
    },
    {
      "id": 874,
      "name": "Foleshill Rd / Broad St => Foleshill Rd / Broad St",
      "length": 0.00038016818646532426,
      "speed": {
        "0:00": 30
      },
      "startid": 370818825,
      "endid": 370818826
    },
    {
      "id": 875,
      "name": "Foleshill Rd / Broad St => Foleshill Rd / Courtaulds Way",
      "length": 0.004239609710810101,
      "speed": {
        "0:00": 30
      },
      "startid": 370818826,
      "endid": 370818780
    },
    {
      "id": 876,
      "name": "Foleshill Rd / Courtaulds Way => Foleshill Rd / Courtaulds Way",
      "length": 0.00035180778843009035,
      "speed": {
        "0:00": 30
      },
      "startid": 370818780,
      "endid": 370818784
    },
    {
      "id": 877,
      "name": "Foleshill Rd / Courtaulds Way => Foleshill Rd / Cashs Lane",
      "length": 0.004273169018420262,
      "speed": {
        "0:00": 30
      },
      "startid": 370818784,
      "endid": 370818776
    },
    {
      "id": 878,
      "name": "Foleshill Rd / Cashs Lane => Foleshill Rd / Cashs Lane",
      "length": 0.00022125555360341274,
      "speed": {
        "0:00": 30
      },
      "startid": 370818776,
      "endid": 370818774
    },
    {
      "id": 879,
      "name": "Foleshill Rd / Cashs Lane => Foleshill Rd / Eagle St",
      "length": 0.0011237341055589636,
      "speed": {
        "0:00": 30
      },
      "startid": 370818774,
      "endid": 370818765
    },
    {
      "id": 880,
      "name": "Foleshill Rd / Eagle St => Foleshill Rd / Eagle St",
      "length": 0.001522061907418469,
      "speed": {
        "0:00": 30
      },
      "startid": 370818765,
      "endid": 370818766
    },
    {
      "id": 881,
      "name": "Foleshill Rd / Eagle St => Foleshill Rd / City Engineers",
      "length": 0.0027907170565999295,
      "speed": {
        "0:00": 30
      },
      "startid": 370818766,
      "endid": 370818762
    },
    {
      "id": 882,
      "name": "Foleshill Rd / City Engineers => Foleshill Rd / City Engineers",
      "length": 0.00022393115013730707,
      "speed": {
        "0:00": 30
      },
      "startid": 370818762,
      "endid": 370818764
    },
    {
      "id": 883,
      "name": "Foleshill Rd / City Engineers => Foleshill Rd / Leicester Row",
      "length": 0.0016005044017478598,
      "speed": {
        "0:00": 30
      },
      "startid": 370818764,
      "endid": 370818761
    },
    {
      "id": 884,
      "name": "Foleshill Rd / Leicester Row => Foleshill Rd / Leicester Row",
      "length": 0.00040428367515873303,
      "speed": {
        "0:00": 30
      },
      "startid": 370818761,
      "endid": 370818758
    },
    {
      "id": 885,
      "name": "Foleshill Rd / Leicester Row => BS1",
      "length": 0.003915537353925627,
      "speed": {
        "0:00": 30
      },
      "startid": 370818758,
      "endid": 370817728
    },
    {
      "id": 886,
      "name": "BS1 => BS2",
      "length": 0.0006854744707142306,
      "speed": {
        "0:00": 30
      },
      "startid": 370817728,
      "endid": 370817727
    },
    {
      "id": 887,
      "name": "BS2 => Roseberry Ave / Riley Square",
      "length": 0.04717752572677198,
      "speed": {
        "0:00": 30
      },
      "startid": 370817727,
      "endid": 2384202462
    },
    {
      "id": 888,
      "name": "Roseberry Ave / Riley Square => Henley Rd / Dame Agnes Grove",
      "length": 0.0028477027811930388,
      "speed": {
        "0:00": 30
      },
      "startid": 2384202462,
      "endid": 370817365
    },
    {
      "id": 889,
      "name": "Henley Rd / Dame Agnes Grove => Henley Rd / Dame Agnes Grove",
      "length": 0.0008064862057111586,
      "speed": {
        "0:00": 30
      },
      "startid": 370817365,
      "endid": 370817363
    },
    {
      "id": 890,
      "name": "Henley Rd / Dame Agnes Grove => Henley Rd / Deedmore Rd",
      "length": 0.005839751414230243,
      "speed": {
        "0:00": 30
      },
      "startid": 370817363,
      "endid": 370817566
    },
    {
      "id": 891,
      "name": "Henley Rd / Deedmore Rd => Henley Rd / Deedmore Rd",
      "length": 0.0011696403720807321,
      "speed": {
        "0:00": 30
      },
      "startid": 370817566,
      "endid": 370817569
    },
    {
      "id": 892,
      "name": "Henley Rd / Deedmore Rd => Henley Rd / Newhall Rd",
      "length": 0.003382197398140166,
      "speed": {
        "0:00": 30
      },
      "startid": 370817569,
      "endid": 370817563
    },
    {
      "id": 893,
      "name": "Henley Rd / Newhall Rd => Henley Rd / Newhall Rd",
      "length": 0.0018112053693614854,
      "speed": {
        "0:00": 30
      },
      "startid": 370817563,
      "endid": 370817565
    },
    {
      "id": 894,
      "name": "Henley Rd / Newhall Rd => Henley Rd / Broad Park Rd",
      "length": 0.0028933466176736867,
      "speed": {
        "0:00": 30
      },
      "startid": 370817565,
      "endid": 370817560
    },
    {
      "id": 895,
      "name": "Henley Rd / Broad Park Rd => Henley Rd / Broad Park Rd",
      "length": 0.001552294434054869,
      "speed": {
        "0:00": 30
      },
      "startid": 370817560,
      "endid": 370817561
    },
    {
      "id": 896,
      "name": "Henley Rd / Broad Park Rd => Henley Rd / Luscombe Rd",
      "length": 0.0013239584019158483,
      "speed": {
        "0:00": 30
      },
      "startid": 370817561,
      "endid": 370817555
    },
    {
      "id": 897,
      "name": "Henley Rd / Luscombe Rd => Henley Rd / Luscombe Rd",
      "length": 0.00031395396159306413,
      "speed": {
        "0:00": 30
      },
      "startid": 370817555,
      "endid": 370817559
    },
    {
      "id": 898,
      "name": "Henley Rd / Luscombe Rd => Henley Rd / Pandora Rd",
      "length": 0.004278657006584846,
      "speed": {
        "0:00": 30
      },
      "startid": 370817559,
      "endid": 370817409
    },
    {
      "id": 899,
      "name": "Henley Rd / Pandora Rd => Henley Rd / Pandora Rd",
      "length": 0.000647642779624707,
      "speed": {
        "0:00": 30
      },
      "startid": 370817409,
      "endid": 370817411
    },
    {
      "id": 900,
      "name": "Henley Rd / Pandora Rd => Woodway Lane / Henley Rd",
      "length": 0.0041314631270286,
      "speed": {
        "0:00": 30
      },
      "startid": 370817411,
      "endid": 370817613
    },
    {
      "id": 901,
      "name": "Woodway Lane / Henley Rd => Woodway Lane / Henley Rd",
      "length": 0.0007164244063370794,
      "speed": {
        "0:00": 30
      },
      "startid": 370817613,
      "endid": 370817614
    },
    {
      "id": 902,
      "name": "Woodway Lane / Henley Rd => Ansty Rd / Walsgrave Church",
      "length": 0.003650553322443421,
      "speed": {
        "0:00": 30
      },
      "startid": 370817614,
      "endid": 370817587
    },
    {
      "id": 903,
      "name": "Ansty Rd / Walsgrave Church => Ansty Rd / Walsgrave Church",
      "length": 0.0003016658581946437,
      "speed": {
        "0:00": 30
      },
      "startid": 370817587,
      "endid": 370817584
    },
    {
      "id": 904,
      "name": "Ansty Rd / Walsgrave Church => WH",
      "length": 0.0030556764881162707,
      "speed": {
        "0:00": 30
      },
      "startid": 370817584,
      "endid": 370817732
    },
    {
      "id": 905,
      "name": "WH => WG",
      "length": 0.000278365084014834,
      "speed": {
        "0:00": 30
      },
      "startid": 370817732,
      "endid": 370817730
    },
    {
      "id": 906,
      "name": "WG => WF",
      "length": 0.003325900281127788,
      "speed": {
        "0:00": 30
      },
      "startid": 370817730,
      "endid": 370817729
    },
    {
      "id": 907,
      "name": "WF => Almond Tree Ave / Honeysuckle Drive",
      "length": 0.03649633537767858,
      "speed": {
        "0:00": 30
      },
      "startid": 370817729,
      "endid": 370819299
    },
    {
      "id": 908,
      "name": "Almond Tree Ave / Honeysuckle Drive => Roseberry Ave / Riley Square",
      "length": 0.0026983161453033497,
      "speed": {
        "0:00": 30
      },
      "startid": 370819299,
      "endid": 370817350
    },
    {
      "id": 909,
      "name": "Roseberry Ave / Riley Square => TS4",
      "length": 0.04702288610474729,
      "speed": {
        "0:00": 30
      },
      "startid": 370817350,
      "endid": 370817662
    },
    {
      "id": 910,
      "name": "TS4 => UH1",
      "length": 0.0723217069754989,
      "speed": {
        "0:00": 30
      },
      "startid": 370817662,
      "endid": 370817643
    },
    {
      "id": 911,
      "name": "Hayes Lane => Heckley Road",
      "length": 0.0019734361149991134,
      "speed": {
        "0:00": 30
      },
      "startid": 487169359,
      "endid": 487174461
    },
    {
      "id": 912,
      "name": "Heckley Road => Trelawney Road",
      "length": 0.0009165142933970633,
      "speed": {
        "0:00": 30
      },
      "startid": 487174461,
      "endid": 487169366
    },
    {
      "id": 913,
      "name": "Trelawney Road => Lord Raglan",
      "length": 0.0008222157867605711,
      "speed": {
        "0:00": 30
      },
      "startid": 487169366,
      "endid": 487174457
    },
    {
      "id": 914,
      "name": "Lord Raglan => Longford Road",
      "length": 0.0028648385434478824,
      "speed": {
        "0:00": 30
      },
      "startid": 487174457,
      "endid": 487166797
    },
    {
      "id": 915,
      "name": "Longford Road => Longford Road",
      "length": 0.00036270456297115243,
      "speed": {
        "0:00": 30
      },
      "startid": 487166797,
      "endid": 487166800
    },
    {
      "id": 916,
      "name": "Longford Road => Boat",
      "length": 0.0106679351779056,
      "speed": {
        "0:00": 30
      },
      "startid": 487166800,
      "endid": 487165316
    },
    {
      "id": 917,
      "name": "Boat => 619436810",
      "length": 0.0015395418604202294,
      "speed": {
        "0:00": 30
      },
      "startid": 487165316,
      "endid": 619436810
    },
    {
      "id": 918,
      "name": "619436810 => 620978722",
      "length": 0.005088427674635968,
      "speed": {
        "0:00": 30
      },
      "startid": 619436810,
      "endid": 620978722
    },
    {
      "id": 919,
      "name": "620978722 => Black Horse",
      "length": 0.0068626825753486526,
      "speed": {
        "0:00": 30
      },
      "startid": 620978722,
      "endid": 487169388
    },
    {
      "id": 920,
      "name": "Black Horse => Black Horse",
      "length": 0.00041012888217990085,
      "speed": {
        "0:00": 30
      },
      "startid": 487169388,
      "endid": 487169349
    },
    {
      "id": 921,
      "name": "Black Horse => Bedworth Rd / Ibstock Rd",
      "length": 0.00473464240888205,
      "speed": {
        "0:00": 30
      },
      "startid": 487169349,
      "endid": 370818879
    },
    {
      "id": 922,
      "name": "Bedworth Rd / Ibstock Rd => Bedworth Rd / Ibstock Rd",
      "length": 0.00033837257572197685,
      "speed": {
        "0:00": 30
      },
      "startid": 370818879,
      "endid": 370818878
    },
    {
      "id": 923,
      "name": "Bedworth Rd / Ibstock Rd => Bedworth Rd / Oban Rd",
      "length": 0.002246773317446427,
      "speed": {
        "0:00": 30
      },
      "startid": 370818878,
      "endid": 370818876
    },
    {
      "id": 924,
      "name": "Bedworth Rd / Oban Rd => Bedworth Rd / Oban Rd",
      "length": 0.0008358934680899525,
      "speed": {
        "0:00": 30
      },
      "startid": 370818876,
      "endid": 370818877
    },
    {
      "id": 925,
      "name": "Bedworth Rd / Oban Rd => Longford Rd / Longford Square",
      "length": 0.00290910894433318,
      "speed": {
        "0:00": 30
      },
      "startid": 370818877,
      "endid": 370818873
    },
    {
      "id": 926,
      "name": "Longford Rd / Longford Square => Longford Rd / Longford Square",
      "length": 0.0003155618639778003,
      "speed": {
        "0:00": 30
      },
      "startid": 370818873,
      "endid": 370818874
    },
    {
      "id": 927,
      "name": "Longford Rd / Longford Square => Longford Rd / Oakmoor Rd",
      "length": 0.0019004607862272331,
      "speed": {
        "0:00": 30
      },
      "startid": 370818874,
      "endid": 370818871
    },
    {
      "id": 928,
      "name": "Longford Rd / Oakmoor Rd => Longford Rd / Vinecote Rd",
      "length": 0.0011475531403839034,
      "speed": {
        "0:00": 30
      },
      "startid": 370818871,
      "endid": 370818872
    },
    {
      "id": 929,
      "name": "Longford Rd / Vinecote Rd => Longford Rd / Longford Bridge",
      "length": 0.0020781797901004042,
      "speed": {
        "0:00": 30
      },
      "startid": 370818872,
      "endid": 370819748
    },
    {
      "id": 930,
      "name": "Longford Rd / Longford Bridge => Longford Rd / Windmill Rd",
      "length": 0.0014970952808711533,
      "speed": {
        "0:00": 30
      },
      "startid": 370819748,
      "endid": 370819732
    },
    {
      "id": 931,
      "name": "Longford Rd / Windmill Rd => Longford Rd / Dovedale Avenue",
      "length": 0.0010496597639259562,
      "speed": {
        "0:00": 30
      },
      "startid": 370819732,
      "endid": 370818870
    },
    {
      "id": 932,
      "name": "Longford Rd / Dovedale Avenue => AC",
      "length": 0.001510979774847205,
      "speed": {
        "0:00": 30
      },
      "startid": 370818870,
      "endid": 370819737
    },
    {
      "id": 933,
      "name": "AC => Windmill Rd / St Thomas' Rd",
      "length": 0.004364151356219984,
      "speed": {
        "0:00": 30
      },
      "startid": 370819737,
      "endid": 370818861
    },
    {
      "id": 934,
      "name": "Windmill Rd / St Thomas' Rd => Windmill Rd / Recreation Rd",
      "length": 0.001029124258775919,
      "speed": {
        "0:00": 30
      },
      "startid": 370818861,
      "endid": 370817401
    },
    {
      "id": 935,
      "name": "Windmill Rd / Recreation Rd => Windmill Rd / Barston Close",
      "length": 0.0026771179372600223,
      "speed": {
        "0:00": 30
      },
      "startid": 370817401,
      "endid": 370818882
    },
    {
      "id": 936,
      "name": "Windmill Rd / Barston Close => Windmill Rd / Barston Close",
      "length": 0.000379546308109366,
      "speed": {
        "0:00": 30
      },
      "startid": 370818882,
      "endid": 370818883
    },
    {
      "id": 937,
      "name": "Windmill Rd / Barston Close => Windmill Rd / Mill Race Lane",
      "length": 0.0023966617199763364,
      "speed": {
        "0:00": 30
      },
      "startid": 370818883,
      "endid": 370817384
    },
    {
      "id": 938,
      "name": "Windmill Rd / Mill Race Lane => Windmill Rd / Mill Race Lane",
      "length": 0.0005935334952651139,
      "speed": {
        "0:00": 30
      },
      "startid": 370817384,
      "endid": 370817386
    },
    {
      "id": 939,
      "name": "Windmill Rd / Mill Race Lane => Hall Green Rd / Dersingham Drive",
      "length": 0.0043879826480969775,
      "speed": {
        "0:00": 30
      },
      "startid": 370817386,
      "endid": 370817369
    },
    {
      "id": 940,
      "name": "Hall Green Rd / Dersingham Drive => Hall Green Rd / Dersingham Drive",
      "length": 0.0001453545320973188,
      "speed": {
        "0:00": 30
      },
      "startid": 370817369,
      "endid": 370817368
    },
    {
      "id": 941,
      "name": "Hall Green Rd / Dersingham Drive => Hall Green Rd / Almond Tree Avenue",
      "length": 0.0024157963490318312,
      "speed": {
        "0:00": 30
      },
      "startid": 370817368,
      "endid": 370817362
    },
    {
      "id": 942,
      "name": "Hall Green Rd / Almond Tree Avenue => Hall Green Rd / Almond Tree Avenue",
      "length": 0.000748740449017119,
      "speed": {
        "0:00": 30
      },
      "startid": 370817362,
      "endid": 370817360
    },
    {
      "id": 943,
      "name": "Hall Green Rd / Almond Tree Avenue => Hall Green Rd / Old Church Rd",
      "length": 0.002447835421352187,
      "speed": {
        "0:00": 30
      },
      "startid": 370817360,
      "endid": 370819297
    },
    {
      "id": 944,
      "name": "Hall Green Rd / Old Church Rd => Henley Rd / Old Church Rd",
      "length": 0.0010644874071574137,
      "speed": {
        "0:00": 30
      },
      "startid": 370819297,
      "endid": 370819625
    },
    {
      "id": 945,
      "name": "Henley Rd / Old Church Rd => Henley Rd / Dame Agnes Grove",
      "length": 0.0015153622570181903,
      "speed": {
        "0:00": 30
      },
      "startid": 370819625,
      "endid": 370817363
    },
    {
      "id": 946,
      "name": "Henley Rd / Dame Agnes Grove => Henley Rd / Dame Agnes Grove",
      "length": 0.0008064862057111586,
      "speed": {
        "0:00": 30
      },
      "startid": 370817363,
      "endid": 370817365
    },
    {
      "id": 947,
      "name": "Henley Rd / Dame Agnes Grove => Henley Rd / Deedmore Rd",
      "length": 0.005039856365016028,
      "speed": {
        "0:00": 30
      },
      "startid": 370817365,
      "endid": 370817566
    },
    {
      "id": 948,
      "name": "Henley Rd / Deedmore Rd => Henley Rd / Deedmore Rd",
      "length": 0.0011696403720807321,
      "speed": {
        "0:00": 30
      },
      "startid": 370817566,
      "endid": 370817569
    },
    {
      "id": 949,
      "name": "Henley Rd / Deedmore Rd => Henley Rd / Newhall Rd",
      "length": 0.003382197398140166,
      "speed": {
        "0:00": 30
      },
      "startid": 370817569,
      "endid": 370817563
    },
    {
      "id": 950,
      "name": "Henley Rd / Newhall Rd => Henley Rd / Newhall Rd",
      "length": 0.0018112053693614854,
      "speed": {
        "0:00": 30
      },
      "startid": 370817563,
      "endid": 370817565
    },
    {
      "id": 951,
      "name": "Henley Rd / Newhall Rd => Henley Rd / Broad Park Rd",
      "length": 0.004441592151469653,
      "speed": {
        "0:00": 30
      },
      "startid": 370817565,
      "endid": 370817561
    },
    {
      "id": 952,
      "name": "Henley Rd / Broad Park Rd => Henley Rd / Broad Park Rd",
      "length": 0.001552294434054869,
      "speed": {
        "0:00": 30
      },
      "startid": 370817561,
      "endid": 370817560
    },
    {
      "id": 953,
      "name": "Henley Rd / Broad Park Rd => Henley Rd / Luscombe Rd",
      "length": 0.003119328301092934,
      "speed": {
        "0:00": 30
      },
      "startid": 370817560,
      "endid": 370817559
    },
    {
      "id": 954,
      "name": "Henley Rd / Luscombe Rd => Henley Rd / Luscombe Rd",
      "length": 0.00031395396159306413,
      "speed": {
        "0:00": 30
      },
      "startid": 370817559,
      "endid": 370817555
    },
    {
      "id": 955,
      "name": "Henley Rd / Luscombe Rd => Henley Rd / Pandora Rd",
      "length": 0.004563601193136676,
      "speed": {
        "0:00": 30
      },
      "startid": 370817555,
      "endid": 370817409
    },
    {
      "id": 956,
      "name": "Henley Rd / Pandora Rd => Henley Rd / Pandora Rd",
      "length": 0.000647642779624707,
      "speed": {
        "0:00": 30
      },
      "startid": 370817409,
      "endid": 370817411
    },
    {
      "id": 957,
      "name": "Henley Rd / Pandora Rd => Woodway Lane / Henley Rd",
      "length": 0.0041314631270286,
      "speed": {
        "0:00": 30
      },
      "startid": 370817411,
      "endid": 370817613
    },
    {
      "id": 958,
      "name": "Woodway Lane / Henley Rd => Woodway Lane / Henley Rd",
      "length": 0.0007164244063370794,
      "speed": {
        "0:00": 30
      },
      "startid": 370817613,
      "endid": 370817614
    },
    {
      "id": 959,
      "name": "Woodway Lane / Henley Rd => WF",
      "length": 0.007720458497394788,
      "speed": {
        "0:00": 30
      },
      "startid": 370817614,
      "endid": 370817729
    },
    {
      "id": 960,
      "name": "WF => WH",
      "length": 0.00313308919119921,
      "speed": {
        "0:00": 30
      },
      "startid": 370817729,
      "endid": 370817732
    },
    {
      "id": 961,
      "name": "WH => WG",
      "length": 0.000278365084014834,
      "speed": {
        "0:00": 30
      },
      "startid": 370817732,
      "endid": 370817730
    },
    {
      "id": 962,
      "name": "WG => Ansty Rd / Walsgrave Church",
      "length": 0.003265412096506487,
      "speed": {
        "0:00": 30
      },
      "startid": 370817730,
      "endid": 370817584
    },
    {
      "id": 963,
      "name": "Ansty Rd / Walsgrave Church => Ansty Rd / Walsgrave Church",
      "length": 0.0003016658581946437,
      "speed": {
        "0:00": 30
      },
      "startid": 370817584,
      "endid": 370817587
    },
    {
      "id": 964,
      "name": "Ansty Rd / Walsgrave Church => Coventry Road",
      "length": 0.05816428177928438,
      "speed": {
        "0:00": 30
      },
      "startid": 370817587,
      "endid": 487160281
    },
    {
      "id": 965,
      "name": "Coventry Road => Armson Road",
      "length": 0.0018019165907449727,
      "speed": {
        "0:00": 30
      },
      "startid": 487160281,
      "endid": 487160287
    },
    {
      "id": 966,
      "name": "Armson Road => Butlers Crescent",
      "length": 0.0034076568166384025,
      "speed": {
        "0:00": 30
      },
      "startid": 487160287,
      "endid": 487166870
    },
    {
      "id": 967,
      "name": "Butlers Crescent => Jones Road",
      "length": 0.00018893398318178844,
      "speed": {
        "0:00": 30
      },
      "startid": 487166870,
      "endid": 487166874
    },
    {
      "id": 968,
      "name": "Jones Road => Marshall Road",
      "length": 0.0022575600014171655,
      "speed": {
        "0:00": 30
      },
      "startid": 487166874,
      "endid": 487166879
    },
    {
      "id": 969,
      "name": "Marshall Road => Marshall Road",
      "length": 0.0001556540073365487,
      "speed": {
        "0:00": 30
      },
      "startid": 487166879,
      "endid": 487166882
    },
    {
      "id": 970,
      "name": "Windmill Rd / St Thomas' Rd => Blackhorse Road",
      "length": 0.01866992033325566,
      "speed": {
        "0:00": 30
      },
      "startid": 370818859,
      "endid": 487169369
    },
    {
      "id": 971,
      "name": "Cedars Road => Cedars Road",
      "length": 0.00009587251952832346,
      "speed": {
        "0:00": 30
      },
      "startid": 487166701,
      "endid": 487166699
    },
    {
      "id": 972,
      "name": "Cedars Road => Field View Close",
      "length": 0.0020560256151158076,
      "speed": {
        "0:00": 30
      },
      "startid": 487166699,
      "endid": 487169363
    },
    {
      "id": 973,
      "name": "Field View Close => Field View Close",
      "length": 0.0005728722894345266,
      "speed": {
        "0:00": 30
      },
      "startid": 487169363,
      "endid": 487169354
    },
    {
      "id": 974,
      "name": "Field View Close => Hayes Lane",
      "length": 0.0008336227264145015,
      "speed": {
        "0:00": 30
      },
      "startid": 487169354,
      "endid": 487174464
    },
    {
      "id": 975,
      "name": "4674661761 => Woodshires Rd / Glenmore Drive",
      "length": 0.0022547725605931218,
      "speed": {
        "0:00": 30
      },
      "startid": 4674661761,
      "endid": 370819600
    },
    {
      "id": 976,
      "name": "Woodshires Rd / Glenmore Drive => Wilsons Lane / Woodshires Rd",
      "length": 0.0022931043696310625,
      "speed": {
        "0:00": 30
      },
      "startid": 370819600,
      "endid": 370818692
    },
    {
      "id": 977,
      "name": "Wilsons Lane / Woodshires Rd => Bedworth Rd / Oban Rd",
      "length": 0.006341556664574085,
      "speed": {
        "0:00": 30
      },
      "startid": 370818692,
      "endid": 370818877
    },
    {
      "id": 978,
      "name": "Bedworth Rd / Oban Rd => Longford Rd / Longford Square",
      "length": 0.0026911415013017555,
      "speed": {
        "0:00": 30
      },
      "startid": 370818877,
      "endid": 370818874
    },
    {
      "id": 979,
      "name": "Longford Rd / Longford Square => Longford Rd / Longford Square",
      "length": 0.0003155618639778003,
      "speed": {
        "0:00": 30
      },
      "startid": 370818874,
      "endid": 370818873
    },
    {
      "id": 980,
      "name": "Longford Rd / Longford Square => Longford Rd / Vinecote Rd",
      "length": 0.0027949190256651227,
      "speed": {
        "0:00": 30
      },
      "startid": 370818873,
      "endid": 370818872
    },
    {
      "id": 981,
      "name": "Longford Rd / Vinecote Rd => Longford Rd / Oakmoor Rd",
      "length": 0.0011475531403839034,
      "speed": {
        "0:00": 30
      },
      "startid": 370818872,
      "endid": 370818871
    },
    {
      "id": 982,
      "name": "Longford Rd / Oakmoor Rd => Longford Rd / Longford Bridge",
      "length": 0.0032066862163273296,
      "speed": {
        "0:00": 30
      },
      "startid": 370818871,
      "endid": 370819748
    },
    {
      "id": 983,
      "name": "Longford Rd / Longford Bridge => Longford Rd / Windmill Rd",
      "length": 0.0014970952808711533,
      "speed": {
        "0:00": 30
      },
      "startid": 370819748,
      "endid": 370819732
    },
    {
      "id": 984,
      "name": "Longford Rd / Windmill Rd => Longford Rd / Dovedale Avenue",
      "length": 0.0010496597639259562,
      "speed": {
        "0:00": 30
      },
      "startid": 370819732,
      "endid": 370818870
    },
    {
      "id": 985,
      "name": "Longford Rd / Dovedale Avenue => AG",
      "length": 0.0021072323103976083,
      "speed": {
        "0:00": 30
      },
      "startid": 370818870,
      "endid": 370818869
    },
    {
      "id": 986,
      "name": "AG => AF",
      "length": 0.0008466729474816734,
      "speed": {
        "0:00": 30
      },
      "startid": 370818869,
      "endid": 370818867
    },
    {
      "id": 987,
      "name": "AF => Foleshill Rd / The Wheatsheaf",
      "length": 0.001456813598235208,
      "speed": {
        "0:00": 30
      },
      "startid": 370818867,
      "endid": 370818864
    },
    {
      "id": 988,
      "name": "Foleshill Rd / The Wheatsheaf => Foleshill Rd / The Wheatsheaf",
      "length": 0.00031738230889481126,
      "speed": {
        "0:00": 30
      },
      "startid": 370818864,
      "endid": 370818865
    },
    {
      "id": 989,
      "name": "Foleshill Rd / The Wheatsheaf => Foleshill Rd / Old Church Rd",
      "length": 0.0031598401984935013,
      "speed": {
        "0:00": 30
      },
      "startid": 370818865,
      "endid": 370818863
    },
    {
      "id": 990,
      "name": "Foleshill Rd / Old Church Rd => Foleshill Rd / Old Church Rd",
      "length": 0.0003347000000000211,
      "speed": {
        "0:00": 30
      },
      "startid": 370818863,
      "endid": 370818862
    },
    {
      "id": 991,
      "name": "Foleshill Rd / Old Church Rd => Foleshill Rd / Phoenix Way",
      "length": 0.0035533042270538776,
      "speed": {
        "0:00": 30
      },
      "startid": 370818862,
      "endid": 370818832
    },
    {
      "id": 992,
      "name": "Foleshill Rd / Phoenix Way => Foleshill Rd / Phoenix Way",
      "length": 0.0002803520108717694,
      "speed": {
        "0:00": 30
      },
      "startid": 370818832,
      "endid": 370818834
    },
    {
      "id": 993,
      "name": "Foleshill Rd / Phoenix Way => Foleshill Rd / Cross Rd",
      "length": 0.0016837137820924367,
      "speed": {
        "0:00": 30
      },
      "startid": 370818834,
      "endid": 370818830
    },
    {
      "id": 994,
      "name": "Foleshill Rd / Cross Rd => Foleshill Rd / Cross Rd",
      "length": 0.0004945206264681952,
      "speed": {
        "0:00": 30
      },
      "startid": 370818830,
      "endid": 370818831
    },
    {
      "id": 995,
      "name": "Foleshill Rd / Cross Rd => Foleshill Rd / Family Centre",
      "length": 0.0026930447174148245,
      "speed": {
        "0:00": 30
      },
      "startid": 370818831,
      "endid": 370819702
    },
    {
      "id": 996,
      "name": "Foleshill Rd / Family Centre => Foleshill Rd / Family Centre",
      "length": 0.00016455625178377943,
      "speed": {
        "0:00": 30
      },
      "startid": 370819702,
      "endid": 370819703
    },
    {
      "id": 997,
      "name": "Foleshill Rd / Family Centre => Foleshill Rd / Station St",
      "length": 0.0014088894953136236,
      "speed": {
        "0:00": 30
      },
      "startid": 370819703,
      "endid": 370818829
    },
    {
      "id": 998,
      "name": "Foleshill Rd / Station St => Foleshill Rd / Station St",
      "length": 0.0013386575364890566,
      "speed": {
        "0:00": 30
      },
      "startid": 370818829,
      "endid": 370818827
    },
    {
      "id": 999,
      "name": "Foleshill Rd / Station St => Foleshill Rd / Broad St",
      "length": 0.0028052413532526385,
      "speed": {
        "0:00": 30
      },
      "startid": 370818827,
      "endid": 370818825
    },
    {
      "id": 1000,
      "name": "Foleshill Rd / Broad St => Foleshill Rd / Broad St",
      "length": 0.00038016818646532426,
      "speed": {
        "0:00": 30
      },
      "startid": 370818825,
      "endid": 370818826
    },
    {
      "id": 1001,
      "name": "Foleshill Rd / Broad St => Foleshill Rd / Courtaulds Way",
      "length": 0.004239609710810101,
      "speed": {
        "0:00": 30
      },
      "startid": 370818826,
      "endid": 370818780
    },
    {
      "id": 1002,
      "name": "Foleshill Rd / Courtaulds Way => Foleshill Rd / Courtaulds Way",
      "length": 0.00035180778843009035,
      "speed": {
        "0:00": 30
      },
      "startid": 370818780,
      "endid": 370818784
    },
    {
      "id": 1003,
      "name": "Foleshill Rd / Courtaulds Way => Foleshill Rd / Cashs Lane",
      "length": 0.004273169018420262,
      "speed": {
        "0:00": 30
      },
      "startid": 370818784,
      "endid": 370818776
    },
    {
      "id": 1004,
      "name": "Foleshill Rd / Cashs Lane => Foleshill Rd / Cashs Lane",
      "length": 0.00022125555360341274,
      "speed": {
        "0:00": 30
      },
      "startid": 370818776,
      "endid": 370818774
    },
    {
      "id": 1005,
      "name": "Foleshill Rd / Cashs Lane => Foleshill Rd / Eagle St",
      "length": 0.0011237341055589636,
      "speed": {
        "0:00": 30
      },
      "startid": 370818774,
      "endid": 370818765
    },
    {
      "id": 1006,
      "name": "Foleshill Rd / Eagle St => Foleshill Rd / Eagle St",
      "length": 0.001522061907418469,
      "speed": {
        "0:00": 30
      },
      "startid": 370818765,
      "endid": 370818766
    },
    {
      "id": 1007,
      "name": "Foleshill Rd / Eagle St => Foleshill Rd / City Engineers",
      "length": 0.0027907170565999295,
      "speed": {
        "0:00": 30
      },
      "startid": 370818766,
      "endid": 370818762
    },
    {
      "id": 1008,
      "name": "Foleshill Rd / City Engineers => Foleshill Rd / City Engineers",
      "length": 0.00022393115013730707,
      "speed": {
        "0:00": 30
      },
      "startid": 370818762,
      "endid": 370818764
    },
    {
      "id": 1009,
      "name": "Foleshill Rd / City Engineers => Foleshill Rd / Leicester Row",
      "length": 0.0016005044017478598,
      "speed": {
        "0:00": 30
      },
      "startid": 370818764,
      "endid": 370818761
    },
    {
      "id": 1010,
      "name": "Foleshill Rd / Leicester Row => Foleshill Rd / Leicester Row",
      "length": 0.00040428367515873303,
      "speed": {
        "0:00": 30
      },
      "startid": 370818761,
      "endid": 370818758
    },
    {
      "id": 1011,
      "name": "Foleshill Rd / Leicester Row => BS1",
      "length": 0.003915537353925627,
      "speed": {
        "0:00": 30
      },
      "startid": 370818758,
      "endid": 370817728
    },
    {
      "id": 1012,
      "name": "BS1 => BS2",
      "length": 0.0006854744707142306,
      "speed": {
        "0:00": 30
      },
      "startid": 370817728,
      "endid": 370817727
    },
    {
      "id": 1013,
      "name": "BS2 => TS4",
      "length": 0.002139564165897073,
      "speed": {
        "0:00": 30
      },
      "startid": 370817727,
      "endid": 370817662
    },
    {
      "id": 1014,
      "name": "CU5 => CU1",
      "length": 0.0021117262535691986,
      "speed": {
        "0:00": 30
      },
      "startid": 370819676,
      "endid": 370817766
    },
    {
      "id": 1015,
      "name": "CU1 => CU2",
      "length": 0.00010206831045847219,
      "speed": {
        "0:00": 30
      },
      "startid": 370817766,
      "endid": 370819680
    },
    {
      "id": 1016,
      "name": "CU2 => Walsgrave Rd / Swan Lane",
      "length": 0.013072843649719269,
      "speed": {
        "0:00": 30
      },
      "startid": 370819680,
      "endid": 370817464
    },
    {
      "id": 1017,
      "name": "Walsgrave Rd / Swan Lane => Walsgrave Rd / Swan Lane",
      "length": 0.0017645372707868672,
      "speed": {
        "0:00": 30
      },
      "startid": 370817464,
      "endid": 370817463
    },
    {
      "id": 1018,
      "name": "Walsgrave Rd / Swan Lane => Walsgrave Rd / Clements St",
      "length": 0.0030988222827398773,
      "speed": {
        "0:00": 30
      },
      "startid": 370817463,
      "endid": 370817467
    },
    {
      "id": 1019,
      "name": "Walsgrave Rd / Clements St => Walsgrave Rd / Clements St",
      "length": 0.0005896212004330483,
      "speed": {
        "0:00": 30
      },
      "startid": 370817467,
      "endid": 370817465
    },
    {
      "id": 1020,
      "name": "Walsgrave Rd / Clements St => Walsgrave Rd / Harefield Rd",
      "length": 0.00521431387624442,
      "speed": {
        "0:00": 30
      },
      "startid": 370817465,
      "endid": 370817501
    },
    {
      "id": 1021,
      "name": "Walsgrave Rd / Harefield Rd => Walsgrave Rd / Harefield Rd",
      "length": 0.0006063554485614267,
      "speed": {
        "0:00": 30
      },
      "startid": 370817501,
      "endid": 370817500
    },
    {
      "id": 1022,
      "name": "Walsgrave Rd / Harefield Rd => Walsgrave Rd / Burns Rd",
      "length": 0.0036222750930872813,
      "speed": {
        "0:00": 30
      },
      "startid": 370817500,
      "endid": 370817504
    },
    {
      "id": 1023,
      "name": "Walsgrave Rd / Burns Rd => Walsgrave Rd / Burns Rd",
      "length": 0.0015216241651606255,
      "speed": {
        "0:00": 30
      },
      "startid": 370817504,
      "endid": 370817502
    },
    {
      "id": 1024,
      "name": "Walsgrave Rd / Burns Rd => Ansty Rd / Dane Rd",
      "length": 0.003590546539177356,
      "speed": {
        "0:00": 30
      },
      "startid": 370817502,
      "endid": 370817521
    },
    {
      "id": 1025,
      "name": "Ansty Rd / Dane Rd => Ansty Rd / Dane Rd",
      "length": 0.0005844890075955145,
      "speed": {
        "0:00": 30
      },
      "startid": 370817521,
      "endid": 370817522
    },
    {
      "id": 1026,
      "name": "Ansty Rd / Dane Rd => Ansty Rd / Mellowdew Rd",
      "length": 0.0019575913567442286,
      "speed": {
        "0:00": 30
      },
      "startid": 370817522,
      "endid": 370817524
    },
    {
      "id": 1027,
      "name": "Ansty Rd / Mellowdew Rd => Ansty Rd / Mellowdew Rd",
      "length": 0.0011267458630953426,
      "speed": {
        "0:00": 30
      },
      "startid": 370817524,
      "endid": 370817526
    },
    {
      "id": 1028,
      "name": "Ansty Rd / Mellowdew Rd => Ansty Rd / Morris Avenue",
      "length": 0.0028913000017288313,
      "speed": {
        "0:00": 30
      },
      "startid": 370817526,
      "endid": 370817620
    },
    {
      "id": 1029,
      "name": "Ansty Rd / Morris Avenue => Ansty Rd / Morris Avenue",
      "length": 0.000945145517896747,
      "speed": {
        "0:00": 30
      },
      "startid": 370817620,
      "endid": 370817621
    },
    {
      "id": 1030,
      "name": "Ansty Rd / Morris Avenue => Ansty Rd / Hipswell Highway",
      "length": 0.004199777155992796,
      "speed": {
        "0:00": 30
      },
      "startid": 370817621,
      "endid": 370817527
    },
    {
      "id": 1031,
      "name": "Ansty Rd / Hipswell Highway => Ansty Rd / Hipswell Highway",
      "length": 0.001124690188452074,
      "speed": {
        "0:00": 30
      },
      "startid": 370817527,
      "endid": 370817528
    },
    {
      "id": 1032,
      "name": "Ansty Rd / Hipswell Highway => Ansty Rd / Arch Rd",
      "length": 0.004807771429676437,
      "speed": {
        "0:00": 30
      },
      "startid": 370817528,
      "endid": 370817531
    },
    {
      "id": 1033,
      "name": "Ansty Rd / Arch Rd => Ansty Rd / Arch Rd",
      "length": 0.001321381398385821,
      "speed": {
        "0:00": 30
      },
      "startid": 370817531,
      "endid": 370817532
    },
    {
      "id": 1034,
      "name": "Ansty Rd / Arch Rd => Ansty Rd / Norton Hill Drive",
      "length": 0.0027710291896699047,
      "speed": {
        "0:00": 30
      },
      "startid": 370817532,
      "endid": 370817581
    },
    {
      "id": 1035,
      "name": "Ansty Rd / Norton Hill Drive => Ansty Rd / Norton Hill Drive",
      "length": 0.0008620050695904217,
      "speed": {
        "0:00": 30
      },
      "startid": 370817581,
      "endid": 370817583
    },
    {
      "id": 1036,
      "name": "Ansty Rd / Norton Hill Drive => Ansty Rd / Clifford Bridge Rd",
      "length": 0.0030995913359663616,
      "speed": {
        "0:00": 30
      },
      "startid": 370817583,
      "endid": 370817629
    },
    {
      "id": 1037,
      "name": "Ansty Rd / Clifford Bridge Rd => Ansty Rd / Clifford Bridge Rd",
      "length": 0.0004618862630562424,
      "speed": {
        "0:00": 30
      },
      "startid": 370817629,
      "endid": 370817630
    },
    {
      "id": 1038,
      "name": "Ansty Rd / Clifford Bridge Rd => Ansty Rd / Walsgrave Church",
      "length": 0.005442802955280496,
      "speed": {
        "0:00": 30
      },
      "startid": 370817630,
      "endid": 370817587
    },
    {
      "id": 1039,
      "name": "Ansty Rd / Walsgrave Church => Ansty Rd / Walsgrave Church",
      "length": 0.0003016658581946437,
      "speed": {
        "0:00": 30
      },
      "startid": 370817587,
      "endid": 370817584
    },
    {
      "id": 1040,
      "name": "Ansty Rd / Walsgrave Church => Woodway Lane / Henley Rd",
      "length": 0.003928488830327353,
      "speed": {
        "0:00": 30
      },
      "startid": 370817584,
      "endid": 370817614
    },
    {
      "id": 1041,
      "name": "Woodway Lane / Henley Rd => Woodway Lane / Henley Rd",
      "length": 0.0007164244063370794,
      "speed": {
        "0:00": 30
      },
      "startid": 370817614,
      "endid": 370817613
    },
    {
      "id": 1042,
      "name": "Woodway Lane / Henley Rd => Woodway Lane / Woodway Walk",
      "length": 0.0031015658319662616,
      "speed": {
        "0:00": 30
      },
      "startid": 370817613,
      "endid": 370817616
    },
    {
      "id": 1043,
      "name": "Woodway Lane / Woodway Walk => Woodway Lane / Woodway Walk",
      "length": 0.00015028965366803217,
      "speed": {
        "0:00": 30
      },
      "startid": 370817616,
      "endid": 370817617
    },
    {
      "id": 1044,
      "name": "Woodway Lane / Woodway Walk => Woodway Lane / Potters Green Rd",
      "length": 0.004838284081160959,
      "speed": {
        "0:00": 30
      },
      "startid": 370817617,
      "endid": 370817618
    },
    {
      "id": 1045,
      "name": "Woodway Lane / Potters Green Rd => Woodway Lane / Potters Green Rd",
      "length": 0.0006930219404853976,
      "speed": {
        "0:00": 30
      },
      "startid": 370817618,
      "endid": 370817619
    },
    {
      "id": 1046,
      "name": "Woodway Lane / Potters Green Rd => Ringwood Highway / Potters Green Primary School",
      "length": 0.0021865191629648964,
      "speed": {
        "0:00": 30
      },
      "startid": 370817619,
      "endid": 370817605
    },
    {
      "id": 1047,
      "name": "Ringwood Highway / Potters Green Primary School => Parkway / Parkway Island",
      "length": 0.017986836831973635,
      "speed": {
        "0:00": 30
      },
      "startid": 370817605,
      "endid": 370818753
    },
    {
      "id": 1048,
      "name": "Parkway / Parkway Island => Parkway / Parkway Island",
      "length": 0.0005167718258571753,
      "speed": {
        "0:00": 30
      },
      "startid": 370818753,
      "endid": 370818754
    },
    {
      "id": 1049,
      "name": "Parkway / Parkway Island => Wigston Rd / Macdonalds",
      "length": 0.00616987517296901,
      "speed": {
        "0:00": 30
      },
      "startid": 370818754,
      "endid": 370819822
    },
    {
      "id": 1050,
      "name": "Wigston Rd / Macdonalds => Wigston Rd / Macdonalds",
      "length": 0.00030607796392459756,
      "speed": {
        "0:00": 30
      },
      "startid": 370819822,
      "endid": 370819820
    },
    {
      "id": 1051,
      "name": "Wigston Rd / Macdonalds => Wigston Rd / Leven Way",
      "length": 0.002826446569456594,
      "speed": {
        "0:00": 30
      },
      "startid": 370819820,
      "endid": 370817596
    },
    {
      "id": 1052,
      "name": "Wigston Rd / Leven Way => Wigston Rd / Leven Way",
      "length": 0.0018455821330939115,
      "speed": {
        "0:00": 30
      },
      "startid": 370817596,
      "endid": 370817594
    },
    {
      "id": 1053,
      "name": "Wigston Rd / Leven Way => Wigston Rd / Deanston Croft",
      "length": 0.002542038758559566,
      "speed": {
        "0:00": 30
      },
      "startid": 370817594,
      "endid": 370817598
    },
    {
      "id": 1054,
      "name": "Wigston Rd / Deanston Croft => Wigston Rd / Grace Academy",
      "length": 0.002103014355633351,
      "speed": {
        "0:00": 30
      },
      "startid": 370817598,
      "endid": 370817600
    },
    {
      "id": 1055,
      "name": "Wigston Rd / Grace Academy => Wigston Rd / Grace Academy",
      "length": 0.0008319727038791563,
      "speed": {
        "0:00": 30
      },
      "startid": 370817600,
      "endid": 370817601
    },
    {
      "id": 1056,
      "name": "Wigston Rd / Grace Academy => CU4",
      "length": 0.06454913482867135,
      "speed": {
        "0:00": 30
      },
      "startid": 370817601,
      "endid": 370819679
    },
    {
      "id": 1057,
      "name": "CU4 => Olivier Way / Showcase Cinema & Megabowl",
      "length": 0.07742662524958484,
      "speed": {
        "0:00": 30
      },
      "startid": 370819679,
      "endid": 370818749
    },
    {
      "id": 1058,
      "name": "Olivier Way / Showcase Cinema & Megabowl => P",
      "length": 0.0808415678846584,
      "speed": {
        "0:00": 30
      },
      "startid": 370818749,
      "endid": 370817747
    },
    {
      "id": 1059,
      "name": "P => Q",
      "length": 0.00030688020463805893,
      "speed": {
        "0:00": 30
      },
      "startid": 370817747,
      "endid": 370817749
    },
    {
      "id": 1060,
      "name": "Q => BS3",
      "length": 0.0038994414176904083,
      "speed": {
        "0:00": 30
      },
      "startid": 370817749,
      "endid": 370817695
    },
    {
      "id": 1061,
      "name": "BS3 => Sky Blue Way / Walkway To Gosford St",
      "length": 0.01570945654979733,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 4815874919
    },
    {
      "id": 1062,
      "name": "Sky Blue Way / Walkway To Gosford St => Sky Blue Way / Gosford Green",
      "length": 0.0029580316495925675,
      "speed": {
        "0:00": 30
      },
      "startid": 4815874919,
      "endid": 4815880373
    },
    {
      "id": 1063,
      "name": "Sky Blue Way / Gosford Green => Sky Blue Way / Gosford Green",
      "length": 0.0003139044440539605,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880373,
      "endid": 4815880374
    },
    {
      "id": 1064,
      "name": "Sky Blue Way / Gosford Green => FX1",
      "length": 0.01127751991574347,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880374,
      "endid": 370817768
    },
    {
      "id": 1065,
      "name": "FX1 => UL3",
      "length": 0.009610634942604229,
      "speed": {
        "0:00": 30
      },
      "startid": 370817768,
      "endid": 370817723
    },
    {
      "id": 1066,
      "name": "UL3 => UL4",
      "length": 0.00031591698276652307,
      "speed": {
        "0:00": 30
      },
      "startid": 370817723,
      "endid": 370817719
    },
    {
      "id": 1067,
      "name": "UL4 => Holyhead Rd / Ringway",
      "length": 0.006236031257939766,
      "speed": {
        "0:00": 30
      },
      "startid": 370817719,
      "endid": 370819355
    },
    {
      "id": 1068,
      "name": "Holyhead Rd / Ringway => Holyhead Rd / Ringway",
      "length": 0.0001523425416673504,
      "speed": {
        "0:00": 30
      },
      "startid": 370819355,
      "endid": 370819357
    },
    {
      "id": 1069,
      "name": "Holyhead Rd / Ringway => Holyhead Rd / Meriden St",
      "length": 0.0024659519865556133,
      "speed": {
        "0:00": 30
      },
      "startid": 370819357,
      "endid": 370819360
    },
    {
      "id": 1070,
      "name": "Holyhead Rd / Meriden St => Holyhead Rd / Meriden St",
      "length": 0.0008530438792932072,
      "speed": {
        "0:00": 30
      },
      "startid": 370819360,
      "endid": 370819359
    },
    {
      "id": 1071,
      "name": "Holyhead Rd / Meriden St => Holyhead Rd / Alvis Retail Park",
      "length": 0.006018893655815038,
      "speed": {
        "0:00": 30
      },
      "startid": 370819359,
      "endid": 370819363
    },
    {
      "id": 1072,
      "name": "Holyhead Rd / Alvis Retail Park => Holyhead Rd / Alvis Retail Park",
      "length": 0.0002442421953716176,
      "speed": {
        "0:00": 30
      },
      "startid": 370819363,
      "endid": 370819361
    },
    {
      "id": 1073,
      "name": "Holyhead Rd / Alvis Retail Park => Four Pounds Ave / Stepping Stones Rd",
      "length": 0.003542406353031694,
      "speed": {
        "0:00": 30
      },
      "startid": 370819361,
      "endid": 370819400
    },
    {
      "id": 1074,
      "name": "Four Pounds Ave / Stepping Stones Rd => Four Pounds Ave / Stepping Stones Rd",
      "length": 0.0007076708062391888,
      "speed": {
        "0:00": 30
      },
      "startid": 370819400,
      "endid": 370819402
    },
    {
      "id": 1075,
      "name": "Four Pounds Ave / Stepping Stones Rd => Four Pounds Ave / Prince Of Wales Rd",
      "length": 0.0050199410853109935,
      "speed": {
        "0:00": 30
      },
      "startid": 370819402,
      "endid": 370819406
    },
    {
      "id": 1076,
      "name": "Four Pounds Ave / Prince Of Wales Rd => Four Pounds Ave / Prince Of Wales Rd",
      "length": 0.0002627699373970591,
      "speed": {
        "0:00": 30
      },
      "startid": 370819406,
      "endid": 370819403
    },
    {
      "id": 1077,
      "name": "Four Pounds Ave / Prince Of Wales Rd => Allesley Old Rd / Maudslay Rd",
      "length": 0.0034029024743594395,
      "speed": {
        "0:00": 30
      },
      "startid": 370819403,
      "endid": 370819412
    },
    {
      "id": 1078,
      "name": "Allesley Old Rd / Maudslay Rd => Allesley Old Rd / Maudslay Rd",
      "length": 0.000531371809565509,
      "speed": {
        "0:00": 30
      },
      "startid": 370819412,
      "endid": 370819413
    },
    {
      "id": 1079,
      "name": "Allesley Old Rd / Maudslay Rd => Allesley Old Rd / Billing Rd",
      "length": 0.0041417317006282066,
      "speed": {
        "0:00": 30
      },
      "startid": 370819413,
      "endid": 370818150
    },
    {
      "id": 1080,
      "name": "Allesley Old Rd / Billing Rd => Allesley Old Rd / Billing Rd",
      "length": 0.0010952660407406464,
      "speed": {
        "0:00": 30
      },
      "startid": 370818150,
      "endid": 370818154
    },
    {
      "id": 1081,
      "name": "Allesley Old Rd / Billing Rd => Allesley Old Rd / Oldfield Rd",
      "length": 0.001976047400749496,
      "speed": {
        "0:00": 30
      },
      "startid": 370818154,
      "endid": 370819418
    },
    {
      "id": 1082,
      "name": "Allesley Old Rd / Oldfield Rd => Allesley Old Rd / Oldfield Rd",
      "length": 0.0016390592210153375,
      "speed": {
        "0:00": 30
      },
      "startid": 370819418,
      "endid": 370819420
    },
    {
      "id": 1083,
      "name": "Allesley Old Rd / Oldfield Rd => Winsford Ave / Torbay Rd",
      "length": 0.003461318760242941,
      "speed": {
        "0:00": 30
      },
      "startid": 370819420,
      "endid": 370819438
    },
    {
      "id": 1084,
      "name": "Winsford Ave / Torbay Rd => Winsford Ave / Torbay Rd",
      "length": 0.0006442830589105463,
      "speed": {
        "0:00": 30
      },
      "startid": 370819438,
      "endid": 370819439
    },
    {
      "id": 1085,
      "name": "Winsford Ave / Torbay Rd => Winsford Ave / Ashbridge Rd",
      "length": 0.003004248395189595,
      "speed": {
        "0:00": 30
      },
      "startid": 370819439,
      "endid": 370819440
    },
    {
      "id": 1086,
      "name": "Winsford Ave / Ashbridge Rd => Winsford Ave / Ashbridge Rd",
      "length": 0.0007835176705091614,
      "speed": {
        "0:00": 30
      },
      "startid": 370819440,
      "endid": 370819441
    },
    {
      "id": 1087,
      "name": "Winsford Ave / Ashbridge Rd => Winsford Ave / Wendover Rise",
      "length": 0.004722880448412754,
      "speed": {
        "0:00": 30
      },
      "startid": 370819441,
      "endid": 370819443
    },
    {
      "id": 1088,
      "name": "Winsford Ave / Wendover Rise => Winsford Ave / Wendover Rise",
      "length": 0.000743058180763111,
      "speed": {
        "0:00": 30
      },
      "startid": 370819443,
      "endid": 370819444
    },
    {
      "id": 1089,
      "name": "Winsford Ave / Wendover Rise => Winsford Ave / Frilsham Way",
      "length": 0.0035808360937093987,
      "speed": {
        "0:00": 30
      },
      "startid": 370819444,
      "endid": 370819504
    },
    {
      "id": 1090,
      "name": "Winsford Ave / Frilsham Way => Winsford Ave / Frilsham Way",
      "length": 0.0006174624280073454,
      "speed": {
        "0:00": 30
      },
      "startid": 370819504,
      "endid": 370819502
    },
    {
      "id": 1091,
      "name": "Winsford Ave / Frilsham Way => Winsford Ave / The Chilterns",
      "length": 0.0025139168502562384,
      "speed": {
        "0:00": 30
      },
      "startid": 370819502,
      "endid": 370819445
    },
    {
      "id": 1092,
      "name": "Winsford Ave / The Chilterns => BS5",
      "length": 0.05141328793463762,
      "speed": {
        "0:00": 30
      },
      "startid": 370819445,
      "endid": 370817666
    },
    {
      "id": 1093,
      "name": "Jobs Lane / Lime Tree Ave => CS1",
      "length": 0.05815434452575245,
      "speed": {
        "0:00": 30
      },
      "startid": 4815881222,
      "endid": 370817698
    },
    {
      "id": 1094,
      "name": "CS1 => CR2",
      "length": 0.003280321624474374,
      "speed": {
        "0:00": 30
      },
      "startid": 370817698,
      "endid": 370817811
    },
    {
      "id": 1095,
      "name": "CR2 => Butts Radial Link / Albany Rd",
      "length": 0.005168403206019783,
      "speed": {
        "0:00": 30
      },
      "startid": 370817811,
      "endid": 370817816
    },
    {
      "id": 1096,
      "name": "Butts Radial Link / Albany Rd => Butts Radial Link / Albany Rd",
      "length": 0.0017027777688234339,
      "speed": {
        "0:00": 30
      },
      "startid": 370817816,
      "endid": 370817814
    },
    {
      "id": 1097,
      "name": "Butts Radial Link / Albany Rd => Spon End / The Arches",
      "length": 0.004784828060651391,
      "speed": {
        "0:00": 30
      },
      "startid": 370817814,
      "endid": 370818019
    },
    {
      "id": 1098,
      "name": "Spon End / The Arches => Spon End / The Arches",
      "length": 0.00015506108474010497,
      "speed": {
        "0:00": 30
      },
      "startid": 370818019,
      "endid": 370818021
    },
    {
      "id": 1099,
      "name": "Spon End / The Arches => Hearsall Lane / Farman Rd",
      "length": 0.004305751897173334,
      "speed": {
        "0:00": 30
      },
      "startid": 370818021,
      "endid": 370818039
    },
    {
      "id": 1100,
      "name": "Hearsall Lane / Farman Rd => Hearsall Lane / Farman Rd",
      "length": 0.00020274560414026315,
      "speed": {
        "0:00": 30
      },
      "startid": 370818039,
      "endid": 370818036
    },
    {
      "id": 1101,
      "name": "Hearsall Lane / Farman Rd => Hearsall Common / Earlsdon Ave North",
      "length": 0.005212303636589388,
      "speed": {
        "0:00": 30
      },
      "startid": 370818036,
      "endid": 370818127
    },
    {
      "id": 1102,
      "name": "Hearsall Common / Earlsdon Ave North => Hearsall Lane / Queensland Avenue",
      "length": 0.0025661573392898904,
      "speed": {
        "0:00": 30
      },
      "startid": 370818127,
      "endid": 370819672
    },
    {
      "id": 1103,
      "name": "Hearsall Lane / Queensland Avenue => Tile Hill Lane / Hearsall Common",
      "length": 0.008118906370933264,
      "speed": {
        "0:00": 30
      },
      "startid": 370819672,
      "endid": 370818854
    },
    {
      "id": 1104,
      "name": "Tile Hill Lane / Hearsall Common => Tile Hill Lane / Hearsall Common",
      "length": 0.0010889620838209612,
      "speed": {
        "0:00": 30
      },
      "startid": 370818854,
      "endid": 370818853
    },
    {
      "id": 1105,
      "name": "Tile Hill Lane / Hearsall Common => Tile Hill Lane / Brd Lane",
      "length": 0.004768650479957528,
      "speed": {
        "0:00": 30
      },
      "startid": 370818853,
      "endid": 370818159
    },
    {
      "id": 1106,
      "name": "Tile Hill Lane / Brd Lane => Tile Hill Lane / Broad Lane",
      "length": 0.00033008995743662075,
      "speed": {
        "0:00": 30
      },
      "startid": 370818159,
      "endid": 370818157
    },
    {
      "id": 1107,
      "name": "Tile Hill Lane / Broad Lane => Tile Hill Lane / Stewart Close",
      "length": 0.005184375437793909,
      "speed": {
        "0:00": 30
      },
      "startid": 370818157,
      "endid": 370817711
    },
    {
      "id": 1108,
      "name": "Tile Hill Lane / Stewart Close => Tile Hill Lane / Fletchamstead Highway",
      "length": 0.007400540501882298,
      "speed": {
        "0:00": 30
      },
      "startid": 370817711,
      "endid": 370818174
    },
    {
      "id": 1109,
      "name": "Tile Hill Lane / Fletchamstead Highway => Tile Hill Lane / Fletchamstead Highway",
      "length": 0.0001837258827754596,
      "speed": {
        "0:00": 30
      },
      "startid": 370818174,
      "endid": 370818176
    },
    {
      "id": 1110,
      "name": "Tile Hill Lane / Fletchamstead Highway => Tile Hill Lane / Sainsburys Supermarket",
      "length": 0.003935641513146247,
      "speed": {
        "0:00": 30
      },
      "startid": 370818176,
      "endid": 370817406
    },
    {
      "id": 1111,
      "name": "Tile Hill Lane / Sainsburys Supermarket => Tile Hill Lane / Middlecotes",
      "length": 0.007280354437113521,
      "speed": {
        "0:00": 30
      },
      "startid": 370817406,
      "endid": 370818178
    },
    {
      "id": 1112,
      "name": "Tile Hill Lane / Middlecotes => Tile Hill Lane / Westcotes",
      "length": 0.0014775972692168422,
      "speed": {
        "0:00": 30
      },
      "startid": 370818178,
      "endid": 370817965
    },
    {
      "id": 1113,
      "name": "Tile Hill Lane / Malam Close => Jobs Lane / Lime Tree Ave",
      "length": 0.0037313349514625765,
      "speed": {
        "0:00": 30
      },
      "startid": 370819554,
      "endid": 370817770
    },
    {
      "id": 1114,
      "name": "Jobs Lane / Lime Tree Ave => Jardine Cres / Tile Hill North Terminus",
      "length": 0.003253505718453385,
      "speed": {
        "0:00": 30
      },
      "startid": 370817770,
      "endid": 370818246
    },
    {
      "id": 1115,
      "name": "Jardine Cres / Tile Hill North Terminus => Jardine Cres / Tile Hill North Terminus",
      "length": 0.0001506872589189024,
      "speed": {
        "0:00": 30
      },
      "startid": 370818246,
      "endid": 370818245
    },
    {
      "id": 1116,
      "name": "Jardine Cres / Tile Hill North Terminus => Jardine Cres / Shopping Centre",
      "length": 0.0031497679422460506,
      "speed": {
        "0:00": 30
      },
      "startid": 370818245,
      "endid": 370818242
    },
    {
      "id": 1117,
      "name": "Jardine Cres / Shopping Centre => Jardine Cres / Shopping Centre",
      "length": 0.00047158156240413373,
      "speed": {
        "0:00": 30
      },
      "startid": 370818242,
      "endid": 370818241
    },
    {
      "id": 1118,
      "name": "Jardine Cres / Shopping Centre => Jardine Cres / Tile Hill Library",
      "length": 0.0013733965632693602,
      "speed": {
        "0:00": 30
      },
      "startid": 370818241,
      "endid": 370818240
    },
    {
      "id": 1119,
      "name": "Jardine Cres / Tile Hill Library => Jardine Cres / Tile Hill Library",
      "length": 0.0007638431318011407,
      "speed": {
        "0:00": 30
      },
      "startid": 370818240,
      "endid": 370818238
    },
    {
      "id": 1120,
      "name": "Jardine Cres / Tile Hill Library => Jardine Cres / Faseman Ave",
      "length": 0.0020893628693955915,
      "speed": {
        "0:00": 30
      },
      "startid": 370818238,
      "endid": 370819767
    },
    {
      "id": 1121,
      "name": "Jardine Cres / Faseman Ave => Jardine Cres / Faseman Ave",
      "length": 0.001120791332049032,
      "speed": {
        "0:00": 30
      },
      "startid": 370819767,
      "endid": 370819768
    },
    {
      "id": 1122,
      "name": "Jardine Cres / Faseman Ave => Jardine Cres / Coleman St",
      "length": 0.0019029404641286332,
      "speed": {
        "0:00": 30
      },
      "startid": 370819768,
      "endid": 370819341
    },
    {
      "id": 1123,
      "name": "Jardine Cres / Coleman St => Jardine Cres / Coleman St",
      "length": 0.0003622436334845222,
      "speed": {
        "0:00": 30
      },
      "startid": 370819341,
      "endid": 370819342
    },
    {
      "id": 1124,
      "name": "Jardine Cres / Coleman St => Broad Lane / Eastern Green Rd",
      "length": 0.0007862191615536772,
      "speed": {
        "0:00": 30
      },
      "startid": 370819342,
      "endid": 370818227
    },
    {
      "id": 1125,
      "name": "Broad Lane / Eastern Green Rd => Broad Lane / Vesey & Sharples Works",
      "length": 0.0027755512317384906,
      "speed": {
        "0:00": 30
      },
      "startid": 370818227,
      "endid": 370818264
    },
    {
      "id": 1126,
      "name": "Broad Lane / Vesey & Sharples Works => Broad Lane / Vesey & Sharples Works",
      "length": 0.00043992728944673254,
      "speed": {
        "0:00": 30
      },
      "startid": 370818264,
      "endid": 370818265
    },
    {
      "id": 1127,
      "name": "Broad Lane / Vesey & Sharples Works => Broad Lane / Hawthorn Lane",
      "length": 0.003551304306870963,
      "speed": {
        "0:00": 30
      },
      "startid": 370818265,
      "endid": 370818267
    },
    {
      "id": 1128,
      "name": "Broad Lane / Hawthorn Lane => Broad Lane / Hawthorn Lane",
      "length": 0.0010905285507499046,
      "speed": {
        "0:00": 30
      },
      "startid": 370818267,
      "endid": 370818266
    },
    {
      "id": 1129,
      "name": "Broad Lane / Hawthorn Lane => Broad Lane / The Woodlands School",
      "length": 0.004940104689174536,
      "speed": {
        "0:00": 30
      },
      "startid": 370818266,
      "endid": 370819697
    },
    {
      "id": 1130,
      "name": "Broad Lane / The Woodlands School => Broad Lane / Farcroft Ave",
      "length": 0.0010506175802824705,
      "speed": {
        "0:00": 30
      },
      "startid": 370819697,
      "endid": 370818269
    },
    {
      "id": 1131,
      "name": "Broad Lane / Farcroft Ave => Broad Lane / Farcroft Ave",
      "length": 0.0035981472746404223,
      "speed": {
        "0:00": 30
      },
      "startid": 370818269,
      "endid": 370818270
    },
    {
      "id": 1132,
      "name": "Broad Lane / Farcroft Ave => Banner Lane / Broad Lane",
      "length": 0.0021461271747037418,
      "speed": {
        "0:00": 30
      },
      "startid": 370818270,
      "endid": 370819695
    },
    {
      "id": 1133,
      "name": "Banner Lane / Broad Lane => Banner Lane / Broad Lane",
      "length": 0.0007271705439559529,
      "speed": {
        "0:00": 30
      },
      "startid": 370819695,
      "endid": 370819696
    },
    {
      "id": 1134,
      "name": "Banner Lane / Broad Lane => Banner Lane / Astoria Drive",
      "length": 0.0007634622321989104,
      "speed": {
        "0:00": 30
      },
      "startid": 370819696,
      "endid": 370819329
    },
    {
      "id": 1135,
      "name": "Banner Lane / Astoria Drive => Banner Lane / Astoria Drive",
      "length": 0.0007953226074998468,
      "speed": {
        "0:00": 30
      },
      "startid": 370819329,
      "endid": 370819330
    },
    {
      "id": 1136,
      "name": "Banner Lane / Astoria Drive => Banner Lane / Bannerbrook Park",
      "length": 0.00168801791459928,
      "speed": {
        "0:00": 30
      },
      "startid": 370819330,
      "endid": 370819328
    },
    {
      "id": 1137,
      "name": "Banner Lane / Bannerbrook Park => Banner Lane / Bannerbrook Park",
      "length": 0.0003876625465527169,
      "speed": {
        "0:00": 30
      },
      "startid": 370819328,
      "endid": 370819326
    },
    {
      "id": 1138,
      "name": "Banner Lane / Bannerbrook Park => Banner Lane / Wickman'S",
      "length": 0.002976322712675995,
      "speed": {
        "0:00": 30
      },
      "startid": 370819326,
      "endid": 370819325
    },
    {
      "id": 1139,
      "name": "Banner Lane / Wickman'S => Banner Lane / Wickman'S",
      "length": 0.00040896483956532486,
      "speed": {
        "0:00": 30
      },
      "startid": 370819325,
      "endid": 370819324
    },
    {
      "id": 1140,
      "name": "Banner Lane / Wickman'S => Goodman Way / Edgehill Place",
      "length": 0.003916498448866751,
      "speed": {
        "0:00": 30
      },
      "startid": 370819324,
      "endid": 370819320
    },
    {
      "id": 1141,
      "name": "Goodman Way / Edgehill Place => Goodman Way / Edgehill Place",
      "length": 0.0005257617045775399,
      "speed": {
        "0:00": 30
      },
      "startid": 370819320,
      "endid": 370819319
    },
    {
      "id": 1142,
      "name": "Goodman Way / Edgehill Place => Goodman Way / Tanyard Farm",
      "length": 0.0017018772135513902,
      "speed": {
        "0:00": 30
      },
      "startid": 370819319,
      "endid": 370819322
    },
    {
      "id": 1143,
      "name": "Goodman Way / Tanyard Farm => Tile Hill Lane / Westcotes",
      "length": 0.034234285313556934,
      "speed": {
        "0:00": 30
      },
      "startid": 370819322,
      "endid": 370817963
    },
    {
      "id": 1144,
      "name": "Tile Hill Lane / Westcotes => BS3",
      "length": 0.05465317529668256,
      "speed": {
        "0:00": 30
      },
      "startid": 370817963,
      "endid": 370817695
    },
    {
      "id": 1145,
      "name": "BS3 => CS4",
      "length": 0.003071773762827612,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 370817702
    },
    {
      "id": 1146,
      "name": "CS4 => R",
      "length": 0.006968894202096288,
      "speed": {
        "0:00": 30
      },
      "startid": 370817702,
      "endid": 370817750
    },
    {
      "id": 1147,
      "name": "R => CR4",
      "length": 0.010154747626603377,
      "speed": {
        "0:00": 30
      },
      "startid": 370817750,
      "endid": 370817813
    },
    {
      "id": 1148,
      "name": "CR4 => Goodman Way / Banner Lane",
      "length": 0.07912731695849451,
      "speed": {
        "0:00": 30
      },
      "startid": 370817813,
      "endid": 4815875262
    },
    {
      "id": 1149,
      "name": "Goodman Way / Banner Lane => Banner Lane / Goodman Way",
      "length": 0.0008796490663940991,
      "speed": {
        "0:00": 30
      },
      "startid": 4815875262,
      "endid": 4815875261
    },
    {
      "id": 1150,
      "name": "Banner Lane / Goodman Way => Herald Avenue / Business Park",
      "length": 0.044318022146413616,
      "speed": {
        "0:00": 30
      },
      "startid": 4815875261,
      "endid": 370817716
    },
    {
      "id": 1151,
      "name": "Herald Avenue / Business Park => Herald Avenue / Vanguard Avenue",
      "length": 0.003840197032705414,
      "speed": {
        "0:00": 30
      },
      "startid": 370817716,
      "endid": 370817403
    },
    {
      "id": 1152,
      "name": "Herald Avenue / Vanguard Avenue => BS7",
      "length": 0.04425088466697486,
      "speed": {
        "0:00": 30
      },
      "startid": 370817403,
      "endid": 7620250858
    },
    {
      "id": 1153,
      "name": "Remembrance Rd / Robin Hood Rd => Robin Hood Rd / Willenhall Social Club",
      "length": 0.0014490230778025177,
      "speed": {
        "0:00": 30
      },
      "startid": 370819020,
      "endid": 370819060
    },
    {
      "id": 1154,
      "name": "Robin Hood Rd / Willenhall Social Club => Remembrance Rd / Meadfoot Rd",
      "length": 0.0045265002165026874,
      "speed": {
        "0:00": 30
      },
      "startid": 370819060,
      "endid": 370819015
    },
    {
      "id": 1155,
      "name": "Remembrance Rd / Meadfoot Rd => St James Lane / Willenhall Wood School",
      "length": 0.0013200700928394727,
      "speed": {
        "0:00": 30
      },
      "startid": 370819015,
      "endid": 370819002
    },
    {
      "id": 1156,
      "name": "St James Lane / Willenhall Wood School => St James Lane / Dunsmore Avenue",
      "length": 0.00395027802565762,
      "speed": {
        "0:00": 30
      },
      "startid": 370819002,
      "endid": 370818999
    },
    {
      "id": 1157,
      "name": "St James Lane / Dunsmore Avenue => St James Lane / Dunsmore Avenue",
      "length": 0.0009609037933145949,
      "speed": {
        "0:00": 30
      },
      "startid": 370818999,
      "endid": 370818997
    },
    {
      "id": 1158,
      "name": "St James Lane / Dunsmore Avenue => St James Lane / Cedric Close",
      "length": 0.0022731797817127104,
      "speed": {
        "0:00": 30
      },
      "startid": 370818997,
      "endid": 370818995
    },
    {
      "id": 1159,
      "name": "St James Lane / Cedric Close => St James Lane / Cedric Close",
      "length": 0.0005462948013669836,
      "speed": {
        "0:00": 30
      },
      "startid": 370818995,
      "endid": 370818990
    },
    {
      "id": 1160,
      "name": "St James Lane / Cedric Close => St James Lane / London Rd",
      "length": 0.004031236182612137,
      "speed": {
        "0:00": 30
      },
      "startid": 370818990,
      "endid": 370819723
    },
    {
      "id": 1161,
      "name": "St James Lane / London Rd => London Rd / St James Lane",
      "length": 0.0022078424762651877,
      "speed": {
        "0:00": 30
      },
      "startid": 370819723,
      "endid": 370818985
    },
    {
      "id": 1162,
      "name": "London Rd / St James Lane => London Rd / Abbey Rd",
      "length": 0.004713155674279393,
      "speed": {
        "0:00": 30
      },
      "startid": 370818985,
      "endid": 370818604
    },
    {
      "id": 1163,
      "name": "London Rd / Abbey Rd => London Rd / Abbey Rd",
      "length": 0.0013384568203700501,
      "speed": {
        "0:00": 30
      },
      "startid": 370818604,
      "endid": 370818602
    },
    {
      "id": 1164,
      "name": "London Rd / Abbey Rd => London Rd / Tonbridge Rd",
      "length": 0.0029230135220401805,
      "speed": {
        "0:00": 30
      },
      "startid": 370818602,
      "endid": 370818601
    },
    {
      "id": 1165,
      "name": "London Rd / Tonbridge Rd => London Rd / Tonbridge Rd",
      "length": 0.0003229243409830427,
      "speed": {
        "0:00": 30
      },
      "startid": 370818601,
      "endid": 370818600
    },
    {
      "id": 1166,
      "name": "London Rd / Tonbridge Rd => London Rd / Riverside Close",
      "length": 0.007027076958452551,
      "speed": {
        "0:00": 30
      },
      "startid": 370818600,
      "endid": 370818598
    },
    {
      "id": 1167,
      "name": "London Rd / Riverside Close => London Rd / Riverside Close",
      "length": 0.0011431498676901016,
      "speed": {
        "0:00": 30
      },
      "startid": 370818598,
      "endid": 370818597
    },
    {
      "id": 1168,
      "name": "London Rd / Riverside Close => Daventry Rd / London Rd",
      "length": 0.010202120523206083,
      "speed": {
        "0:00": 30
      },
      "startid": 370818597,
      "endid": 370818524
    },
    {
      "id": 1169,
      "name": "Daventry Rd / London Rd => Daventry Rd / London Rd",
      "length": 0.00033666725412569983,
      "speed": {
        "0:00": 30
      },
      "startid": 370818524,
      "endid": 370818522
    },
    {
      "id": 1170,
      "name": "Daventry Rd / London Rd => Daventry Rd / The Mount",
      "length": 0.003176179316411741,
      "speed": {
        "0:00": 30
      },
      "startid": 370818522,
      "endid": 370818519
    },
    {
      "id": 1171,
      "name": "Daventry Rd / The Mount => Daventry Rd / The Mount",
      "length": 0.0015180390541750693,
      "speed": {
        "0:00": 30
      },
      "startid": 370818519,
      "endid": 370818521
    },
    {
      "id": 1172,
      "name": "Daventry Rd / The Mount => Queen Isabels Ave / Daventry Rd",
      "length": 0.004185984483964002,
      "speed": {
        "0:00": 30
      },
      "startid": 370818521,
      "endid": 370818516
    },
    {
      "id": 1173,
      "name": "Queen Isabels Ave / Daventry Rd => Queen Isabels Ave / Daventry Rd",
      "length": 0.00023318492661311281,
      "speed": {
        "0:00": 30
      },
      "startid": 370818516,
      "endid": 370818518
    },
    {
      "id": 1174,
      "name": "Queen Isabels Ave / The Mount => Mile Lane / Thomas Lansdail St",
      "length": 0.0015672730106782253,
      "speed": {
        "0:00": 30
      },
      "startid": 370819721,
      "endid": 370818512
    },
    {
      "id": 1175,
      "name": "Mile Lane / Thomas Lansdail St => Mile Lane / Thomas Lansdail St",
      "length": 0.0004991193845145756,
      "speed": {
        "0:00": 30
      },
      "startid": 370818512,
      "endid": 370818513
    },
    {
      "id": 1176,
      "name": "Mile Lane / Thomas Lansdail St => Mile Lane / Furlong Rd",
      "length": 0.001976166764221807,
      "speed": {
        "0:00": 30
      },
      "startid": 370818513,
      "endid": 370818502
    },
    {
      "id": 1177,
      "name": "Mile Lane / Furlong Rd => Mile Lane / Furlong Rd",
      "length": 0.0007341031262712063,
      "speed": {
        "0:00": 30
      },
      "startid": 370818502,
      "endid": 370818500
    },
    {
      "id": 1178,
      "name": "Mile Lane / Furlong Rd => Mile Lane / Ibis Hotel",
      "length": 0.002974524829279188,
      "speed": {
        "0:00": 30
      },
      "startid": 370818500,
      "endid": 370818531
    },
    {
      "id": 1179,
      "name": "Mile Lane / Ibis Hotel => Mile Lane / Ibis Hotel",
      "length": 0.0002302223707599752,
      "speed": {
        "0:00": 30
      },
      "startid": 370818531,
      "endid": 370818532
    },
    {
      "id": 1180,
      "name": "Mile Lane / Ibis Hotel => GR2",
      "length": 0.007403848907832494,
      "speed": {
        "0:00": 30
      },
      "startid": 370818532,
      "endid": 370817796
    },
    {
      "id": 1181,
      "name": "GR2 => Hillmorton Rd / Deedmore Rd",
      "length": 0.05853771406759768,
      "speed": {
        "0:00": 30
      },
      "startid": 370817796,
      "endid": 370819180
    },
    {
      "id": 1182,
      "name": "Hillmorton Rd / Deedmore Rd => Hillmorton Rd / Deedmore Rd",
      "length": 0.0001535305181388248,
      "speed": {
        "0:00": 30
      },
      "startid": 370819180,
      "endid": 370819178
    },
    {
      "id": 1183,
      "name": "Hillmorton Rd / Deedmore Rd => Hillmorton Rd / Lillington Rd",
      "length": 0.002628263769106573,
      "speed": {
        "0:00": 30
      },
      "startid": 370819178,
      "endid": 370817624
    },
    {
      "id": 1184,
      "name": "Hillmorton Rd / Lillington Rd => Hillmorton Rd / Lillington Rd",
      "length": 0.0005985330483773023,
      "speed": {
        "0:00": 30
      },
      "startid": 370817624,
      "endid": 370817623
    },
    {
      "id": 1185,
      "name": "Hillmorton Rd / Lillington Rd => Hillmorton Rd / Haseley Rd",
      "length": 0.002180897267182483,
      "speed": {
        "0:00": 30
      },
      "startid": 370817623,
      "endid": 370817553
    },
    {
      "id": 1186,
      "name": "Hillmorton Rd / Haseley Rd => Hillmorton Rd / Haseley Rd",
      "length": 0.00030505766667847915,
      "speed": {
        "0:00": 30
      },
      "startid": 370817553,
      "endid": 370817554
    },
    {
      "id": 1187,
      "name": "Hillmorton Rd / Haseley Rd => Hillmorton Rd / Milverton Rd",
      "length": 0.0012627199570774312,
      "speed": {
        "0:00": 30
      },
      "startid": 370817554,
      "endid": 370817550
    },
    {
      "id": 1188,
      "name": "Hillmorton Rd / Milverton Rd => Hillmorton Rd / Milverton Rd",
      "length": 0.0012114260769849937,
      "speed": {
        "0:00": 30
      },
      "startid": 370817550,
      "endid": 370817549
    },
    {
      "id": 1189,
      "name": "Hillmorton Rd / Milverton Rd => Hillmorton Rd / Almond Tree Avenue",
      "length": 0.0023270686496090942,
      "speed": {
        "0:00": 30
      },
      "startid": 370817549,
      "endid": 370817366
    },
    {
      "id": 1190,
      "name": "Hillmorton Rd / Almond Tree Avenue => Almond Tree Ave / Hillmorton Rd",
      "length": 0.0009547437614367769,
      "speed": {
        "0:00": 30
      },
      "startid": 370817366,
      "endid": 370818816
    },
    {
      "id": 1191,
      "name": "Almond Tree Ave / Hillmorton Rd => Almond Tree Ave / Palm Tree Avenue",
      "length": 0.0010056628311679852,
      "speed": {
        "0:00": 30
      },
      "startid": 370818816,
      "endid": 370817353
    },
    {
      "id": 1192,
      "name": "Almond Tree Ave / Palm Tree Avenue => Almond Tree Ave / Palm Tree Avenue",
      "length": 0.0006733394092149403,
      "speed": {
        "0:00": 30
      },
      "startid": 370817353,
      "endid": 370817351
    },
    {
      "id": 1193,
      "name": "Almond Tree Ave / Palm Tree Avenue => Roseberry Ave / Riley Square",
      "length": 0.0023944296878364423,
      "speed": {
        "0:00": 30
      },
      "startid": 370817351,
      "endid": 370817350
    },
    {
      "id": 1194,
      "name": "Roseberry Ave / Riley Square => Roseberry Ave / Riley Square",
      "length": 0.00018048083000679553,
      "speed": {
        "0:00": 30
      },
      "startid": 370817350,
      "endid": 370817347
    },
    {
      "id": 1195,
      "name": "Roseberry Ave / Riley Square => Henley Rd / Old Church Rd",
      "length": 0.002076311896128197,
      "speed": {
        "0:00": 30
      },
      "startid": 370817347,
      "endid": 370819625
    },
    {
      "id": 1196,
      "name": "Henley Rd / Old Church Rd => Old Church Rd / Henley Rd",
      "length": 0.0014413129882161538,
      "speed": {
        "0:00": 30
      },
      "startid": 370819625,
      "endid": 370817346
    },
    {
      "id": 1197,
      "name": "Old Church Rd / Henley Rd => Bell Green Rd / Carey St",
      "length": 0.002762311658737569,
      "speed": {
        "0:00": 30
      },
      "startid": 370817346,
      "endid": 370817345
    },
    {
      "id": 1198,
      "name": "Bell Green Rd / Carey St => Bell Green Rd / Carey St",
      "length": 0.0001488198911465316,
      "speed": {
        "0:00": 30
      },
      "startid": 370817345,
      "endid": 370818890
    },
    {
      "id": 1199,
      "name": "Bell Green Rd / Carey St => Bell Green Rd / Weavers Arms",
      "length": 0.0024643627999952804,
      "speed": {
        "0:00": 30
      },
      "startid": 370818890,
      "endid": 370819173
    },
    {
      "id": 1200,
      "name": "Bell Green Rd / Weavers Arms => Bell Green Rd / Weavers Arms",
      "length": 0.0005814151872809625,
      "speed": {
        "0:00": 30
      },
      "startid": 370819173,
      "endid": 370819172
    },
    {
      "id": 1201,
      "name": "Bell Green Rd / Weavers Arms => Bell Green Rd / Sewall Highway",
      "length": 0.0019331059593303101,
      "speed": {
        "0:00": 30
      },
      "startid": 370819172,
      "endid": 370818888
    },
    {
      "id": 1202,
      "name": "Bell Green Rd / Sewall Highway => Bell Green Rd / Nuffield Rd",
      "length": 0.00242254322768477,
      "speed": {
        "0:00": 30
      },
      "startid": 370818888,
      "endid": 370818886
    },
    {
      "id": 1203,
      "name": "Bell Green Rd / Nuffield Rd => Bell Green Rd / Nuffield Rd",
      "length": 0.00017216904483243866,
      "speed": {
        "0:00": 30
      },
      "startid": 370818886,
      "endid": 370818885
    },
    {
      "id": 1204,
      "name": "Bell Green Rd / Nuffield Rd => Stoney Stanton Rd / Eden St",
      "length": 0.005553710042844506,
      "speed": {
        "0:00": 30
      },
      "startid": 370818885,
      "endid": 370818851
    },
    {
      "id": 1205,
      "name": "Stoney Stanton Rd / Eden St => Stoney Stanton Rd / Eden St",
      "length": 0.00015681836627588546,
      "speed": {
        "0:00": 30
      },
      "startid": 370818851,
      "endid": 370818852
    },
    {
      "id": 1206,
      "name": "Stoney Stanton Rd / Eden St => Stoney Stanton Rd / Station St East",
      "length": 0.0037912339785359617,
      "speed": {
        "0:00": 30
      },
      "startid": 370818852,
      "endid": 370818850
    },
    {
      "id": 1207,
      "name": "Stoney Stanton Rd / Station St East => Stoney Stanton Rd / Station St East",
      "length": 0.0006210058373328827,
      "speed": {
        "0:00": 30
      },
      "startid": 370818850,
      "endid": 370818848
    },
    {
      "id": 1208,
      "name": "Stoney Stanton Rd / Station St East => Stoney Stanton Rd / Hanford Close",
      "length": 0.0039097994833474405,
      "speed": {
        "0:00": 30
      },
      "startid": 370818848,
      "endid": 370818842
    },
    {
      "id": 1209,
      "name": "Stoney Stanton Rd / Hanford Close => Stoney Stanton Rd / Hanford Close",
      "length": 0.0009570044566287776,
      "speed": {
        "0:00": 30
      },
      "startid": 370818842,
      "endid": 370818845
    },
    {
      "id": 1210,
      "name": "Stoney Stanton Rd / Hanford Close => Stoney Stanton Rd / Peel St",
      "length": 0.0022242675041465724,
      "speed": {
        "0:00": 30
      },
      "startid": 370818845,
      "endid": 370818805
    },
    {
      "id": 1211,
      "name": "Stoney Stanton Rd / Peel St => Stoney Stanton Rd / Peel St",
      "length": 0.00022189414142833507,
      "speed": {
        "0:00": 30
      },
      "startid": 370818805,
      "endid": 370818807
    },
    {
      "id": 1212,
      "name": "Stoney Stanton Rd / Peel St => Stoney Stanton Rd / Red Lane",
      "length": 0.001130535669499075,
      "speed": {
        "0:00": 30
      },
      "startid": 370818807,
      "endid": 370818802
    },
    {
      "id": 1213,
      "name": "Stoney Stanton Rd / Red Lane => Stoney Stanton Rd / Red Lane",
      "length": 0.0007679482534652206,
      "speed": {
        "0:00": 30
      },
      "startid": 370818802,
      "endid": 370818804
    },
    {
      "id": 1214,
      "name": "Stoney Stanton Rd / Red Lane => Stoney Stanton Rd / Cambridge St",
      "length": 0.002748587741000615,
      "speed": {
        "0:00": 30
      },
      "startid": 370818804,
      "endid": 370818801
    },
    {
      "id": 1215,
      "name": "Stoney Stanton Rd / Cambridge St => Stoney Stanton Rd / Cambridge St",
      "length": 0.00020804761474186095,
      "speed": {
        "0:00": 30
      },
      "startid": 370818801,
      "endid": 370818799
    },
    {
      "id": 1216,
      "name": "Stoney Stanton Rd / Cambridge St => Stoney Stanton Rd / Eagle St East",
      "length": 0.0029448853441181523,
      "speed": {
        "0:00": 30
      },
      "startid": 370818799,
      "endid": 370818797
    },
    {
      "id": 1217,
      "name": "Stoney Stanton Rd / Eagle St East => Stoney Stanton Rd / Eagle St East",
      "length": 0.0008340346875264894,
      "speed": {
        "0:00": 30
      },
      "startid": 370818797,
      "endid": 370818798
    },
    {
      "id": 1218,
      "name": "Stoney Stanton Rd / Eagle St East => Stoney Stanton Rd / Harnall Lane East",
      "length": 0.001196668241411058,
      "speed": {
        "0:00": 30
      },
      "startid": 370818798,
      "endid": 370818796
    },
    {
      "id": 1219,
      "name": "Stoney Stanton Rd / Harnall Lane East => Swanswell St / City College",
      "length": 0.0022126107023144465,
      "speed": {
        "0:00": 30
      },
      "startid": 370818796,
      "endid": 370817756
    },
    {
      "id": 1220,
      "name": "Swanswell St / City College => Stoney Stanton Rd / Swanswell St",
      "length": 0.0010650563647048277,
      "speed": {
        "0:00": 30
      },
      "startid": 370817756,
      "endid": 370817781
    },
    {
      "id": 1221,
      "name": "Stoney Stanton Rd / Swanswell St => BY1",
      "length": 0.010424135644263127,
      "speed": {
        "0:00": 30
      },
      "startid": 370817781,
      "endid": 370817684
    },
    {
      "id": 1222,
      "name": "BY1 => White St / Bus Garage",
      "length": 0.009747790942051603,
      "speed": {
        "0:00": 30
      },
      "startid": 370817684,
      "endid": 370817758
    },
    {
      "id": 1223,
      "name": "White St / Bus Garage => TS1",
      "length": 0.0049819636650602584,
      "speed": {
        "0:00": 30
      },
      "startid": 370817758,
      "endid": 370817658
    },
    {
      "id": 1224,
      "name": "TS1 => BY5",
      "length": 0.005353411698162737,
      "speed": {
        "0:00": 30
      },
      "startid": 370817658,
      "endid": 370817679
    },
    {
      "id": 1225,
      "name": "BY5 => GR1",
      "length": 0.0031498880630907375,
      "speed": {
        "0:00": 30
      },
      "startid": 370817679,
      "endid": 370817794
    },
    {
      "id": 1226,
      "name": "GR1 => VR3",
      "length": 0.002224508586183148,
      "speed": {
        "0:00": 30
      },
      "startid": 370817794,
      "endid": 370817718
    },
    {
      "id": 1227,
      "name": "VR3 => CS4",
      "length": 0.002391225267514317,
      "speed": {
        "0:00": 30
      },
      "startid": 370817718,
      "endid": 370817702
    },
    {
      "id": 1228,
      "name": "CS4 => London Rd / Chace Avenue",
      "length": 0.04661912946044815,
      "speed": {
        "0:00": 30
      },
      "startid": 370817702,
      "endid": 4248964910
    },
    {
      "id": 1229,
      "name": "London Rd / Chace Avenue => HS3",
      "length": 0.04222758977126461,
      "speed": {
        "0:00": 30
      },
      "startid": 4248964910,
      "endid": 4458326372
    },
    {
      "id": 1230,
      "name": "HS3 => VR2",
      "length": 0.00830374601249271,
      "speed": {
        "0:00": 30
      },
      "startid": 4458326372,
      "endid": 370817717
    },
    {
      "id": 1231,
      "name": "VR2 => CS3",
      "length": 0.0021289177156473215,
      "speed": {
        "0:00": 30
      },
      "startid": 370817717,
      "endid": 370817701
    },
    {
      "id": 1232,
      "name": "CS3 => Hillmorton Rd / Wexford Road",
      "length": 0.0570863659072798,
      "speed": {
        "0:00": 30
      },
      "startid": 370817701,
      "endid": 4815880363
    },
    {
      "id": 1233,
      "name": "Lentons Lane / Shilton Lane => Lentons Lane / Lentons Lane Middle",
      "length": 0.010893684116037618,
      "speed": {
        "0:00": 30
      },
      "startid": 370817611,
      "endid": 370817382
    },
    {
      "id": 1234,
      "name": "Lentons Lane / Lentons Lane Middle => Lentons Lane / Lentons Lane Middle",
      "length": 0.00028644372920352205,
      "speed": {
        "0:00": 30
      },
      "startid": 370817382,
      "endid": 370817383
    },
    {
      "id": 1235,
      "name": "Lentons Lane / Lentons Lane Middle => Lentons Lane / Parish Hall",
      "length": 0.003180583672849926,
      "speed": {
        "0:00": 30
      },
      "startid": 370817383,
      "endid": 370817395
    },
    {
      "id": 1236,
      "name": "Lentons Lane / Parish Hall => Lentons Lane / Parish Hall",
      "length": 0.00043927354803052006,
      "speed": {
        "0:00": 30
      },
      "startid": 370817395,
      "endid": 370817393
    },
    {
      "id": 1237,
      "name": "Lentons Lane / Parish Hall => Lentons Lane / Hawkesbury Lane",
      "length": 0.004530768377439266,
      "speed": {
        "0:00": 30
      },
      "startid": 370817393,
      "endid": 370819626
    },
    {
      "id": 1238,
      "name": "Lentons Lane / Hawkesbury Lane => Aldermans Green Rd / Lenton'S Lane",
      "length": 0.0008874151734110801,
      "speed": {
        "0:00": 30
      },
      "startid": 370819626,
      "endid": 370817381
    },
    {
      "id": 1239,
      "name": "Aldermans Green Rd / Lenton'S Lane => Aldermans Green Rd / M6 Bridge",
      "length": 0.005225289706800145,
      "speed": {
        "0:00": 30
      },
      "startid": 370817381,
      "endid": 370817379
    },
    {
      "id": 1240,
      "name": "Aldermans Green Rd / M6 Bridge => Aldermans Green Rd / M6 Bridge",
      "length": 0.00010736000185869479,
      "speed": {
        "0:00": 30
      },
      "startid": 370817379,
      "endid": 370817378
    },
    {
      "id": 1241,
      "name": "Aldermans Green Rd / M6 Bridge => Aldermans Green Rd / Canberra Rd",
      "length": 0.003822565803225842,
      "speed": {
        "0:00": 30
      },
      "startid": 370817378,
      "endid": 370817688
    },
    {
      "id": 1242,
      "name": "Aldermans Green Rd / Canberra Rd => Jackers Rd / Farmcote Rd",
      "length": 0.0011479152756196072,
      "speed": {
        "0:00": 30
      },
      "startid": 370817688,
      "endid": 370819627
    },
    {
      "id": 1243,
      "name": "Jackers Rd / Farmcote Rd => Jackers Rd / Jacker'S Rd",
      "length": 0.004449379965792818,
      "speed": {
        "0:00": 30
      },
      "startid": 370819627,
      "endid": 4815880411
    },
    {
      "id": 1244,
      "name": "Jackers Rd / Jacker'S Rd => Grange Rd / Cheadle Close",
      "length": 0.002764245866416109,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880411,
      "endid": 370817396
    },
    {
      "id": 1245,
      "name": "Grange Rd / Cheadle Close => Grange Rd / Cheadle Close",
      "length": 0.0008262299982461528,
      "speed": {
        "0:00": 30
      },
      "startid": 370817396,
      "endid": 370817398
    },
    {
      "id": 1246,
      "name": "Grange Rd / Cheadle Close => Longford Rd / Vinecote Rd",
      "length": 0.006083534507175781,
      "speed": {
        "0:00": 30
      },
      "startid": 370817398,
      "endid": 370818872
    },
    {
      "id": 1247,
      "name": "Longford Rd / Vinecote Rd => Longford Rd / Longford Bridge",
      "length": 0.0020781797901004042,
      "speed": {
        "0:00": 30
      },
      "startid": 370818872,
      "endid": 370819748
    },
    {
      "id": 1248,
      "name": "Longford Rd / Longford Bridge => Longford Rd / Windmill Rd",
      "length": 0.0014970952808711533,
      "speed": {
        "0:00": 30
      },
      "startid": 370819748,
      "endid": 370819732
    },
    {
      "id": 1249,
      "name": "Longford Rd / Windmill Rd => Longford Rd / Dovedale Avenue",
      "length": 0.0010496597639259562,
      "speed": {
        "0:00": 30
      },
      "startid": 370819732,
      "endid": 370818870
    },
    {
      "id": 1250,
      "name": "Longford Rd / Dovedale Avenue => AG",
      "length": 0.0021072323103976083,
      "speed": {
        "0:00": 30
      },
      "startid": 370818870,
      "endid": 370818869
    },
    {
      "id": 1251,
      "name": "AG => AF",
      "length": 0.0008466729474816734,
      "speed": {
        "0:00": 30
      },
      "startid": 370818869,
      "endid": 370818867
    },
    {
      "id": 1252,
      "name": "AF => Foleshill Rd / The Wheatsheaf",
      "length": 0.001456813598235208,
      "speed": {
        "0:00": 30
      },
      "startid": 370818867,
      "endid": 370818864
    },
    {
      "id": 1253,
      "name": "Foleshill Rd / The Wheatsheaf => Foleshill Rd / The Wheatsheaf",
      "length": 0.00031738230889481126,
      "speed": {
        "0:00": 30
      },
      "startid": 370818864,
      "endid": 370818865
    },
    {
      "id": 1254,
      "name": "Foleshill Rd / The Wheatsheaf => Foleshill Rd / Old Church Rd",
      "length": 0.0031598401984935013,
      "speed": {
        "0:00": 30
      },
      "startid": 370818865,
      "endid": 370818863
    },
    {
      "id": 1255,
      "name": "Foleshill Rd / Old Church Rd => Foleshill Rd / Old Church Rd",
      "length": 0.0003347000000000211,
      "speed": {
        "0:00": 30
      },
      "startid": 370818863,
      "endid": 370818862
    },
    {
      "id": 1256,
      "name": "Foleshill Rd / Old Church Rd => Foleshill Rd / Phoenix Way",
      "length": 0.0035533042270538776,
      "speed": {
        "0:00": 30
      },
      "startid": 370818862,
      "endid": 370818832
    },
    {
      "id": 1257,
      "name": "Foleshill Rd / Phoenix Way => Foleshill Rd / Cross Rd",
      "length": 0.0014007685961625698,
      "speed": {
        "0:00": 30
      },
      "startid": 370818832,
      "endid": 370818831
    },
    {
      "id": 1258,
      "name": "Foleshill Rd / Cross Rd => Foleshill Rd / Cross Rd",
      "length": 0.0004945206264681952,
      "speed": {
        "0:00": 30
      },
      "startid": 370818831,
      "endid": 370818830
    },
    {
      "id": 1259,
      "name": "Foleshill Rd / Cross Rd => Foleshill Rd / Phoenix Way",
      "length": 0.0016837137820924367,
      "speed": {
        "0:00": 30
      },
      "startid": 370818830,
      "endid": 370818834
    },
    {
      "id": 1260,
      "name": "Foleshill Rd / Phoenix Way => Foleshill Rd / Family Centre",
      "length": 0.004012790291057641,
      "speed": {
        "0:00": 30
      },
      "startid": 370818834,
      "endid": 370819703
    },
    {
      "id": 1261,
      "name": "Foleshill Rd / Family Centre => Foleshill Rd / Family Centre",
      "length": 0.00016455625178377943,
      "speed": {
        "0:00": 30
      },
      "startid": 370819703,
      "endid": 370819702
    },
    {
      "id": 1262,
      "name": "Foleshill Rd / Family Centre => Foleshill Rd / Station St",
      "length": 0.0015067931145365627,
      "speed": {
        "0:00": 30
      },
      "startid": 370819702,
      "endid": 370818829
    },
    {
      "id": 1263,
      "name": "Foleshill Rd / Station St => Foleshill Rd / Station St",
      "length": 0.0013386575364890566,
      "speed": {
        "0:00": 30
      },
      "startid": 370818829,
      "endid": 370818827
    },
    {
      "id": 1264,
      "name": "Foleshill Rd / Station St => Foleshill Rd / Broad St",
      "length": 0.0024773627630995656,
      "speed": {
        "0:00": 30
      },
      "startid": 370818827,
      "endid": 370818826
    },
    {
      "id": 1265,
      "name": "Foleshill Rd / Broad St => Foleshill Rd / Broad St",
      "length": 0.00038016818646532426,
      "speed": {
        "0:00": 30
      },
      "startid": 370818826,
      "endid": 370818825
    },
    {
      "id": 1266,
      "name": "Foleshill Rd / Broad St => Foleshill Rd / Courtaulds Way",
      "length": 0.0039097452461746675,
      "speed": {
        "0:00": 30
      },
      "startid": 370818825,
      "endid": 370818780
    },
    {
      "id": 1267,
      "name": "Foleshill Rd / Courtaulds Way => Foleshill Rd / Courtaulds Way",
      "length": 0.00035180778843009035,
      "speed": {
        "0:00": 30
      },
      "startid": 370818780,
      "endid": 370818784
    },
    {
      "id": 1268,
      "name": "Foleshill Rd / Courtaulds Way => Foleshill Rd / Cashs Lane",
      "length": 0.004189703516956552,
      "speed": {
        "0:00": 30
      },
      "startid": 370818784,
      "endid": 370818774
    },
    {
      "id": 1269,
      "name": "Foleshill Rd / Cashs Lane => Foleshill Rd / Cashs Lane",
      "length": 0.00022125555360341274,
      "speed": {
        "0:00": 30
      },
      "startid": 370818774,
      "endid": 370818776
    },
    {
      "id": 1270,
      "name": "Foleshill Rd / Cashs Lane => Foleshill Rd / Eagle St",
      "length": 0.0010602588363222854,
      "speed": {
        "0:00": 30
      },
      "startid": 370818776,
      "endid": 370818765
    },
    {
      "id": 1271,
      "name": "Foleshill Rd / Eagle St => Foleshill Rd / Eagle St",
      "length": 0.001522061907418469,
      "speed": {
        "0:00": 30
      },
      "startid": 370818765,
      "endid": 370818766
    },
    {
      "id": 1272,
      "name": "Foleshill Rd / Eagle St => Foleshill Rd / City Engineers",
      "length": 0.0026961933257796727,
      "speed": {
        "0:00": 30
      },
      "startid": 370818766,
      "endid": 370818764
    },
    {
      "id": 1273,
      "name": "Foleshill Rd / City Engineers => Foleshill Rd / City Engineers",
      "length": 0.00022393115013730707,
      "speed": {
        "0:00": 30
      },
      "startid": 370818764,
      "endid": 370818762
    },
    {
      "id": 1274,
      "name": "Foleshill Rd / City Engineers => Foleshill Rd / Leicester Row",
      "length": 0.0014337131163520442,
      "speed": {
        "0:00": 30
      },
      "startid": 370818762,
      "endid": 370818761
    },
    {
      "id": 1275,
      "name": "Foleshill Rd / Leicester Row => Foleshill Rd / Leicester Row",
      "length": 0.00040428367515873303,
      "speed": {
        "0:00": 30
      },
      "startid": 370818761,
      "endid": 370818758
    },
    {
      "id": 1276,
      "name": "Foleshill Rd / Leicester Row => TS4",
      "length": 0.005637328454148691,
      "speed": {
        "0:00": 30
      },
      "startid": 370818758,
      "endid": 370817662
    },
    {
      "id": 1277,
      "name": "TS4 => BS2",
      "length": 0.002139564165897073,
      "speed": {
        "0:00": 30
      },
      "startid": 370817662,
      "endid": 370817727
    },
    {
      "id": 1278,
      "name": "BS2 => BS1",
      "length": 0.0006854744707142306,
      "speed": {
        "0:00": 30
      },
      "startid": 370817727,
      "endid": 370817728
    },
    {
      "id": 1279,
      "name": "BS1 => Lentons Lane / Shilton Lane",
      "length": 0.07484769462555498,
      "speed": {
        "0:00": 30
      },
      "startid": 370817728,
      "endid": 370817612
    },
    {
      "id": 1280,
      "name": "Lentons Lane / Shilton Lane => Ringwood Highway / Potters Green Primary School",
      "length": 0.009732997049214771,
      "speed": {
        "0:00": 30
      },
      "startid": 370817612,
      "endid": 370817603
    },
    {
      "id": 1281,
      "name": "Ringwood Highway / Potters Green Primary School => Ringwood Highway / Potters Green Primary School",
      "length": 0.0005837635822809273,
      "speed": {
        "0:00": 30
      },
      "startid": 370817603,
      "endid": 4739801317
    },
    {
      "id": 1282,
      "name": "Ringwood Highway / Potters Green Primary School => Ringwood Highway / Deedmore Rd",
      "length": 0.0051569405668489545,
      "speed": {
        "0:00": 30
      },
      "startid": 4739801317,
      "endid": 370817606
    },
    {
      "id": 1283,
      "name": "Ringwood Highway / Deedmore Rd => Ringwood Highway / Deedmore Rd",
      "length": 0.00012534851415092722,
      "speed": {
        "0:00": 30
      },
      "startid": 370817606,
      "endid": 370817607
    },
    {
      "id": 1284,
      "name": "Ringwood Highway / Deedmore Rd => Shilton Lane / The Boat Inn",
      "length": 0.0020393848214586316,
      "speed": {
        "0:00": 30
      },
      "startid": 370817607,
      "endid": 370817610
    },
    {
      "id": 1285,
      "name": "Shilton Lane / The Boat Inn => Shilton Lane / The Boat Inn",
      "length": 0.0005185770145324861,
      "speed": {
        "0:00": 30
      },
      "startid": 370817610,
      "endid": 370817609
    },
    {
      "id": 1286,
      "name": "Shilton Lane / The Boat Inn => Ringwood Highway / Potters Green Primary School",
      "length": 0.005236505071133684,
      "speed": {
        "0:00": 30
      },
      "startid": 370817609,
      "endid": 370817605
    },
    {
      "id": 1287,
      "name": "Ringwood Highway / Potters Green Primary School => Woodway Lane / Potters Green Rd",
      "length": 0.0021865191629648964,
      "speed": {
        "0:00": 30
      },
      "startid": 370817605,
      "endid": 370817619
    },
    {
      "id": 1288,
      "name": "Woodway Lane / Potters Green Rd => Woodway Lane / Potters Green Rd",
      "length": 0.0006930219404853976,
      "speed": {
        "0:00": 30
      },
      "startid": 370817619,
      "endid": 370817618
    },
    {
      "id": 1289,
      "name": "Woodway Lane / Potters Green Rd => Woodway Lane / Woodway Walk",
      "length": 0.004925361108588731,
      "speed": {
        "0:00": 30
      },
      "startid": 370817618,
      "endid": 370817616
    },
    {
      "id": 1290,
      "name": "Woodway Lane / Woodway Walk => Woodway Lane / Woodway Walk",
      "length": 0.00015028965366803217,
      "speed": {
        "0:00": 30
      },
      "startid": 370817616,
      "endid": 370817617
    },
    {
      "id": 1291,
      "name": "Woodway Lane / Woodway Walk => Narberth Way / Walsgrave Club",
      "length": 0.0021570335926932977,
      "speed": {
        "0:00": 30
      },
      "startid": 370817617,
      "endid": 370818287
    },
    {
      "id": 1292,
      "name": "Narberth Way / Walsgrave Club => Narberth Way / Walsgrave Club",
      "length": 0.0004513370359282702,
      "speed": {
        "0:00": 30
      },
      "startid": 370818287,
      "endid": 370818288
    },
    {
      "id": 1293,
      "name": "Narberth Way / Walsgrave Club => Narberth Way / Caspian Way",
      "length": 0.004395085260834505,
      "speed": {
        "0:00": 30
      },
      "startid": 370818288,
      "endid": 370817638
    },
    {
      "id": 1294,
      "name": "Narberth Way / Caspian Way => Narberth Way / Caspian Way",
      "length": 0.0004951981522592259,
      "speed": {
        "0:00": 30
      },
      "startid": 370817638,
      "endid": 370817637
    },
    {
      "id": 1295,
      "name": "Narberth Way / Caspian Way => Wigston Rd / Macdonalds",
      "length": 0.002511382479830568,
      "speed": {
        "0:00": 30
      },
      "startid": 370817637,
      "endid": 370819820
    },
    {
      "id": 1296,
      "name": "Wigston Rd / Macdonalds => Wigston Rd / Macdonalds",
      "length": 0.00030607796392459756,
      "speed": {
        "0:00": 30
      },
      "startid": 370819820,
      "endid": 370819822
    },
    {
      "id": 1297,
      "name": "Wigston Rd / Macdonalds => Brade Dr / Manfield Avenue",
      "length": 0.004121196488885354,
      "speed": {
        "0:00": 30
      },
      "startid": 370819822,
      "endid": 4815875236
    },
    {
      "id": 1298,
      "name": "Brade Dr / Manfield Avenue => Boswell Dr / Lucian Close",
      "length": 0.0034293283453158065,
      "speed": {
        "0:00": 30
      },
      "startid": 4815875236,
      "endid": 4815875235
    },
    {
      "id": 1299,
      "name": "Boswell Dr / Lucian Close => Boswell Dr / Walsgrave Infants School",
      "length": 0.006270298169146384,
      "speed": {
        "0:00": 30
      },
      "startid": 4815875235,
      "endid": 370819151
    },
    {
      "id": 1300,
      "name": "Boswell Dr / Walsgrave Infants School => Boswell Dr / Walsgrave Infants School",
      "length": 0.00031637093735050907,
      "speed": {
        "0:00": 30
      },
      "startid": 370819151,
      "endid": 370819148
    },
    {
      "id": 1301,
      "name": "Boswell Dr / Walsgrave Infants School => Ansty Rd / Walsgrave Church",
      "length": 0.003369792909067193,
      "speed": {
        "0:00": 30
      },
      "startid": 370819148,
      "endid": 370817584
    },
    {
      "id": 1302,
      "name": "Ansty Rd / Walsgrave Church => UH2",
      "length": 0.006849500423389326,
      "speed": {
        "0:00": 30
      },
      "startid": 370817584,
      "endid": 370817645
    },
    {
      "id": 1303,
      "name": "UH2 => WF",
      "length": 0.0025795850848541794,
      "speed": {
        "0:00": 30
      },
      "startid": 370817645,
      "endid": 370817729
    },
    {
      "id": 1304,
      "name": "WF => WG",
      "length": 0.003325900281127788,
      "speed": {
        "0:00": 30
      },
      "startid": 370817729,
      "endid": 370817730
    },
    {
      "id": 1305,
      "name": "WG => WH",
      "length": 0.000278365084014834,
      "speed": {
        "0:00": 30
      },
      "startid": 370817730,
      "endid": 370817732
    },
    {
      "id": 1306,
      "name": "WH => Jackers Rd / Farmcote Rd",
      "length": 0.04146465353647989,
      "speed": {
        "0:00": 30
      },
      "startid": 370817732,
      "endid": 4739803237
    },
    {
      "id": 1307,
      "name": "Jobs Lane / Lime Tree Ave => Goodman Way / Tanyard Farm",
      "length": 0.027892158411281474,
      "speed": {
        "0:00": 30
      },
      "startid": 4815881222,
      "endid": 370819322
    },
    {
      "id": 1308,
      "name": "Goodman Way / Tanyard Farm => Goodman Way / Edgehill Place",
      "length": 0.0020980849029540996,
      "speed": {
        "0:00": 30
      },
      "startid": 370819322,
      "endid": 370819320
    },
    {
      "id": 1309,
      "name": "Goodman Way / Edgehill Place => Goodman Way / Edgehill Place",
      "length": 0.0005257617045775399,
      "speed": {
        "0:00": 30
      },
      "startid": 370819320,
      "endid": 370819319
    },
    {
      "id": 1310,
      "name": "Goodman Way / Edgehill Place => Banner Lane / Tile Hill Lane",
      "length": 0.003185509643683348,
      "speed": {
        "0:00": 30
      },
      "startid": 370819319,
      "endid": 370819318
    },
    {
      "id": 1311,
      "name": "Banner Lane / Tile Hill Lane => Banner Lane / Tile Hill Lane",
      "length": 0.00017872585151608396,
      "speed": {
        "0:00": 30
      },
      "startid": 370819318,
      "endid": 370819314
    },
    {
      "id": 1312,
      "name": "Banner Lane / Tile Hill Lane => Tile Hill Lane / Tile Hill Wood School",
      "length": 0.005995180092374057,
      "speed": {
        "0:00": 30
      },
      "startid": 370819314,
      "endid": 370818250
    },
    {
      "id": 1313,
      "name": "Tile Hill Lane / Tile Hill Wood School => Tile Hill Lane / Tile Hill Wood School",
      "length": 0.0005114159950559935,
      "speed": {
        "0:00": 30
      },
      "startid": 370818250,
      "endid": 370818252
    },
    {
      "id": 1314,
      "name": "Tile Hill Lane / Tile Hill Wood School => Tile Hill Lane / Hawthorn Lane",
      "length": 0.0023928939320412776,
      "speed": {
        "0:00": 30
      },
      "startid": 370818252,
      "endid": 370818248
    },
    {
      "id": 1315,
      "name": "Tile Hill Lane / Hawthorn Lane => Tile Hill Lane / Hawthorn Lane",
      "length": 0.002419744633220715,
      "speed": {
        "0:00": 30
      },
      "startid": 370818248,
      "endid": 370818249
    },
    {
      "id": 1316,
      "name": "Tile Hill Lane / Hawthorn Lane => Tile Hill Lane / Bushbery Avenue",
      "length": 0.0011330625490235794,
      "speed": {
        "0:00": 30
      },
      "startid": 370818249,
      "endid": 370818230
    },
    {
      "id": 1317,
      "name": "Tile Hill Lane / Bushbery Avenue => Bushbery Avenue / Pinnock Place",
      "length": 0.001244928885518061,
      "speed": {
        "0:00": 30
      },
      "startid": 370818230,
      "endid": 370818232
    },
    {
      "id": 1318,
      "name": "Bushbery Avenue / Pinnock Place => Bushbery Avenue / Pinnock Place",
      "length": 0.0006943204231441324,
      "speed": {
        "0:00": 30
      },
      "startid": 370818232,
      "endid": 370818234
    },
    {
      "id": 1319,
      "name": "Bushbery Avenue / Pinnock Place => Bushbery Avenue / Frisby Rd",
      "length": 0.0014614778581995209,
      "speed": {
        "0:00": 30
      },
      "startid": 370818234,
      "endid": 370818236
    },
    {
      "id": 1320,
      "name": "Bushbery Avenue / Frisby Rd => Bushbery Avenue / Frisby Rd",
      "length": 0.00025803784606058316,
      "speed": {
        "0:00": 30
      },
      "startid": 370818236,
      "endid": 370818237
    },
    {
      "id": 1321,
      "name": "Bushbery Avenue / Frisby Rd => Bushbery Avenue / Jardine Crescent",
      "length": 0.0016594919011543182,
      "speed": {
        "0:00": 30
      },
      "startid": 370818237,
      "endid": 370819766
    },
    {
      "id": 1322,
      "name": "Bushbery Avenue / Jardine Crescent => Jardine Cres / Tile Hill Library",
      "length": 0.0009825968705425175,
      "speed": {
        "0:00": 30
      },
      "startid": 370819766,
      "endid": 370818238
    },
    {
      "id": 1323,
      "name": "Jardine Cres / Tile Hill Library => Jardine Cres / Tile Hill Library",
      "length": 0.0007638431318011407,
      "speed": {
        "0:00": 30
      },
      "startid": 370818238,
      "endid": 370818240
    },
    {
      "id": 1324,
      "name": "Jardine Cres / Tile Hill Library => Jardine Cres / Shopping Centre",
      "length": 0.0013733965632693602,
      "speed": {
        "0:00": 30
      },
      "startid": 370818240,
      "endid": 370818241
    },
    {
      "id": 1325,
      "name": "Jardine Cres / Shopping Centre => Jardine Cres / Shopping Centre",
      "length": 0.00047158156240413373,
      "speed": {
        "0:00": 30
      },
      "startid": 370818241,
      "endid": 370818242
    },
    {
      "id": 1326,
      "name": "Jardine Cres / Shopping Centre => Jardine Cres / Tile Hill North Terminus",
      "length": 0.0031497679422460506,
      "speed": {
        "0:00": 30
      },
      "startid": 370818242,
      "endid": 370818245
    },
    {
      "id": 1327,
      "name": "Jardine Cres / Tile Hill North Terminus => Jardine Cres / Tile Hill North Terminus",
      "length": 0.0001506872589189024,
      "speed": {
        "0:00": 30
      },
      "startid": 370818245,
      "endid": 370818246
    },
    {
      "id": 1328,
      "name": "Jardine Cres / Tile Hill North Terminus => Jobs Lane / Lime Tree Ave",
      "length": 0.003253505718453385,
      "speed": {
        "0:00": 30
      },
      "startid": 370818246,
      "endid": 370817770
    },
    {
      "id": 1329,
      "name": "Tile Hill Lane / Malam Close => Tile Hill Lane / Westcotes",
      "length": 0.0031507023534451846,
      "speed": {
        "0:00": 30
      },
      "startid": 370819554,
      "endid": 370817963
    },
    {
      "id": 1330,
      "name": "Tile Hill Lane / Westcotes => Tile Hill Lane / Westcotes",
      "length": 0.0009043555495492955,
      "speed": {
        "0:00": 30
      },
      "startid": 370817963,
      "endid": 370817965
    },
    {
      "id": 1331,
      "name": "Tile Hill Lane / Westcotes => Tile Hill Lane / Middlecotes",
      "length": 0.0014775972692168422,
      "speed": {
        "0:00": 30
      },
      "startid": 370817965,
      "endid": 370818178
    },
    {
      "id": 1332,
      "name": "Tile Hill Lane / Middlecotes => Tile Hill Lane / Fletchamstead Highway",
      "length": 0.0033492053281336353,
      "speed": {
        "0:00": 30
      },
      "startid": 370818178,
      "endid": 370818176
    },
    {
      "id": 1333,
      "name": "Tile Hill Lane / Fletchamstead Highway => Tile Hill Lane / Fletchamstead Highway",
      "length": 0.0001837258827754596,
      "speed": {
        "0:00": 30
      },
      "startid": 370818176,
      "endid": 370818174
    },
    {
      "id": 1334,
      "name": "Tile Hill Lane / Fletchamstead Highway => Tile Hill Lane / Sainsburys Supermarket",
      "length": 0.004021224574678767,
      "speed": {
        "0:00": 30
      },
      "startid": 370818174,
      "endid": 370817406
    },
    {
      "id": 1335,
      "name": "Tile Hill Lane / Sainsburys Supermarket => Tile Hill Lane / Stewart Close",
      "length": 0.003381800005914112,
      "speed": {
        "0:00": 30
      },
      "startid": 370817406,
      "endid": 370817711
    },
    {
      "id": 1336,
      "name": "Tile Hill Lane / Stewart Close => Tile Hill Lane / Broad Lane",
      "length": 0.005184375437793909,
      "speed": {
        "0:00": 30
      },
      "startid": 370817711,
      "endid": 370818157
    },
    {
      "id": 1337,
      "name": "Tile Hill Lane / Broad Lane => Tile Hill Lane / Brd Lane",
      "length": 0.00033008995743662075,
      "speed": {
        "0:00": 30
      },
      "startid": 370818157,
      "endid": 370818159
    },
    {
      "id": 1338,
      "name": "Tile Hill Lane / Brd Lane => Tile Hill Lane / Hearsall Common",
      "length": 0.004768650479957528,
      "speed": {
        "0:00": 30
      },
      "startid": 370818159,
      "endid": 370818853
    },
    {
      "id": 1339,
      "name": "Tile Hill Lane / Hearsall Common => Tile Hill Lane / Hearsall Common",
      "length": 0.0010889620838209612,
      "speed": {
        "0:00": 30
      },
      "startid": 370818853,
      "endid": 370818854
    },
    {
      "id": 1340,
      "name": "Tile Hill Lane / Hearsall Common => Hearsall Common / Earlsdon Ave North",
      "length": 0.005590708725197465,
      "speed": {
        "0:00": 30
      },
      "startid": 370818854,
      "endid": 370818127
    },
    {
      "id": 1341,
      "name": "Hearsall Common / Earlsdon Ave North => Hearsall Lane / Queensland Avenue",
      "length": 0.0025661573392898904,
      "speed": {
        "0:00": 30
      },
      "startid": 370818127,
      "endid": 370819672
    },
    {
      "id": 1342,
      "name": "Hearsall Lane / Queensland Avenue => Hearsall Lane / Farman Rd",
      "length": 0.002659731702637258,
      "speed": {
        "0:00": 30
      },
      "startid": 370819672,
      "endid": 370818036
    },
    {
      "id": 1343,
      "name": "Hearsall Lane / Farman Rd => Hearsall Lane / Farman Rd",
      "length": 0.00020274560414026315,
      "speed": {
        "0:00": 30
      },
      "startid": 370818036,
      "endid": 370818039
    },
    {
      "id": 1344,
      "name": "Hearsall Lane / Farman Rd => Spon End / The Arches",
      "length": 0.004305751897173334,
      "speed": {
        "0:00": 30
      },
      "startid": 370818039,
      "endid": 370818021
    },
    {
      "id": 1345,
      "name": "Spon End / The Arches => Spon End / The Arches",
      "length": 0.00015506108474010497,
      "speed": {
        "0:00": 30
      },
      "startid": 370818021,
      "endid": 370818019
    },
    {
      "id": 1346,
      "name": "Spon End / The Arches => Butts Radial Link / Albany Rd",
      "length": 0.004784828060651391,
      "speed": {
        "0:00": 30
      },
      "startid": 370818019,
      "endid": 370817814
    },
    {
      "id": 1347,
      "name": "Butts Radial Link / Albany Rd => Butts Radial Link / Albany Rd",
      "length": 0.0017027777688234339,
      "speed": {
        "0:00": 30
      },
      "startid": 370817814,
      "endid": 370817816
    },
    {
      "id": 1348,
      "name": "Butts Radial Link / Albany Rd => CR2",
      "length": 0.005168403206019783,
      "speed": {
        "0:00": 30
      },
      "startid": 370817816,
      "endid": 370817811
    },
    {
      "id": 1349,
      "name": "CR2 => CS1",
      "length": 0.003280321624474374,
      "speed": {
        "0:00": 30
      },
      "startid": 370817811,
      "endid": 370817698
    },
    {
      "id": 1350,
      "name": "CS1 => BS3",
      "length": 0.0029627712466539736,
      "speed": {
        "0:00": 30
      },
      "startid": 370817698,
      "endid": 370817695
    },
    {
      "id": 1351,
      "name": "BS3 => CS4",
      "length": 0.003071773762827612,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 370817702
    },
    {
      "id": 1352,
      "name": "CS4 => R",
      "length": 0.006968894202096288,
      "speed": {
        "0:00": 30
      },
      "startid": 370817702,
      "endid": 370817750
    },
    {
      "id": 1353,
      "name": "R => CR4",
      "length": 0.010154747626603377,
      "speed": {
        "0:00": 30
      },
      "startid": 370817750,
      "endid": 370817813
    },
    {
      "id": 1354,
      "name": "CR4 => Goodman Way / Banner Lane",
      "length": 0.07912731695849451,
      "speed": {
        "0:00": 30
      },
      "startid": 370817813,
      "endid": 4815875262
    },
    {
      "id": 1355,
      "name": "Goodman Way / Banner Lane => Herald Avenue / Business Park",
      "length": 0.04467640394716219,
      "speed": {
        "0:00": 30
      },
      "startid": 4815875262,
      "endid": 370817716
    },
    {
      "id": 1356,
      "name": "Herald Avenue / Business Park => Herald Avenue / Vanguard Avenue",
      "length": 0.003840197032705414,
      "speed": {
        "0:00": 30
      },
      "startid": 370817716,
      "endid": 370817403
    },
    {
      "id": 1357,
      "name": "Herald Avenue / Vanguard Avenue => BS7",
      "length": 0.04425088466697486,
      "speed": {
        "0:00": 30
      },
      "startid": 370817403,
      "endid": 7620250858
    },
    {
      "id": 1358,
      "name": "BS7 => BS3",
      "length": 0.00013405539899585386,
      "speed": {
        "0:00": 30
      },
      "startid": 7620250858,
      "endid": 370817695
    },
    {
      "id": 1359,
      "name": "BS3 => CS1",
      "length": 0.0029627712466539736,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 370817698
    },
    {
      "id": 1360,
      "name": "CS1 => CS4",
      "length": 0.00019329627518438407,
      "speed": {
        "0:00": 30
      },
      "startid": 370817698,
      "endid": 370817702
    },
    {
      "id": 1361,
      "name": "CS4 => VR3",
      "length": 0.002391225267514317,
      "speed": {
        "0:00": 30
      },
      "startid": 370817702,
      "endid": 370817718
    },
    {
      "id": 1362,
      "name": "VR3 => CR4",
      "length": 0.0013516956018254098,
      "speed": {
        "0:00": 30
      },
      "startid": 370817718,
      "endid": 370817813
    },
    {
      "id": 1363,
      "name": "CR4 => Butts Radial Link / Albany Rd",
      "length": 0.004735637618103989,
      "speed": {
        "0:00": 30
      },
      "startid": 370817813,
      "endid": 370817816
    },
    {
      "id": 1364,
      "name": "Butts Radial Link / Albany Rd => Albany Rd / City College",
      "length": 0.0016911294805551588,
      "speed": {
        "0:00": 30
      },
      "startid": 370817816,
      "endid": 370817817
    },
    {
      "id": 1365,
      "name": "Albany Rd / City College => Albany Rd / City College",
      "length": 0.00018201178533224562,
      "speed": {
        "0:00": 30
      },
      "startid": 370817817,
      "endid": 370817818
    },
    {
      "id": 1366,
      "name": "Albany Rd / City College => Albany Rd / Broomfield Rd",
      "length": 0.0034891287279193548,
      "speed": {
        "0:00": 30
      },
      "startid": 370817818,
      "endid": 370818022
    },
    {
      "id": 1367,
      "name": "Albany Rd / Broomfield Rd => Albany Rd / Broomfield Rd",
      "length": 0.0005570244608624081,
      "speed": {
        "0:00": 30
      },
      "startid": 370818022,
      "endid": 370818025
    },
    {
      "id": 1368,
      "name": "Albany Rd / Broomfield Rd => Albany Rd / Broadway",
      "length": 0.002721246082223814,
      "speed": {
        "0:00": 30
      },
      "startid": 370818025,
      "endid": 370819124
    },
    {
      "id": 1369,
      "name": "Albany Rd / Broadway => Albany Rd / Broadway",
      "length": 0.0002120785231948061,
      "speed": {
        "0:00": 30
      },
      "startid": 370819124,
      "endid": 370819127
    },
    {
      "id": 1370,
      "name": "Albany Rd / Broadway => Earlsdon St / Earlsdon Avenue",
      "length": 0.003458285569469386,
      "speed": {
        "0:00": 30
      },
      "startid": 370819127,
      "endid": 370819113
    },
    {
      "id": 1371,
      "name": "Earlsdon St / Earlsdon Avenue => Earlsdon St / Earlsdon Avenue",
      "length": 0.00024332895429876643,
      "speed": {
        "0:00": 30
      },
      "startid": 370819113,
      "endid": 370819114
    },
    {
      "id": 1372,
      "name": "Earlsdon St / Earlsdon Avenue => Earlsdon St / Providence St",
      "length": 0.0028033207486848235,
      "speed": {
        "0:00": 30
      },
      "startid": 370819114,
      "endid": 370819130
    },
    {
      "id": 1373,
      "name": "Earlsdon St / Providence St => Earlsdon St / Providence St",
      "length": 0.0010705297473691854,
      "speed": {
        "0:00": 30
      },
      "startid": 370819130,
      "endid": 370819128
    },
    {
      "id": 1374,
      "name": "Earlsdon St / Providence St => Radcliffe Rd / Shaftesbury Rd",
      "length": 0.00256686754625135,
      "speed": {
        "0:00": 30
      },
      "startid": 370819128,
      "endid": 370819132
    },
    {
      "id": 1375,
      "name": "Radcliffe Rd / Shaftesbury Rd => Radcliffe Rd / Shaftesbury Rd",
      "length": 0.0002819890068767573,
      "speed": {
        "0:00": 30
      },
      "startid": 370819132,
      "endid": 370819134
    },
    {
      "id": 1376,
      "name": "Radcliffe Rd / Shaftesbury Rd => Rochester Rd / St Andrews Rd",
      "length": 0.0027963258465356438,
      "speed": {
        "0:00": 30
      },
      "startid": 370819134,
      "endid": 370817902
    },
    {
      "id": 1377,
      "name": "Rochester Rd / St Andrews Rd => Rochester Rd / St Andrews Rd",
      "length": 0.0004207556179067329,
      "speed": {
        "0:00": 30
      },
      "startid": 370817902,
      "endid": 370817901
    },
    {
      "id": 1378,
      "name": "Rochester Rd / St Andrews Rd => Beechwood Ave / Shaftesbury Rd",
      "length": 0.0014072120700121648,
      "speed": {
        "0:00": 30
      },
      "startid": 370817901,
      "endid": 370819137
    },
    {
      "id": 1379,
      "name": "Beechwood Ave / Shaftesbury Rd => Beechwood Ave / Shaftesbury Rd",
      "length": 0.000650801966809613,
      "speed": {
        "0:00": 30
      },
      "startid": 370819137,
      "endid": 370819135
    },
    {
      "id": 1380,
      "name": "Beechwood Ave / Shaftesbury Rd => Canley Rd / Canley Rd",
      "length": 0.006499488959909687,
      "speed": {
        "0:00": 30
      },
      "startid": 370819135,
      "endid": 370818136
    },
    {
      "id": 1381,
      "name": "Canley Rd / Canley Rd => Dolomite Avenue / Dolomite Avenue",
      "length": 0.002426306378014798,
      "speed": {
        "0:00": 30
      },
      "startid": 370818136,
      "endid": 370819689
    },
    {
      "id": 1382,
      "name": "Dolomite Avenue / Dolomite Avenue => Dolomite Avenue / The Village Hotel",
      "length": 0.0009593649201417805,
      "speed": {
        "0:00": 30
      },
      "startid": 370819689,
      "endid": 370817418
    },
    {
      "id": 1383,
      "name": "Dolomite Avenue / The Village Hotel => Dolomite Avenue / The Village Hotel",
      "length": 0.0014798110994318396,
      "speed": {
        "0:00": 30
      },
      "startid": 370817418,
      "endid": 370817417
    },
    {
      "id": 1384,
      "name": "Dolomite Avenue / The Village Hotel => Herald Avenue / Business Park",
      "length": 0.0032564644462975234,
      "speed": {
        "0:00": 30
      },
      "startid": 370817417,
      "endid": 370817716
    },
    {
      "id": 1385,
      "name": "Herald Avenue / Business Park => Herald Avenue / Business Park",
      "length": 0.00012615902663344223,
      "speed": {
        "0:00": 30
      },
      "startid": 370817716,
      "endid": 370817713
    },
    {
      "id": 1386,
      "name": "Herald Avenue / Business Park => Herald Avenue / Vanguard Avenue",
      "length": 0.0039010029902577913,
      "speed": {
        "0:00": 30
      },
      "startid": 370817713,
      "endid": 370817403
    },
    {
      "id": 1387,
      "name": "Herald Avenue / Vanguard Avenue => Herald Avenue / Vanguard Avenue",
      "length": 0.0006769428336276444,
      "speed": {
        "0:00": 30
      },
      "startid": 370817403,
      "endid": 370817405
    },
    {
      "id": 1388,
      "name": "Herald Avenue / Vanguard Avenue => Torrington Ave / Eastcotes",
      "length": 0.008259845522164114,
      "speed": {
        "0:00": 30
      },
      "startid": 370817405,
      "endid": 370818186
    },
    {
      "id": 1389,
      "name": "Torrington Ave / Eastcotes => Torrington Ave / Eastcotes",
      "length": 0.00047775488485142395,
      "speed": {
        "0:00": 30
      },
      "startid": 370818186,
      "endid": 370818188
    },
    {
      "id": 1390,
      "name": "Torrington Ave / Eastcotes => Torrington Ave / Westcotes",
      "length": 0.0022150343225333436,
      "speed": {
        "0:00": 30
      },
      "startid": 370818188,
      "endid": 370818190
    },
    {
      "id": 1391,
      "name": "Torrington Ave / Westcotes => Torrington Ave / Westcotes",
      "length": 0.0005128377618707075,
      "speed": {
        "0:00": 30
      },
      "startid": 370818190,
      "endid": 370818191
    },
    {
      "id": 1392,
      "name": "Torrington Ave / Westcotes => Torrington Ave / Templar Avenue",
      "length": 0.0030879474088783354,
      "speed": {
        "0:00": 30
      },
      "startid": 370818191,
      "endid": 370819312
    },
    {
      "id": 1393,
      "name": "Torrington Ave / Templar Avenue => Torrington Ave / Templar Avenue",
      "length": 0.0017776843476845015,
      "speed": {
        "0:00": 30
      },
      "startid": 370819312,
      "endid": 370819313
    },
    {
      "id": 1394,
      "name": "Torrington Ave / Templar Avenue => Torrington Ave / Wolfe Rd",
      "length": 0.0024500648746511905,
      "speed": {
        "0:00": 30
      },
      "startid": 370819313,
      "endid": 370818194
    },
    {
      "id": 1395,
      "name": "Torrington Ave / Wolfe Rd => Torrington Ave / Wolfe Rd",
      "length": 0.0031646521594007877,
      "speed": {
        "0:00": 30
      },
      "startid": 370818194,
      "endid": 370818198
    },
    {
      "id": 1396,
      "name": "Torrington Ave / Wolfe Rd => Torrington Ave / Gravel Hill",
      "length": 0.0023899021841908294,
      "speed": {
        "0:00": 30
      },
      "startid": 370818198,
      "endid": 370818201
    },
    {
      "id": 1397,
      "name": "Torrington Ave / Gravel Hill => Torrington Ave / Gravel Hill",
      "length": 0.0005534496634754676,
      "speed": {
        "0:00": 30
      },
      "startid": 370818201,
      "endid": 370818203
    },
    {
      "id": 1398,
      "name": "Torrington Ave / Gravel Hill => Torrington Ave / Nickson Rd",
      "length": 0.005229098775123562,
      "speed": {
        "0:00": 30
      },
      "startid": 370818203,
      "endid": 370818255
    },
    {
      "id": 1399,
      "name": "Torrington Ave / Nickson Rd => Torrington Ave / Nickson Rd",
      "length": 0.0004799438404651654,
      "speed": {
        "0:00": 30
      },
      "startid": 370818255,
      "endid": 370818254
    },
    {
      "id": 1400,
      "name": "Torrington Ave / Nickson Rd => Torrington Ave / Plants Hill Crescent",
      "length": 0.0038062571024563016,
      "speed": {
        "0:00": 30
      },
      "startid": 370818254,
      "endid": 4815875263
    },
    {
      "id": 1401,
      "name": "Torrington Ave / Plants Hill Crescent => Torrington Ave / Plants Hill Crescent",
      "length": 0.00012937097820345838,
      "speed": {
        "0:00": 30
      },
      "startid": 4815875263,
      "endid": 4815875264
    },
    {
      "id": 1402,
      "name": "Torrington Ave / Plants Hill Crescent => Torrington Ave / Station Avenue",
      "length": 0.005869790936652033,
      "speed": {
        "0:00": 30
      },
      "startid": 4815875264,
      "endid": 370818258
    },
    {
      "id": 1403,
      "name": "Torrington Ave / Station Avenue => Torrington Ave / Station Avenue",
      "length": 0.00026873574380902873,
      "speed": {
        "0:00": 30
      },
      "startid": 370818258,
      "endid": 370818256
    },
    {
      "id": 1404,
      "name": "Torrington Ave / Station Avenue => L",
      "length": 0.08911272467431325,
      "speed": {
        "0:00": 30
      },
      "startid": 370818256,
      "endid": 370817744
    },
    {
      "id": 1405,
      "name": "BS3 => CS4",
      "length": 0.003071773762827612,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 370817702
    },
    {
      "id": 1406,
      "name": "CS4 => CS1",
      "length": 0.00019329627518438407,
      "speed": {
        "0:00": 30
      },
      "startid": 370817702,
      "endid": 370817698
    },
    {
      "id": 1407,
      "name": "CS1 => CR4",
      "length": 0.0037459906153076926,
      "speed": {
        "0:00": 30
      },
      "startid": 370817698,
      "endid": 370817813
    },
    {
      "id": 1408,
      "name": "CR4 => Butts Radial Link / Albany Rd",
      "length": 0.006404540102146532,
      "speed": {
        "0:00": 30
      },
      "startid": 370817813,
      "endid": 370817814
    },
    {
      "id": 1409,
      "name": "Butts Radial Link / Albany Rd => Butts Radial Link / Albany Rd",
      "length": 0.0017027777688234339,
      "speed": {
        "0:00": 30
      },
      "startid": 370817814,
      "endid": 370817816
    },
    {
      "id": 1410,
      "name": "Butts Radial Link / Albany Rd => Spon End / The Arches",
      "length": 0.006341274146415984,
      "speed": {
        "0:00": 30
      },
      "startid": 370817816,
      "endid": 370818021
    },
    {
      "id": 1411,
      "name": "Spon End / The Arches => Spon End / The Arches",
      "length": 0.00015506108474010497,
      "speed": {
        "0:00": 30
      },
      "startid": 370818021,
      "endid": 370818019
    },
    {
      "id": 1412,
      "name": "Spon End / The Arches => Hearsall Lane / Farman Rd",
      "length": 0.004176989971259531,
      "speed": {
        "0:00": 30
      },
      "startid": 370818019,
      "endid": 370818039
    },
    {
      "id": 1413,
      "name": "Hearsall Lane / Farman Rd => Hearsall Lane / Farman Rd",
      "length": 0.00020274560414026315,
      "speed": {
        "0:00": 30
      },
      "startid": 370818039,
      "endid": 370818036
    },
    {
      "id": 1414,
      "name": "Hearsall Lane / Farman Rd => Hearsall Lane / Queensland Avenue",
      "length": 0.002659731702637258,
      "speed": {
        "0:00": 30
      },
      "startid": 370818036,
      "endid": 370819672
    },
    {
      "id": 1415,
      "name": "Hearsall Lane / Queensland Avenue => Hearsall Common / Earlsdon Ave North",
      "length": 0.0025661573392898904,
      "speed": {
        "0:00": 30
      },
      "startid": 370819672,
      "endid": 370818127
    },
    {
      "id": 1416,
      "name": "Hearsall Common / Earlsdon Ave North => Tile Hill Lane / Hearsall Common",
      "length": 0.005590708725197465,
      "speed": {
        "0:00": 30
      },
      "startid": 370818127,
      "endid": 370818854
    },
    {
      "id": 1417,
      "name": "Tile Hill Lane / Hearsall Common => Tile Hill Lane / Hearsall Common",
      "length": 0.0010889620838209612,
      "speed": {
        "0:00": 30
      },
      "startid": 370818854,
      "endid": 370818853
    },
    {
      "id": 1418,
      "name": "Tile Hill Lane / Hearsall Common => Tile Hill Lane / Broad Lane",
      "length": 0.005069562744458173,
      "speed": {
        "0:00": 30
      },
      "startid": 370818853,
      "endid": 370818157
    },
    {
      "id": 1419,
      "name": "Tile Hill Lane / Broad Lane => Tile Hill Lane / Brd Lane",
      "length": 0.00033008995743662075,
      "speed": {
        "0:00": 30
      },
      "startid": 370818157,
      "endid": 370818159
    },
    {
      "id": 1420,
      "name": "Tile Hill Lane / Brd Lane => Herald Avenue / Business Park",
      "length": 0.003972316140490556,
      "speed": {
        "0:00": 30
      },
      "startid": 370818159,
      "endid": 370817716
    },
    {
      "id": 1421,
      "name": "Herald Avenue / Business Park => Herald Avenue / Business Park",
      "length": 0.00012615902663344223,
      "speed": {
        "0:00": 30
      },
      "startid": 370817716,
      "endid": 370817713
    },
    {
      "id": 1422,
      "name": "Herald Avenue / Business Park => Herald Avenue / Vanguard Avenue",
      "length": 0.004546689324112717,
      "speed": {
        "0:00": 30
      },
      "startid": 370817713,
      "endid": 370817405
    },
    {
      "id": 1423,
      "name": "Herald Avenue / Vanguard Avenue => Herald Avenue / Vanguard Avenue",
      "length": 0.0006769428336276444,
      "speed": {
        "0:00": 30
      },
      "startid": 370817405,
      "endid": 370817403
    },
    {
      "id": 1424,
      "name": "Herald Avenue / Vanguard Avenue => Fletchamstead Highway / Torrington Avenue",
      "length": 0.004357169614556578,
      "speed": {
        "0:00": 30
      },
      "startid": 370817403,
      "endid": 370818204
    },
    {
      "id": 1425,
      "name": "Fletchamstead Highway / Torrington Avenue => Prior Deram Walk / Fletchamstead Highway",
      "length": 0.005392149531496474,
      "speed": {
        "0:00": 30
      },
      "startid": 370818204,
      "endid": 4815876523
    },
    {
      "id": 1426,
      "name": "Prior Deram Walk / Fletchamstead Highway => Prior Deram Walk / Fletchamstead Highway",
      "length": 0.00010448564494865598,
      "speed": {
        "0:00": 30
      },
      "startid": 4815876523,
      "endid": 4815876524
    },
    {
      "id": 1427,
      "name": "Prior Deram Walk / Fletchamstead Highway => Sheriff Ave / Prior Deram Walk",
      "length": 0.005011514505615828,
      "speed": {
        "0:00": 30
      },
      "startid": 4815876524,
      "endid": 370819155
    },
    {
      "id": 1428,
      "name": "Sheriff Ave / Prior Deram Walk => Prior Deram Walk / John Ross Ave",
      "length": 0.0032020073781933484,
      "speed": {
        "0:00": 30
      },
      "startid": 370819155,
      "endid": 370819682
    },
    {
      "id": 1429,
      "name": "Prior Deram Walk / John Ross Ave => Templars Fields / John Ross Avenue",
      "length": 0.0005438519743467372,
      "speed": {
        "0:00": 30
      },
      "startid": 370819682,
      "endid": 370819687
    },
    {
      "id": 1430,
      "name": "Templars Fields / John Ross Avenue => John Rous Ave / Wendiburgh St",
      "length": 0.0018530347999994171,
      "speed": {
        "0:00": 30
      },
      "startid": 370819687,
      "endid": 370817979
    },
    {
      "id": 1431,
      "name": "John Rous Ave / Wendiburgh St => John Rous Ave / Wendiburgh St",
      "length": 0.00015920050251101692,
      "speed": {
        "0:00": 30
      },
      "startid": 370817979,
      "endid": 370817980
    },
    {
      "id": 1432,
      "name": "John Rous Ave / Wendiburgh St => Charter Ave / John Rous Ave",
      "length": 0.0016137827610889553,
      "speed": {
        "0:00": 30
      },
      "startid": 370817980,
      "endid": 370817981
    },
    {
      "id": 1433,
      "name": "Charter Ave / John Rous Ave => Charter Ave / Mitchell Ave",
      "length": 0.0029593990014863333,
      "speed": {
        "0:00": 30
      },
      "startid": 370817981,
      "endid": 370817984
    },
    {
      "id": 1434,
      "name": "Charter Ave / Mitchell Ave => Charter Ave / Mitchell Ave",
      "length": 0.0001658795044617579,
      "speed": {
        "0:00": 30
      },
      "startid": 370817984,
      "endid": 370817985
    },
    {
      "id": 1435,
      "name": "Charter Ave / Mitchell Ave => Charter Ave / Ten Shilling Wood",
      "length": 0.0038769225553261584,
      "speed": {
        "0:00": 30
      },
      "startid": 370817985,
      "endid": 370817987
    },
    {
      "id": 1436,
      "name": "Charter Ave / Ten Shilling Wood => Charter Ave / Ten Shilling Wood",
      "length": 0.0008599757264015652,
      "speed": {
        "0:00": 30
      },
      "startid": 370817987,
      "endid": 370817986
    },
    {
      "id": 1437,
      "name": "Charter Ave / Ten Shilling Wood => Charter Ave / Wolfe Rd",
      "length": 0.0024701140398776956,
      "speed": {
        "0:00": 30
      },
      "startid": 370817986,
      "endid": 370817991
    },
    {
      "id": 1438,
      "name": "Charter Ave / Wolfe Rd => Charter Ave / Wolfe Rd",
      "length": 0.00106623742665507,
      "speed": {
        "0:00": 30
      },
      "startid": 370817991,
      "endid": 370817990
    },
    {
      "id": 1439,
      "name": "Charter Ave / Wolfe Rd => Charter Ave / Marler Rd",
      "length": 0.002550340951715976,
      "speed": {
        "0:00": 30
      },
      "startid": 370817990,
      "endid": 370817994
    },
    {
      "id": 1440,
      "name": "Charter Ave / Marler Rd => Charter Ave / Marler Rd",
      "length": 0.0005352118552501463,
      "speed": {
        "0:00": 30
      },
      "startid": 370817994,
      "endid": 370817996
    },
    {
      "id": 1441,
      "name": "Charter Ave / Marler Rd => Charter Ave / Warren Green",
      "length": 0.002650100424512346,
      "speed": {
        "0:00": 30
      },
      "startid": 370817996,
      "endid": 370817999
    },
    {
      "id": 1442,
      "name": "Charter Ave / Warren Green => Charter Ave / Warren Green",
      "length": 0.0006786605115951983,
      "speed": {
        "0:00": 30
      },
      "startid": 370817999,
      "endid": 370817997
    },
    {
      "id": 1443,
      "name": "Charter Ave / Warren Green => Charter Ave / Bradney Green",
      "length": 0.002562906562869614,
      "speed": {
        "0:00": 30
      },
      "startid": 370817997,
      "endid": 370818003
    },
    {
      "id": 1444,
      "name": "Charter Ave / Bradney Green => Charter Ave / Bradney Green",
      "length": 0.0007407507813021757,
      "speed": {
        "0:00": 30
      },
      "startid": 370818003,
      "endid": 370818000
    },
    {
      "id": 1445,
      "name": "Charter Ave / Bradney Green => Charter Ave / Marina Close",
      "length": 0.0040959540976431485,
      "speed": {
        "0:00": 30
      },
      "startid": 370818000,
      "endid": 370818005
    },
    {
      "id": 1446,
      "name": "Charter Ave / Marina Close => Charter Ave / Marina Close",
      "length": 0.0005919281206352491,
      "speed": {
        "0:00": 30
      },
      "startid": 370818005,
      "endid": 370818006
    },
    {
      "id": 1447,
      "name": "Charter Ave / Marina Close => Charter Ave / Dalmeny Rd",
      "length": 0.005579417590573337,
      "speed": {
        "0:00": 30
      },
      "startid": 370818006,
      "endid": 370818017
    },
    {
      "id": 1448,
      "name": "Charter Ave / Dalmeny Rd => Charter Ave / Dalmeny Rd",
      "length": 0.0014327701281086536,
      "speed": {
        "0:00": 30
      },
      "startid": 370818017,
      "endid": 370818016
    },
    {
      "id": 1449,
      "name": "Charter Ave / Dalmeny Rd => Cromwell Lane / Tile Hill Rail Station",
      "length": 0.0010329564608424775,
      "speed": {
        "0:00": 30
      },
      "startid": 370818016,
      "endid": 370818007
    },
    {
      "id": 1450,
      "name": "Cromwell Lane / Tile Hill Rail Station => Cromwell Lane / Tile Hill Rail Station",
      "length": 0.00012686378521843434,
      "speed": {
        "0:00": 30
      },
      "startid": 370818007,
      "endid": 370818008
    },
    {
      "id": 1451,
      "name": "Cromwell Lane / Tile Hill Rail Station => Station Ave / Torrington Ave",
      "length": 0.003986429501446275,
      "speed": {
        "0:00": 30
      },
      "startid": 370818008,
      "endid": 4316311353
    },
    {
      "id": 1452,
      "name": "Station Ave / Torrington Ave => Torrington Ave / Station Avenue",
      "length": 0.0007348293543436731,
      "speed": {
        "0:00": 30
      },
      "startid": 4316311353,
      "endid": 370818256
    },
    {
      "id": 1453,
      "name": "Torrington Ave / Station Avenue => VR3",
      "length": 0.07969210212223003,
      "speed": {
        "0:00": 30
      },
      "startid": 370818256,
      "endid": 370817718
    },
    {
      "id": 1454,
      "name": "VR3 => BS7",
      "length": 0.005316306727418198,
      "speed": {
        "0:00": 30
      },
      "startid": 370817718,
      "endid": 7620250858
    },
    {
      "id": 1455,
      "name": "BS7 => U",
      "length": 0.005002861671083985,
      "speed": {
        "0:00": 30
      },
      "startid": 7620250858,
      "endid": 370817754
    },
    {
      "id": 1456,
      "name": "Birmingham Rd / Oak Lane => Birmingham Rd / Oak Lane",
      "length": 0.0001902503876463026,
      "speed": {
        "0:00": 30
      },
      "startid": 370819532,
      "endid": 370819533
    },
    {
      "id": 1457,
      "name": "Birmingham Rd / Brickhill Lane => Birmingham Rd / Brickhill Lane",
      "length": 0.0006062756633735554,
      "speed": {
        "0:00": 30
      },
      "startid": 370819527,
      "endid": 370819530
    },
    {
      "id": 1458,
      "name": "Birmingham Rd / Brickhill Lane => Birmingham Rd / Windmill Farm",
      "length": 0.012881388064957972,
      "speed": {
        "0:00": 30
      },
      "startid": 370819530,
      "endid": 370819525
    },
    {
      "id": 1459,
      "name": "Birmingham Rd / Windmill Farm => Birmingham Rd / Neale Avenue",
      "length": 0.010618614085180432,
      "speed": {
        "0:00": 30
      },
      "startid": 370819525,
      "endid": 370819493
    },
    {
      "id": 1460,
      "name": "Birmingham Rd / Neale Avenue => Birmingham Rd / Neale Avenue",
      "length": 0.0014933214590289524,
      "speed": {
        "0:00": 30
      },
      "startid": 370819493,
      "endid": 370819494
    },
    {
      "id": 1461,
      "name": "Birmingham Rd / Neale Avenue => Birmingham Rd / Allesley Post Office",
      "length": 0.0015646175379312936,
      "speed": {
        "0:00": 30
      },
      "startid": 370819494,
      "endid": 370819489
    },
    {
      "id": 1462,
      "name": "Birmingham Rd / Allesley Post Office => Birmingham Rd / Allesley Post Office",
      "length": 0.0008820798716671872,
      "speed": {
        "0:00": 30
      },
      "startid": 370819489,
      "endid": 370819490
    },
    {
      "id": 1463,
      "name": "Birmingham Rd / Allesley Post Office => Birmingham Rd / Butchers Lane",
      "length": 0.002760424034455538,
      "speed": {
        "0:00": 30
      },
      "startid": 370819490,
      "endid": 370819486
    },
    {
      "id": 1464,
      "name": "Birmingham Rd / Butchers Lane => Birmingham Rd / Butchers Lane",
      "length": 0.002666668160832974,
      "speed": {
        "0:00": 30
      },
      "startid": 370819486,
      "endid": 370819484
    },
    {
      "id": 1465,
      "name": "Birmingham Rd / Butchers Lane => Birmingham Rd / Norton Grange",
      "length": 0.0032394266313661847,
      "speed": {
        "0:00": 30
      },
      "startid": 370819484,
      "endid": 370819481
    },
    {
      "id": 1466,
      "name": "Birmingham Rd / Norton Grange => Birmingham Rd / Norton Grange",
      "length": 0.00018735042033075414,
      "speed": {
        "0:00": 30
      },
      "startid": 370819481,
      "endid": 370819482
    },
    {
      "id": 1467,
      "name": "Birmingham Rd / Norton Grange => Holyhead Rd / Dulverton Avenue",
      "length": 0.005333658446132934,
      "speed": {
        "0:00": 30
      },
      "startid": 370819482,
      "endid": 370819479
    },
    {
      "id": 1468,
      "name": "Holyhead Rd / Dulverton Avenue => Holyhead Rd / Dulverton Avenue",
      "length": 0.0004808124894384671,
      "speed": {
        "0:00": 30
      },
      "startid": 370819479,
      "endid": 370819480
    },
    {
      "id": 1469,
      "name": "Holyhead Rd / Dulverton Avenue => Holyhead Rd / Grayswood Avenue",
      "length": 0.005298354314313946,
      "speed": {
        "0:00": 30
      },
      "startid": 370819480,
      "endid": 370819453
    },
    {
      "id": 1470,
      "name": "Holyhead Rd / Grayswood Avenue => Holyhead Rd / Grayswood Avenue",
      "length": 0.0015367593988653307,
      "speed": {
        "0:00": 30
      },
      "startid": 370819453,
      "endid": 370819454
    },
    {
      "id": 1471,
      "name": "Holyhead Rd / Grayswood Avenue => Holyhead Rd / Southbank Rd",
      "length": 0.0018399552304324976,
      "speed": {
        "0:00": 30
      },
      "startid": 370819454,
      "endid": 370819450
    },
    {
      "id": 1472,
      "name": "Holyhead Rd / Southbank Rd => Holyhead Rd / Southbank Rd",
      "length": 0.0020147104010257858,
      "speed": {
        "0:00": 30
      },
      "startid": 370819450,
      "endid": 370819452
    },
    {
      "id": 1473,
      "name": "Holyhead Rd / Southbank Rd => Holyhead Rd / Redesdale Avenue",
      "length": 0.0032341260334133653,
      "speed": {
        "0:00": 30
      },
      "startid": 370819452,
      "endid": 370819398
    },
    {
      "id": 1474,
      "name": "Holyhead Rd / Redesdale Avenue => Holyhead Rd / Redesdale Avenue",
      "length": 0.0006598299856777957,
      "speed": {
        "0:00": 30
      },
      "startid": 370819398,
      "endid": 370819399
    },
    {
      "id": 1475,
      "name": "Holyhead Rd / Redesdale Avenue => Holyhead Rd / Moseley Avenue",
      "length": 0.003837463750968571,
      "speed": {
        "0:00": 30
      },
      "startid": 370819399,
      "endid": 370819395
    },
    {
      "id": 1476,
      "name": "Holyhead Rd / Moseley Avenue => Holyhead Rd / Moseley Avenue",
      "length": 0.0008869628740820093,
      "speed": {
        "0:00": 30
      },
      "startid": 370819395,
      "endid": 370819397
    },
    {
      "id": 1477,
      "name": "Holyhead Rd / Moseley Avenue => Holyhead Rd / Alvis Retail Park",
      "length": 0.0043102225893796985,
      "speed": {
        "0:00": 30
      },
      "startid": 370819397,
      "endid": 370819361
    },
    {
      "id": 1478,
      "name": "Holyhead Rd / Alvis Retail Park => Holyhead Rd / Alvis Retail Park",
      "length": 0.0002442421953716176,
      "speed": {
        "0:00": 30
      },
      "startid": 370819361,
      "endid": 370819363
    },
    {
      "id": 1479,
      "name": "Holyhead Rd / Alvis Retail Park => Holyhead Rd / Meriden St",
      "length": 0.006867083871630511,
      "speed": {
        "0:00": 30
      },
      "startid": 370819363,
      "endid": 370819360
    },
    {
      "id": 1480,
      "name": "Holyhead Rd / Meriden St => Holyhead Rd / Meriden St",
      "length": 0.0008530438792932072,
      "speed": {
        "0:00": 30
      },
      "startid": 370819360,
      "endid": 370819359
    },
    {
      "id": 1481,
      "name": "Holyhead Rd / Meriden St => Holyhead Rd / Ringway",
      "length": 0.0034018527613649606,
      "speed": {
        "0:00": 30
      },
      "startid": 370819359,
      "endid": 370819355
    },
    {
      "id": 1482,
      "name": "Holyhead Rd / Ringway => Holyhead Rd / Ringway",
      "length": 0.0001523425416673504,
      "speed": {
        "0:00": 30
      },
      "startid": 370819355,
      "endid": 370819357
    },
    {
      "id": 1483,
      "name": "Holyhead Rd / Ringway => UL3",
      "length": 0.0059757926938607455,
      "speed": {
        "0:00": 30
      },
      "startid": 370819357,
      "endid": 370817723
    },
    {
      "id": 1484,
      "name": "UL4 => BS3",
      "length": 0.002031303665137189,
      "speed": {
        "0:00": 30
      },
      "startid": 370817719,
      "endid": 370817695
    },
    {
      "id": 1485,
      "name": "BS7 => BS3",
      "length": 0.00013405539899585386,
      "speed": {
        "0:00": 30
      },
      "startid": 7620250858,
      "endid": 370817695
    },
    {
      "id": 1486,
      "name": "BS3 => CS1",
      "length": 0.0029627712466539736,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 370817698
    },
    {
      "id": 1487,
      "name": "CS1 => CS4",
      "length": 0.00019329627518438407,
      "speed": {
        "0:00": 30
      },
      "startid": 370817698,
      "endid": 370817702
    },
    {
      "id": 1488,
      "name": "CS4 => VR3",
      "length": 0.002391225267514317,
      "speed": {
        "0:00": 30
      },
      "startid": 370817702,
      "endid": 370817718
    },
    {
      "id": 1489,
      "name": "VR3 => CR4",
      "length": 0.0013516956018254098,
      "speed": {
        "0:00": 30
      },
      "startid": 370817718,
      "endid": 370817813
    },
    {
      "id": 1490,
      "name": "CR4 => Butts Radial Link / Albany Rd",
      "length": 0.004735637618103989,
      "speed": {
        "0:00": 30
      },
      "startid": 370817813,
      "endid": 370817816
    },
    {
      "id": 1491,
      "name": "Butts Radial Link / Albany Rd => Albany Rd / City College",
      "length": 0.0016911294805551588,
      "speed": {
        "0:00": 30
      },
      "startid": 370817816,
      "endid": 370817817
    },
    {
      "id": 1492,
      "name": "Albany Rd / City College => Albany Rd / City College",
      "length": 0.00018201178533224562,
      "speed": {
        "0:00": 30
      },
      "startid": 370817817,
      "endid": 370817818
    },
    {
      "id": 1493,
      "name": "Albany Rd / City College => Albany Rd / Broomfield Rd",
      "length": 0.0034891287279193548,
      "speed": {
        "0:00": 30
      },
      "startid": 370817818,
      "endid": 370818022
    },
    {
      "id": 1494,
      "name": "Albany Rd / Broomfield Rd => Albany Rd / Broomfield Rd",
      "length": 0.0005570244608624081,
      "speed": {
        "0:00": 30
      },
      "startid": 370818022,
      "endid": 370818025
    },
    {
      "id": 1495,
      "name": "Albany Rd / Broomfield Rd => Albany Rd / Broadway",
      "length": 0.002721246082223814,
      "speed": {
        "0:00": 30
      },
      "startid": 370818025,
      "endid": 370819124
    },
    {
      "id": 1496,
      "name": "Albany Rd / Broadway => Albany Rd / Broadway",
      "length": 0.0002120785231948061,
      "speed": {
        "0:00": 30
      },
      "startid": 370819124,
      "endid": 370819127
    },
    {
      "id": 1497,
      "name": "Albany Rd / Broadway => Earlsdon St / Earlsdon Avenue",
      "length": 0.003458285569469386,
      "speed": {
        "0:00": 30
      },
      "startid": 370819127,
      "endid": 370819113
    },
    {
      "id": 1498,
      "name": "Earlsdon St / Earlsdon Avenue => Earlsdon St / Earlsdon Avenue",
      "length": 0.00024332895429876643,
      "speed": {
        "0:00": 30
      },
      "startid": 370819113,
      "endid": 370819114
    },
    {
      "id": 1499,
      "name": "Earlsdon St / Earlsdon Avenue => Earlsdon St / Providence St",
      "length": 0.0028033207486848235,
      "speed": {
        "0:00": 30
      },
      "startid": 370819114,
      "endid": 370819130
    },
    {
      "id": 1500,
      "name": "Earlsdon St / Providence St => Earlsdon St / Providence St",
      "length": 0.0010705297473691854,
      "speed": {
        "0:00": 30
      },
      "startid": 370819130,
      "endid": 370819128
    },
    {
      "id": 1501,
      "name": "Earlsdon St / Providence St => Radcliffe Rd / Shaftesbury Rd",
      "length": 0.00256686754625135,
      "speed": {
        "0:00": 30
      },
      "startid": 370819128,
      "endid": 370819132
    },
    {
      "id": 1502,
      "name": "Radcliffe Rd / Shaftesbury Rd => Radcliffe Rd / Shaftesbury Rd",
      "length": 0.0002819890068767573,
      "speed": {
        "0:00": 30
      },
      "startid": 370819132,
      "endid": 370819134
    },
    {
      "id": 1503,
      "name": "Radcliffe Rd / Shaftesbury Rd => Rochester Rd / St Andrews Rd",
      "length": 0.0027963258465356438,
      "speed": {
        "0:00": 30
      },
      "startid": 370819134,
      "endid": 370817902
    },
    {
      "id": 1504,
      "name": "Rochester Rd / St Andrews Rd => Rochester Rd / St Andrews Rd",
      "length": 0.0004207556179067329,
      "speed": {
        "0:00": 30
      },
      "startid": 370817902,
      "endid": 370817901
    },
    {
      "id": 1505,
      "name": "Rochester Rd / St Andrews Rd => Beechwood Ave / Shaftesbury Rd",
      "length": 0.0014072120700121648,
      "speed": {
        "0:00": 30
      },
      "startid": 370817901,
      "endid": 370819137
    },
    {
      "id": 1506,
      "name": "Beechwood Ave / Shaftesbury Rd => Beechwood Ave / Shaftesbury Rd",
      "length": 0.000650801966809613,
      "speed": {
        "0:00": 30
      },
      "startid": 370819137,
      "endid": 370819135
    },
    {
      "id": 1507,
      "name": "Beechwood Ave / Shaftesbury Rd => Canley Rd / Canley Rd",
      "length": 0.006499488959909687,
      "speed": {
        "0:00": 30
      },
      "startid": 370819135,
      "endid": 370818136
    },
    {
      "id": 1508,
      "name": "Canley Rd / Canley Rd => Dolomite Avenue / Dolomite Avenue",
      "length": 0.002426306378014798,
      "speed": {
        "0:00": 30
      },
      "startid": 370818136,
      "endid": 370819689
    },
    {
      "id": 1509,
      "name": "Dolomite Avenue / Dolomite Avenue => Dolomite Avenue / The Village Hotel",
      "length": 0.0009593649201417805,
      "speed": {
        "0:00": 30
      },
      "startid": 370819689,
      "endid": 370817418
    },
    {
      "id": 1510,
      "name": "Dolomite Avenue / The Village Hotel => Dolomite Avenue / The Village Hotel",
      "length": 0.0014798110994318396,
      "speed": {
        "0:00": 30
      },
      "startid": 370817418,
      "endid": 370817417
    },
    {
      "id": 1511,
      "name": "Dolomite Avenue / The Village Hotel => Tile Hill Lane / Broad Lane",
      "length": 0.001230580306194953,
      "speed": {
        "0:00": 30
      },
      "startid": 370817417,
      "endid": 370818157
    },
    {
      "id": 1512,
      "name": "Tile Hill Lane / Broad Lane => Tile Hill Lane / Brd Lane",
      "length": 0.00033008995743662075,
      "speed": {
        "0:00": 30
      },
      "startid": 370818157,
      "endid": 370818159
    },
    {
      "id": 1513,
      "name": "Tile Hill Lane / Brd Lane => Broad Lane / Guphill Avenue",
      "length": 0.0026135655683363246,
      "speed": {
        "0:00": 30
      },
      "startid": 370818159,
      "endid": 370818163
    },
    {
      "id": 1514,
      "name": "Broad Lane / Guphill Avenue => Broad Lane / Guphill Avenue",
      "length": 0.0008312963611127701,
      "speed": {
        "0:00": 30
      },
      "startid": 370818163,
      "endid": 4815880383
    },
    {
      "id": 1515,
      "name": "Grayswood Avenue / Allesley Old Rd => Grayswood Avenue / Allesley Old Rd",
      "length": 0.00014018059780044486,
      "speed": {
        "0:00": 30
      },
      "startid": 370819675,
      "endid": 370819673
    },
    {
      "id": 1516,
      "name": "Grayswood Avenue / Allesley Old Rd => Grayswood Avenue / Lincroft Crescent",
      "length": 0.002239405961409797,
      "speed": {
        "0:00": 30
      },
      "startid": 370819673,
      "endid": 370819422
    },
    {
      "id": 1517,
      "name": "Grayswood Avenue / Lincroft Crescent => Grayswood Avenue / Lincroft Crescent",
      "length": 0.00039742220622244556,
      "speed": {
        "0:00": 30
      },
      "startid": 370819422,
      "endid": 370819423
    },
    {
      "id": 1518,
      "name": "Grayswood Avenue / Lincroft Crescent => Grayswood Avenue / Westbury Rd",
      "length": 0.001945023783919739,
      "speed": {
        "0:00": 30
      },
      "startid": 370819423,
      "endid": 370819425
    },
    {
      "id": 1519,
      "name": "Grayswood Avenue / Westbury Rd => Grayswood Avenue / Westbury Rd",
      "length": 0.0004298546847459111,
      "speed": {
        "0:00": 30
      },
      "startid": 370819425,
      "endid": 370819426
    },
    {
      "id": 1520,
      "name": "Grayswood Avenue / Westbury Rd => Kingsbury Rd / Morfa Gardens",
      "length": 0.001869744052001299,
      "speed": {
        "0:00": 30
      },
      "startid": 370819426,
      "endid": 370818814
    },
    {
      "id": 1521,
      "name": "Kingsbury Rd / Morfa Gardens => Kingsbury Rd / Morfa Gardens",
      "length": 0.0002346570476252687,
      "speed": {
        "0:00": 30
      },
      "startid": 370818814,
      "endid": 370818815
    },
    {
      "id": 1522,
      "name": "Kingsbury Rd / Morfa Gardens => Kingsbury Rd / Forfield Rd",
      "length": 0.002124688071222401,
      "speed": {
        "0:00": 30
      },
      "startid": 370818815,
      "endid": 370819531
    },
    {
      "id": 1523,
      "name": "Kingsbury Rd / Forfield Rd => Forfield Rd / Kingsbury Rd",
      "length": 0.0006363882148532272,
      "speed": {
        "0:00": 30
      },
      "startid": 370819531,
      "endid": 370819476
    },
    {
      "id": 1524,
      "name": "Forfield Rd / Kingsbury Rd => Forfield Rd / Donnington Avenue",
      "length": 0.0039029464203348737,
      "speed": {
        "0:00": 30
      },
      "startid": 370819476,
      "endid": 370819474
    },
    {
      "id": 1525,
      "name": "Forfield Rd / Donnington Avenue => Forfield Rd / Donnington Avenue",
      "length": 0.0007997796258971145,
      "speed": {
        "0:00": 30
      },
      "startid": 370819474,
      "endid": 370819475
    },
    {
      "id": 1526,
      "name": "Forfield Rd / Donnington Avenue => Forfield Rd / Coundon Jun & Inf School",
      "length": 0.0018597823367256243,
      "speed": {
        "0:00": 30
      },
      "startid": 370819475,
      "endid": 370819781
    },
    {
      "id": 1527,
      "name": "Forfield Rd / Coundon Jun & Inf School => Courtland Ave / Evenlode Crescent",
      "length": 0.0012915526508817362,
      "speed": {
        "0:00": 30
      },
      "startid": 370819781,
      "endid": 370819468
    },
    {
      "id": 1528,
      "name": "Courtland Ave / Evenlode Crescent => Courtland Ave / Westhill Rd",
      "length": 0.0022943387108270504,
      "speed": {
        "0:00": 30
      },
      "startid": 370819468,
      "endid": 370819779
    },
    {
      "id": 1529,
      "name": "Courtland Ave / Westhill Rd => Westhill Rd / Courtland Avenue",
      "length": 0.0011599790429136195,
      "speed": {
        "0:00": 30
      },
      "startid": 370819779,
      "endid": 370819456
    },
    {
      "id": 1530,
      "name": "Westhill Rd / Courtland Avenue => L",
      "length": 0.029829962297831778,
      "speed": {
        "0:00": 30
      },
      "startid": 370819456,
      "endid": 370817744
    },
    {
      "id": 1531,
      "name": "Nunts Lane / Wheelwright Lane => Nunts Lane / Wheelwright Lane",
      "length": 0.0007817865949221464,
      "speed": {
        "0:00": 30
      },
      "startid": 370818714,
      "endid": 370818716
    },
    {
      "id": 1532,
      "name": "Nunts Lane / Wheelwright Lane => Nunts Lane / Meadow Rd",
      "length": 0.003030058621542563,
      "speed": {
        "0:00": 30
      },
      "startid": 370818716,
      "endid": 370818712
    },
    {
      "id": 1533,
      "name": "Nunts Lane / Meadow Rd => Nunts Lane / Meadow Rd",
      "length": 0.00026166027593344074,
      "speed": {
        "0:00": 30
      },
      "startid": 370818712,
      "endid": 370818711
    },
    {
      "id": 1534,
      "name": "Nunts Lane / Meadow Rd => Nunts Lane / President Kennedy School",
      "length": 0.004345190878430753,
      "speed": {
        "0:00": 30
      },
      "startid": 370818711,
      "endid": 370819701
    },
    {
      "id": 1535,
      "name": "Nunts Lane / President Kennedy School => Nunts Lane / Rookery Lane",
      "length": 0.0008203896939888987,
      "speed": {
        "0:00": 30
      },
      "startid": 370819701,
      "endid": 370818688
    },
    {
      "id": 1536,
      "name": "Nunts Lane / Rookery Lane => Nunts Lane / Penny Park Lane",
      "length": 0.0015526625679787574,
      "speed": {
        "0:00": 30
      },
      "startid": 370818688,
      "endid": 370819699
    },
    {
      "id": 1537,
      "name": "Nunts Lane / Penny Park Lane => Nunts Lane / Penny Park Lane",
      "length": 0.0001726166851722771,
      "speed": {
        "0:00": 30
      },
      "startid": 370819699,
      "endid": 370819700
    },
    {
      "id": 1538,
      "name": "Nunts Lane / Penny Park Lane => Beake Ave / Parkgate Rd",
      "length": 0.0009538853704683507,
      "speed": {
        "0:00": 30
      },
      "startid": 370819700,
      "endid": 370818684
    },
    {
      "id": 1539,
      "name": "Beake Ave / Parkgate Rd => Beake Ave / Parkgate Rd",
      "length": 0.0006693548012856229,
      "speed": {
        "0:00": 30
      },
      "startid": 370818684,
      "endid": 370818685
    },
    {
      "id": 1540,
      "name": "Beake Ave / Parkgate Rd => Beake Ave / Malmesbury Rd",
      "length": 0.0017924738045482253,
      "speed": {
        "0:00": 30
      },
      "startid": 370818685,
      "endid": 370818681
    },
    {
      "id": 1541,
      "name": "Beake Ave / Malmesbury Rd => Beake Ave / Malmesbury Rd",
      "length": 0.00038853145303937534,
      "speed": {
        "0:00": 30
      },
      "startid": 370818681,
      "endid": 370818682
    },
    {
      "id": 1542,
      "name": "Beake Ave / Malmesbury Rd => Beake Ave / Charlewood Rd",
      "length": 0.002171343017582009,
      "speed": {
        "0:00": 30
      },
      "startid": 370818682,
      "endid": 370818680
    },
    {
      "id": 1543,
      "name": "Beake Ave / Charlewood Rd => Beake Ave / Charlewood Rd",
      "length": 0.0010172803939915557,
      "speed": {
        "0:00": 30
      },
      "startid": 370818680,
      "endid": 370818678
    },
    {
      "id": 1544,
      "name": "Beake Ave / Charlewood Rd => Beake Ave / Rylston Avenue",
      "length": 0.0008496359926433696,
      "speed": {
        "0:00": 30
      },
      "startid": 370818678,
      "endid": 370818677
    },
    {
      "id": 1545,
      "name": "Beake Ave / Rylston Avenue => Beake Ave / Rylston Avenue",
      "length": 0.0007987534350477337,
      "speed": {
        "0:00": 30
      },
      "startid": 370818677,
      "endid": 370818676
    },
    {
      "id": 1546,
      "name": "Beake Ave / Rylston Avenue => Beake Ave / Burnaby Rd",
      "length": 0.0027552680613679033,
      "speed": {
        "0:00": 30
      },
      "startid": 370818676,
      "endid": 370818674
    },
    {
      "id": 1547,
      "name": "Beake Ave / Burnaby Rd => Beake Ave / Burnaby Rd",
      "length": 0.001202855610623443,
      "speed": {
        "0:00": 30
      },
      "startid": 370818674,
      "endid": 370818673
    },
    {
      "id": 1548,
      "name": "Beake Ave / Burnaby Rd => Beake Ave / Bruce Rd",
      "length": 0.0016678367336138821,
      "speed": {
        "0:00": 30
      },
      "startid": 370818673,
      "endid": 370818637
    },
    {
      "id": 1549,
      "name": "Beake Ave / Bruce Rd => Beake Ave / Bruce Rd",
      "length": 0.0005624411524788363,
      "speed": {
        "0:00": 30
      },
      "startid": 370818637,
      "endid": 370818635
    },
    {
      "id": 1550,
      "name": "Beake Ave / Bruce Rd => Links Rd / St Francis Church",
      "length": 0.0027401997080509772,
      "speed": {
        "0:00": 30
      },
      "startid": 370818635,
      "endid": 370819713
    },
    {
      "id": 1551,
      "name": "Links Rd / St Francis Church => Jubilee Cres / Catesby Rd",
      "length": 0.003171995972569986,
      "speed": {
        "0:00": 30
      },
      "startid": 370819713,
      "endid": 370818625
    },
    {
      "id": 1552,
      "name": "Jubilee Cres / Catesby Rd => Jubilee Cres / Cheveral Avenue",
      "length": 0.001403347440940119,
      "speed": {
        "0:00": 30
      },
      "startid": 370818625,
      "endid": 370818623
    },
    {
      "id": 1553,
      "name": "Jubilee Cres / Cheveral Avenue => Jubilee Cres / Cheveral Avenue",
      "length": 0.0005373033593782694,
      "speed": {
        "0:00": 30
      },
      "startid": 370818623,
      "endid": 370818624
    },
    {
      "id": 1554,
      "name": "Jubilee Cres / Cheveral Avenue => Cheveral Ave / Capmartin Rd",
      "length": 0.001744769981976498,
      "speed": {
        "0:00": 30
      },
      "startid": 370818624,
      "endid": 370818620
    },
    {
      "id": 1555,
      "name": "Cheveral Ave / Capmartin Rd => Cheveral Ave / Villa Rd",
      "length": 0.002890468814910147,
      "speed": {
        "0:00": 30
      },
      "startid": 370818620,
      "endid": 370817840
    },
    {
      "id": 1556,
      "name": "Cheveral Ave / Villa Rd => Cheveral Ave / Villa Rd",
      "length": 0.0005671686257178555,
      "speed": {
        "0:00": 30
      },
      "startid": 370817840,
      "endid": 370817839
    },
    {
      "id": 1557,
      "name": "Cheveral Ave / Villa Rd => Cheveral Ave / Capmartin Rd",
      "length": 0.0030643068547356964,
      "speed": {
        "0:00": 30
      },
      "startid": 370817839,
      "endid": 370818619
    },
    {
      "id": 1558,
      "name": "Cheveral Ave / Capmartin Rd => Cheveral Ave / Lanchester Rd",
      "length": 0.005029855231514759,
      "speed": {
        "0:00": 30
      },
      "startid": 370818619,
      "endid": 370817838
    },
    {
      "id": 1559,
      "name": "Cheveral Ave / Lanchester Rd => Cheveral Ave / Lanchester Rd",
      "length": 0.0004154093162158902,
      "speed": {
        "0:00": 30
      },
      "startid": 370817838,
      "endid": 370817836
    },
    {
      "id": 1560,
      "name": "Cheveral Ave / Lanchester Rd => Middlemarch Rd / Cheveral Ave",
      "length": 0.003575306132348245,
      "speed": {
        "0:00": 30
      },
      "startid": 370817836,
      "endid": 370817835
    },
    {
      "id": 1561,
      "name": "Sandy Lane / Ellys Rd => Sandy Lane / Ellys Rd",
      "length": 0.001170397475221997,
      "speed": {
        "0:00": 30
      },
      "startid": 370817834,
      "endid": 370817832
    },
    {
      "id": 1562,
      "name": "Sandy Lane / Ellys Rd => St Nicholas St / Sandy Lane",
      "length": 0.0021774297922035023,
      "speed": {
        "0:00": 30
      },
      "startid": 370817832,
      "endid": 370818790
    },
    {
      "id": 1563,
      "name": "St Nicholas St / Sandy Lane => St Nicholas St / Sandy Lane",
      "length": 0.00036177523408451083,
      "speed": {
        "0:00": 30
      },
      "startid": 370818790,
      "endid": 370818786
    },
    {
      "id": 1564,
      "name": "St Nicholas St / Sandy Lane => Radford Rd / Nauls Mill House",
      "length": 0.0019665262291672096,
      "speed": {
        "0:00": 30
      },
      "startid": 370818786,
      "endid": 370817830
    },
    {
      "id": 1565,
      "name": "Radford Rd / Nauls Mill House => UL1",
      "length": 0.0036185522657547556,
      "speed": {
        "0:00": 30
      },
      "startid": 370817830,
      "endid": 370817726
    },
    {
      "id": 1566,
      "name": "UL1 => FX1",
      "length": 0.009435829558655578,
      "speed": {
        "0:00": 30
      },
      "startid": 370817726,
      "endid": 370817768
    },
    {
      "id": 1567,
      "name": "FX1 => CU4",
      "length": 0.001230879766667563,
      "speed": {
        "0:00": 30
      },
      "startid": 370817768,
      "endid": 370819679
    },
    {
      "id": 1568,
      "name": "CU4 => CU5",
      "length": 0.0005253710783815626,
      "speed": {
        "0:00": 30
      },
      "startid": 370819679,
      "endid": 370819676
    },
    {
      "id": 1569,
      "name": "CU5 => CU1",
      "length": 0.0021117262535691986,
      "speed": {
        "0:00": 30
      },
      "startid": 370819676,
      "endid": 370817766
    },
    {
      "id": 1570,
      "name": "CU1 => CU2",
      "length": 0.00010206831045847219,
      "speed": {
        "0:00": 30
      },
      "startid": 370817766,
      "endid": 370819680
    },
    {
      "id": 1571,
      "name": "CU2 => Binley Rd / Kingsway",
      "length": 0.016530180219525733,
      "speed": {
        "0:00": 30
      },
      "startid": 370819680,
      "endid": 370818331
    },
    {
      "id": 1572,
      "name": "Binley Rd / Kingsway => Binley Rd / Kingsway",
      "length": 0.00018105593058337426,
      "speed": {
        "0:00": 30
      },
      "startid": 370818331,
      "endid": 370818333
    },
    {
      "id": 1573,
      "name": "Binley Rd / Kingsway => Binley Rd / Bulls Head Lane",
      "length": 0.00749600886939167,
      "speed": {
        "0:00": 30
      },
      "startid": 370818333,
      "endid": 370818334
    },
    {
      "id": 1574,
      "name": "Binley Rd / Bulls Head Lane => Binley Rd / Bulls Head Lane",
      "length": 0.00028935241488505436,
      "speed": {
        "0:00": 30
      },
      "startid": 370818334,
      "endid": 370818335
    },
    {
      "id": 1575,
      "name": "Binley Rd / Bulls Head Lane => Binley Rd / Raleigh Rd",
      "length": 0.004580672816302087,
      "speed": {
        "0:00": 30
      },
      "startid": 370818335,
      "endid": 370818354
    },
    {
      "id": 1576,
      "name": "Binley Rd / Raleigh Rd => Binley Rd / Raleigh Rd",
      "length": 0.00018749146647080057,
      "speed": {
        "0:00": 30
      },
      "startid": 370818354,
      "endid": 370818353
    },
    {
      "id": 1577,
      "name": "Binley Rd / Raleigh Rd => Binley Rd / Uxbridge Avenue",
      "length": 0.0025842683838951724,
      "speed": {
        "0:00": 30
      },
      "startid": 370818353,
      "endid": 370818357
    },
    {
      "id": 1578,
      "name": "Binley Rd / Uxbridge Avenue => Binley Rd / Uxbridge Avenue",
      "length": 0.0016673498283206552,
      "speed": {
        "0:00": 30
      },
      "startid": 370818357,
      "endid": 370818356
    },
    {
      "id": 1579,
      "name": "Binley Rd / Uxbridge Avenue => Binley Rd / Bromleigh Drive",
      "length": 0.001940932984416144,
      "speed": {
        "0:00": 30
      },
      "startid": 370818356,
      "endid": 370818360
    },
    {
      "id": 1580,
      "name": "Binley Rd / Bromleigh Drive => Binley Rd / Bromleigh Drive",
      "length": 0.0017399300704338118,
      "speed": {
        "0:00": 30
      },
      "startid": 370818360,
      "endid": 370818359
    },
    {
      "id": 1581,
      "name": "Binley Rd / Bromleigh Drive => Binley Rd / Hipswell Highway",
      "length": 0.004219849173846242,
      "speed": {
        "0:00": 30
      },
      "startid": 370818359,
      "endid": 370818363
    },
    {
      "id": 1582,
      "name": "Binley Rd / Hipswell Highway => Binley Rd / Hipswell Highway",
      "length": 0.0021794502724310242,
      "speed": {
        "0:00": 30
      },
      "startid": 370818363,
      "endid": 370818361
    },
    {
      "id": 1583,
      "name": "Binley Rd / Hipswell Highway => Binley Rd / Binley Rd Post Office",
      "length": 0.004144084219702413,
      "speed": {
        "0:00": 30
      },
      "startid": 370818361,
      "endid": 370818380
    },
    {
      "id": 1584,
      "name": "Binley Rd / Binley Rd Post Office => Binley Rd / Binley Rd Post Office",
      "length": 0.002033100710737182,
      "speed": {
        "0:00": 30
      },
      "startid": 370818380,
      "endid": 370818378
    },
    {
      "id": 1585,
      "name": "Binley Rd / Binley Rd Post Office => Binley Rd / Princethorpe Way",
      "length": 0.0021313370005712384,
      "speed": {
        "0:00": 30
      },
      "startid": 370818378,
      "endid": 370818382
    },
    {
      "id": 1586,
      "name": "Binley Rd / Princethorpe Way => Binley Rd / Princethorpe Way",
      "length": 0.0018588263635960756,
      "speed": {
        "0:00": 30
      },
      "startid": 370818382,
      "endid": 370818381
    },
    {
      "id": 1587,
      "name": "Binley Rd / Princethorpe Way => Binley Rd / Ebro Crescent",
      "length": 0.0016824441090271,
      "speed": {
        "0:00": 30
      },
      "startid": 370818381,
      "endid": 370817807
    },
    {
      "id": 1588,
      "name": "Binley Rd / Ebro Crescent => Brandon Rd / Binley Park Inn",
      "length": 0.0017650665284913514,
      "speed": {
        "0:00": 30
      },
      "startid": 370817807,
      "endid": 370818456
    },
    {
      "id": 1589,
      "name": "Brandon Rd / Binley Park Inn => Brandon Rd / Binley Park Inn",
      "length": 0.0005661131512307444,
      "speed": {
        "0:00": 30
      },
      "startid": 370818456,
      "endid": 370818453
    },
    {
      "id": 1590,
      "name": "Brandon Rd / Binley Park Inn => Brandon Rd / Willenhall Lane",
      "length": 0.0039827592570996434,
      "speed": {
        "0:00": 30
      },
      "startid": 370818453,
      "endid": 370818461
    },
    {
      "id": 1591,
      "name": "Brandon Rd / Willenhall Lane => Brandon Rd / Willenhall Lane",
      "length": 0.0003965726289091613,
      "speed": {
        "0:00": 30
      },
      "startid": 370818461,
      "endid": 370818463
    },
    {
      "id": 1592,
      "name": "Brandon Rd / Willenhall Lane => Quorn Way / William Mckee Close",
      "length": 0.01069690745776319,
      "speed": {
        "0:00": 30
      },
      "startid": 370818463,
      "endid": 370818481
    },
    {
      "id": 1593,
      "name": "Quorn Way / William Mckee Close => Quorn Way / William Mckee Close",
      "length": 0.00033093233447511073,
      "speed": {
        "0:00": 30
      },
      "startid": 370818481,
      "endid": 370818482
    },
    {
      "id": 1594,
      "name": "Quorn Way / William Mckee Close => Bredon Avenue / Ashby Close",
      "length": 0.001413791091355694,
      "speed": {
        "0:00": 30
      },
      "startid": 370818482,
      "endid": 370818479
    },
    {
      "id": 1595,
      "name": "Bredon Avenue / Ashby Close => Bredon Avenue / Ashby Close",
      "length": 0.0005371153041952862,
      "speed": {
        "0:00": 30
      },
      "startid": 370818479,
      "endid": 370818478
    },
    {
      "id": 1596,
      "name": "Bredon Avenue / Ashby Close => Bredon Avenue / Invicta Rd",
      "length": 0.0017172689043927207,
      "speed": {
        "0:00": 30
      },
      "startid": 370818478,
      "endid": 370818474
    },
    {
      "id": 1597,
      "name": "Bredon Avenue / Invicta Rd => Bredon Avenue / Invicta Rd",
      "length": 0.0013760327030977414,
      "speed": {
        "0:00": 30
      },
      "startid": 370818474,
      "endid": 370818475
    },
    {
      "id": 1598,
      "name": "Bredon Avenue / Invicta Rd => Bredon Avenue / Sandwick Close",
      "length": 0.001335234391409192,
      "speed": {
        "0:00": 30
      },
      "startid": 370818475,
      "endid": 370818472
    },
    {
      "id": 1599,
      "name": "Bredon Avenue / Sandwick Close => Bredon Avenue / Sandwick Close",
      "length": 0.0002288041302067782,
      "speed": {
        "0:00": 30
      },
      "startid": 370818472,
      "endid": 370818471
    },
    {
      "id": 1600,
      "name": "Bredon Avenue / Sandwick Close => Deerdale Way / Willenhall Lane",
      "length": 0.004044732185200675,
      "speed": {
        "0:00": 30
      },
      "startid": 370818471,
      "endid": 370818400
    },
    {
      "id": 1601,
      "name": "Deerdale Way / Willenhall Lane => Deerdale Way / Willenhall Lane",
      "length": 0.0007129659879684774,
      "speed": {
        "0:00": 30
      },
      "startid": 370818400,
      "endid": 370818402
    },
    {
      "id": 1602,
      "name": "Deerdale Way / Willenhall Lane => Willenhall Lane / Industrial Estate",
      "length": 0.001456776413868924,
      "speed": {
        "0:00": 30
      },
      "startid": 370818402,
      "endid": 370818470
    },
    {
      "id": 1603,
      "name": "Willenhall Lane / Industrial Estate => Willenhall Lane / Craigends Avenue",
      "length": 0.011664377478460067,
      "speed": {
        "0:00": 30
      },
      "startid": 370818470,
      "endid": 370818485
    },
    {
      "id": 1604,
      "name": "Willenhall Lane / Craigends Avenue => Willenhall Lane / Craigends Avenue",
      "length": 0.0001938537593170669,
      "speed": {
        "0:00": 30
      },
      "startid": 370818485,
      "endid": 370818483
    },
    {
      "id": 1605,
      "name": "Willenhall Lane / Craigends Avenue => St James Lane / Middle Ride",
      "length": 0.003727561472329797,
      "speed": {
        "0:00": 30
      },
      "startid": 370818483,
      "endid": 370819037
    },
    {
      "id": 1606,
      "name": "St James Lane / Middle Ride => St James Lane / Middle Ride",
      "length": 0.0009964726589326248,
      "speed": {
        "0:00": 30
      },
      "startid": 370819037,
      "endid": 370819033
    },
    {
      "id": 1607,
      "name": "St James Lane / Middle Ride => St James Lane / Remembrance Rd",
      "length": 0.0017672077778229558,
      "speed": {
        "0:00": 30
      },
      "startid": 370819033,
      "endid": 370819030
    },
    {
      "id": 1608,
      "name": "St James Lane / Remembrance Rd => St James Lane / Willenhall Wood School",
      "length": 0.0033931926043192875,
      "speed": {
        "0:00": 30
      },
      "startid": 370819030,
      "endid": 370819002
    },
    {
      "id": 1609,
      "name": "St James Lane / Willenhall Wood School => Remembrance Rd / Meadfoot Rd",
      "length": 0.0013200700928394727,
      "speed": {
        "0:00": 30
      },
      "startid": 370819002,
      "endid": 370819015
    },
    {
      "id": 1610,
      "name": "Remembrance Rd / Meadfoot Rd => Robin Hood Rd / Willenhall Social Club",
      "length": 0.0045265002165026874,
      "speed": {
        "0:00": 30
      },
      "startid": 370819015,
      "endid": 370819060
    },
    {
      "id": 1611,
      "name": "Robin Hood Rd / Willenhall Social Club => Remembrance Rd / Robin Hood Rd",
      "length": 0.0014578932917113077,
      "speed": {
        "0:00": 30
      },
      "startid": 370819060,
      "endid": 370819023
    },
    {
      "id": 1612,
      "name": "Remembrance Rd / Robin Hood Rd => Radford Rd / Nauls Mill House",
      "length": 0.057876319776310935,
      "speed": {
        "0:00": 30
      },
      "startid": 370819023,
      "endid": 370817828
    },
    {
      "id": 1613,
      "name": "Radford Rd / Nauls Mill House => St James Lane / Remembrance Rd",
      "length": 0.06369611897321496,
      "speed": {
        "0:00": 30
      },
      "startid": 370817828,
      "endid": 370819024
    },
    {
      "id": 1614,
      "name": "St James Lane / Remembrance Rd => UL5",
      "length": 0.06126347933124472,
      "speed": {
        "0:00": 30
      },
      "startid": 370819024,
      "endid": 370817721
    },
    {
      "id": 1615,
      "name": "UL5 => BS4",
      "length": 0.002976046861189749,
      "speed": {
        "0:00": 30
      },
      "startid": 370817721,
      "endid": 4815881232
    },
    {
      "id": 1616,
      "name": "BS4 => HS2",
      "length": 0.0013113488704368352,
      "speed": {
        "0:00": 30
      },
      "startid": 4815881232,
      "endid": 717585774
    },
    {
      "id": 1617,
      "name": "HS2 => Sky Blue Way / Walkway To Gosford St",
      "length": 0.01374081876017471,
      "speed": {
        "0:00": 30
      },
      "startid": 717585774,
      "endid": 4815874919
    },
    {
      "id": 1618,
      "name": "Sky Blue Way / Walkway To Gosford St => Far Gosford St / Bramble St",
      "length": 0.0009964229724399199,
      "speed": {
        "0:00": 30
      },
      "startid": 4815874919,
      "endid": 4815880407
    },
    {
      "id": 1619,
      "name": "Far Gosford St / Bramble St => Far Gosford St / Gosford Green",
      "length": 0.004033183017171992,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880407,
      "endid": 4815880406
    },
    {
      "id": 1620,
      "name": "Far Gosford St / Gosford Green => Sky Blue Way / Gosford Green",
      "length": 0.000299047170195088,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880406,
      "endid": 4815880374
    },
    {
      "id": 1621,
      "name": "Nunts Lane / Wheelwright Lane => Nunts Lane / Wheelwright Lane",
      "length": 0.0007817865949221464,
      "speed": {
        "0:00": 30
      },
      "startid": 370818714,
      "endid": 370818716
    },
    {
      "id": 1622,
      "name": "Nunts Lane / Wheelwright Lane => Nunts Lane / Meadow Rd",
      "length": 0.003030058621542563,
      "speed": {
        "0:00": 30
      },
      "startid": 370818716,
      "endid": 370818712
    },
    {
      "id": 1623,
      "name": "Nunts Lane / Meadow Rd => Nunts Lane / Meadow Rd",
      "length": 0.00026166027593344074,
      "speed": {
        "0:00": 30
      },
      "startid": 370818712,
      "endid": 370818711
    },
    {
      "id": 1624,
      "name": "Nunts Lane / Meadow Rd => Nunts Lane / President Kennedy School",
      "length": 0.004345190878430753,
      "speed": {
        "0:00": 30
      },
      "startid": 370818711,
      "endid": 370819701
    },
    {
      "id": 1625,
      "name": "Nunts Lane / President Kennedy School => Nunts Lane / Rookery Lane",
      "length": 0.0008203896939888987,
      "speed": {
        "0:00": 30
      },
      "startid": 370819701,
      "endid": 370818688
    },
    {
      "id": 1626,
      "name": "Nunts Lane / Rookery Lane => Nunts Lane / Penny Park Lane",
      "length": 0.0015526625679787574,
      "speed": {
        "0:00": 30
      },
      "startid": 370818688,
      "endid": 370819699
    },
    {
      "id": 1627,
      "name": "Nunts Lane / Penny Park Lane => Nunts Lane / Penny Park Lane",
      "length": 0.0001726166851722771,
      "speed": {
        "0:00": 30
      },
      "startid": 370819699,
      "endid": 370819700
    },
    {
      "id": 1628,
      "name": "Nunts Lane / Penny Park Lane => Beake Ave / Parkgate Rd",
      "length": 0.0009538853704683507,
      "speed": {
        "0:00": 30
      },
      "startid": 370819700,
      "endid": 370818684
    },
    {
      "id": 1629,
      "name": "Beake Ave / Parkgate Rd => Beake Ave / Parkgate Rd",
      "length": 0.0006693548012856229,
      "speed": {
        "0:00": 30
      },
      "startid": 370818684,
      "endid": 370818685
    },
    {
      "id": 1630,
      "name": "Beake Ave / Parkgate Rd => Beake Ave / Malmesbury Rd",
      "length": 0.0017924738045482253,
      "speed": {
        "0:00": 30
      },
      "startid": 370818685,
      "endid": 370818681
    },
    {
      "id": 1631,
      "name": "Beake Ave / Malmesbury Rd => Beake Ave / Malmesbury Rd",
      "length": 0.00038853145303937534,
      "speed": {
        "0:00": 30
      },
      "startid": 370818681,
      "endid": 370818682
    },
    {
      "id": 1632,
      "name": "Beake Ave / Malmesbury Rd => Beake Ave / Charlewood Rd",
      "length": 0.002171343017582009,
      "speed": {
        "0:00": 30
      },
      "startid": 370818682,
      "endid": 370818680
    },
    {
      "id": 1633,
      "name": "Beake Ave / Charlewood Rd => Beake Ave / Charlewood Rd",
      "length": 0.0010172803939915557,
      "speed": {
        "0:00": 30
      },
      "startid": 370818680,
      "endid": 370818678
    },
    {
      "id": 1634,
      "name": "Beake Ave / Charlewood Rd => Beake Ave / Rylston Avenue",
      "length": 0.0008496359926433696,
      "speed": {
        "0:00": 30
      },
      "startid": 370818678,
      "endid": 370818677
    },
    {
      "id": 1635,
      "name": "Beake Ave / Rylston Avenue => Beake Ave / Rylston Avenue",
      "length": 0.0007987534350477337,
      "speed": {
        "0:00": 30
      },
      "startid": 370818677,
      "endid": 370818676
    },
    {
      "id": 1636,
      "name": "Beake Ave / Rylston Avenue => Beake Ave / Burnaby Rd",
      "length": 0.0027552680613679033,
      "speed": {
        "0:00": 30
      },
      "startid": 370818676,
      "endid": 370818674
    },
    {
      "id": 1637,
      "name": "Beake Ave / Burnaby Rd => Beake Ave / Burnaby Rd",
      "length": 0.001202855610623443,
      "speed": {
        "0:00": 30
      },
      "startid": 370818674,
      "endid": 370818673
    },
    {
      "id": 1638,
      "name": "Beake Ave / Burnaby Rd => Beake Ave / Bruce Rd",
      "length": 0.0016678367336138821,
      "speed": {
        "0:00": 30
      },
      "startid": 370818673,
      "endid": 370818637
    },
    {
      "id": 1639,
      "name": "Beake Ave / Bruce Rd => Beake Ave / Bruce Rd",
      "length": 0.0005624411524788363,
      "speed": {
        "0:00": 30
      },
      "startid": 370818637,
      "endid": 370818635
    },
    {
      "id": 1640,
      "name": "Beake Ave / Bruce Rd => Links Rd / St Francis Church",
      "length": 0.0027401997080509772,
      "speed": {
        "0:00": 30
      },
      "startid": 370818635,
      "endid": 370819713
    },
    {
      "id": 1641,
      "name": "Links Rd / St Francis Church => Jubilee Cres / Catesby Rd",
      "length": 0.003171995972569986,
      "speed": {
        "0:00": 30
      },
      "startid": 370819713,
      "endid": 370818625
    },
    {
      "id": 1642,
      "name": "Jubilee Cres / Catesby Rd => Jubilee Cres / Cheveral Avenue",
      "length": 0.001403347440940119,
      "speed": {
        "0:00": 30
      },
      "startid": 370818625,
      "endid": 370818623
    },
    {
      "id": 1643,
      "name": "Jubilee Cres / Cheveral Avenue => Jubilee Cres / Cheveral Avenue",
      "length": 0.0005373033593782694,
      "speed": {
        "0:00": 30
      },
      "startid": 370818623,
      "endid": 370818624
    },
    {
      "id": 1644,
      "name": "Jubilee Cres / Cheveral Avenue => Cheveral Ave / Capmartin Rd",
      "length": 0.001744769981976498,
      "speed": {
        "0:00": 30
      },
      "startid": 370818624,
      "endid": 370818620
    },
    {
      "id": 1645,
      "name": "Cheveral Ave / Capmartin Rd => Cheveral Ave / Villa Rd",
      "length": 0.002890468814910147,
      "speed": {
        "0:00": 30
      },
      "startid": 370818620,
      "endid": 370817840
    },
    {
      "id": 1646,
      "name": "Cheveral Ave / Villa Rd => Cheveral Ave / Villa Rd",
      "length": 0.0005671686257178555,
      "speed": {
        "0:00": 30
      },
      "startid": 370817840,
      "endid": 370817839
    },
    {
      "id": 1647,
      "name": "Cheveral Ave / Villa Rd => Cheveral Ave / Capmartin Rd",
      "length": 0.0030643068547356964,
      "speed": {
        "0:00": 30
      },
      "startid": 370817839,
      "endid": 370818619
    },
    {
      "id": 1648,
      "name": "Cheveral Ave / Capmartin Rd => Cheveral Ave / Lanchester Rd",
      "length": 0.005029855231514759,
      "speed": {
        "0:00": 30
      },
      "startid": 370818619,
      "endid": 370817838
    },
    {
      "id": 1649,
      "name": "Cheveral Ave / Lanchester Rd => Cheveral Ave / Lanchester Rd",
      "length": 0.0004154093162158902,
      "speed": {
        "0:00": 30
      },
      "startid": 370817838,
      "endid": 370817836
    },
    {
      "id": 1650,
      "name": "Cheveral Ave / Lanchester Rd => Middlemarch Rd / Cheveral Ave",
      "length": 0.003575306132348245,
      "speed": {
        "0:00": 30
      },
      "startid": 370817836,
      "endid": 370817835
    },
    {
      "id": 1651,
      "name": "Sandy Lane / Ellys Rd => Sandy Lane / Ellys Rd",
      "length": 0.001170397475221997,
      "speed": {
        "0:00": 30
      },
      "startid": 370817834,
      "endid": 370817832
    },
    {
      "id": 1652,
      "name": "Sandy Lane / Ellys Rd => St Nicholas St / Sandy Lane",
      "length": 0.0021774297922035023,
      "speed": {
        "0:00": 30
      },
      "startid": 370817832,
      "endid": 370818790
    },
    {
      "id": 1653,
      "name": "St Nicholas St / Sandy Lane => St Nicholas St / Sandy Lane",
      "length": 0.00036177523408451083,
      "speed": {
        "0:00": 30
      },
      "startid": 370818790,
      "endid": 370818786
    },
    {
      "id": 1654,
      "name": "St Nicholas St / Sandy Lane => Radford Rd / Nauls Mill House",
      "length": 0.0019665262291672096,
      "speed": {
        "0:00": 30
      },
      "startid": 370818786,
      "endid": 370817830
    },
    {
      "id": 1655,
      "name": "Radford Rd / Nauls Mill House => UL1",
      "length": 0.0036185522657547556,
      "speed": {
        "0:00": 30
      },
      "startid": 370817830,
      "endid": 370817726
    },
    {
      "id": 1656,
      "name": "UL1 => FX1",
      "length": 0.009435829558655578,
      "speed": {
        "0:00": 30
      },
      "startid": 370817726,
      "endid": 370817768
    },
    {
      "id": 1657,
      "name": "FX1 => CU4",
      "length": 0.001230879766667563,
      "speed": {
        "0:00": 30
      },
      "startid": 370817768,
      "endid": 370819679
    },
    {
      "id": 1658,
      "name": "CU4 => CU5",
      "length": 0.0005253710783815626,
      "speed": {
        "0:00": 30
      },
      "startid": 370819679,
      "endid": 370819676
    },
    {
      "id": 1659,
      "name": "CU5 => CU1",
      "length": 0.0021117262535691986,
      "speed": {
        "0:00": 30
      },
      "startid": 370819676,
      "endid": 370817766
    },
    {
      "id": 1660,
      "name": "CU1 => CU2",
      "length": 0.00010206831045847219,
      "speed": {
        "0:00": 30
      },
      "startid": 370817766,
      "endid": 370819680
    },
    {
      "id": 1661,
      "name": "CU2 => Binley Rd / Kingsway",
      "length": 0.016530180219525733,
      "speed": {
        "0:00": 30
      },
      "startid": 370819680,
      "endid": 370818331
    },
    {
      "id": 1662,
      "name": "Binley Rd / Kingsway => Binley Rd / Kingsway",
      "length": 0.00018105593058337426,
      "speed": {
        "0:00": 30
      },
      "startid": 370818331,
      "endid": 370818333
    },
    {
      "id": 1663,
      "name": "Binley Rd / Kingsway => Binley Rd / Bulls Head Lane",
      "length": 0.00749600886939167,
      "speed": {
        "0:00": 30
      },
      "startid": 370818333,
      "endid": 370818334
    },
    {
      "id": 1664,
      "name": "Binley Rd / Bulls Head Lane => Binley Rd / Bulls Head Lane",
      "length": 0.00028935241488505436,
      "speed": {
        "0:00": 30
      },
      "startid": 370818334,
      "endid": 370818335
    },
    {
      "id": 1665,
      "name": "Binley Rd / Bulls Head Lane => Binley Rd / Raleigh Rd",
      "length": 0.004580672816302087,
      "speed": {
        "0:00": 30
      },
      "startid": 370818335,
      "endid": 370818354
    },
    {
      "id": 1666,
      "name": "Binley Rd / Raleigh Rd => Binley Rd / Raleigh Rd",
      "length": 0.00018749146647080057,
      "speed": {
        "0:00": 30
      },
      "startid": 370818354,
      "endid": 370818353
    },
    {
      "id": 1667,
      "name": "Binley Rd / Raleigh Rd => Binley Rd / Uxbridge Avenue",
      "length": 0.0025842683838951724,
      "speed": {
        "0:00": 30
      },
      "startid": 370818353,
      "endid": 370818357
    },
    {
      "id": 1668,
      "name": "Binley Rd / Uxbridge Avenue => Binley Rd / Uxbridge Avenue",
      "length": 0.0016673498283206552,
      "speed": {
        "0:00": 30
      },
      "startid": 370818357,
      "endid": 370818356
    },
    {
      "id": 1669,
      "name": "Binley Rd / Uxbridge Avenue => Binley Rd / Bromleigh Drive",
      "length": 0.001940932984416144,
      "speed": {
        "0:00": 30
      },
      "startid": 370818356,
      "endid": 370818360
    },
    {
      "id": 1670,
      "name": "Binley Rd / Bromleigh Drive => Binley Rd / Bromleigh Drive",
      "length": 0.0017399300704338118,
      "speed": {
        "0:00": 30
      },
      "startid": 370818360,
      "endid": 370818359
    },
    {
      "id": 1671,
      "name": "Binley Rd / Bromleigh Drive => Binley Rd / Hipswell Highway",
      "length": 0.004219849173846242,
      "speed": {
        "0:00": 30
      },
      "startid": 370818359,
      "endid": 370818363
    },
    {
      "id": 1672,
      "name": "Binley Rd / Hipswell Highway => Binley Rd / Hipswell Highway",
      "length": 0.0021794502724310242,
      "speed": {
        "0:00": 30
      },
      "startid": 370818363,
      "endid": 370818361
    },
    {
      "id": 1673,
      "name": "Binley Rd / Hipswell Highway => Binley Rd / Binley Rd Post Office",
      "length": 0.004144084219702413,
      "speed": {
        "0:00": 30
      },
      "startid": 370818361,
      "endid": 370818380
    },
    {
      "id": 1674,
      "name": "Binley Rd / Binley Rd Post Office => Binley Rd / Binley Rd Post Office",
      "length": 0.002033100710737182,
      "speed": {
        "0:00": 30
      },
      "startid": 370818380,
      "endid": 370818378
    },
    {
      "id": 1675,
      "name": "Binley Rd / Binley Rd Post Office => Binley Rd / Princethorpe Way",
      "length": 0.0021313370005712384,
      "speed": {
        "0:00": 30
      },
      "startid": 370818378,
      "endid": 370818382
    },
    {
      "id": 1676,
      "name": "Binley Rd / Princethorpe Way => Binley Rd / Princethorpe Way",
      "length": 0.0018588263635960756,
      "speed": {
        "0:00": 30
      },
      "startid": 370818382,
      "endid": 370818381
    },
    {
      "id": 1677,
      "name": "Binley Rd / Princethorpe Way => Binley Rd / Ebro Crescent",
      "length": 0.0016824441090271,
      "speed": {
        "0:00": 30
      },
      "startid": 370818381,
      "endid": 370817807
    },
    {
      "id": 1678,
      "name": "Binley Rd / Ebro Crescent => Brandon Rd / Binley Park Inn",
      "length": 0.0017650665284913514,
      "speed": {
        "0:00": 30
      },
      "startid": 370817807,
      "endid": 370818456
    },
    {
      "id": 1679,
      "name": "Brandon Rd / Binley Park Inn => Brandon Rd / Binley Park Inn",
      "length": 0.0005661131512307444,
      "speed": {
        "0:00": 30
      },
      "startid": 370818456,
      "endid": 370818453
    },
    {
      "id": 1680,
      "name": "Brandon Rd / Binley Park Inn => Brandon Rd / Willenhall Lane",
      "length": 0.0039827592570996434,
      "speed": {
        "0:00": 30
      },
      "startid": 370818453,
      "endid": 370818461
    },
    {
      "id": 1681,
      "name": "Brandon Rd / Willenhall Lane => Brandon Rd / Willenhall Lane",
      "length": 0.0003965726289091613,
      "speed": {
        "0:00": 30
      },
      "startid": 370818461,
      "endid": 370818463
    },
    {
      "id": 1682,
      "name": "Brandon Rd / Willenhall Lane => Brandon Rd / Herald Way",
      "length": 0.002604435086537471,
      "speed": {
        "0:00": 30
      },
      "startid": 370818463,
      "endid": 370817407
    },
    {
      "id": 1683,
      "name": "Brandon Rd / Herald Way => Brandon Rd / Herald Way",
      "length": 0.00024123619131873235,
      "speed": {
        "0:00": 30
      },
      "startid": 370817407,
      "endid": 370817408
    },
    {
      "id": 1684,
      "name": "Brandon Rd / Herald Way => Herald Way / Progress Way",
      "length": 0.0015249998360609253,
      "speed": {
        "0:00": 30
      },
      "startid": 370817408,
      "endid": 370818436
    },
    {
      "id": 1685,
      "name": "Herald Way / Progress Way => Herald Way / Progress Way",
      "length": 0.0009753662286537478,
      "speed": {
        "0:00": 30
      },
      "startid": 370818436,
      "endid": 370818434
    },
    {
      "id": 1686,
      "name": "Herald Way / Progress Way => Herald Way / Hotchkiss Way",
      "length": 0.003621560526903622,
      "speed": {
        "0:00": 30
      },
      "startid": 370818434,
      "endid": 370818492
    },
    {
      "id": 1687,
      "name": "Herald Way / Hotchkiss Way => Herald Way / Hotchkiss Way",
      "length": 0.0009024655672094851,
      "speed": {
        "0:00": 30
      },
      "startid": 370818492,
      "endid": 370818491
    },
    {
      "id": 1688,
      "name": "Herald Way / Hotchkiss Way => Willenhall Lane / Craigends Avenue",
      "length": 0.009717860991491804,
      "speed": {
        "0:00": 30
      },
      "startid": 370818491,
      "endid": 370818485
    },
    {
      "id": 1689,
      "name": "Willenhall Lane / Craigends Avenue => Willenhall Lane / Craigends Avenue",
      "length": 0.0001938537593170669,
      "speed": {
        "0:00": 30
      },
      "startid": 370818485,
      "endid": 370818483
    },
    {
      "id": 1690,
      "name": "Willenhall Lane / Craigends Avenue => St James Lane / Middle Ride",
      "length": 0.003727561472329797,
      "speed": {
        "0:00": 30
      },
      "startid": 370818483,
      "endid": 370819037
    },
    {
      "id": 1691,
      "name": "St James Lane / Middle Ride => St James Lane / Middle Ride",
      "length": 0.0009964726589326248,
      "speed": {
        "0:00": 30
      },
      "startid": 370819037,
      "endid": 370819033
    },
    {
      "id": 1692,
      "name": "St James Lane / Middle Ride => St James Lane / Remembrance Rd",
      "length": 0.0017672077778229558,
      "speed": {
        "0:00": 30
      },
      "startid": 370819033,
      "endid": 370819030
    },
    {
      "id": 1693,
      "name": "St James Lane / Remembrance Rd => St James Lane / Willenhall Wood School",
      "length": 0.0033931926043192875,
      "speed": {
        "0:00": 30
      },
      "startid": 370819030,
      "endid": 370819002
    },
    {
      "id": 1694,
      "name": "St James Lane / Willenhall Wood School => Remembrance Rd / Meadfoot Rd",
      "length": 0.0013200700928394727,
      "speed": {
        "0:00": 30
      },
      "startid": 370819002,
      "endid": 370819015
    },
    {
      "id": 1695,
      "name": "Remembrance Rd / Meadfoot Rd => Robin Hood Rd / Willenhall Social Club",
      "length": 0.0045265002165026874,
      "speed": {
        "0:00": 30
      },
      "startid": 370819015,
      "endid": 370819060
    },
    {
      "id": 1696,
      "name": "Robin Hood Rd / Willenhall Social Club => Remembrance Rd / Robin Hood Rd",
      "length": 0.0014578932917113077,
      "speed": {
        "0:00": 30
      },
      "startid": 370819060,
      "endid": 370819023
    },
    {
      "id": 1697,
      "name": "Remembrance Rd / Robin Hood Rd => Radford Rd / Nauls Mill House",
      "length": 0.057876319776310935,
      "speed": {
        "0:00": 30
      },
      "startid": 370819023,
      "endid": 370817828
    },
    {
      "id": 1698,
      "name": "Radford Rd / Nauls Mill House => St James Lane / Remembrance Rd",
      "length": 0.06369611897321496,
      "speed": {
        "0:00": 30
      },
      "startid": 370817828,
      "endid": 370819024
    },
    {
      "id": 1699,
      "name": "St James Lane / Remembrance Rd => UL5",
      "length": 0.06126347933124472,
      "speed": {
        "0:00": 30
      },
      "startid": 370819024,
      "endid": 370817721
    },
    {
      "id": 1700,
      "name": "UL5 => BS4",
      "length": 0.002976046861189749,
      "speed": {
        "0:00": 30
      },
      "startid": 370817721,
      "endid": 4815881232
    },
    {
      "id": 1701,
      "name": "BS4 => HS2",
      "length": 0.0013113488704368352,
      "speed": {
        "0:00": 30
      },
      "startid": 4815881232,
      "endid": 717585774
    },
    {
      "id": 1702,
      "name": "HS2 => Sky Blue Way / Walkway To Gosford St",
      "length": 0.01374081876017471,
      "speed": {
        "0:00": 30
      },
      "startid": 717585774,
      "endid": 4815874919
    },
    {
      "id": 1703,
      "name": "Sky Blue Way / Walkway To Gosford St => Far Gosford St / Bramble St",
      "length": 0.0009964229724399199,
      "speed": {
        "0:00": 30
      },
      "startid": 4815874919,
      "endid": 4815880407
    },
    {
      "id": 1704,
      "name": "Far Gosford St / Bramble St => Far Gosford St / Gosford Green",
      "length": 0.004033183017171992,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880407,
      "endid": 4815880406
    },
    {
      "id": 1705,
      "name": "Far Gosford St / Gosford Green => Sky Blue Way / Gosford Green",
      "length": 0.000299047170195088,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880406,
      "endid": 4815880374
    },
    {
      "id": 1706,
      "name": "Cromwell Lane / Westwood Heath Rd => Westwood Heath Rd / Cromwell Lane",
      "length": 0.0008921814277368043,
      "speed": {
        "0:00": 30
      },
      "startid": 370818011,
      "endid": 370818014
    },
    {
      "id": 1707,
      "name": "Westwood Heath Rd / Cromwell Lane => Westwood Heath Rd / Cromwell Lane",
      "length": 0.00022379387837956485,
      "speed": {
        "0:00": 30
      },
      "startid": 370818014,
      "endid": 370818013
    },
    {
      "id": 1708,
      "name": "Westwood Heath Rd / Cromwell Lane => Westwood Heath Rd / Bockendon Rd",
      "length": 0.007790139626477543,
      "speed": {
        "0:00": 30
      },
      "startid": 370818013,
      "endid": 370817958
    },
    {
      "id": 1709,
      "name": "Westwood Heath Rd / Bockendon Rd => Westwood Heath Rd / Bockendon Rd",
      "length": 0.0033676133032156754,
      "speed": {
        "0:00": 30
      },
      "startid": 370817958,
      "endid": 370817957
    },
    {
      "id": 1710,
      "name": "Westwood Heath Rd / Bockendon Rd => Westwood Heath Rd / Woodleigh Rd",
      "length": 0.0058215167370711755,
      "speed": {
        "0:00": 30
      },
      "startid": 370817957,
      "endid": 370817960
    },
    {
      "id": 1711,
      "name": "Westwood Heath Rd / Woodleigh Rd => Westwood Heath Rd / Broadwells Crescent",
      "length": 0.006716951541436058,
      "speed": {
        "0:00": 30
      },
      "startid": 370817960,
      "endid": 370817993
    },
    {
      "id": 1712,
      "name": "Westwood Heath Rd / Broadwells Crescent => Westwood Heath Rd / Broadwells Crescent",
      "length": 0.0004890352339050721,
      "speed": {
        "0:00": 30
      },
      "startid": 370817993,
      "endid": 370817992
    },
    {
      "id": 1713,
      "name": "Westwood Heath Rd / Broadwells Crescent => Westwood Heath Rd / Westwood Church",
      "length": 0.003214200542903373,
      "speed": {
        "0:00": 30
      },
      "startid": 370817992,
      "endid": 370817655
    },
    {
      "id": 1714,
      "name": "Westwood Heath Rd / Westwood Church => Westwood Heath Rd / Gibbet Hill Rd",
      "length": 0.002089032465041632,
      "speed": {
        "0:00": 30
      },
      "startid": 370817655,
      "endid": 370817657
    },
    {
      "id": 1715,
      "name": "Westwood Heath Rd / Gibbet Hill Rd => Kirby Corner Rd / Gibbet Hill Rd",
      "length": 0.0027864212208499784,
      "speed": {
        "0:00": 30
      },
      "startid": 370817657,
      "endid": 370819749
    },
    {
      "id": 1716,
      "name": "Kirby Corner Rd / Gibbet Hill Rd => Kirby Corner Rd / University Westwood Site",
      "length": 0.004738827116489978,
      "speed": {
        "0:00": 30
      },
      "startid": 370819749,
      "endid": 370817931
    },
    {
      "id": 1717,
      "name": "Kirby Corner Rd / University Westwood Site => Kirby Corner Rd / University Westwood Site",
      "length": 0.0008440280208634823,
      "speed": {
        "0:00": 30
      },
      "startid": 370817931,
      "endid": 370817930
    },
    {
      "id": 1718,
      "name": "Kirby Corner Rd / University Westwood Site => Kirby Corner Rd / Lynchgate Rd",
      "length": 0.005184185461573927,
      "speed": {
        "0:00": 30
      },
      "startid": 370817930,
      "endid": 370817929
    },
    {
      "id": 1719,
      "name": "Kirby Corner Rd / Lynchgate Rd => Kirby Corner Rd / Lynchgate Rd",
      "length": 0.00029797681117596606,
      "speed": {
        "0:00": 30
      },
      "startid": 370817929,
      "endid": 370817927
    },
    {
      "id": 1720,
      "name": "Kirby Corner Rd / Lynchgate Rd => Lynchgate Rd / Leeming Close",
      "length": 0.0039043109366500898,
      "speed": {
        "0:00": 30
      },
      "startid": 370817927,
      "endid": 370819152
    },
    {
      "id": 1721,
      "name": "Lynchgate Rd / Leeming Close => De Montfort Way / Cannon Park Shops",
      "length": 0.0023546683949164826,
      "speed": {
        "0:00": 30
      },
      "startid": 370819152,
      "endid": 370817920
    },
    {
      "id": 1722,
      "name": "De Montfort Way / Cannon Park Shops => Sir Henry Parkes Rd / Centenary Rd",
      "length": 0.004222512670197375,
      "speed": {
        "0:00": 30
      },
      "startid": 370817920,
      "endid": 370817913
    },
    {
      "id": 1723,
      "name": "Sir Henry Parkes Rd / Centenary Rd => Charter Ave / Sir Henry Parkes Rd",
      "length": 0.001759790942127883,
      "speed": {
        "0:00": 30
      },
      "startid": 370817913,
      "endid": 370817940
    },
    {
      "id": 1724,
      "name": "Charter Ave / Sir Henry Parkes Rd => Charter Ave / Centenary Rd",
      "length": 0.0023897088190822846,
      "speed": {
        "0:00": 30
      },
      "startid": 370817940,
      "endid": 370817918
    },
    {
      "id": 1725,
      "name": "Charter Ave / Centenary Rd => Charter Ave / Fletchamstead Highway",
      "length": 0.0031323945361338627,
      "speed": {
        "0:00": 30
      },
      "startid": 370817918,
      "endid": 466384984
    },
    {
      "id": 1726,
      "name": "Charter Ave / Fletchamstead Highway => Fletchamstead Highway / Canley Rd",
      "length": 0.0009373778853794403,
      "speed": {
        "0:00": 30
      },
      "startid": 466384984,
      "endid": 370819754
    },
    {
      "id": 1727,
      "name": "Fletchamstead Highway / Canley Rd => Fletchamstead Highway / Cannon Park Rd",
      "length": 0.008883542424618952,
      "speed": {
        "0:00": 30
      },
      "startid": 370819754,
      "endid": 370817893
    },
    {
      "id": 1728,
      "name": "Fletchamstead Highway / Cannon Park Rd => Fletchamstead Highway / Cannon Park Rd",
      "length": 0.0025635280942480913,
      "speed": {
        "0:00": 30
      },
      "startid": 370817893,
      "endid": 370817894
    },
    {
      "id": 1729,
      "name": "Fletchamstead Highway / Cannon Park Rd => Kenilworth Rd / Fletchamstead Highway",
      "length": 0.0026321823379088934,
      "speed": {
        "0:00": 30
      },
      "startid": 370817894,
      "endid": 370819143
    },
    {
      "id": 1730,
      "name": "Kenilworth Rd / Fletchamstead Highway => Kenilworth Rd / Fletchamstead Highway",
      "length": 0.0003271508062040479,
      "speed": {
        "0:00": 30
      },
      "startid": 370819143,
      "endid": 370817878
    },
    {
      "id": 1731,
      "name": "Kenilworth Rd / Fletchamstead Highway => Kenilworth Rd / Coat Of Arms Bridge Rd",
      "length": 0.0032329641259982583,
      "speed": {
        "0:00": 30
      },
      "startid": 370817878,
      "endid": 370819121
    },
    {
      "id": 1732,
      "name": "Kenilworth Rd / Coat Of Arms Bridge Rd => Kenilworth Rd / Coat Of Arms Bridge Rd",
      "length": 0.0008588363348187505,
      "speed": {
        "0:00": 30
      },
      "startid": 370819121,
      "endid": 370819120
    },
    {
      "id": 1733,
      "name": "Kenilworth Rd / Coat Of Arms Bridge Rd => Kenilworth Rd / Beechwood Avenue",
      "length": 0.0027098195105921007,
      "speed": {
        "0:00": 30
      },
      "startid": 370819120,
      "endid": 370819119
    },
    {
      "id": 1734,
      "name": "Kenilworth Rd / Beechwood Avenue => Kenilworth Rd / Beechwood Avenue",
      "length": 0.00217378832916246,
      "speed": {
        "0:00": 30
      },
      "startid": 370819119,
      "endid": 370819118
    },
    {
      "id": 1735,
      "name": "Kenilworth Rd / Beechwood Avenue => Kenilworth Rd / Earlsdon Avenue South",
      "length": 0.0019592283072683227,
      "speed": {
        "0:00": 30
      },
      "startid": 370819118,
      "endid": 370819116
    },
    {
      "id": 1736,
      "name": "Kenilworth Rd / Earlsdon Avenue South => Kenilworth Rd / Davenport Rd",
      "length": 0.007036728615628068,
      "speed": {
        "0:00": 30
      },
      "startid": 370819116,
      "endid": 370819138
    },
    {
      "id": 1737,
      "name": "Kenilworth Rd / Davenport Rd => Kenilworth Rd / Davenport Rd",
      "length": 0.000915686103422053,
      "speed": {
        "0:00": 30
      },
      "startid": 370819138,
      "endid": 370819141
    },
    {
      "id": 1738,
      "name": "Kenilworth Rd / Davenport Rd => Warwick Road / Leamington Rd",
      "length": 0.003584891552053543,
      "speed": {
        "0:00": 30
      },
      "startid": 370819141,
      "endid": 370818568
    },
    {
      "id": 1739,
      "name": "Warwick Road / Leamington Rd => Warwick Road / Leamington Rd",
      "length": 0.000625492965591671,
      "speed": {
        "0:00": 30
      },
      "startid": 370818568,
      "endid": 370818566
    },
    {
      "id": 1740,
      "name": "Warwick Road / Leamington Rd => WR5",
      "length": 0.0026801527288538595,
      "speed": {
        "0:00": 30
      },
      "startid": 370818566,
      "endid": 370817793
    },
    {
      "id": 1741,
      "name": "WR5 => Burton Green",
      "length": 0.08609227829236407,
      "speed": {
        "0:00": 30
      },
      "startid": 370817793,
      "endid": 2629273401
    },
    {
      "id": 1742,
      "name": "Burton Green => Burton green",
      "length": 0.000265942192971362,
      "speed": {
        "0:00": 30
      },
      "startid": 2629273401,
      "endid": 2629273407
    },
    {
      "id": 1743,
      "name": "Westwood Heath Rd / Woodleigh Rd => Kenilworth Rd / Earlsdon Avenue South",
      "length": 0.05979805309949543,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880390,
      "endid": 4815880396
    },
    {
      "id": 1744,
      "name": "Kenilworth Rd / Earlsdon Avenue South => WR6",
      "length": 0.010441155587386949,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880396,
      "endid": 370817791
    },
    {
      "id": 1745,
      "name": "WR6 => WR3",
      "length": 0.001157136020523468,
      "speed": {
        "0:00": 30
      },
      "startid": 370817791,
      "endid": 9416517351
    },
    {
      "id": 1746,
      "name": "WR3 => WR1",
      "length": 0.0005164773179946906,
      "speed": {
        "0:00": 30
      },
      "startid": 9416517351,
      "endid": 9590566165
    },
    {
      "id": 1747,
      "name": "Westwood Way / Longwood Close => Westwood Way / Business Park",
      "length": 0.004310372837702662,
      "speed": {
        "0:00": 30
      },
      "startid": 370817955,
      "endid": 370817953
    },
    {
      "id": 1748,
      "name": "Westwood Way / Business Park => Westwood Way / Business Park",
      "length": 0.00020864326013591357,
      "speed": {
        "0:00": 30
      },
      "startid": 370817953,
      "endid": 370817954
    },
    {
      "id": 1749,
      "name": "Westwood Way / Business Park => Mitchell Avenue / Westwood School",
      "length": 0.004842118971069943,
      "speed": {
        "0:00": 30
      },
      "startid": 370817954,
      "endid": 370819688
    },
    {
      "id": 1750,
      "name": "Mitchell Avenue / Westwood School => Charter Ave / Mitchell Ave",
      "length": 0.002820803892511915,
      "speed": {
        "0:00": 30
      },
      "startid": 370819688,
      "endid": 370817985
    },
    {
      "id": 1751,
      "name": "Charter Ave / Mitchell Ave => Charter Ave / Mitchell Ave",
      "length": 0.0001658795044617579,
      "speed": {
        "0:00": 30
      },
      "startid": 370817985,
      "endid": 370817984
    },
    {
      "id": 1752,
      "name": "Charter Ave / Mitchell Ave => Charter Ave / John Rous Ave",
      "length": 0.0029593990014863333,
      "speed": {
        "0:00": 30
      },
      "startid": 370817984,
      "endid": 370817981
    },
    {
      "id": 1753,
      "name": "Charter Ave / John Rous Ave => John Rous Ave / Wendiburgh St",
      "length": 0.0016137827610889553,
      "speed": {
        "0:00": 30
      },
      "startid": 370817981,
      "endid": 370817980
    },
    {
      "id": 1754,
      "name": "John Rous Ave / Wendiburgh St => John Rous Ave / Wendiburgh St",
      "length": 0.00015920050251101692,
      "speed": {
        "0:00": 30
      },
      "startid": 370817980,
      "endid": 370817979
    },
    {
      "id": 1755,
      "name": "John Rous Ave / Wendiburgh St => Templars Fields / John Ross Avenue",
      "length": 0.0018530347999994171,
      "speed": {
        "0:00": 30
      },
      "startid": 370817979,
      "endid": 370819687
    },
    {
      "id": 1756,
      "name": "Templars Fields / John Ross Avenue => Prior Deram Walk / John Ross Ave",
      "length": 0.0005438519743467372,
      "speed": {
        "0:00": 30
      },
      "startid": 370819687,
      "endid": 370819682
    },
    {
      "id": 1757,
      "name": "Prior Deram Walk / John Ross Ave => Sheriff Ave / Prior Deram Walk",
      "length": 0.0032020073781933484,
      "speed": {
        "0:00": 30
      },
      "startid": 370819682,
      "endid": 370819155
    },
    {
      "id": 1758,
      "name": "Sheriff Ave / Prior Deram Walk => Sheriff Ave / Freeburn Causeway",
      "length": 0.002528595013046569,
      "speed": {
        "0:00": 30
      },
      "startid": 370819155,
      "endid": 370817978
    },
    {
      "id": 1759,
      "name": "Sheriff Ave / Freeburn Causeway => Sheriff Ave / Freeburn Causeway",
      "length": 0.00051375968117134,
      "speed": {
        "0:00": 30
      },
      "startid": 370817978,
      "endid": 370817976
    },
    {
      "id": 1760,
      "name": "Sheriff Ave / Freeburn Causeway => Charter Ave / Northfolk Terrace",
      "length": 0.0015742447490750737,
      "speed": {
        "0:00": 30
      },
      "startid": 370817976,
      "endid": 370817975
    },
    {
      "id": 1761,
      "name": "Charter Ave / Northfolk Terrace => Charter Ave / Northfolk Terrace",
      "length": 0.0001849800529801144,
      "speed": {
        "0:00": 30
      },
      "startid": 370817975,
      "endid": 370817974
    },
    {
      "id": 1762,
      "name": "Charter Ave / Northfolk Terrace => Charter Ave / Freeburn Causeway",
      "length": 0.004352989467022337,
      "speed": {
        "0:00": 30
      },
      "startid": 370817974,
      "endid": 370817971
    },
    {
      "id": 1763,
      "name": "Charter Ave / Freeburn Causeway => Charter Ave / Freeburn Causeway",
      "length": 0.0006577919503932914,
      "speed": {
        "0:00": 30
      },
      "startid": 370817971,
      "endid": 370817969
    },
    {
      "id": 1764,
      "name": "Charter Ave / Freeburn Causeway => De Montfort Way / Cannon Park Shops",
      "length": 0.004309186206234103,
      "speed": {
        "0:00": 30
      },
      "startid": 370817969,
      "endid": 370817920
    },
    {
      "id": 1765,
      "name": "De Montfort Way / Cannon Park Shops => Charter Ave / Sir Henry Parkes Rd",
      "length": 0.0026598986089687643,
      "speed": {
        "0:00": 30
      },
      "startid": 370817920,
      "endid": 370817940
    },
    {
      "id": 1766,
      "name": "Charter Ave / Sir Henry Parkes Rd => Charter Ave / Sir Henry Parkes Rd",
      "length": 0.00014656060180219657,
      "speed": {
        "0:00": 30
      },
      "startid": 370817940,
      "endid": 370817939
    },
    {
      "id": 1767,
      "name": "Charter Ave / Sir Henry Parkes Rd => Charter Ave / Centenary Rd",
      "length": 0.0023801326958805555,
      "speed": {
        "0:00": 30
      },
      "startid": 370817939,
      "endid": 370817918
    },
    {
      "id": 1768,
      "name": "Charter Ave / Centenary Rd => Charter Ave / Fletchamstead Highway",
      "length": 0.0018959217204300776,
      "speed": {
        "0:00": 30
      },
      "startid": 370817918,
      "endid": 370817917
    },
    {
      "id": 1769,
      "name": "Charter Ave / Fletchamstead Highway => Charter Ave / Fletchamstead Highway",
      "length": 0.0012521220707257148,
      "speed": {
        "0:00": 30
      },
      "startid": 370817917,
      "endid": 466384984
    },
    {
      "id": 1770,
      "name": "Charter Ave / Fletchamstead Highway => Cannon Hill Rd / Ivy Farm Lane",
      "length": 0.002669639393253391,
      "speed": {
        "0:00": 30
      },
      "startid": 466384984,
      "endid": 4815876531
    },
    {
      "id": 1771,
      "name": "Cannon Hill Rd / Ivy Farm Lane => Cannon Hill Rd / Ivy Farm Lane",
      "length": 0.0003250246144500372,
      "speed": {
        "0:00": 30
      },
      "startid": 4815876531,
      "endid": 4815876532
    },
    {
      "id": 1772,
      "name": "Cannon Hill Rd / Ivy Farm Lane => 0064002",
      "length": 0.0030402612470033954,
      "speed": {
        "0:00": 30
      },
      "startid": 4815876532,
      "endid": 2191193941
    },
    {
      "id": 1773,
      "name": "0064002 => 0064001",
      "length": 0.000127705638087157,
      "speed": {
        "0:00": 30
      },
      "startid": 2191193941,
      "endid": 2191193944
    },
    {
      "id": 1774,
      "name": "0064001 => Cannon Hill Rd /",
      "length": 0.0040710437826202844,
      "speed": {
        "0:00": 30
      },
      "startid": 2191193944,
      "endid": 370817935
    },
    {
      "id": 1775,
      "name": "Cannon Hill Rd / => Cannon Hill Rd",
      "length": 0.0001807249844345754,
      "speed": {
        "0:00": 30
      },
      "startid": 370817935,
      "endid": 370817936
    },
    {
      "id": 1776,
      "name": "Cannon Hill Rd => Kenilworth Rd / Cannon Hill Rd",
      "length": 0.0044148911707994395,
      "speed": {
        "0:00": 30
      },
      "startid": 370817936,
      "endid": 370817888
    },
    {
      "id": 1777,
      "name": "Kenilworth Rd / Cannon Hill Rd => Kenilworth Rd / Cannon Hill Rd",
      "length": 0.0011689251686877041,
      "speed": {
        "0:00": 30
      },
      "startid": 370817888,
      "endid": 370817887
    },
    {
      "id": 1778,
      "name": "Kenilworth Rd / Cannon Hill Rd => Kenilworth Rd / Kenpas Highway",
      "length": 0.004044736443826238,
      "speed": {
        "0:00": 30
      },
      "startid": 370817887,
      "endid": 370819764
    },
    {
      "id": 1779,
      "name": "Kenilworth Rd / Kenpas Highway => Humphrey Burton Rd / Orchard Crescent",
      "length": 0.02486244542216202,
      "speed": {
        "0:00": 30
      },
      "startid": 370819764,
      "endid": 1644854780
    },
    {
      "id": 1780,
      "name": "Humphrey Burton Rd / Orchard Crescent => Humphrey Burton Rd / Orchard Crescent",
      "length": 0.0002696725607111533,
      "speed": {
        "0:00": 30
      },
      "startid": 1644854780,
      "endid": 1644854778
    },
    {
      "id": 1781,
      "name": "Humphrey Burton Rd / Orchard Crescent => Stoney Rd / Asthill Grove",
      "length": 0.0019640005346207644,
      "speed": {
        "0:00": 30
      },
      "startid": 1644854778,
      "endid": 370819563
    },
    {
      "id": 1782,
      "name": "Stoney Rd / Asthill Grove => Stoney Rd / Asthill Grove",
      "length": 0.00020315622067749748,
      "speed": {
        "0:00": 30
      },
      "startid": 370819099,
      "endid": 370819097
    },
    {
      "id": 1783,
      "name": "Stoney Rd / Asthill Grove => WR6",
      "length": 0.00381131712928752,
      "speed": {
        "0:00": 30
      },
      "startid": 370819097,
      "endid": 370817791
    },
    {
      "id": 1784,
      "name": "WR6 => GR2",
      "length": 0.004362892739913887,
      "speed": {
        "0:00": 30
      },
      "startid": 370817791,
      "endid": 370817796
    },
    {
      "id": 1785,
      "name": "GR2 => GR1",
      "length": 0.0004030403081579718,
      "speed": {
        "0:00": 30
      },
      "startid": 370817796,
      "endid": 370817794
    },
    {
      "id": 1786,
      "name": "GR1 => VR2",
      "length": 0.0019344399525493415,
      "speed": {
        "0:00": 30
      },
      "startid": 370817794,
      "endid": 370817717
    },
    {
      "id": 1787,
      "name": "VR2 => VR3",
      "length": 0.0003425542292805766,
      "speed": {
        "0:00": 30
      },
      "startid": 370817717,
      "endid": 370817718
    },
    {
      "id": 1788,
      "name": "VR3 => CS4",
      "length": 0.002391225267514317,
      "speed": {
        "0:00": 30
      },
      "startid": 370817718,
      "endid": 370817702
    },
    {
      "id": 1789,
      "name": "CS4 => CS1",
      "length": 0.00019329627518438407,
      "speed": {
        "0:00": 30
      },
      "startid": 370817702,
      "endid": 370817698
    },
    {
      "id": 1790,
      "name": "CS1 => BS3",
      "length": 0.0029627712466539736,
      "speed": {
        "0:00": 30
      },
      "startid": 370817698,
      "endid": 370817695
    },
    {
      "id": 1791,
      "name": "BS3 => TS5",
      "length": 0.0019269792162839897,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 1769864769
    },
    {
      "id": 1792,
      "name": "TS5 => U",
      "length": 0.004180132965588677,
      "speed": {
        "0:00": 30
      },
      "startid": 1769864769,
      "endid": 370817754
    },
    {
      "id": 1793,
      "name": "U => Lynchgate Rd / Leeming Close",
      "length": 0.054911188877497005,
      "speed": {
        "0:00": 30
      },
      "startid": 370817754,
      "endid": 370819152
    },
    {
      "id": 1794,
      "name": "Lynchgate Rd / Leeming Close => BY5",
      "length": 0.04773184582749833,
      "speed": {
        "0:00": 30
      },
      "startid": 370819152,
      "endid": 370817679
    },
    {
      "id": 1795,
      "name": "BY5 => Kenilworth Rd / Fletchamstead Highway",
      "length": 0.028833742687517806,
      "speed": {
        "0:00": 30
      },
      "startid": 370817679,
      "endid": 370819143
    },
    {
      "id": 1796,
      "name": "Kenilworth Rd / Fletchamstead Highway => Kenilworth Rd / Fletchamstead Highway",
      "length": 0.0003271508062040479,
      "speed": {
        "0:00": 30
      },
      "startid": 370819143,
      "endid": 370817878
    },
    {
      "id": 1797,
      "name": "Kenilworth Rd / Fletchamstead Highway => Kenilworth Rd / Coat Of Arms Bridge Rd",
      "length": 0.0032329641259982583,
      "speed": {
        "0:00": 30
      },
      "startid": 370817878,
      "endid": 370819121
    },
    {
      "id": 1798,
      "name": "Kenilworth Rd / Coat Of Arms Bridge Rd => Kenilworth Rd / Coat Of Arms Bridge Rd",
      "length": 0.0008588363348187505,
      "speed": {
        "0:00": 30
      },
      "startid": 370819121,
      "endid": 370819120
    },
    {
      "id": 1799,
      "name": "Kenilworth Rd / Coat Of Arms Bridge Rd => Kenilworth Rd / Beechwood Avenue",
      "length": 0.0027098195105921007,
      "speed": {
        "0:00": 30
      },
      "startid": 370819120,
      "endid": 370819119
    },
    {
      "id": 1800,
      "name": "Kenilworth Rd / Beechwood Avenue => Kenilworth Rd / Beechwood Avenue",
      "length": 0.00217378832916246,
      "speed": {
        "0:00": 30
      },
      "startid": 370819119,
      "endid": 370819118
    },
    {
      "id": 1801,
      "name": "Kenilworth Rd / Beechwood Avenue => Kenilworth Rd / Earlsdon Avenue South",
      "length": 0.0019592283072683227,
      "speed": {
        "0:00": 30
      },
      "startid": 370819118,
      "endid": 370819116
    },
    {
      "id": 1802,
      "name": "Kenilworth Rd / Earlsdon Avenue South => Kenilworth Rd / Earlsdon Avenue South",
      "length": 0.0018423184116759448,
      "speed": {
        "0:00": 30
      },
      "startid": 370819116,
      "endid": 4815880396
    },
    {
      "id": 1803,
      "name": "Kenilworth Rd / Earlsdon Avenue South => Kenilworth Rd / Davenport Rd",
      "length": 0.004295533391791843,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880396,
      "endid": 370819141
    },
    {
      "id": 1804,
      "name": "Kenilworth Rd / Davenport Rd => Kenilworth Rd / Davenport Rd",
      "length": 0.000915686103422053,
      "speed": {
        "0:00": 30
      },
      "startid": 370819141,
      "endid": 370819138
    },
    {
      "id": 1805,
      "name": "BS4 => BS3",
      "length": 0.0008773073862663951,
      "speed": {
        "0:00": 30
      },
      "startid": 4815881232,
      "endid": 370817695
    },
    {
      "id": 1806,
      "name": "BS3 => UL4",
      "length": 0.002031303665137189,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 370817719
    },
    {
      "id": 1807,
      "name": "UL4 => UL1",
      "length": 0.00014613541665205523,
      "speed": {
        "0:00": 30
      },
      "startid": 370817719,
      "endid": 370817726
    },
    {
      "id": 1808,
      "name": "UL1 => Radford Rd / Nauls Mill House",
      "length": 0.003124653588799152,
      "speed": {
        "0:00": 30
      },
      "startid": 370817726,
      "endid": 370817829
    },
    {
      "id": 1809,
      "name": "Radford Rd / Nauls Mill House => Radford Rd / Nauls Mill House",
      "length": 0.0009099833240236075,
      "speed": {
        "0:00": 30
      },
      "startid": 370817829,
      "endid": 370817830
    },
    {
      "id": 1810,
      "name": "Radford Rd / Nauls Mill House => Radford Rd / Barrs Hill School",
      "length": 0.001961498126434522,
      "speed": {
        "0:00": 30
      },
      "startid": 370817830,
      "endid": 370817843
    },
    {
      "id": 1811,
      "name": "Radford Rd / Barrs Hill School => Radford Rd / Barrs Hill School",
      "length": 0.0011085040099148697,
      "speed": {
        "0:00": 30
      },
      "startid": 370817843,
      "endid": 370817845
    },
    {
      "id": 1812,
      "name": "Radford Rd / Barrs Hill School => Radford Rd / Swillington Rd",
      "length": 0.0018011453383920317,
      "speed": {
        "0:00": 30
      },
      "startid": 370817845,
      "endid": 370817848
    },
    {
      "id": 1813,
      "name": "Radford Rd / Swillington Rd => Radford Rd / Swillington Rd",
      "length": 0.0011675124538931274,
      "speed": {
        "0:00": 30
      },
      "startid": 370817848,
      "endid": 370817846
    },
    {
      "id": 1814,
      "name": "Radford Rd / Swillington Rd => Radford Rd / Lydgate Rd",
      "length": 0.0012705981111280852,
      "speed": {
        "0:00": 30
      },
      "startid": 370817846,
      "endid": 370817853
    },
    {
      "id": 1815,
      "name": "Radford Rd / Lydgate Rd => Radford Rd / Lydgate Rd",
      "length": 0.0014952267420042906,
      "speed": {
        "0:00": 30
      },
      "startid": 370817853,
      "endid": 370817851
    },
    {
      "id": 1816,
      "name": "Radford Rd / Lydgate Rd => Radford Rd / Bingo Hall",
      "length": 0.002516461579281676,
      "speed": {
        "0:00": 30
      },
      "startid": 370817851,
      "endid": 370817855
    },
    {
      "id": 1817,
      "name": "Radford Rd / Bingo Hall => Radford Rd / Bingo Hall",
      "length": 0.0008505658645873711,
      "speed": {
        "0:00": 30
      },
      "startid": 370817855,
      "endid": 370817857
    },
    {
      "id": 1818,
      "name": "Radford Rd / Bingo Hall => Radford Rd / Villa Rd",
      "length": 0.002451498490721967,
      "speed": {
        "0:00": 30
      },
      "startid": 370817857,
      "endid": 370817858
    },
    {
      "id": 1819,
      "name": "Radford Rd / Villa Rd => Radford Rd / Villa Rd",
      "length": 0.0014512725622701594,
      "speed": {
        "0:00": 30
      },
      "startid": 370817858,
      "endid": 370817861
    },
    {
      "id": 1820,
      "name": "Radford Rd / Villa Rd => Radford Rd / Three Spires Avenue",
      "length": 0.0021091604514600214,
      "speed": {
        "0:00": 30
      },
      "startid": 370817861,
      "endid": 370817863
    },
    {
      "id": 1821,
      "name": "Radford Rd / Three Spires Avenue => Radford Rd / Three Spires Avenue",
      "length": 0.0005809130485708061,
      "speed": {
        "0:00": 30
      },
      "startid": 370817863,
      "endid": 370817864
    },
    {
      "id": 1822,
      "name": "Radford Rd / Three Spires Avenue => Keresley Rd / The Scotchill",
      "length": 0.01108900741184371,
      "speed": {
        "0:00": 30
      },
      "startid": 370817864,
      "endid": 370817874
    },
    {
      "id": 1823,
      "name": "Keresley Rd / The Scotchill => Keresley Rd / The Scotchill",
      "length": 0.000337464694446873,
      "speed": {
        "0:00": 30
      },
      "startid": 370817874,
      "endid": 370817875
    },
    {
      "id": 1824,
      "name": "Keresley Rd / The Scotchill => Keresley Rd / Kipling Rd",
      "length": 0.001994693003949959,
      "speed": {
        "0:00": 30
      },
      "startid": 370817875,
      "endid": 370817871
    },
    {
      "id": 1825,
      "name": "Keresley Rd / Kipling Rd => Keresley Rd / Kipling Rd",
      "length": 0.0005681128937131419,
      "speed": {
        "0:00": 30
      },
      "startid": 370817871,
      "endid": 370817873
    },
    {
      "id": 1826,
      "name": "Keresley Rd / Kipling Rd => Keresley Rd / Wallace Rd",
      "length": 0.002387496071201065,
      "speed": {
        "0:00": 30
      },
      "startid": 370817873,
      "endid": 370817870
    },
    {
      "id": 1827,
      "name": "Keresley Rd / Wallace Rd => Keresley Rd / Wallace Rd",
      "length": 0.0008891261609032135,
      "speed": {
        "0:00": 30
      },
      "startid": 370817870,
      "endid": 370817867
    },
    {
      "id": 1828,
      "name": "Keresley Rd / Wallace Rd => Keresley Rd / Brownshill Green Rd",
      "length": 0.0027215178136497527,
      "speed": {
        "0:00": 30
      },
      "startid": 370817867,
      "endid": 370817865
    },
    {
      "id": 1829,
      "name": "Keresley Rd / Brownshill Green Rd => Radford Rd / Brownshill Green Rd",
      "length": 0.001202310197076473,
      "speed": {
        "0:00": 30
      },
      "startid": 370817865,
      "endid": 370819611
    },
    {
      "id": 1830,
      "name": "Radford Rd / Brownshill Green Rd => Radford Rd / Three Spires Avenue",
      "length": 0.003356885094845821,
      "speed": {
        "0:00": 30
      },
      "startid": 370819611,
      "endid": 370817864
    },
    {
      "id": 1831,
      "name": "Radford Rd / Three Spires Avenue => Radford Rd / Three Spires Avenue",
      "length": 0.0005809130485708061,
      "speed": {
        "0:00": 30
      },
      "startid": 370817864,
      "endid": 370817863
    },
    {
      "id": 1832,
      "name": "Radford Rd / Three Spires Avenue => Keresley Green Rd / New Rd",
      "length": 0.01341845371493957,
      "speed": {
        "0:00": 30
      },
      "startid": 370817863,
      "endid": 370819610
    },
    {
      "id": 1833,
      "name": "Keresley Green Rd / New Rd => Keresley Green Rd / New Rd",
      "length": 0.0002165144336974701,
      "speed": {
        "0:00": 30
      },
      "startid": 370819610,
      "endid": 370819608
    },
    {
      "id": 1834,
      "name": "Keresley Green Rd / New Rd => Bennetts Road South / Greens Rd",
      "length": 0.0015207425094370226,
      "speed": {
        "0:00": 30
      },
      "startid": 370819608,
      "endid": 370818607
    },
    {
      "id": 1835,
      "name": "Bennetts Road South / Greens Rd => Bennetts Road South / Greens Rd",
      "length": 0.0003283118791597412,
      "speed": {
        "0:00": 30
      },
      "startid": 370818607,
      "endid": 370818606
    },
    {
      "id": 1836,
      "name": "Bennetts Road South / Greens Rd => Bennetts Road South / Lowe Rd",
      "length": 0.0007762081421926491,
      "speed": {
        "0:00": 30
      },
      "startid": 370818606,
      "endid": 370818610
    },
    {
      "id": 1837,
      "name": "Bennetts Road South / Lowe Rd => Bennetts Road South / Lowe Rd",
      "length": 0.000459915437881801,
      "speed": {
        "0:00": 30
      },
      "startid": 370818610,
      "endid": 370818608
    },
    {
      "id": 1838,
      "name": "Bennetts Road South / Lowe Rd => Bennetts Road South / Cardinal Newman School",
      "length": 0.0018306842463914864,
      "speed": {
        "0:00": 30
      },
      "startid": 370818608,
      "endid": 370817690
    },
    {
      "id": 1839,
      "name": "Bennetts Road South / Cardinal Newman School => Bennetts Road South / Sandpits Lane",
      "length": 0.0009276875875024456,
      "speed": {
        "0:00": 30
      },
      "startid": 370817690,
      "endid": 370818612
    },
    {
      "id": 1840,
      "name": "Bennetts Road South / Sandpits Lane => Bennetts Road South / Sandpits Lane",
      "length": 0.000346563370826229,
      "speed": {
        "0:00": 30
      },
      "startid": 370818612,
      "endid": 370818611
    },
    {
      "id": 1841,
      "name": "Bennetts Road South / Sandpits Lane => Bennetts Road South / Penny Park Lane",
      "length": 0.00204770383112427,
      "speed": {
        "0:00": 30
      },
      "startid": 370818611,
      "endid": 370818660
    },
    {
      "id": 1842,
      "name": "Bennetts Road South / Penny Park Lane => Bennetts Road South / Penny Park Lane",
      "length": 0.00017783939383577514,
      "speed": {
        "0:00": 30
      },
      "startid": 370818660,
      "endid": 370818658
    },
    {
      "id": 1843,
      "name": "Bennetts Road South / Penny Park Lane => Bennetts Rd / Fivefield Rd",
      "length": 0.006409790452890284,
      "speed": {
        "0:00": 30
      },
      "startid": 370818658,
      "endid": 370818662
    },
    {
      "id": 1844,
      "name": "Bennetts Rd / Fivefield Rd => Bennetts Rd / Fivefield Rd",
      "length": 0.00022101918468916745,
      "speed": {
        "0:00": 30
      },
      "startid": 370818662,
      "endid": 370818661
    },
    {
      "id": 1845,
      "name": "Bennetts Rd / Fivefield Rd => Bennetts Rd / Ravenswood",
      "length": 0.0016304614377517762,
      "speed": {
        "0:00": 30
      },
      "startid": 370818661,
      "endid": 370818665
    },
    {
      "id": 1846,
      "name": "Bennetts Rd / Ravenswood => Bennetts Rd / Ravenswood",
      "length": 0.0002647720717909323,
      "speed": {
        "0:00": 30
      },
      "startid": 370818665,
      "endid": 370818664
    },
    {
      "id": 1847,
      "name": "Bennetts Rd / Ravenswood => Bennetts Rd / Prologis Park",
      "length": 0.002646894652226824,
      "speed": {
        "0:00": 30
      },
      "startid": 370818664,
      "endid": 370818668
    },
    {
      "id": 1848,
      "name": "Bennetts Rd / Prologis Park => Bennetts Rd / Prologis Park",
      "length": 0.0015228434752159565,
      "speed": {
        "0:00": 30
      },
      "startid": 370818668,
      "endid": 370818666
    },
    {
      "id": 1849,
      "name": "Bennetts Rd / Prologis Park => Bennetts Rd / Keresley Library",
      "length": 0.0021000729153995514,
      "speed": {
        "0:00": 30
      },
      "startid": 370818666,
      "endid": 370818671
    },
    {
      "id": 1850,
      "name": "Bennetts Rd / Keresley Library => Bennetts Road",
      "length": 0.0008205820982745672,
      "speed": {
        "0:00": 30
      },
      "startid": 370818671,
      "endid": 487171627
    },
    {
      "id": 1851,
      "name": "Bennetts Road => Beaumont Road",
      "length": 0.003369311925305467,
      "speed": {
        "0:00": 30
      },
      "startid": 487171627,
      "endid": 487166826
    },
    {
      "id": 1852,
      "name": "Beaumont Road => Beaumont Road",
      "length": 0.00024082068017539725,
      "speed": {
        "0:00": 30
      },
      "startid": 487166826,
      "endid": 487166830
    },
    {
      "id": 1853,
      "name": "Beaumont Road => Schofield Road",
      "length": 0.0013433154990572177,
      "speed": {
        "0:00": 30
      },
      "startid": 487166830,
      "endid": 487166839
    },
    {
      "id": 1854,
      "name": "Schofield Road => Schofield Road",
      "length": 0.00010906534738360784,
      "speed": {
        "0:00": 30
      },
      "startid": 487166839,
      "endid": 487166834
    },
    {
      "id": 1855,
      "name": "Schofield Road => 2516887795",
      "length": 0.0010876569358029158,
      "speed": {
        "0:00": 30
      },
      "startid": 487166834,
      "endid": 2516887795
    },
    {
      "id": 1856,
      "name": "2516887795 => Bennetts Rd / Keresley Library",
      "length": 0.005224493936258803,
      "speed": {
        "0:00": 30
      },
      "startid": 2516887795,
      "endid": 370818669
    },
    {
      "id": 1857,
      "name": "WR5 => F",
      "length": 0.013810263205676817,
      "speed": {
        "0:00": 30
      },
      "startid": 370817793,
      "endid": 370817739
    },
    {
      "id": 1858,
      "name": "F => CU5",
      "length": 0.003359955679766005,
      "speed": {
        "0:00": 30
      },
      "startid": 370817739,
      "endid": 370819676
    },
    {
      "id": 1859,
      "name": "CU5 => LP1",
      "length": 0.005092234759908326,
      "speed": {
        "0:00": 30
      },
      "startid": 370819676,
      "endid": 370817776
    },
    {
      "id": 1860,
      "name": "LP1 => ES1",
      "length": 0.0016872650799448009,
      "speed": {
        "0:00": 30
      },
      "startid": 370817776,
      "endid": 370817774
    },
    {
      "id": 1861,
      "name": "ES1 => FX1",
      "length": 0.0035009507123061035,
      "speed": {
        "0:00": 30
      },
      "startid": 370817774,
      "endid": 370817768
    },
    {
      "id": 1862,
      "name": "FX1 => BY2",
      "length": 0.007923984625172154,
      "speed": {
        "0:00": 30
      },
      "startid": 370817768,
      "endid": 370817685
    },
    {
      "id": 1863,
      "name": "BY2 => BY4",
      "length": 0.0003973939229535059,
      "speed": {
        "0:00": 30
      },
      "startid": 370817685,
      "endid": 370817678
    },
    {
      "id": 1864,
      "name": "BY4 => SJ1",
      "length": 0.0034968857830933123,
      "speed": {
        "0:00": 30
      },
      "startid": 370817678,
      "endid": 4815869810
    },
    {
      "id": 1865,
      "name": "SJ1 => MP1",
      "length": 0.0026203276512693527,
      "speed": {
        "0:00": 30
      },
      "startid": 4815869810,
      "endid": 4815869811
    },
    {
      "id": 1866,
      "name": "MP1 => Warwick Road / Leamington Rd",
      "length": 0.01371282817692872,
      "speed": {
        "0:00": 30
      },
      "startid": 4815869811,
      "endid": 370818566
    },
    {
      "id": 1867,
      "name": "Warwick Road / Leamington Rd => Warwick Road / Leamington Rd",
      "length": 0.000625492965591671,
      "speed": {
        "0:00": 30
      },
      "startid": 370818566,
      "endid": 370818568
    },
    {
      "id": 1868,
      "name": "Warwick Road / Leamington Rd => Leamington Rd / War Memorial Park",
      "length": 0.0030726059054120613,
      "speed": {
        "0:00": 30
      },
      "startid": 370818568,
      "endid": 370818569
    },
    {
      "id": 1869,
      "name": "Leamington Rd / War Memorial Park => Leamington Rd / War Memorial Park",
      "length": 0.00032981820750473,
      "speed": {
        "0:00": 30
      },
      "startid": 370818569,
      "endid": 370818570
    },
    {
      "id": 1870,
      "name": "Leamington Rd / War Memorial Park => Leamington Rd / Armorial Rd",
      "length": 0.0021197752262931174,
      "speed": {
        "0:00": 30
      },
      "startid": 370818570,
      "endid": 370818562
    },
    {
      "id": 1871,
      "name": "Leamington Rd / Armorial Rd => Leamington Rd / Armorial Rd",
      "length": 0.0003211603026512689,
      "speed": {
        "0:00": 30
      },
      "startid": 370818562,
      "endid": 370818559
    },
    {
      "id": 1872,
      "name": "Leamington Rd / Armorial Rd => Leamington Rd / Stivichall Croft",
      "length": 0.0027066189240428696,
      "speed": {
        "0:00": 30
      },
      "startid": 370818559,
      "endid": 370818574
    },
    {
      "id": 1873,
      "name": "Leamington Rd / Stivichall Croft => Leamington Rd / Stivichall Croft",
      "length": 0.00039644168549778086,
      "speed": {
        "0:00": 30
      },
      "startid": 370818574,
      "endid": 370818572
    },
    {
      "id": 1874,
      "name": "Leamington Rd / Stivichall Croft => Leamington Rd / Baginton Rd",
      "length": 0.0034378628710281943,
      "speed": {
        "0:00": 30
      },
      "startid": 370818572,
      "endid": 370818577
    },
    {
      "id": 1875,
      "name": "Leamington Rd / Baginton Rd => Leamington Rd / Baginton Rd",
      "length": 0.001640813886464955,
      "speed": {
        "0:00": 30
      },
      "startid": 370818577,
      "endid": 370818575
    },
    {
      "id": 1876,
      "name": "Leamington Rd / Baginton Rd => Leamington Rd / Dewsbury Avenue",
      "length": 0.0008850576478397776,
      "speed": {
        "0:00": 30
      },
      "startid": 370818575,
      "endid": 370818578
    },
    {
      "id": 1877,
      "name": "Leamington Rd / Dewsbury Avenue => Leamington Rd / Dewsbury Avenue",
      "length": 0.00026672916975609856,
      "speed": {
        "0:00": 30
      },
      "startid": 370818578,
      "endid": 370818579
    },
    {
      "id": 1878,
      "name": "Leamington Rd / Dewsbury Avenue => Leamington Rd / Stonebridge Highway",
      "length": 0.002528549546679714,
      "speed": {
        "0:00": 30
      },
      "startid": 370818579,
      "endid": 370818935
    },
    {
      "id": 1879,
      "name": "Leamington Rd / Stonebridge Highway => Leamington Rd / Stonebridge Highway",
      "length": 0.00028445586652267,
      "speed": {
        "0:00": 30
      },
      "startid": 370818935,
      "endid": 370818933
    },
    {
      "id": 1880,
      "name": "Leamington Rd / Stonebridge Highway => Mill Hill / Howes Lane",
      "length": 0.011292958877548711,
      "speed": {
        "0:00": 30
      },
      "startid": 370818933,
      "endid": 370819804
    },
    {
      "id": 1881,
      "name": "Mill Hill / Howes Lane => Mill Hill / Howes Lane",
      "length": 0.0002920659172212636,
      "speed": {
        "0:00": 30
      },
      "startid": 370819804,
      "endid": 370819803
    },
    {
      "id": 1882,
      "name": "Mill Hill / Howes Lane => Old Mill Inn",
      "length": 0.0036200541335719345,
      "speed": {
        "0:00": 30
      },
      "startid": 370819803,
      "endid": 487166972
    },
    {
      "id": 1883,
      "name": "Old Mill Inn => Old Mill Inn",
      "length": 0.00025494903412259746,
      "speed": {
        "0:00": 30
      },
      "startid": 487166972,
      "endid": 487166975
    },
    {
      "id": 1884,
      "name": "Old Mill Inn => Holly Walk",
      "length": 0.006659676428325368,
      "speed": {
        "0:00": 30
      },
      "startid": 487166975,
      "endid": 487166961
    },
    {
      "id": 1885,
      "name": "Holly Walk => Holly Walk",
      "length": 0.00042105334579031165,
      "speed": {
        "0:00": 30
      },
      "startid": 487166961,
      "endid": 487166966
    },
    {
      "id": 1886,
      "name": "Holly Walk => Baginton, Kimberley Road.",
      "length": 0.004303560502652983,
      "speed": {
        "0:00": 30
      },
      "startid": 487166966,
      "endid": 944102324
    },
    {
      "id": 1887,
      "name": "Baginton, Kimberley Road. => Post Office",
      "length": 0.00042695110961433146,
      "speed": {
        "0:00": 30
      },
      "startid": 944102324,
      "endid": 487160157
    },
    {
      "id": 1888,
      "name": "Post Office => Church Road",
      "length": 0.002703608481269057,
      "speed": {
        "0:00": 30
      },
      "startid": 487160157,
      "endid": 487160158
    },
    {
      "id": 1889,
      "name": "Church Road => Church Road",
      "length": 0.0002520307322529971,
      "speed": {
        "0:00": 30
      },
      "startid": 487160158,
      "endid": 487160160
    },
    {
      "id": 1890,
      "name": "Church Road => St Martins Rd / Erithway Rd",
      "length": 0.026500485837243477,
      "speed": {
        "0:00": 30
      },
      "startid": 487160160,
      "endid": 370818937
    },
    {
      "id": 1891,
      "name": "St Martins Rd / Erithway Rd => St Martins Rd / Erithway Rd",
      "length": 0.0004672167912177775,
      "speed": {
        "0:00": 30
      },
      "startid": 370818937,
      "endid": 370818938
    },
    {
      "id": 1892,
      "name": "St Martins Rd / Erithway Rd => Hadleigh Rd / St Martins Rd",
      "length": 0.0020704263377444815,
      "speed": {
        "0:00": 30
      },
      "startid": 370818938,
      "endid": 370818942
    },
    {
      "id": 1893,
      "name": "Hadleigh Rd / St Martins Rd => Hadleigh Rd / St Martins Rd",
      "length": 0.00010549090007743969,
      "speed": {
        "0:00": 30
      },
      "startid": 370818942,
      "endid": 370818940
    },
    {
      "id": 1894,
      "name": "Hadleigh Rd / St Martins Rd => Brentwood Avenue / Alfriston Rd",
      "length": 0.004375926347642987,
      "speed": {
        "0:00": 30
      },
      "startid": 370818940,
      "endid": 370818943
    },
    {
      "id": 1895,
      "name": "Brentwood Avenue / Alfriston Rd => Brentwood Avenue / Alfriston Rd",
      "length": 0.00031848089424333243,
      "speed": {
        "0:00": 30
      },
      "startid": 370818943,
      "endid": 370818944
    },
    {
      "id": 1896,
      "name": "Brentwood Avenue / Alfriston Rd => CU3",
      "length": 0.03300505219174778,
      "speed": {
        "0:00": 30
      },
      "startid": 370818944,
      "endid": 370817767
    },
    {
      "id": 1897,
      "name": "CU3 => WR6",
      "length": 0.013451624734579016,
      "speed": {
        "0:00": 30
      },
      "startid": 370817767,
      "endid": 370817791
    },
    {
      "id": 1898,
      "name": "E => UH8",
      "length": 0.06829286783449612,
      "speed": {
        "0:00": 30
      },
      "startid": 370817737,
      "endid": 4062225928
    },
    {
      "id": 1899,
      "name": "UH8 => UH9",
      "length": 0.0002945095753964451,
      "speed": {
        "0:00": 30
      },
      "startid": 4062225928,
      "endid": 4062225927
    },
    {
      "id": 1900,
      "name": "UH9 => CU5",
      "length": 0.06600520442154507,
      "speed": {
        "0:00": 30
      },
      "startid": 4062225927,
      "endid": 370819676
    },
    {
      "id": 1901,
      "name": "CU5 => CU3",
      "length": 0.000888082090805107,
      "speed": {
        "0:00": 30
      },
      "startid": 370819676,
      "endid": 370817767
    },
    {
      "id": 1902,
      "name": "CU3 => CU2",
      "length": 0.001764996433423732,
      "speed": {
        "0:00": 30
      },
      "startid": 370817767,
      "endid": 370819680
    },
    {
      "id": 1903,
      "name": "CU2 => CU1",
      "length": 0.00010206831045847219,
      "speed": {
        "0:00": 30
      },
      "startid": 370819680,
      "endid": 370817766
    },
    {
      "id": 1904,
      "name": "Sky Blue Way / Gosford Green => Sky Blue Way / Gosford Green",
      "length": 0.0003139044440539605,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880374,
      "endid": 4815880373
    },
    {
      "id": 1905,
      "name": "Sky Blue Way / Gosford Green => Sky Blue Way / Walkway To Gosford St",
      "length": 0.0029580316495925675,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880373,
      "endid": 4815874919
    },
    {
      "id": 1906,
      "name": "Sky Blue Way / Walkway To Gosford St => Walsgrave Rd / Swan Lane",
      "length": 0.008529217335722039,
      "speed": {
        "0:00": 30
      },
      "startid": 4815874919,
      "endid": 370817463
    },
    {
      "id": 1907,
      "name": "Walsgrave Rd / Swan Lane => Walsgrave Rd / Swan Lane",
      "length": 0.0017645372707868672,
      "speed": {
        "0:00": 30
      },
      "startid": 370817463,
      "endid": 370817464
    },
    {
      "id": 1908,
      "name": "Walsgrave Rd / Swan Lane => Walsgrave Rd / Clements St",
      "length": 0.0048603790181425,
      "speed": {
        "0:00": 30
      },
      "startid": 370817464,
      "endid": 370817467
    },
    {
      "id": 1909,
      "name": "Walsgrave Rd / Clements St => Walsgrave Rd / Clements St",
      "length": 0.0005896212004330483,
      "speed": {
        "0:00": 30
      },
      "startid": 370817467,
      "endid": 370817465
    },
    {
      "id": 1910,
      "name": "Walsgrave Rd / Clements St => Walsgrave Rd / Harefield Rd",
      "length": 0.00521431387624442,
      "speed": {
        "0:00": 30
      },
      "startid": 370817465,
      "endid": 370817501
    },
    {
      "id": 1911,
      "name": "Walsgrave Rd / Harefield Rd => Walsgrave Rd / Harefield Rd",
      "length": 0.0006063554485614267,
      "speed": {
        "0:00": 30
      },
      "startid": 370817501,
      "endid": 370817500
    },
    {
      "id": 1912,
      "name": "Walsgrave Rd / Harefield Rd => Walsgrave Rd / Burns Rd",
      "length": 0.0036222750930872813,
      "speed": {
        "0:00": 30
      },
      "startid": 370817500,
      "endid": 370817504
    },
    {
      "id": 1913,
      "name": "Walsgrave Rd / Burns Rd => Walsgrave Rd / Burns Rd",
      "length": 0.0015216241651606255,
      "speed": {
        "0:00": 30
      },
      "startid": 370817504,
      "endid": 370817502
    },
    {
      "id": 1914,
      "name": "Walsgrave Rd / Burns Rd => Ansty Rd / Dane Rd",
      "length": 0.003590546539177356,
      "speed": {
        "0:00": 30
      },
      "startid": 370817502,
      "endid": 370817521
    },
    {
      "id": 1915,
      "name": "Ansty Rd / Dane Rd => Ansty Rd / Dane Rd",
      "length": 0.0005844890075955145,
      "speed": {
        "0:00": 30
      },
      "startid": 370817521,
      "endid": 370817522
    },
    {
      "id": 1916,
      "name": "Ansty Rd / Dane Rd => Ansty Rd / Mellowdew Rd",
      "length": 0.0019575913567442286,
      "speed": {
        "0:00": 30
      },
      "startid": 370817522,
      "endid": 370817524
    },
    {
      "id": 1917,
      "name": "Ansty Rd / Mellowdew Rd => Ansty Rd / Mellowdew Rd",
      "length": 0.0011267458630953426,
      "speed": {
        "0:00": 30
      },
      "startid": 370817524,
      "endid": 370817526
    },
    {
      "id": 1918,
      "name": "Ansty Rd / Mellowdew Rd => Ansty Rd / Morris Avenue",
      "length": 0.0028913000017288313,
      "speed": {
        "0:00": 30
      },
      "startid": 370817526,
      "endid": 370817620
    },
    {
      "id": 1919,
      "name": "Ansty Rd / Morris Avenue => Ansty Rd / Morris Avenue",
      "length": 0.000945145517896747,
      "speed": {
        "0:00": 30
      },
      "startid": 370817620,
      "endid": 370817621
    },
    {
      "id": 1920,
      "name": "Ansty Rd / Morris Avenue => Ansty Rd / Hipswell Highway",
      "length": 0.0031013986941376545,
      "speed": {
        "0:00": 30
      },
      "startid": 370817621,
      "endid": 370817528
    },
    {
      "id": 1921,
      "name": "Ansty Rd / Hipswell Highway => Ansty Rd / Hipswell Highway",
      "length": 0.001124690188452074,
      "speed": {
        "0:00": 30
      },
      "startid": 370817528,
      "endid": 370817527
    },
    {
      "id": 1922,
      "name": "Ansty Rd / Hipswell Highway => Ansty Rd / Arch Rd",
      "length": 0.003705011516852265,
      "speed": {
        "0:00": 30
      },
      "startid": 370817527,
      "endid": 370817531
    },
    {
      "id": 1923,
      "name": "Ansty Rd / Arch Rd => Ansty Rd / Arch Rd",
      "length": 0.001321381398385821,
      "speed": {
        "0:00": 30
      },
      "startid": 370817531,
      "endid": 370817532
    },
    {
      "id": 1924,
      "name": "Ansty Rd / Arch Rd => Ansty Rd / Norton Hill Drive",
      "length": 0.003601649673413492,
      "speed": {
        "0:00": 30
      },
      "startid": 370817532,
      "endid": 370817583
    },
    {
      "id": 1925,
      "name": "Ansty Rd / Norton Hill Drive => Ansty Rd / Norton Hill Drive",
      "length": 0.0008620050695904217,
      "speed": {
        "0:00": 30
      },
      "startid": 370817583,
      "endid": 370817581
    },
    {
      "id": 1926,
      "name": "Ansty Rd / Norton Hill Drive => Ansty Rd / Clifford Bridge Rd",
      "length": 0.003566049838405886,
      "speed": {
        "0:00": 30
      },
      "startid": 370817581,
      "endid": 370817630
    },
    {
      "id": 1927,
      "name": "Ansty Rd / Clifford Bridge Rd => Ansty Rd / Clifford Bridge Rd",
      "length": 0.0004618862630562424,
      "speed": {
        "0:00": 30
      },
      "startid": 370817630,
      "endid": 370817629
    },
    {
      "id": 1928,
      "name": "Ansty Rd / Clifford Bridge Rd => Ansty Rd / Walsgrave Church",
      "length": 0.0049350409157380955,
      "speed": {
        "0:00": 30
      },
      "startid": 370817629,
      "endid": 370817584
    },
    {
      "id": 1929,
      "name": "Ansty Rd / Walsgrave Church => Ansty Rd / Walsgrave Church",
      "length": 0.0003016658581946437,
      "speed": {
        "0:00": 30
      },
      "startid": 370817584,
      "endid": 370817587
    },
    {
      "id": 1930,
      "name": "Ansty Rd / Walsgrave Church => Hinckley Rd / Harmer Close",
      "length": 0.004558486776332544,
      "speed": {
        "0:00": 30
      },
      "startid": 370817587,
      "endid": 370817588
    },
    {
      "id": 1931,
      "name": "Hinckley Rd / Harmer Close => Hinckley Rd / Harmer Close",
      "length": 0.000851335632990817,
      "speed": {
        "0:00": 30
      },
      "startid": 370817588,
      "endid": 370817589
    },
    {
      "id": 1932,
      "name": "Hinckley Rd / Harmer Close => Hinckley Rd / Mount Pleasant",
      "length": 0.0022642991078894894,
      "speed": {
        "0:00": 30
      },
      "startid": 370817589,
      "endid": 370817592
    },
    {
      "id": 1933,
      "name": "Hinckley Rd / Mount Pleasant => Hinckley Rd / Mount Pleasant",
      "length": 0.0002528821266917535,
      "speed": {
        "0:00": 30
      },
      "startid": 370817592,
      "endid": 370817593
    },
    {
      "id": 1934,
      "name": "UL4 => BS3",
      "length": 0.002031303665137189,
      "speed": {
        "0:00": 30
      },
      "startid": 370817719,
      "endid": 370817695
    },
    {
      "id": 1935,
      "name": "BS3 => E",
      "length": 0.00541034712841983,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 370817737
    },
    {
      "id": 1936,
      "name": "E => BS5",
      "length": 0.00455258052537209,
      "speed": {
        "0:00": 30
      },
      "startid": 370817737,
      "endid": 370817666
    },
    {
      "id": 1937,
      "name": "BS5 => UL1",
      "length": 0.0031054879890275626,
      "speed": {
        "0:00": 30
      },
      "startid": 370817666,
      "endid": 370817726
    },
    {
      "id": 1938,
      "name": "London Rd / Brandon Lane => London Rd / Brandon Lane",
      "length": 0.0011037872983497982,
      "speed": {
        "0:00": 30
      },
      "startid": 370819052,
      "endid": 370819054
    },
    {
      "id": 1939,
      "name": "London Rd / Brandon Lane => Holly Walk",
      "length": 0.03311182262878326,
      "speed": {
        "0:00": 30
      },
      "startid": 370819054,
      "endid": 487166966
    },
    {
      "id": 1940,
      "name": "Holly Walk => Holly Walk",
      "length": 0.00042105334579031165,
      "speed": {
        "0:00": 30
      },
      "startid": 487166966,
      "endid": 487166961
    },
    {
      "id": 1941,
      "name": "Holly Walk => Old Mill Inn",
      "length": 0.006659676428325368,
      "speed": {
        "0:00": 30
      },
      "startid": 487166961,
      "endid": 487166975
    },
    {
      "id": 1942,
      "name": "Old Mill Inn => Old Mill Inn",
      "length": 0.00025494903412259746,
      "speed": {
        "0:00": 30
      },
      "startid": 487166975,
      "endid": 487166972
    },
    {
      "id": 1943,
      "name": "Old Mill Inn => Mill Hill / Howes Lane",
      "length": 0.0036200541335719345,
      "speed": {
        "0:00": 30
      },
      "startid": 487166972,
      "endid": 370819803
    },
    {
      "id": 1944,
      "name": "Mill Hill / Howes Lane => Mill Hill / Howes Lane",
      "length": 0.0002920659172212636,
      "speed": {
        "0:00": 30
      },
      "startid": 370819803,
      "endid": 370819804
    },
    {
      "id": 1945,
      "name": "Mill Hill / Howes Lane => Brentwood Avenue / Alfriston Rd",
      "length": 0.00540579816863295,
      "speed": {
        "0:00": 30
      },
      "startid": 370819804,
      "endid": 370818943
    },
    {
      "id": 1946,
      "name": "Brentwood Avenue / Alfriston Rd => Brentwood Avenue / Alfriston Rd",
      "length": 0.00031848089424333243,
      "speed": {
        "0:00": 30
      },
      "startid": 370818943,
      "endid": 370818944
    },
    {
      "id": 1947,
      "name": "Brentwood Avenue / Alfriston Rd => Hadleigh Rd / St Martins Rd",
      "length": 0.004172986332351912,
      "speed": {
        "0:00": 30
      },
      "startid": 370818944,
      "endid": 370818942
    },
    {
      "id": 1948,
      "name": "Hadleigh Rd / St Martins Rd => Hadleigh Rd / St Martins Rd",
      "length": 0.00010549090007743969,
      "speed": {
        "0:00": 30
      },
      "startid": 370818942,
      "endid": 370818940
    },
    {
      "id": 1949,
      "name": "Hadleigh Rd / St Martins Rd => St Martins Rd / Erithway Rd",
      "length": 0.0021740875166395787,
      "speed": {
        "0:00": 30
      },
      "startid": 370818940,
      "endid": 370818938
    },
    {
      "id": 1950,
      "name": "St Martins Rd / Erithway Rd => St Martins Rd / Erithway Rd",
      "length": 0.0004672167912177775,
      "speed": {
        "0:00": 30
      },
      "startid": 370818938,
      "endid": 370818937
    },
    {
      "id": 1951,
      "name": "St Martins Rd / Erithway Rd => Leamington Rd / Stonebridge Highway",
      "length": 0.002346814106405063,
      "speed": {
        "0:00": 30
      },
      "startid": 370818937,
      "endid": 370818933
    },
    {
      "id": 1952,
      "name": "Leamington Rd / Stonebridge Highway => Leamington Rd / Stonebridge Highway",
      "length": 0.00028445586652267,
      "speed": {
        "0:00": 30
      },
      "startid": 370818933,
      "endid": 370818935
    },
    {
      "id": 1953,
      "name": "Leamington Rd / Stonebridge Highway => Leamington Rd / Dewsbury Avenue",
      "length": 0.002528549546679714,
      "speed": {
        "0:00": 30
      },
      "startid": 370818935,
      "endid": 370818579
    },
    {
      "id": 1954,
      "name": "Leamington Rd / Dewsbury Avenue => Leamington Rd / Dewsbury Avenue",
      "length": 0.00026672916975609856,
      "speed": {
        "0:00": 30
      },
      "startid": 370818579,
      "endid": 370818578
    },
    {
      "id": 1955,
      "name": "Leamington Rd / Dewsbury Avenue => Leamington Rd / Baginton Rd",
      "length": 0.0008850576478397776,
      "speed": {
        "0:00": 30
      },
      "startid": 370818578,
      "endid": 370818575
    },
    {
      "id": 1956,
      "name": "Leamington Rd / Baginton Rd => Leamington Rd / Baginton Rd",
      "length": 0.001640813886464955,
      "speed": {
        "0:00": 30
      },
      "startid": 370818575,
      "endid": 370818577
    },
    {
      "id": 1957,
      "name": "Leamington Rd / Baginton Rd => Leamington Rd / Stivichall Croft",
      "length": 0.0031634906432593717,
      "speed": {
        "0:00": 30
      },
      "startid": 370818577,
      "endid": 370818574
    },
    {
      "id": 1958,
      "name": "Leamington Rd / Stivichall Croft => Leamington Rd / Stivichall Croft",
      "length": 0.00039644168549778086,
      "speed": {
        "0:00": 30
      },
      "startid": 370818574,
      "endid": 370818572
    },
    {
      "id": 1959,
      "name": "Leamington Rd / Stivichall Croft => Leamington Rd / Armorial Rd",
      "length": 0.0023907359808194324,
      "speed": {
        "0:00": 30
      },
      "startid": 370818572,
      "endid": 370818559
    },
    {
      "id": 1960,
      "name": "Leamington Rd / Armorial Rd => Leamington Rd / Armorial Rd",
      "length": 0.0003211603026512689,
      "speed": {
        "0:00": 30
      },
      "startid": 370818559,
      "endid": 370818562
    },
    {
      "id": 1961,
      "name": "Leamington Rd / Armorial Rd => Leamington Rd / War Memorial Park",
      "length": 0.0021197752262931174,
      "speed": {
        "0:00": 30
      },
      "startid": 370818562,
      "endid": 370818570
    },
    {
      "id": 1962,
      "name": "Leamington Rd / War Memorial Park => Leamington Rd / War Memorial Park",
      "length": 0.00032981820750473,
      "speed": {
        "0:00": 30
      },
      "startid": 370818570,
      "endid": 370818569
    },
    {
      "id": 1963,
      "name": "Leamington Rd / War Memorial Park => Warwick Road / Leamington Rd",
      "length": 0.0030726059054120613,
      "speed": {
        "0:00": 30
      },
      "startid": 370818569,
      "endid": 370818568
    },
    {
      "id": 1964,
      "name": "Warwick Road / Leamington Rd => Warwick Road / Leamington Rd",
      "length": 0.000625492965591671,
      "speed": {
        "0:00": 30
      },
      "startid": 370818568,
      "endid": 370818566
    },
    {
      "id": 1965,
      "name": "Warwick Road / Leamington Rd => WR5",
      "length": 0.0026801527288538595,
      "speed": {
        "0:00": 30
      },
      "startid": 370818566,
      "endid": 370817793
    },
    {
      "id": 1966,
      "name": "WR5 => WR6",
      "length": 0.0004939037153162216,
      "speed": {
        "0:00": 30
      },
      "startid": 370817793,
      "endid": 370817791
    },
    {
      "id": 1967,
      "name": "WR6 => BY2",
      "length": 0.006360279312262274,
      "speed": {
        "0:00": 30
      },
      "startid": 370817791,
      "endid": 370817685
    },
    {
      "id": 1968,
      "name": "BY2 => BY5",
      "length": 0.000648345224398062,
      "speed": {
        "0:00": 30
      },
      "startid": 370817685,
      "endid": 370817679
    },
    {
      "id": 1969,
      "name": "BY5 => SJ1",
      "length": 0.0037519047429273086,
      "speed": {
        "0:00": 30
      },
      "startid": 370817679,
      "endid": 4815869810
    },
    {
      "id": 1970,
      "name": "SJ1 => LP1",
      "length": 0.001256202392133201,
      "speed": {
        "0:00": 30
      },
      "startid": 4815869810,
      "endid": 370817776
    },
    {
      "id": 1971,
      "name": "LP1 => ES1",
      "length": 0.0016872650799448009,
      "speed": {
        "0:00": 30
      },
      "startid": 370817776,
      "endid": 370817774
    },
    {
      "id": 1972,
      "name": "ES1 => MP1",
      "length": 0.0010158778371435512,
      "speed": {
        "0:00": 30
      },
      "startid": 370817774,
      "endid": 4815869811
    },
    {
      "id": 1973,
      "name": "MP1 => CU3",
      "length": 0.002172796990056551,
      "speed": {
        "0:00": 30
      },
      "startid": 4815869811,
      "endid": 370817767
    },
    {
      "id": 1974,
      "name": "CU3 => CU5",
      "length": 0.000888082090805107,
      "speed": {
        "0:00": 30
      },
      "startid": 370817767,
      "endid": 370819676
    },
    {
      "id": 1975,
      "name": "CU5 => FX1",
      "length": 0.001435590516124241,
      "speed": {
        "0:00": 30
      },
      "startid": 370819676,
      "endid": 370817768
    },
    {
      "id": 1976,
      "name": "FX1 => F",
      "length": 0.0020783494845687056,
      "speed": {
        "0:00": 30
      },
      "startid": 370817768,
      "endid": 370817739
    },
    {
      "id": 1977,
      "name": "WR3 => WR1",
      "length": 0.0005164773179946906,
      "speed": {
        "0:00": 30
      },
      "startid": 9416517351,
      "endid": 9590566165
    },
    {
      "id": 1978,
      "name": "London Rd / Daventry Rd => London Rd / Daventry Rd",
      "length": 0.0011816018661076123,
      "speed": {
        "0:00": 30
      },
      "startid": 370818595,
      "endid": 370818594
    },
    {
      "id": 1979,
      "name": "London Rd / Daventry Rd => London Rd / Bar Rd",
      "length": 0.0017843402870548358,
      "speed": {
        "0:00": 30
      },
      "startid": 370818594,
      "endid": 370818593
    },
    {
      "id": 1980,
      "name": "London Rd / Bar Rd => London Rd / Bar Rd",
      "length": 0.0012993232584707116,
      "speed": {
        "0:00": 30
      },
      "startid": 370818593,
      "endid": 370818591
    },
    {
      "id": 1981,
      "name": "London Rd / Bar Rd => London Rd / Acacia Avenue",
      "length": 0.005140785677304741,
      "speed": {
        "0:00": 30
      },
      "startid": 370818591,
      "endid": 370818528
    },
    {
      "id": 1982,
      "name": "London Rd / Acacia Avenue => London Rd / Acacia Avenue",
      "length": 0.00020782649013074858,
      "speed": {
        "0:00": 30
      },
      "startid": 370818528,
      "endid": 370818530
    },
    {
      "id": 1983,
      "name": "London Rd / Acacia Avenue => London Rd / Gulson Rd",
      "length": 0.0020553022770407204,
      "speed": {
        "0:00": 30
      },
      "startid": 370818530,
      "endid": 370818527
    },
    {
      "id": 1984,
      "name": "London Rd / Gulson Rd => London Rd / Gulson Rd",
      "length": 0.00036303261561743133,
      "speed": {
        "0:00": 30
      },
      "startid": 370818527,
      "endid": 370818526
    },
    {
      "id": 1985,
      "name": "London Rd / Gulson Rd => CS3",
      "length": 0.015131671868634976,
      "speed": {
        "0:00": 30
      },
      "startid": 370818526,
      "endid": 370817701
    },
    {
      "id": 1986,
      "name": "CS3 => GR2",
      "length": 0.0037685887783093603,
      "speed": {
        "0:00": 30
      },
      "startid": 370817701,
      "endid": 370817796
    },
    {
      "id": 1987,
      "name": "GR2 => BY3",
      "length": 0.003752197794626417,
      "speed": {
        "0:00": 30
      },
      "startid": 370817796,
      "endid": 370817681
    },
    {
      "id": 1988,
      "name": "BY3 => BY4",
      "length": 0.0007744497465937541,
      "speed": {
        "0:00": 30
      },
      "startid": 370817681,
      "endid": 370817678
    },
    {
      "id": 1989,
      "name": "BY4 => GR1",
      "length": 0.00339214891329977,
      "speed": {
        "0:00": 30
      },
      "startid": 370817678,
      "endid": 370817794
    },
    {
      "id": 1990,
      "name": "GR1 => VR3",
      "length": 0.002224508586183148,
      "speed": {
        "0:00": 30
      },
      "startid": 370817794,
      "endid": 370817718
    },
    {
      "id": 1991,
      "name": "VR3 => CS4",
      "length": 0.002391225267514317,
      "speed": {
        "0:00": 30
      },
      "startid": 370817718,
      "endid": 370817702
    },
    {
      "id": 1992,
      "name": "CS4 => TS2",
      "length": 0.005355488715327541,
      "speed": {
        "0:00": 30
      },
      "startid": 370817702,
      "endid": 370817660
    },
    {
      "id": 1993,
      "name": "GH5 => GH6",
      "length": 0.003083086677340662,
      "speed": {
        "0:00": 30
      },
      "startid": 370819587,
      "endid": 370819586
    },
    {
      "id": 1994,
      "name": "GH6 => UW5",
      "length": 0.007892891592441185,
      "speed": {
        "0:00": 30
      },
      "startid": 370819586,
      "endid": 3731158219
    },
    {
      "id": 1995,
      "name": "E => UH3",
      "length": 0.06848654388454738,
      "speed": {
        "0:00": 30
      },
      "startid": 370817737,
      "endid": 370817649
    },
    {
      "id": 1996,
      "name": "UH3 => UH8",
      "length": 0.00019671697944123576,
      "speed": {
        "0:00": 30
      },
      "startid": 370817649,
      "endid": 4062225928
    },
    {
      "id": 1997,
      "name": "GR2 => VR2",
      "length": 0.0020745281728630723,
      "speed": {
        "0:00": 30
      },
      "startid": 370817796,
      "endid": 370817717
    },
    {
      "id": 1998,
      "name": "VR2 => CS3",
      "length": 0.0021289177156473215,
      "speed": {
        "0:00": 30
      },
      "startid": 370817717,
      "endid": 370817701
    },
    {
      "id": 1999,
      "name": "CS3 => Quinton Rd / Park Rd",
      "length": 0.008778979978337641,
      "speed": {
        "0:00": 30
      },
      "startid": 370817701,
      "endid": 370817761
    },
    {
      "id": 2000,
      "name": "Quinton Rd / Park Rd => Quinton Rd / Park Rd",
      "length": 0.00028927594092737423,
      "speed": {
        "0:00": 30
      },
      "startid": 370817761,
      "endid": 370817762
    },
    {
      "id": 2001,
      "name": "Quinton Rd / Park Rd => Quinton Rd / Stoney Rd",
      "length": 0.0013972925427406058,
      "speed": {
        "0:00": 30
      },
      "startid": 370817762,
      "endid": 370818291
    },
    {
      "id": 2002,
      "name": "Quinton Rd / Stoney Rd => Quinton Rd / Stoney Rd",
      "length": 0.0004313330267910657,
      "speed": {
        "0:00": 30
      },
      "startid": 370818291,
      "endid": 370818294
    },
    {
      "id": 2003,
      "name": "Quinton Rd / Stoney Rd => Quinton Rd / The Martyrs Close",
      "length": 0.0030395899542527307,
      "speed": {
        "0:00": 30
      },
      "startid": 370818294,
      "endid": 370818506
    },
    {
      "id": 2004,
      "name": "Quinton Rd / The Martyrs Close => Quinton Rd / The Martyrs Close",
      "length": 0.0005721483111920976,
      "speed": {
        "0:00": 30
      },
      "startid": 370818506,
      "endid": 370818505
    },
    {
      "id": 2005,
      "name": "Quinton Rd / The Martyrs Close => Quinton Rd / Lichfield Rd",
      "length": 0.002933190121697732,
      "speed": {
        "0:00": 30
      },
      "startid": 370818505,
      "endid": 370818507
    },
    {
      "id": 2006,
      "name": "Quinton Rd / Lichfield Rd => Quinton Park / Blondvil St",
      "length": 0.0010224467761226605,
      "speed": {
        "0:00": 30
      },
      "startid": 370818507,
      "endid": 370818556
    },
    {
      "id": 2007,
      "name": "Quinton Park / Blondvil St => Quinton Park / Blondvil St",
      "length": 0.0005186051484463979,
      "speed": {
        "0:00": 30
      },
      "startid": 370818556,
      "endid": 370818558
    },
    {
      "id": 2008,
      "name": "Quinton Park / Blondvil St => Quinton Park / Brightwalton Rd",
      "length": 0.0017305165760546526,
      "speed": {
        "0:00": 30
      },
      "startid": 370818558,
      "endid": 370818534
    },
    {
      "id": 2009,
      "name": "Quinton Park / Brightwalton Rd => Quinton Park / Brightwalton Rd",
      "length": 0.00032683006287288844,
      "speed": {
        "0:00": 30
      },
      "startid": 370818534,
      "endid": 370818533
    },
    {
      "id": 2010,
      "name": "Quinton Park / Brightwalton Rd => Black Prince Ave / Mary Herbert St",
      "length": 0.0046660534609022425,
      "speed": {
        "0:00": 30
      },
      "startid": 370818533,
      "endid": 370818537
    },
    {
      "id": 2011,
      "name": "Black Prince Ave / Mary Herbert St => Black Prince Ave / Mary Herbert St",
      "length": 0.000678884828230006,
      "speed": {
        "0:00": 30
      },
      "startid": 370818537,
      "endid": 370818536
    },
    {
      "id": 2012,
      "name": "Black Prince Ave / Mary Herbert St => Black Prince Ave / Arundel Rd",
      "length": 0.004298238137889643,
      "speed": {
        "0:00": 30
      },
      "startid": 370818536,
      "endid": 370818538
    },
    {
      "id": 2013,
      "name": "Black Prince Ave / Arundel Rd => Black Prince Ave / Arundel Rd",
      "length": 0.0008693496247180646,
      "speed": {
        "0:00": 30
      },
      "startid": 370818538,
      "endid": 370818540
    },
    {
      "id": 2014,
      "name": "Black Prince Ave / Arundel Rd => Chatsworth Rise / Newby Close",
      "length": 0.0024783564009264233,
      "speed": {
        "0:00": 30
      },
      "startid": 370818540,
      "endid": 370818541
    },
    {
      "id": 2015,
      "name": "Chatsworth Rise / Newby Close => Chatsworth Rise / Newby Close",
      "length": 0.000542213288289379,
      "speed": {
        "0:00": 30
      },
      "startid": 370818541,
      "endid": 370818544
    },
    {
      "id": 2016,
      "name": "Chatsworth Rise / Newby Close => Exminster Rd / Porlock Close",
      "length": 0.0024867474117849587,
      "speed": {
        "0:00": 30
      },
      "startid": 370818544,
      "endid": 370818550
    },
    {
      "id": 2017,
      "name": "Exminster Rd / Porlock Close => Exminster Rd / Porlock Close",
      "length": 0.0003232980204072183,
      "speed": {
        "0:00": 30
      },
      "startid": 370818550,
      "endid": 370818549
    },
    {
      "id": 2018,
      "name": "Exminster Rd / Porlock Close => Postbridge Rd / Bigbury Close",
      "length": 0.0023131172732949452,
      "speed": {
        "0:00": 30
      },
      "startid": 370818549,
      "endid": 370819589
    },
    {
      "id": 2019,
      "name": "Postbridge Rd / Bigbury Close => Postbridge Rd / Modbury Close",
      "length": 0.0009005638289426289,
      "speed": {
        "0:00": 30
      },
      "startid": 370819589,
      "endid": 370819714
    },
    {
      "id": 2020,
      "name": "Postbridge Rd / Modbury Close => Charminster Dr / Fenside Avenue",
      "length": 0.0038643935423281826,
      "speed": {
        "0:00": 30
      },
      "startid": 370819714,
      "endid": 370819165
    },
    {
      "id": 2021,
      "name": "Charminster Dr / Fenside Avenue => Charminster Dr / Gregory Hood Rd",
      "length": 0.0023281350927280633,
      "speed": {
        "0:00": 30
      },
      "startid": 370819165,
      "endid": 370819081
    },
    {
      "id": 2022,
      "name": "Charminster Dr / Gregory Hood Rd => Charminster Dr / Gregory Hood Rd",
      "length": 0.00014046017229110252,
      "speed": {
        "0:00": 30
      },
      "startid": 370819081,
      "endid": 2646363094
    },
    {
      "id": 2023,
      "name": "Charminster Dr / Gregory Hood Rd => BY1",
      "length": 0.026052490344113943,
      "speed": {
        "0:00": 30
      },
      "startid": 2646363094,
      "endid": 370817684
    },
    {
      "id": 2024,
      "name": "BY1 => White St / Bus Garage",
      "length": 0.009747790942051603,
      "speed": {
        "0:00": 30
      },
      "startid": 370817684,
      "endid": 370817758
    },
    {
      "id": 2025,
      "name": "White St / Bus Garage => TS2",
      "length": 0.005213860014422566,
      "speed": {
        "0:00": 30
      },
      "startid": 370817758,
      "endid": 370817660
    },
    {
      "id": 2026,
      "name": "TS2 => BS3",
      "length": 0.0025764621421626955,
      "speed": {
        "0:00": 30
      },
      "startid": 370817660,
      "endid": 370817695
    },
    {
      "id": 2027,
      "name": "BS3 => VR3",
      "length": 0.005259339564050662,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 370817718
    },
    {
      "id": 2028,
      "name": "VR3 => GR1",
      "length": 0.002224508586183148,
      "speed": {
        "0:00": 30
      },
      "startid": 370817718,
      "endid": 370817794
    },
    {
      "id": 2029,
      "name": "GR1 => BY5",
      "length": 0.0031498880630907375,
      "speed": {
        "0:00": 30
      },
      "startid": 370817794,
      "endid": 370817679
    },
    {
      "id": 2030,
      "name": "BY5 => N",
      "length": 0.006724098430274631,
      "speed": {
        "0:00": 30
      },
      "startid": 370817679,
      "endid": 370817746
    },
    {
      "id": 2031,
      "name": "N => S",
      "length": 0.0005991124769199075,
      "speed": {
        "0:00": 30
      },
      "startid": 370817746,
      "endid": 370817751
    },
    {
      "id": 2032,
      "name": "S => White St / Bus Garage",
      "length": 0.0024134042512565564,
      "speed": {
        "0:00": 30
      },
      "startid": 370817751,
      "endid": 370817757
    },
    {
      "id": 2033,
      "name": "White St / Bus Garage => Victoria St / Vine St",
      "length": 0.003888743563157784,
      "speed": {
        "0:00": 30
      },
      "startid": 370817757,
      "endid": 370817453
    },
    {
      "id": 2034,
      "name": "Victoria St / Vine St => Victoria St / Vine St",
      "length": 0.0007354850440354118,
      "speed": {
        "0:00": 30
      },
      "startid": 370817453,
      "endid": 370817454
    },
    {
      "id": 2035,
      "name": "Victoria St / Vine St => King William St / St Benedicts School",
      "length": 0.003619327810519606,
      "speed": {
        "0:00": 30
      },
      "startid": 370817454,
      "endid": 370817456
    },
    {
      "id": 2036,
      "name": "King William St / St Benedicts School => King William St / St Benedicts School",
      "length": 0.0004073053891133307,
      "speed": {
        "0:00": 30
      },
      "startid": 370817456,
      "endid": 370817455
    },
    {
      "id": 2037,
      "name": "King William St / St Benedicts School => Berry St / Vauxhall St",
      "length": 0.0032078499871399328,
      "speed": {
        "0:00": 30
      },
      "startid": 370817455,
      "endid": 370817459
    },
    {
      "id": 2038,
      "name": "Berry St / Vauxhall St => Berry St / Vauxhall St",
      "length": 0.00015018511910524452,
      "speed": {
        "0:00": 30
      },
      "startid": 370817459,
      "endid": 370817458
    },
    {
      "id": 2039,
      "name": "Berry St / Vauxhall St => Paynes Lane / Days Lane",
      "length": 0.0021721072095999775,
      "speed": {
        "0:00": 30
      },
      "startid": 370817458,
      "endid": 370817460
    },
    {
      "id": 2040,
      "name": "Paynes Lane / Days Lane => Paynes Lane / Days Lane",
      "length": 0.00018780718835871655,
      "speed": {
        "0:00": 30
      },
      "startid": 370817460,
      "endid": 370817462
    },
    {
      "id": 2041,
      "name": "Paynes Lane / Days Lane => Walsgrave Rd / Swan Lane",
      "length": 0.005192963008727335,
      "speed": {
        "0:00": 30
      },
      "startid": 370817462,
      "endid": 370817463
    },
    {
      "id": 2042,
      "name": "Walsgrave Rd / Swan Lane => Walsgrave Rd / Clements St",
      "length": 0.0030988222827398773,
      "speed": {
        "0:00": 30
      },
      "startid": 370817463,
      "endid": 370817467
    },
    {
      "id": 2043,
      "name": "Walsgrave Rd / Clements St => Walsgrave Rd / Clements St",
      "length": 0.0005896212004330483,
      "speed": {
        "0:00": 30
      },
      "startid": 370817467,
      "endid": 370817465
    },
    {
      "id": 2044,
      "name": "Walsgrave Rd / Clements St => Walsgrave Rd / Harefield Rd",
      "length": 0.00521431387624442,
      "speed": {
        "0:00": 30
      },
      "startid": 370817465,
      "endid": 370817501
    },
    {
      "id": 2045,
      "name": "Walsgrave Rd / Harefield Rd => Walsgrave Rd / Harefield Rd",
      "length": 0.0006063554485614267,
      "speed": {
        "0:00": 30
      },
      "startid": 370817501,
      "endid": 370817500
    },
    {
      "id": 2046,
      "name": "Walsgrave Rd / Harefield Rd => Walsgrave Rd / Burns Rd",
      "length": 0.0036222750930872813,
      "speed": {
        "0:00": 30
      },
      "startid": 370817500,
      "endid": 370817504
    },
    {
      "id": 2047,
      "name": "Walsgrave Rd / Burns Rd => Walsgrave Rd / Burns Rd",
      "length": 0.0015216241651606255,
      "speed": {
        "0:00": 30
      },
      "startid": 370817504,
      "endid": 370817502
    },
    {
      "id": 2048,
      "name": "Walsgrave Rd / Burns Rd => Longfellow Rd / Coleridge Rd",
      "length": 0.003106956911513569,
      "speed": {
        "0:00": 30
      },
      "startid": 370817502,
      "endid": 370818337
    },
    {
      "id": 2049,
      "name": "Longfellow Rd / Coleridge Rd => Longfellow Rd / Coleridge Rd",
      "length": 0.0008177070685765369,
      "speed": {
        "0:00": 30
      },
      "startid": 370818337,
      "endid": 370818336
    },
    {
      "id": 2050,
      "name": "Longfellow Rd / Coleridge Rd => Longfellow Rd / Mellowdew Rd",
      "length": 0.002345184926610366,
      "speed": {
        "0:00": 30
      },
      "startid": 370818336,
      "endid": 370817507
    },
    {
      "id": 2051,
      "name": "Longfellow Rd / Mellowdew Rd => Longfellow Rd / Mellowdew Rd",
      "length": 0.0009740439517803643,
      "speed": {
        "0:00": 30
      },
      "startid": 370817507,
      "endid": 370817505
    },
    {
      "id": 2052,
      "name": "Longfellow Rd / Mellowdew Rd => Longfellow Rd / Morris Ave",
      "length": 0.0029103147269665982,
      "speed": {
        "0:00": 30
      },
      "startid": 370817505,
      "endid": 370817512
    },
    {
      "id": 2053,
      "name": "Longfellow Rd / Morris Ave => Longfellow Rd / Morris Ave",
      "length": 0.0009356046707877733,
      "speed": {
        "0:00": 30
      },
      "startid": 370817512,
      "endid": 370817510
    },
    {
      "id": 2054,
      "name": "Longfellow Rd / Morris Ave => Longfellow Rd / Hipswell Highway",
      "length": 0.002224853581700198,
      "speed": {
        "0:00": 30
      },
      "startid": 370817510,
      "endid": 370817703
    },
    {
      "id": 2055,
      "name": "Longfellow Rd / Hipswell Highway => Longfellow Rd / Hipswell Highway",
      "length": 0.0003073880446606868,
      "speed": {
        "0:00": 30
      },
      "startid": 370817703,
      "endid": 370817705
    },
    {
      "id": 2056,
      "name": "Longfellow Rd / Hipswell Highway => Hipswell Highway / Longfellow Rd",
      "length": 0.0013628606164965294,
      "speed": {
        "0:00": 30
      },
      "startid": 370817705,
      "endid": 370817430
    },
    {
      "id": 2057,
      "name": "Hipswell Highway / Longfellow Rd => Hipswell Highway / Meredith Rd",
      "length": 0.0014559813529020406,
      "speed": {
        "0:00": 30
      },
      "startid": 370817430,
      "endid": 370818376
    },
    {
      "id": 2058,
      "name": "Hipswell Highway / Meredith Rd => Hipswell Highway / Meredith Rd",
      "length": 0.00048271595167421127,
      "speed": {
        "0:00": 30
      },
      "startid": 370818376,
      "endid": 370818375
    },
    {
      "id": 2059,
      "name": "Hipswell Highway / Meredith Rd => Mayflower Dr / Allerton Close",
      "length": 0.003259330570836959,
      "speed": {
        "0:00": 30
      },
      "startid": 370818375,
      "endid": 370818365
    },
    {
      "id": 2060,
      "name": "Mayflower Dr / Allerton Close => Mayflower Dr / Allerton Close",
      "length": 0.0008543406873121222,
      "speed": {
        "0:00": 30
      },
      "startid": 370818365,
      "endid": 370818364
    },
    {
      "id": 2061,
      "name": "Mayflower Dr / Allerton Close => Harry Rose Rd / Lloyd Crescent",
      "length": 0.003015470797404941,
      "speed": {
        "0:00": 30
      },
      "startid": 370818364,
      "endid": 370818369
    },
    {
      "id": 2062,
      "name": "Harry Rose Rd / Lloyd Crescent => Harry Rose Rd / Lloyd Crescent",
      "length": 0.000690972712923798,
      "speed": {
        "0:00": 30
      },
      "startid": 370818369,
      "endid": 370818367
    },
    {
      "id": 2063,
      "name": "Harry Rose Rd / Lloyd Crescent => Attoxhall Rd / Hopedale Close",
      "length": 0.002773932320731819,
      "speed": {
        "0:00": 30
      },
      "startid": 370818367,
      "endid": 370818370
    },
    {
      "id": 2064,
      "name": "Attoxhall Rd / Hopedale Close => Attoxhall Rd / Hopedale Close",
      "length": 0.0002227371994051731,
      "speed": {
        "0:00": 30
      },
      "startid": 370818370,
      "endid": 370818371
    },
    {
      "id": 2065,
      "name": "Attoxhall Rd / Hopedale Close => Attoxhall Rd / Belgrave Lodge",
      "length": 0.0014797770440169876,
      "speed": {
        "0:00": 30
      },
      "startid": 370818371,
      "endid": 370818372
    },
    {
      "id": 2066,
      "name": "Attoxhall Rd / Belgrave Lodge => Attoxhall Rd / Belgrave Lodge",
      "length": 0.00024058582668387877,
      "speed": {
        "0:00": 30
      },
      "startid": 370818372,
      "endid": 370818373
    },
    {
      "id": 2067,
      "name": "Attoxhall Rd / Belgrave Lodge => Attoxhall Rd / Axholme Rd",
      "length": 0.001724253948808374,
      "speed": {
        "0:00": 30
      },
      "startid": 370818373,
      "endid": 370818495
    },
    {
      "id": 2068,
      "name": "Attoxhall Rd / Axholme Rd => Belgrave Rd / Attoxhall Rd",
      "length": 0.0013658181797013085,
      "speed": {
        "0:00": 30
      },
      "startid": 370818495,
      "endid": 370819303
    },
    {
      "id": 2069,
      "name": "Belgrave Rd / Attoxhall Rd => Belgrave Rd / Arch Rd",
      "length": 0.0035260788207304087,
      "speed": {
        "0:00": 30
      },
      "startid": 370819303,
      "endid": 370817571
    },
    {
      "id": 2070,
      "name": "Belgrave Rd / Arch Rd => Belgrave Rd / Arch Rd",
      "length": 0.00045216626366826956,
      "speed": {
        "0:00": 30
      },
      "startid": 370817571,
      "endid": 370817572
    },
    {
      "id": 2071,
      "name": "Belgrave Rd / Arch Rd => Belgrave Rd / Westmorland Rd",
      "length": 0.003083393536349537,
      "speed": {
        "0:00": 30
      },
      "startid": 370817572,
      "endid": 370817627
    },
    {
      "id": 2072,
      "name": "Belgrave Rd / Westmorland Rd => Belgrave Rd / Westmorland Rd",
      "length": 0.0001048001908401134,
      "speed": {
        "0:00": 30
      },
      "startid": 370817627,
      "endid": 370817625
    },
    {
      "id": 2073,
      "name": "Belgrave Rd / Westmorland Rd => Belgrave Rd / Clifford Bridge Rd",
      "length": 0.0021349345118752226,
      "speed": {
        "0:00": 30
      },
      "startid": 370817625,
      "endid": 370817709
    },
    {
      "id": 2074,
      "name": "Belgrave Rd / Clifford Bridge Rd => Belgrave Rd / Clifford Bridge Rd",
      "length": 0.000413697050992378,
      "speed": {
        "0:00": 30
      },
      "startid": 370817709,
      "endid": 370817707
    },
    {
      "id": 2075,
      "name": "Belgrave Rd / Clifford Bridge Rd => Clifford Bridge Rd / Dorchester Way",
      "length": 0.0028021035544781208,
      "speed": {
        "0:00": 30
      },
      "startid": 370817707,
      "endid": 370817578
    },
    {
      "id": 2076,
      "name": "Clifford Bridge Rd / Dorchester Way => UH6",
      "length": 0.008406966828171356,
      "speed": {
        "0:00": 30
      },
      "startid": 370817578,
      "endid": 4062225929
    },
    {
      "id": 2077,
      "name": "UH6 => WH",
      "length": 0.005721260320069507,
      "speed": {
        "0:00": 30
      },
      "startid": 4062225929,
      "endid": 370817732
    },
    {
      "id": 2078,
      "name": "WH => WG",
      "length": 0.000278365084014834,
      "speed": {
        "0:00": 30
      },
      "startid": 370817732,
      "endid": 370817730
    },
    {
      "id": 2079,
      "name": "WG => WF",
      "length": 0.003325900281127788,
      "speed": {
        "0:00": 30
      },
      "startid": 370817730,
      "endid": 370817729
    },
    {
      "id": 2080,
      "name": "WF => CS4",
      "length": 0.07458682604374647,
      "speed": {
        "0:00": 30
      },
      "startid": 370817729,
      "endid": 370817702
    },
    {
      "id": 2081,
      "name": "CS4 => Britannia Street / Wren Street",
      "length": 0.023480313232152696,
      "speed": {
        "0:00": 30
      },
      "startid": 370817702,
      "endid": 7857415187
    },
    {
      "id": 2082,
      "name": "Britannia Street / Wren Street => Swan Lane / Britannia Street",
      "length": 0.0021032121552519,
      "speed": {
        "0:00": 30
      },
      "startid": 7857415187,
      "endid": 7857415186
    },
    {
      "id": 2083,
      "name": "Brinklow Rd / Coombe Court => Brinklow Rd / Porchester Close",
      "length": 0.0018598436923576822,
      "speed": {
        "0:00": 30
      },
      "startid": 370819174,
      "endid": 370818428
    },
    {
      "id": 2084,
      "name": "Brinklow Rd / Porchester Close => Brinklow Rd / Porchester Close",
      "length": 0.0019948509367861797,
      "speed": {
        "0:00": 30
      },
      "startid": 370818428,
      "endid": 370818424
    },
    {
      "id": 2085,
      "name": "Brinklow Rd / Porchester Close => Clifford Bridge Rd / Coombe Park Rd",
      "length": 0.003751182184325483,
      "speed": {
        "0:00": 30
      },
      "startid": 370818424,
      "endid": 370818409
    },
    {
      "id": 2086,
      "name": "Clifford Bridge Rd / Coombe Park Rd => Clifford Bridge Rd / Coombe Park Rd",
      "length": 0.0005575986459799535,
      "speed": {
        "0:00": 30
      },
      "startid": 370818409,
      "endid": 370818406
    },
    {
      "id": 2087,
      "name": "Clifford Bridge Rd / Coombe Park Rd => Clifford Bridge Rd / Bridgeacre Gardens",
      "length": 0.0025707344942616124,
      "speed": {
        "0:00": 30
      },
      "startid": 370818406,
      "endid": 370818410
    },
    {
      "id": 2088,
      "name": "Clifford Bridge Rd / Bridgeacre Gardens => Clifford Bridge Rd / Bridgeacre Gardens",
      "length": 0.00034793569808658665,
      "speed": {
        "0:00": 30
      },
      "startid": 370818410,
      "endid": 370818412
    },
    {
      "id": 2089,
      "name": "Clifford Bridge Rd / Bridgeacre Gardens => Clifford Bridge Rd / Gainford Rise",
      "length": 0.0010103507608701986,
      "speed": {
        "0:00": 30
      },
      "startid": 370818412,
      "endid": 370818415
    },
    {
      "id": 2090,
      "name": "Clifford Bridge Rd / Gainford Rise => Clifford Bridge Rd / Gainford Rise",
      "length": 0.0007986141120735769,
      "speed": {
        "0:00": 30
      },
      "startid": 370818415,
      "endid": 370818418
    },
    {
      "id": 2091,
      "name": "Clifford Bridge Rd / Gainford Rise => Clifford Bridge Rd / Tesco",
      "length": 0.0022040893856635595,
      "speed": {
        "0:00": 30
      },
      "startid": 370818418,
      "endid": 370817577
    },
    {
      "id": 2092,
      "name": "Clifford Bridge Rd / Tesco => Clifford Bridge Rd / Tesco",
      "length": 0.0011893140922393406,
      "speed": {
        "0:00": 30
      },
      "startid": 370817577,
      "endid": 370817575
    },
    {
      "id": 2093,
      "name": "Clifford Bridge Rd / Tesco => WG",
      "length": 0.007871720858873762,
      "speed": {
        "0:00": 30
      },
      "startid": 370817575,
      "endid": 370817730
    },
    {
      "id": 2094,
      "name": "WG => WH",
      "length": 0.000278365084014834,
      "speed": {
        "0:00": 30
      },
      "startid": 370817730,
      "endid": 370817732
    },
    {
      "id": 2095,
      "name": "WH => WF",
      "length": 0.00313308919119921,
      "speed": {
        "0:00": 30
      },
      "startid": 370817732,
      "endid": 370817729
    },
    {
      "id": 2096,
      "name": "WF => CU4",
      "length": 0.06393272887848582,
      "speed": {
        "0:00": 30
      },
      "startid": 370817729,
      "endid": 370819679
    },
    {
      "id": 2097,
      "name": "CU4 => CU5",
      "length": 0.0005253710783815626,
      "speed": {
        "0:00": 30
      },
      "startid": 370819679,
      "endid": 370819676
    },
    {
      "id": 2098,
      "name": "CU5 => CU1",
      "length": 0.0021117262535691986,
      "speed": {
        "0:00": 30
      },
      "startid": 370819676,
      "endid": 370817766
    },
    {
      "id": 2099,
      "name": "CU1 => CU2",
      "length": 0.00010206831045847219,
      "speed": {
        "0:00": 30
      },
      "startid": 370817766,
      "endid": 370819680
    },
    {
      "id": 2100,
      "name": "CU2 => Walsgrave Rd / Swan Lane",
      "length": 0.013072843649719269,
      "speed": {
        "0:00": 30
      },
      "startid": 370819680,
      "endid": 370817464
    },
    {
      "id": 2101,
      "name": "Walsgrave Rd / Swan Lane => Walsgrave Rd / Swan Lane",
      "length": 0.0017645372707868672,
      "speed": {
        "0:00": 30
      },
      "startid": 370817464,
      "endid": 370817463
    },
    {
      "id": 2102,
      "name": "Walsgrave Rd / Swan Lane => Walsgrave Rd / Clements St",
      "length": 0.0030988222827398773,
      "speed": {
        "0:00": 30
      },
      "startid": 370817463,
      "endid": 370817467
    },
    {
      "id": 2103,
      "name": "Walsgrave Rd / Clements St => Walsgrave Rd / Clements St",
      "length": 0.0005896212004330483,
      "speed": {
        "0:00": 30
      },
      "startid": 370817467,
      "endid": 370817465
    },
    {
      "id": 2104,
      "name": "Walsgrave Rd / Clements St => Walsgrave Rd / Harefield Rd",
      "length": 0.00521431387624442,
      "speed": {
        "0:00": 30
      },
      "startid": 370817465,
      "endid": 370817501
    },
    {
      "id": 2105,
      "name": "Walsgrave Rd / Harefield Rd => Walsgrave Rd / Harefield Rd",
      "length": 0.0006063554485614267,
      "speed": {
        "0:00": 30
      },
      "startid": 370817501,
      "endid": 370817500
    },
    {
      "id": 2106,
      "name": "Walsgrave Rd / Harefield Rd => Walsgrave Rd / Burns Rd",
      "length": 0.0036222750930872813,
      "speed": {
        "0:00": 30
      },
      "startid": 370817500,
      "endid": 370817504
    },
    {
      "id": 2107,
      "name": "Walsgrave Rd / Burns Rd => Walsgrave Rd / Burns Rd",
      "length": 0.0015216241651606255,
      "speed": {
        "0:00": 30
      },
      "startid": 370817504,
      "endid": 370817502
    },
    {
      "id": 2108,
      "name": "Walsgrave Rd / Burns Rd => Ansty Rd / Dane Rd",
      "length": 0.004151565397533642,
      "speed": {
        "0:00": 30
      },
      "startid": 370817502,
      "endid": 370817522
    },
    {
      "id": 2109,
      "name": "Ansty Rd / Dane Rd => Ansty Rd / Dane Rd",
      "length": 0.0005844890075955145,
      "speed": {
        "0:00": 30
      },
      "startid": 370817522,
      "endid": 370817521
    },
    {
      "id": 2110,
      "name": "Ansty Rd / Dane Rd => Ansty Rd / Mellowdew Rd",
      "length": 0.0024803214388454432,
      "speed": {
        "0:00": 30
      },
      "startid": 370817521,
      "endid": 370817524
    },
    {
      "id": 2111,
      "name": "Ansty Rd / Mellowdew Rd => Ansty Rd / Mellowdew Rd",
      "length": 0.0011267458630953426,
      "speed": {
        "0:00": 30
      },
      "startid": 370817524,
      "endid": 370817526
    },
    {
      "id": 2112,
      "name": "Ansty Rd / Mellowdew Rd => Ansty Rd / Morris Avenue",
      "length": 0.0028913000017288313,
      "speed": {
        "0:00": 30
      },
      "startid": 370817526,
      "endid": 370817620
    },
    {
      "id": 2113,
      "name": "Ansty Rd / Morris Avenue => Ansty Rd / Morris Avenue",
      "length": 0.000945145517896747,
      "speed": {
        "0:00": 30
      },
      "startid": 370817620,
      "endid": 370817621
    },
    {
      "id": 2114,
      "name": "Ansty Rd / Morris Avenue => Ansty Rd / Hipswell Highway",
      "length": 0.0031013986941376545,
      "speed": {
        "0:00": 30
      },
      "startid": 370817621,
      "endid": 370817528
    },
    {
      "id": 2115,
      "name": "Ansty Rd / Hipswell Highway => Ansty Rd / Hipswell Highway",
      "length": 0.001124690188452074,
      "speed": {
        "0:00": 30
      },
      "startid": 370817528,
      "endid": 370817527
    },
    {
      "id": 2116,
      "name": "Ansty Rd / Hipswell Highway => Ansty Rd / Arch Rd",
      "length": 0.003705011516852265,
      "speed": {
        "0:00": 30
      },
      "startid": 370817527,
      "endid": 370817531
    },
    {
      "id": 2117,
      "name": "Ansty Rd / Arch Rd => Ansty Rd / Arch Rd",
      "length": 0.001321381398385821,
      "speed": {
        "0:00": 30
      },
      "startid": 370817531,
      "endid": 370817532
    },
    {
      "id": 2118,
      "name": "Ansty Rd / Arch Rd => Ansty Rd / Norton Hill Drive",
      "length": 0.0027710291896699047,
      "speed": {
        "0:00": 30
      },
      "startid": 370817532,
      "endid": 370817581
    },
    {
      "id": 2119,
      "name": "Ansty Rd / Norton Hill Drive => Ansty Rd / Norton Hill Drive",
      "length": 0.0008620050695904217,
      "speed": {
        "0:00": 30
      },
      "startid": 370817581,
      "endid": 370817583
    },
    {
      "id": 2120,
      "name": "Ansty Rd / Norton Hill Drive => Ansty Rd / Clifford Bridge Rd",
      "length": 0.0027758262787859972,
      "speed": {
        "0:00": 30
      },
      "startid": 370817583,
      "endid": 370817630
    },
    {
      "id": 2121,
      "name": "Ansty Rd / Clifford Bridge Rd => Ansty Rd / Clifford Bridge Rd",
      "length": 0.0004618862630562424,
      "speed": {
        "0:00": 30
      },
      "startid": 370817630,
      "endid": 370817629
    },
    {
      "id": 2122,
      "name": "Ansty Rd / Clifford Bridge Rd => Clifford Bridge Rd / Dorchester Way",
      "length": 0.0037729902756277857,
      "speed": {
        "0:00": 30
      },
      "startid": 370817629,
      "endid": 370817578
    },
    {
      "id": 2123,
      "name": "Clifford Bridge Rd / Dorchester Way => FX1",
      "length": 0.05885796404948178,
      "speed": {
        "0:00": 30
      },
      "startid": 370817578,
      "endid": 370817768
    },
    {
      "id": 2124,
      "name": "FX1 => UH8",
      "length": 0.06670826585671405,
      "speed": {
        "0:00": 30
      },
      "startid": 370817768,
      "endid": 4062225928
    },
    {
      "id": 2125,
      "name": "UH8 => UH9",
      "length": 0.0002945095753964451,
      "speed": {
        "0:00": 30
      },
      "startid": 4062225928,
      "endid": 4062225927
    },
    {
      "id": 2126,
      "name": "UH9 => Sky Blue Way / Walkway To Gosford St",
      "length": 0.05856966329807571,
      "speed": {
        "0:00": 30
      },
      "startid": 4062225927,
      "endid": 4815874919
    },
    {
      "id": 2127,
      "name": "Sky Blue Way / Walkway To Gosford St => Sky Blue Way / Gosford Green",
      "length": 0.002963493080808429,
      "speed": {
        "0:00": 30
      },
      "startid": 4815874919,
      "endid": 4815880374
    },
    {
      "id": 2128,
      "name": "Sky Blue Way / Gosford Green => Sky Blue Way / Gosford Green",
      "length": 0.0003139044440539605,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880374,
      "endid": 4815880373
    },
    {
      "id": 2129,
      "name": "Sky Blue Way / Gosford Green => Brinklow Rd / Coombe Social Club",
      "length": 0.05068172879105407,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880373,
      "endid": 4815880370
    },
    {
      "id": 2130,
      "name": "Brinklow Rd / Coombe Social Club => Brinklow Rd / Rannock Close",
      "length": 0.0007116764222595206,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880370,
      "endid": 4815876529
    },
    {
      "id": 2131,
      "name": "Brinklow Rd / Rannock Close => F",
      "length": 0.06308781278860426,
      "speed": {
        "0:00": 30
      },
      "startid": 4815876529,
      "endid": 370817739
    },
    {
      "id": 2132,
      "name": "Siskin Parkway West => Middlemarch Business Park",
      "length": 0.006366140936231869,
      "speed": {
        "0:00": 30
      },
      "startid": 487166912,
      "endid": 487166905
    },
    {
      "id": 2133,
      "name": "Middlemarch Business Park => Siskin Dr / Rowley Lane",
      "length": 0.009272410284819352,
      "speed": {
        "0:00": 30
      },
      "startid": 487166905,
      "endid": 370819056
    },
    {
      "id": 2134,
      "name": "Siskin Dr / Rowley Lane => Siskin Dr / Rowley Lane",
      "length": 0.0007706453529341519,
      "speed": {
        "0:00": 30
      },
      "startid": 370819056,
      "endid": 370819057
    },
    {
      "id": 2135,
      "name": "Siskin Dr / Rowley Lane => Middlemarch Business Park",
      "length": 0.0028905170506348774,
      "speed": {
        "0:00": 30
      },
      "startid": 370819057,
      "endid": 487166895
    },
    {
      "id": 2136,
      "name": "Middlemarch Business Park => Middlemarch Business Park",
      "length": 0.0003998980995210296,
      "speed": {
        "0:00": 30
      },
      "startid": 487166895,
      "endid": 487166900
    },
    {
      "id": 2137,
      "name": "Middlemarch Business Park => London Rd / Sunbury Rd",
      "length": 0.00882351459283505,
      "speed": {
        "0:00": 30
      },
      "startid": 487166900,
      "endid": 370819047
    },
    {
      "id": 2138,
      "name": "London Rd / Sunbury Rd => London Rd / Sunbury Rd",
      "length": 0.00023836258095914363,
      "speed": {
        "0:00": 30
      },
      "startid": 370819047,
      "endid": 370819044
    },
    {
      "id": 2139,
      "name": "London Rd / Sunbury Rd => London Rd / St James Lane",
      "length": 0.00453077325078063,
      "speed": {
        "0:00": 30
      },
      "startid": 370819044,
      "endid": 370818985
    },
    {
      "id": 2140,
      "name": "London Rd / St James Lane => London Rd / St James Lane",
      "length": 0.0022272216638678536,
      "speed": {
        "0:00": 30
      },
      "startid": 370818985,
      "endid": 370818960
    },
    {
      "id": 2141,
      "name": "London Rd / St James Lane => London Rd / Abbey Rd",
      "length": 0.006926643271455397,
      "speed": {
        "0:00": 30
      },
      "startid": 370818960,
      "endid": 370818604
    },
    {
      "id": 2142,
      "name": "London Rd / Abbey Rd => London Rd / Abbey Rd",
      "length": 0.0013384568203700501,
      "speed": {
        "0:00": 30
      },
      "startid": 370818604,
      "endid": 370818602
    },
    {
      "id": 2143,
      "name": "London Rd / Abbey Rd => London Rd / Tonbridge Rd",
      "length": 0.0027695408716981364,
      "speed": {
        "0:00": 30
      },
      "startid": 370818602,
      "endid": 370818600
    },
    {
      "id": 2144,
      "name": "London Rd / Tonbridge Rd => London Rd / Tonbridge Rd",
      "length": 0.0003229243409830427,
      "speed": {
        "0:00": 30
      },
      "startid": 370818600,
      "endid": 370818601
    },
    {
      "id": 2145,
      "name": "London Rd / Tonbridge Rd => London Rd / Riverside Close",
      "length": 0.0056439592707584075,
      "speed": {
        "0:00": 30
      },
      "startid": 370818601,
      "endid": 370818597
    },
    {
      "id": 2146,
      "name": "London Rd / Riverside Close => London Rd / Riverside Close",
      "length": 0.0011431498676901016,
      "speed": {
        "0:00": 30
      },
      "startid": 370818597,
      "endid": 370818598
    },
    {
      "id": 2147,
      "name": "London Rd / Riverside Close => London Rd / Chace Avenue",
      "length": 0.01330746564489501,
      "speed": {
        "0:00": 30
      },
      "startid": 370818598,
      "endid": 4248964910
    },
    {
      "id": 2148,
      "name": "London Rd / Chace Avenue => Daventry Rd / London Rd",
      "length": 0.021904163370922176,
      "speed": {
        "0:00": 30
      },
      "startid": 4248964910,
      "endid": 370818522
    },
    {
      "id": 2149,
      "name": "Daventry Rd / London Rd => Daventry Rd / London Rd",
      "length": 0.00033666725412569983,
      "speed": {
        "0:00": 30
      },
      "startid": 370818522,
      "endid": 370818524
    },
    {
      "id": 2150,
      "name": "Daventry Rd / London Rd => Daventry Rd / The Mount",
      "length": 0.002846572003304803,
      "speed": {
        "0:00": 30
      },
      "startid": 370818524,
      "endid": 370818519
    },
    {
      "id": 2151,
      "name": "Daventry Rd / The Mount => Daventry Rd / The Mount",
      "length": 0.0015180390541750693,
      "speed": {
        "0:00": 30
      },
      "startid": 370818519,
      "endid": 370818521
    },
    {
      "id": 2152,
      "name": "Daventry Rd / The Mount => Queen Isabels Ave / Daventry Rd",
      "length": 0.004404053011713418,
      "speed": {
        "0:00": 30
      },
      "startid": 370818521,
      "endid": 370818518
    },
    {
      "id": 2153,
      "name": "Queen Isabels Ave / Daventry Rd => Queen Isabels Ave / Daventry Rd",
      "length": 0.00023318492661311281,
      "speed": {
        "0:00": 30
      },
      "startid": 370818518,
      "endid": 370818516
    },
    {
      "id": 2154,
      "name": "Queen Isabels Ave / Daventry Rd => Queen Isabels Ave / The Mount",
      "length": 0.0020399606589372966,
      "speed": {
        "0:00": 30
      },
      "startid": 370818516,
      "endid": 4815874918
    },
    {
      "id": 2155,
      "name": "Queen Isabels Ave / The Mount => Queen Isabels Ave / The Mount",
      "length": 0.00013533986848030953,
      "speed": {
        "0:00": 30
      },
      "startid": 4815874918,
      "endid": 370819721
    },
    {
      "id": 2156,
      "name": "Queen Isabels Ave / The Mount => Mile Lane / Thomas Lansdail St",
      "length": 0.0015672730106782253,
      "speed": {
        "0:00": 30
      },
      "startid": 370819721,
      "endid": 370818512
    },
    {
      "id": 2157,
      "name": "Mile Lane / Thomas Lansdail St => Mile Lane / Thomas Lansdail St",
      "length": 0.0004991193845145756,
      "speed": {
        "0:00": 30
      },
      "startid": 370818512,
      "endid": 370818513
    },
    {
      "id": 2158,
      "name": "Mile Lane / Thomas Lansdail St => Mile Lane / Furlong Rd",
      "length": 0.001976166764221807,
      "speed": {
        "0:00": 30
      },
      "startid": 370818513,
      "endid": 370818502
    },
    {
      "id": 2159,
      "name": "Mile Lane / Furlong Rd => Mile Lane / Furlong Rd",
      "length": 0.0007341031262712063,
      "speed": {
        "0:00": 30
      },
      "startid": 370818502,
      "endid": 370818500
    },
    {
      "id": 2160,
      "name": "Mile Lane / Furlong Rd => Mile Lane / Ibis Hotel",
      "length": 0.002974524829279188,
      "speed": {
        "0:00": 30
      },
      "startid": 370818500,
      "endid": 370818531
    },
    {
      "id": 2161,
      "name": "Mile Lane / Ibis Hotel => Mile Lane / Ibis Hotel",
      "length": 0.0002302223707599752,
      "speed": {
        "0:00": 30
      },
      "startid": 370818531,
      "endid": 370818532
    },
    {
      "id": 2162,
      "name": "Mile Lane / Ibis Hotel => GR2",
      "length": 0.007403848907832494,
      "speed": {
        "0:00": 30
      },
      "startid": 370818532,
      "endid": 370817796
    },
    {
      "id": 2163,
      "name": "GR2 => GR1",
      "length": 0.0004030403081579718,
      "speed": {
        "0:00": 30
      },
      "startid": 370817796,
      "endid": 370817794
    },
    {
      "id": 2164,
      "name": "GR1 => VR3",
      "length": 0.002224508586183148,
      "speed": {
        "0:00": 30
      },
      "startid": 370817794,
      "endid": 370817718
    },
    {
      "id": 2165,
      "name": "VR3 => CS4",
      "length": 0.002391225267514317,
      "speed": {
        "0:00": 30
      },
      "startid": 370817718,
      "endid": 370817702
    },
    {
      "id": 2166,
      "name": "CS4 => TS1",
      "length": 0.005556658126068728,
      "speed": {
        "0:00": 30
      },
      "startid": 370817702,
      "endid": 370817658
    },
    {
      "id": 2167,
      "name": "TS1 => HS3",
      "length": 0.001100515847227857,
      "speed": {
        "0:00": 30
      },
      "startid": 370817658,
      "endid": 4458326372
    },
    {
      "id": 2168,
      "name": "HS3 => VR2",
      "length": 0.00830374601249271,
      "speed": {
        "0:00": 30
      },
      "startid": 4458326372,
      "endid": 370817717
    },
    {
      "id": 2169,
      "name": "VR2 => CS3",
      "length": 0.0021289177156473215,
      "speed": {
        "0:00": 30
      },
      "startid": 370817717,
      "endid": 370817701
    },
    {
      "id": 2170,
      "name": "CS3 => BY5",
      "length": 0.004260969603273784,
      "speed": {
        "0:00": 30
      },
      "startid": 370817701,
      "endid": 370817679
    },
    {
      "id": 2171,
      "name": "BY5 => BY1",
      "length": 0.00030798210987087254,
      "speed": {
        "0:00": 30
      },
      "startid": 370817679,
      "endid": 370817684
    },
    {
      "id": 2172,
      "name": "BY1 => London Rd / Robert Close",
      "length": 0.05108550171594625,
      "speed": {
        "0:00": 30
      },
      "startid": 370817684,
      "endid": 4815874904
    },
    {
      "id": 2173,
      "name": "London Rd / Robert Close => London Rd / Coventry Eastern Bypass",
      "length": 0.0011640695898468664,
      "speed": {
        "0:00": 30
      },
      "startid": 4815874904,
      "endid": 4815880398
    },
    {
      "id": 2174,
      "name": "ES1 => LP1",
      "length": 0.0016872650799448009,
      "speed": {
        "0:00": 30
      },
      "startid": 370817774,
      "endid": 370817776
    },
    {
      "id": 2175,
      "name": "LP1 => FX1",
      "length": 0.0050140651391863056,
      "speed": {
        "0:00": 30
      },
      "startid": 370817776,
      "endid": 370817768
    },
    {
      "id": 2176,
      "name": "FX1 => Walsgrave Rd / Swan Lane",
      "length": 0.015001350180900406,
      "speed": {
        "0:00": 30
      },
      "startid": 370817768,
      "endid": 370817464
    },
    {
      "id": 2177,
      "name": "Walsgrave Rd / Swan Lane => Walsgrave Rd / Swan Lane",
      "length": 0.0017645372707868672,
      "speed": {
        "0:00": 30
      },
      "startid": 370817464,
      "endid": 370817463
    },
    {
      "id": 2178,
      "name": "Walsgrave Rd / Swan Lane => Walsgrave Rd / Clements St",
      "length": 0.0036749426254029296,
      "speed": {
        "0:00": 30
      },
      "startid": 370817463,
      "endid": 370817465
    },
    {
      "id": 2179,
      "name": "Walsgrave Rd / Clements St => Walsgrave Rd / Clements St",
      "length": 0.0005896212004330483,
      "speed": {
        "0:00": 30
      },
      "startid": 370817465,
      "endid": 370817467
    },
    {
      "id": 2180,
      "name": "Walsgrave Rd / Clements St => Walsgrave Rd / Harefield Rd",
      "length": 0.005796096676211783,
      "speed": {
        "0:00": 30
      },
      "startid": 370817467,
      "endid": 370817501
    },
    {
      "id": 2181,
      "name": "Walsgrave Rd / Harefield Rd => Walsgrave Rd / Harefield Rd",
      "length": 0.0006063554485614267,
      "speed": {
        "0:00": 30
      },
      "startid": 370817501,
      "endid": 370817500
    },
    {
      "id": 2182,
      "name": "Walsgrave Rd / Harefield Rd => Walsgrave Rd / Burns Rd",
      "length": 0.0036222750930872813,
      "speed": {
        "0:00": 30
      },
      "startid": 370817500,
      "endid": 370817504
    },
    {
      "id": 2183,
      "name": "Walsgrave Rd / Burns Rd => Walsgrave Rd / Burns Rd",
      "length": 0.0015216241651606255,
      "speed": {
        "0:00": 30
      },
      "startid": 370817504,
      "endid": 370817502
    },
    {
      "id": 2184,
      "name": "Walsgrave Rd / Burns Rd => Ansty Rd / Dane Rd",
      "length": 0.003590546539177356,
      "speed": {
        "0:00": 30
      },
      "startid": 370817502,
      "endid": 370817521
    },
    {
      "id": 2185,
      "name": "Ansty Rd / Dane Rd => Ansty Rd / Dane Rd",
      "length": 0.0005844890075955145,
      "speed": {
        "0:00": 30
      },
      "startid": 370817521,
      "endid": 370817522
    },
    {
      "id": 2186,
      "name": "Ansty Rd / Dane Rd => Ansty Rd / Mellowdew Rd",
      "length": 0.0019575913567442286,
      "speed": {
        "0:00": 30
      },
      "startid": 370817522,
      "endid": 370817524
    },
    {
      "id": 2187,
      "name": "Ansty Rd / Mellowdew Rd => Ansty Rd / Mellowdew Rd",
      "length": 0.0011267458630953426,
      "speed": {
        "0:00": 30
      },
      "startid": 370817524,
      "endid": 370817526
    },
    {
      "id": 2188,
      "name": "Ansty Rd / Mellowdew Rd => Ansty Rd / Morris Avenue",
      "length": 0.0028913000017288313,
      "speed": {
        "0:00": 30
      },
      "startid": 370817526,
      "endid": 370817620
    },
    {
      "id": 2189,
      "name": "Ansty Rd / Morris Avenue => Ansty Rd / Morris Avenue",
      "length": 0.000945145517896747,
      "speed": {
        "0:00": 30
      },
      "startid": 370817620,
      "endid": 370817621
    },
    {
      "id": 2190,
      "name": "Ansty Rd / Morris Avenue => Ansty Rd / Hipswell Highway",
      "length": 0.0031013986941376545,
      "speed": {
        "0:00": 30
      },
      "startid": 370817621,
      "endid": 370817528
    },
    {
      "id": 2191,
      "name": "Ansty Rd / Hipswell Highway => Ansty Rd / Hipswell Highway",
      "length": 0.001124690188452074,
      "speed": {
        "0:00": 30
      },
      "startid": 370817528,
      "endid": 370817527
    },
    {
      "id": 2192,
      "name": "Ansty Rd / Hipswell Highway => Ansty Rd / Arch Rd",
      "length": 0.003705011516852265,
      "speed": {
        "0:00": 30
      },
      "startid": 370817527,
      "endid": 370817531
    },
    {
      "id": 2193,
      "name": "Ansty Rd / Arch Rd => Ansty Rd / Arch Rd",
      "length": 0.001321381398385821,
      "speed": {
        "0:00": 30
      },
      "startid": 370817531,
      "endid": 370817532
    },
    {
      "id": 2194,
      "name": "Ansty Rd / Arch Rd => Ansty Rd / Norton Hill Drive",
      "length": 0.003601649673413492,
      "speed": {
        "0:00": 30
      },
      "startid": 370817532,
      "endid": 370817583
    },
    {
      "id": 2195,
      "name": "Ansty Rd / Norton Hill Drive => Ansty Rd / Norton Hill Drive",
      "length": 0.0008620050695904217,
      "speed": {
        "0:00": 30
      },
      "startid": 370817583,
      "endid": 370817581
    },
    {
      "id": 2196,
      "name": "Ansty Rd / Norton Hill Drive => Ansty Rd / Clifford Bridge Rd",
      "length": 0.003918888200752029,
      "speed": {
        "0:00": 30
      },
      "startid": 370817581,
      "endid": 370817629
    },
    {
      "id": 2197,
      "name": "Ansty Rd / Clifford Bridge Rd => Ansty Rd / Clifford Bridge Rd",
      "length": 0.0004618862630562424,
      "speed": {
        "0:00": 30
      },
      "startid": 370817629,
      "endid": 370817630
    },
    {
      "id": 2198,
      "name": "Ansty Rd / Clifford Bridge Rd => Clifford Bridge Rd / Dorchester Way",
      "length": 0.004182537567073722,
      "speed": {
        "0:00": 30
      },
      "startid": 370817630,
      "endid": 370817578
    },
    {
      "id": 2199,
      "name": "Clifford Bridge Rd / Dorchester Way => Clifford Bridge Rd / Tesco",
      "length": 0.006370308992510571,
      "speed": {
        "0:00": 30
      },
      "startid": 370817578,
      "endid": 370817575
    },
    {
      "id": 2200,
      "name": "Clifford Bridge Rd / Tesco => 2806400124",
      "length": 0.038314988212188525,
      "speed": {
        "0:00": 30
      },
      "startid": 370817575,
      "endid": 2806400124
    },
    {
      "id": 2201,
      "name": "2806400124 => Clifford Bridge Rd / Tesco",
      "length": 0.038169445518243264,
      "speed": {
        "0:00": 30
      },
      "startid": 2806400124,
      "endid": 370817577
    },
    {
      "id": 2202,
      "name": "Clifford Bridge Rd / Tesco => CU5",
      "length": 0.06021420218528153,
      "speed": {
        "0:00": 30
      },
      "startid": 370817577,
      "endid": 370819676
    },
    {
      "id": 2203,
      "name": "CU5 => BY2",
      "length": 0.008046912404767657,
      "speed": {
        "0:00": 30
      },
      "startid": 370819676,
      "endid": 370817685
    },
    {
      "id": 2204,
      "name": "Sky Blue Way / Gosford Green => Sky Blue Way / Gosford Green",
      "length": 0.0003139044440539605,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880374,
      "endid": 4815880373
    },
    {
      "id": 2205,
      "name": "Sky Blue Way / Gosford Green => Sky Blue Way / Walkway To Gosford St",
      "length": 0.0029580316495925675,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880373,
      "endid": 4815874919
    },
    {
      "id": 2206,
      "name": "Sky Blue Way / Walkway To Gosford St => WR4",
      "length": 0.021452258505342804,
      "speed": {
        "0:00": 30
      },
      "startid": 4815874919,
      "endid": 9416517352
    },
    {
      "id": 2207,
      "name": "Hayes Lane => Heckley Road",
      "length": 0.0019734361149991134,
      "speed": {
        "0:00": 30
      },
      "startid": 487169359,
      "endid": 487174461
    },
    {
      "id": 2208,
      "name": "Heckley Road => Trelawney Road",
      "length": 0.0009165142933970633,
      "speed": {
        "0:00": 30
      },
      "startid": 487174461,
      "endid": 487169366
    },
    {
      "id": 2209,
      "name": "Trelawney Road => Lord Raglan",
      "length": 0.0008222157867605711,
      "speed": {
        "0:00": 30
      },
      "startid": 487169366,
      "endid": 487174457
    },
    {
      "id": 2210,
      "name": "Lord Raglan => Longford Road",
      "length": 0.0028648385434478824,
      "speed": {
        "0:00": 30
      },
      "startid": 487174457,
      "endid": 487166797
    },
    {
      "id": 2211,
      "name": "Longford Road => Longford Road",
      "length": 0.00036270456297115243,
      "speed": {
        "0:00": 30
      },
      "startid": 487166797,
      "endid": 487166800
    },
    {
      "id": 2212,
      "name": "Longford Road => Boat",
      "length": 0.0106679351779056,
      "speed": {
        "0:00": 30
      },
      "startid": 487166800,
      "endid": 487165316
    },
    {
      "id": 2213,
      "name": "Boat => 619436810",
      "length": 0.0015395418604202294,
      "speed": {
        "0:00": 30
      },
      "startid": 487165316,
      "endid": 619436810
    },
    {
      "id": 2214,
      "name": "619436810 => 620978722",
      "length": 0.005088427674635968,
      "speed": {
        "0:00": 30
      },
      "startid": 619436810,
      "endid": 620978722
    },
    {
      "id": 2215,
      "name": "620978722 => Black Horse",
      "length": 0.0068626825753486526,
      "speed": {
        "0:00": 30
      },
      "startid": 620978722,
      "endid": 487169388
    },
    {
      "id": 2216,
      "name": "Black Horse => Black Horse",
      "length": 0.00041012888217990085,
      "speed": {
        "0:00": 30
      },
      "startid": 487169388,
      "endid": 487169349
    },
    {
      "id": 2217,
      "name": "Black Horse => Bedworth Rd / Ibstock Rd",
      "length": 0.00473464240888205,
      "speed": {
        "0:00": 30
      },
      "startid": 487169349,
      "endid": 370818879
    },
    {
      "id": 2218,
      "name": "Bedworth Rd / Ibstock Rd => Bedworth Rd / Ibstock Rd",
      "length": 0.00033837257572197685,
      "speed": {
        "0:00": 30
      },
      "startid": 370818879,
      "endid": 370818878
    },
    {
      "id": 2219,
      "name": "Bedworth Rd / Ibstock Rd => Bedworth Rd / Oban Rd",
      "length": 0.002246773317446427,
      "speed": {
        "0:00": 30
      },
      "startid": 370818878,
      "endid": 370818876
    },
    {
      "id": 2220,
      "name": "Bedworth Rd / Oban Rd => Bedworth Rd / Oban Rd",
      "length": 0.0008358934680899525,
      "speed": {
        "0:00": 30
      },
      "startid": 370818876,
      "endid": 370818877
    },
    {
      "id": 2221,
      "name": "Bedworth Rd / Oban Rd => Longford Rd / Longford Square",
      "length": 0.00290910894433318,
      "speed": {
        "0:00": 30
      },
      "startid": 370818877,
      "endid": 370818873
    },
    {
      "id": 2222,
      "name": "Longford Rd / Longford Square => Longford Rd / Longford Square",
      "length": 0.0003155618639778003,
      "speed": {
        "0:00": 30
      },
      "startid": 370818873,
      "endid": 370818874
    },
    {
      "id": 2223,
      "name": "Longford Rd / Longford Square => Longford Rd / Oakmoor Rd",
      "length": 0.0019004607862272331,
      "speed": {
        "0:00": 30
      },
      "startid": 370818874,
      "endid": 370818871
    },
    {
      "id": 2224,
      "name": "Longford Rd / Oakmoor Rd => Longford Rd / Vinecote Rd",
      "length": 0.0011475531403839034,
      "speed": {
        "0:00": 30
      },
      "startid": 370818871,
      "endid": 370818872
    },
    {
      "id": 2225,
      "name": "Longford Rd / Vinecote Rd => Longford Rd / Longford Bridge",
      "length": 0.0020781797901004042,
      "speed": {
        "0:00": 30
      },
      "startid": 370818872,
      "endid": 370819748
    },
    {
      "id": 2226,
      "name": "Longford Rd / Longford Bridge => Longford Rd / Windmill Rd",
      "length": 0.0014970952808711533,
      "speed": {
        "0:00": 30
      },
      "startid": 370819748,
      "endid": 370819732
    },
    {
      "id": 2227,
      "name": "Longford Rd / Windmill Rd => Longford Rd / Dovedale Avenue",
      "length": 0.0010496597639259562,
      "speed": {
        "0:00": 30
      },
      "startid": 370819732,
      "endid": 370818870
    },
    {
      "id": 2228,
      "name": "Longford Rd / Dovedale Avenue => AC",
      "length": 0.001510979774847205,
      "speed": {
        "0:00": 30
      },
      "startid": 370818870,
      "endid": 370819737
    },
    {
      "id": 2229,
      "name": "AC => Windmill Rd / St Thomas' Rd",
      "length": 0.004364151356219984,
      "speed": {
        "0:00": 30
      },
      "startid": 370819737,
      "endid": 370818861
    },
    {
      "id": 2230,
      "name": "Windmill Rd / St Thomas' Rd => Windmill Rd / Recreation Rd",
      "length": 0.001029124258775919,
      "speed": {
        "0:00": 30
      },
      "startid": 370818861,
      "endid": 370817401
    },
    {
      "id": 2231,
      "name": "Windmill Rd / Recreation Rd => Windmill Rd / Barston Close",
      "length": 0.0026771179372600223,
      "speed": {
        "0:00": 30
      },
      "startid": 370817401,
      "endid": 370818882
    },
    {
      "id": 2232,
      "name": "Windmill Rd / Barston Close => Windmill Rd / Barston Close",
      "length": 0.000379546308109366,
      "speed": {
        "0:00": 30
      },
      "startid": 370818882,
      "endid": 370818883
    },
    {
      "id": 2233,
      "name": "Windmill Rd / Barston Close => Windmill Rd / Mill Race Lane",
      "length": 0.0023966617199763364,
      "speed": {
        "0:00": 30
      },
      "startid": 370818883,
      "endid": 370817384
    },
    {
      "id": 2234,
      "name": "Windmill Rd / Mill Race Lane => Windmill Rd / Mill Race Lane",
      "length": 0.0005935334952651139,
      "speed": {
        "0:00": 30
      },
      "startid": 370817384,
      "endid": 370817386
    },
    {
      "id": 2235,
      "name": "Windmill Rd / Mill Race Lane => Hall Green Rd / Dersingham Drive",
      "length": 0.0043879826480969775,
      "speed": {
        "0:00": 30
      },
      "startid": 370817386,
      "endid": 370817369
    },
    {
      "id": 2236,
      "name": "Hall Green Rd / Dersingham Drive => Hall Green Rd / Dersingham Drive",
      "length": 0.0001453545320973188,
      "speed": {
        "0:00": 30
      },
      "startid": 370817369,
      "endid": 370817368
    },
    {
      "id": 2237,
      "name": "Hall Green Rd / Dersingham Drive => Hall Green Rd / Almond Tree Avenue",
      "length": 0.0024157963490318312,
      "speed": {
        "0:00": 30
      },
      "startid": 370817368,
      "endid": 370817362
    },
    {
      "id": 2238,
      "name": "Hall Green Rd / Almond Tree Avenue => Hall Green Rd / Almond Tree Avenue",
      "length": 0.000748740449017119,
      "speed": {
        "0:00": 30
      },
      "startid": 370817362,
      "endid": 370817360
    },
    {
      "id": 2239,
      "name": "Hall Green Rd / Almond Tree Avenue => Hall Green Rd / Old Church Rd",
      "length": 0.002447835421352187,
      "speed": {
        "0:00": 30
      },
      "startid": 370817360,
      "endid": 370819297
    },
    {
      "id": 2240,
      "name": "Hall Green Rd / Old Church Rd => Henley Rd / Old Church Rd",
      "length": 0.0010644874071574137,
      "speed": {
        "0:00": 30
      },
      "startid": 370819297,
      "endid": 370819625
    },
    {
      "id": 2241,
      "name": "Henley Rd / Old Church Rd => Henley Rd / Dame Agnes Grove",
      "length": 0.0015153622570181903,
      "speed": {
        "0:00": 30
      },
      "startid": 370819625,
      "endid": 370817363
    },
    {
      "id": 2242,
      "name": "Henley Rd / Dame Agnes Grove => Henley Rd / Dame Agnes Grove",
      "length": 0.0008064862057111586,
      "speed": {
        "0:00": 30
      },
      "startid": 370817363,
      "endid": 370817365
    },
    {
      "id": 2243,
      "name": "Henley Rd / Dame Agnes Grove => Henley Rd / Deedmore Rd",
      "length": 0.005039856365016028,
      "speed": {
        "0:00": 30
      },
      "startid": 370817365,
      "endid": 370817566
    },
    {
      "id": 2244,
      "name": "Henley Rd / Deedmore Rd => Henley Rd / Deedmore Rd",
      "length": 0.0011696403720807321,
      "speed": {
        "0:00": 30
      },
      "startid": 370817566,
      "endid": 370817569
    },
    {
      "id": 2245,
      "name": "Henley Rd / Deedmore Rd => Henley Rd / Newhall Rd",
      "length": 0.003382197398140166,
      "speed": {
        "0:00": 30
      },
      "startid": 370817569,
      "endid": 370817563
    },
    {
      "id": 2246,
      "name": "Henley Rd / Newhall Rd => Henley Rd / Newhall Rd",
      "length": 0.0018112053693614854,
      "speed": {
        "0:00": 30
      },
      "startid": 370817563,
      "endid": 370817565
    },
    {
      "id": 2247,
      "name": "Henley Rd / Newhall Rd => Henley Rd / Broad Park Rd",
      "length": 0.004441592151469653,
      "speed": {
        "0:00": 30
      },
      "startid": 370817565,
      "endid": 370817561
    },
    {
      "id": 2248,
      "name": "Henley Rd / Broad Park Rd => Henley Rd / Broad Park Rd",
      "length": 0.001552294434054869,
      "speed": {
        "0:00": 30
      },
      "startid": 370817561,
      "endid": 370817560
    },
    {
      "id": 2249,
      "name": "Henley Rd / Broad Park Rd => Henley Rd / Luscombe Rd",
      "length": 0.003119328301092934,
      "speed": {
        "0:00": 30
      },
      "startid": 370817560,
      "endid": 370817559
    },
    {
      "id": 2250,
      "name": "Henley Rd / Luscombe Rd => Henley Rd / Luscombe Rd",
      "length": 0.00031395396159306413,
      "speed": {
        "0:00": 30
      },
      "startid": 370817559,
      "endid": 370817555
    },
    {
      "id": 2251,
      "name": "Henley Rd / Luscombe Rd => Henley Rd / Pandora Rd",
      "length": 0.004563601193136676,
      "speed": {
        "0:00": 30
      },
      "startid": 370817555,
      "endid": 370817409
    },
    {
      "id": 2252,
      "name": "Henley Rd / Pandora Rd => Henley Rd / Pandora Rd",
      "length": 0.000647642779624707,
      "speed": {
        "0:00": 30
      },
      "startid": 370817409,
      "endid": 370817411
    },
    {
      "id": 2253,
      "name": "Henley Rd / Pandora Rd => Woodway Lane / Henley Rd",
      "length": 0.0041314631270286,
      "speed": {
        "0:00": 30
      },
      "startid": 370817411,
      "endid": 370817613
    },
    {
      "id": 2254,
      "name": "Woodway Lane / Henley Rd => Woodway Lane / Henley Rd",
      "length": 0.0007164244063370794,
      "speed": {
        "0:00": 30
      },
      "startid": 370817613,
      "endid": 370817614
    },
    {
      "id": 2255,
      "name": "Woodway Lane / Henley Rd => WF",
      "length": 0.007720458497394788,
      "speed": {
        "0:00": 30
      },
      "startid": 370817614,
      "endid": 370817729
    },
    {
      "id": 2256,
      "name": "WF => WH",
      "length": 0.00313308919119921,
      "speed": {
        "0:00": 30
      },
      "startid": 370817729,
      "endid": 370817732
    },
    {
      "id": 2257,
      "name": "WH => WG",
      "length": 0.000278365084014834,
      "speed": {
        "0:00": 30
      },
      "startid": 370817732,
      "endid": 370817730
    },
    {
      "id": 2258,
      "name": "WG => Ansty Rd / Walsgrave Church",
      "length": 0.003265412096506487,
      "speed": {
        "0:00": 30
      },
      "startid": 370817730,
      "endid": 370817584
    },
    {
      "id": 2259,
      "name": "Ansty Rd / Walsgrave Church => Ansty Rd / Walsgrave Church",
      "length": 0.0003016658581946437,
      "speed": {
        "0:00": 30
      },
      "startid": 370817584,
      "endid": 370817587
    },
    {
      "id": 2260,
      "name": "Ansty Rd / Walsgrave Church => Coventry Road",
      "length": 0.05816428177928438,
      "speed": {
        "0:00": 30
      },
      "startid": 370817587,
      "endid": 487160281
    },
    {
      "id": 2261,
      "name": "Coventry Road => Armson Road",
      "length": 0.0018019165907449727,
      "speed": {
        "0:00": 30
      },
      "startid": 487160281,
      "endid": 487160287
    },
    {
      "id": 2262,
      "name": "Armson Road => Butlers Crescent",
      "length": 0.0034076568166384025,
      "speed": {
        "0:00": 30
      },
      "startid": 487160287,
      "endid": 487166870
    },
    {
      "id": 2263,
      "name": "Butlers Crescent => Jones Road",
      "length": 0.00018893398318178844,
      "speed": {
        "0:00": 30
      },
      "startid": 487166870,
      "endid": 487166874
    },
    {
      "id": 2264,
      "name": "Jones Road => Marshall Road",
      "length": 0.0022575600014171655,
      "speed": {
        "0:00": 30
      },
      "startid": 487166874,
      "endid": 487166879
    },
    {
      "id": 2265,
      "name": "Marshall Road => Marshall Road",
      "length": 0.0001556540073365487,
      "speed": {
        "0:00": 30
      },
      "startid": 487166879,
      "endid": 487166882
    },
    {
      "id": 2266,
      "name": "Windmill Rd / St Thomas' Rd => Blackhorse Road",
      "length": 0.01866992033325566,
      "speed": {
        "0:00": 30
      },
      "startid": 370818859,
      "endid": 487169369
    },
    {
      "id": 2267,
      "name": "Cedars Road => Cedars Road",
      "length": 0.00009587251952832346,
      "speed": {
        "0:00": 30
      },
      "startid": 487166701,
      "endid": 487166699
    },
    {
      "id": 2268,
      "name": "Cedars Road => Field View Close",
      "length": 0.0020560256151158076,
      "speed": {
        "0:00": 30
      },
      "startid": 487166699,
      "endid": 487169363
    },
    {
      "id": 2269,
      "name": "Field View Close => Field View Close",
      "length": 0.0005728722894345266,
      "speed": {
        "0:00": 30
      },
      "startid": 487169363,
      "endid": 487169354
    },
    {
      "id": 2270,
      "name": "Field View Close => Hayes Lane",
      "length": 0.0008336227264145015,
      "speed": {
        "0:00": 30
      },
      "startid": 487169354,
      "endid": 487174464
    },
    {
      "id": 2271,
      "name": "Brandon Rd / East By-Pass => Brandon Rd / East By-Pass",
      "length": 0.0010798288938525175,
      "speed": {
        "0:00": 30
      },
      "startid": 370818486,
      "endid": 370818489
    },
    {
      "id": 2272,
      "name": "Brandon Rd / East By-Pass => Brandon Rd / Herald Way",
      "length": 0.002967906806151397,
      "speed": {
        "0:00": 30
      },
      "startid": 370818489,
      "endid": 370817408
    },
    {
      "id": 2273,
      "name": "Brandon Rd / Herald Way => Brandon Rd / Herald Way",
      "length": 0.00024123619131873235,
      "speed": {
        "0:00": 30
      },
      "startid": 370817408,
      "endid": 370817407
    },
    {
      "id": 2274,
      "name": "Brandon Rd / Herald Way => Brandon Rd / Willenhall Lane",
      "length": 0.002604435086537471,
      "speed": {
        "0:00": 30
      },
      "startid": 370817407,
      "endid": 370818463
    },
    {
      "id": 2275,
      "name": "Brandon Rd / Willenhall Lane => Brandon Rd / Willenhall Lane",
      "length": 0.0003965726289091613,
      "speed": {
        "0:00": 30
      },
      "startid": 370818463,
      "endid": 370818461
    },
    {
      "id": 2276,
      "name": "Brandon Rd / Willenhall Lane => Brandon Rd / Binley Park Inn",
      "length": 0.0039827592570996434,
      "speed": {
        "0:00": 30
      },
      "startid": 370818461,
      "endid": 370818453
    },
    {
      "id": 2277,
      "name": "Brandon Rd / Binley Park Inn => Brandon Rd / Binley Park Inn",
      "length": 0.0005661131512307444,
      "speed": {
        "0:00": 30
      },
      "startid": 370818453,
      "endid": 370818456
    },
    {
      "id": 2278,
      "name": "Brandon Rd / Binley Park Inn => Binley Rd / Ebro Crescent",
      "length": 0.0017650665284913514,
      "speed": {
        "0:00": 30
      },
      "startid": 370818456,
      "endid": 370817807
    },
    {
      "id": 2279,
      "name": "Binley Rd / Ebro Crescent => Binley Rd / Princethorpe Way",
      "length": 0.0016824441090271,
      "speed": {
        "0:00": 30
      },
      "startid": 370817807,
      "endid": 370818381
    },
    {
      "id": 2280,
      "name": "Binley Rd / Princethorpe Way => Binley Rd / Princethorpe Way",
      "length": 0.0018588263635960756,
      "speed": {
        "0:00": 30
      },
      "startid": 370818381,
      "endid": 370818382
    },
    {
      "id": 2281,
      "name": "Binley Rd / Princethorpe Way => Binley Rd / Binley Rd Post Office",
      "length": 0.0021313370005712384,
      "speed": {
        "0:00": 30
      },
      "startid": 370818382,
      "endid": 370818378
    },
    {
      "id": 2282,
      "name": "Binley Rd / Binley Rd Post Office => Binley Rd / Binley Rd Post Office",
      "length": 0.002033100710737182,
      "speed": {
        "0:00": 30
      },
      "startid": 370818378,
      "endid": 370818380
    },
    {
      "id": 2283,
      "name": "Binley Rd / Binley Rd Post Office => Binley Rd / Hipswell Highway",
      "length": 0.004144084219702413,
      "speed": {
        "0:00": 30
      },
      "startid": 370818380,
      "endid": 370818361
    },
    {
      "id": 2284,
      "name": "Binley Rd / Hipswell Highway => Binley Rd / Hipswell Highway",
      "length": 0.0021794502724310242,
      "speed": {
        "0:00": 30
      },
      "startid": 370818361,
      "endid": 370818363
    },
    {
      "id": 2285,
      "name": "Binley Rd / Hipswell Highway => Binley Rd / Bromleigh Drive",
      "length": 0.004219849173846242,
      "speed": {
        "0:00": 30
      },
      "startid": 370818363,
      "endid": 370818359
    },
    {
      "id": 2286,
      "name": "Binley Rd / Bromleigh Drive => Binley Rd / Bromleigh Drive",
      "length": 0.0017399300704338118,
      "speed": {
        "0:00": 30
      },
      "startid": 370818359,
      "endid": 370818360
    },
    {
      "id": 2287,
      "name": "Binley Rd / Bromleigh Drive => Binley Rd / Uxbridge Avenue",
      "length": 0.001940932984416144,
      "speed": {
        "0:00": 30
      },
      "startid": 370818360,
      "endid": 370818356
    },
    {
      "id": 2288,
      "name": "Binley Rd / Uxbridge Avenue => Binley Rd / Uxbridge Avenue",
      "length": 0.0016673498283206552,
      "speed": {
        "0:00": 30
      },
      "startid": 370818356,
      "endid": 370818357
    },
    {
      "id": 2289,
      "name": "Binley Rd / Uxbridge Avenue => Binley Rd / Raleigh Rd",
      "length": 0.002453510279171192,
      "speed": {
        "0:00": 30
      },
      "startid": 370818357,
      "endid": 370818354
    },
    {
      "id": 2290,
      "name": "Binley Rd / Raleigh Rd => Binley Rd / Raleigh Rd",
      "length": 0.00018749146647080057,
      "speed": {
        "0:00": 30
      },
      "startid": 370818354,
      "endid": 370818353
    },
    {
      "id": 2291,
      "name": "Binley Rd / Raleigh Rd => Binley Rd / Bulls Head Lane",
      "length": 0.004688348879936896,
      "speed": {
        "0:00": 30
      },
      "startid": 370818353,
      "endid": 370818334
    },
    {
      "id": 2292,
      "name": "Binley Rd / Bulls Head Lane => Binley Rd / Bulls Head Lane",
      "length": 0.00028935241488505436,
      "speed": {
        "0:00": 30
      },
      "startid": 370818334,
      "endid": 370818335
    },
    {
      "id": 2293,
      "name": "Binley Rd / Bulls Head Lane => Binley Rd / Kingsway",
      "length": 0.0077463133482967555,
      "speed": {
        "0:00": 30
      },
      "startid": 370818335,
      "endid": 370818333
    },
    {
      "id": 2294,
      "name": "Binley Rd / Kingsway => Binley Rd / Kingsway",
      "length": 0.00018105593058337426,
      "speed": {
        "0:00": 30
      },
      "startid": 370818333,
      "endid": 370818331
    },
    {
      "id": 2295,
      "name": "Binley Rd / Kingsway => CU1",
      "length": 0.016480598554967633,
      "speed": {
        "0:00": 30
      },
      "startid": 370818331,
      "endid": 370817766
    },
    {
      "id": 2296,
      "name": "CU1 => CU2",
      "length": 0.00010206831045847219,
      "speed": {
        "0:00": 30
      },
      "startid": 370817766,
      "endid": 370819680
    },
    {
      "id": 2297,
      "name": "CU2 => CU3",
      "length": 0.001764996433423732,
      "speed": {
        "0:00": 30
      },
      "startid": 370819680,
      "endid": 370817767
    },
    {
      "id": 2298,
      "name": "CU3 => CU5",
      "length": 0.000888082090805107,
      "speed": {
        "0:00": 30
      },
      "startid": 370817767,
      "endid": 370819676
    },
    {
      "id": 2299,
      "name": "CU5 => CU4",
      "length": 0.0005253710783815626,
      "speed": {
        "0:00": 30
      },
      "startid": 370819676,
      "endid": 370819679
    },
    {
      "id": 2300,
      "name": "CU4 => HS1",
      "length": 0.005990081242352411,
      "speed": {
        "0:00": 30
      },
      "startid": 370819679,
      "endid": 370819604
    },
    {
      "id": 2301,
      "name": "HS1 => Sky Blue Way / Walkway To Gosford St",
      "length": 0.013271125953738024,
      "speed": {
        "0:00": 30
      },
      "startid": 370819604,
      "endid": 4815874919
    },
    {
      "id": 2302,
      "name": "Sky Blue Way / Walkway To Gosford St => Sky Blue Way / Gosford Green",
      "length": 0.002963493080808429,
      "speed": {
        "0:00": 30
      },
      "startid": 4815874919,
      "endid": 4815880374
    },
    {
      "id": 2303,
      "name": "Sky Blue Way / Gosford Green => Sky Blue Way / Gosford Green",
      "length": 0.0003139044440539605,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880374,
      "endid": 4815880373
    },
    {
      "id": 2304,
      "name": "GH6 => GH5",
      "length": 0.003083086677340662,
      "speed": {
        "0:00": 30
      },
      "startid": 370819586,
      "endid": 370819587
    },
    {
      "id": 2305,
      "name": "GH5 => Kenilworth Rd / Gibbet Hill Rd",
      "length": 0.004086090411382296,
      "speed": {
        "0:00": 30
      },
      "startid": 370819587,
      "endid": 370817937
    },
    {
      "id": 2306,
      "name": "Kenilworth Rd / Gibbet Hill Rd => Kenilworth Rd / Abberton Way",
      "length": 0.007789447649865396,
      "speed": {
        "0:00": 30
      },
      "startid": 370817937,
      "endid": 370817891
    },
    {
      "id": 2307,
      "name": "Kenilworth Rd / Abberton Way => Kenilworth Rd / Abberton Way",
      "length": 0.0005769771225966482,
      "speed": {
        "0:00": 30
      },
      "startid": 370817891,
      "endid": 370817890
    },
    {
      "id": 2308,
      "name": "Kenilworth Rd / Abberton Way => Kenilworth Rd / Cannon Hill Rd",
      "length": 0.00704878890164937,
      "speed": {
        "0:00": 30
      },
      "startid": 370817890,
      "endid": 370817888
    },
    {
      "id": 2309,
      "name": "Kenilworth Rd / Cannon Hill Rd => Kenilworth Rd / Cannon Hill Rd",
      "length": 0.0011689251686877041,
      "speed": {
        "0:00": 30
      },
      "startid": 370817888,
      "endid": 370817887
    },
    {
      "id": 2310,
      "name": "Kenilworth Rd / Cannon Hill Rd => Kenilworth Rd / Kenpas Highway",
      "length": 0.004044736443826238,
      "speed": {
        "0:00": 30
      },
      "startid": 370817887,
      "endid": 370819764
    },
    {
      "id": 2311,
      "name": "Kenilworth Rd / Kenpas Highway => Kenilworth Rd / Fletchamstead Highway",
      "length": 0.0020272871059602952,
      "speed": {
        "0:00": 30
      },
      "startid": 370819764,
      "endid": 370819143
    },
    {
      "id": 2312,
      "name": "Kenilworth Rd / Fletchamstead Highway => Kenilworth Rd / Fletchamstead Highway",
      "length": 0.0003271508062040479,
      "speed": {
        "0:00": 30
      },
      "startid": 370819143,
      "endid": 370817878
    },
    {
      "id": 2313,
      "name": "Kenilworth Rd / Fletchamstead Highway => Kenilworth Rd / Coat Of Arms Bridge Rd",
      "length": 0.0032329641259982583,
      "speed": {
        "0:00": 30
      },
      "startid": 370817878,
      "endid": 370819121
    },
    {
      "id": 2314,
      "name": "Kenilworth Rd / Coat Of Arms Bridge Rd => Kenilworth Rd / Coat Of Arms Bridge Rd",
      "length": 0.0008588363348187505,
      "speed": {
        "0:00": 30
      },
      "startid": 370819121,
      "endid": 370819120
    },
    {
      "id": 2315,
      "name": "Kenilworth Rd / Coat Of Arms Bridge Rd => Kenilworth Rd / Beechwood Avenue",
      "length": 0.0027098195105921007,
      "speed": {
        "0:00": 30
      },
      "startid": 370819120,
      "endid": 370819119
    },
    {
      "id": 2316,
      "name": "Kenilworth Rd / Beechwood Avenue => Kenilworth Rd / Beechwood Avenue",
      "length": 0.00217378832916246,
      "speed": {
        "0:00": 30
      },
      "startid": 370819119,
      "endid": 370819118
    },
    {
      "id": 2317,
      "name": "Kenilworth Rd / Beechwood Avenue => Kenilworth Rd / Earlsdon Avenue South",
      "length": 0.0019592283072683227,
      "speed": {
        "0:00": 30
      },
      "startid": 370819118,
      "endid": 370819116
    },
    {
      "id": 2318,
      "name": "Kenilworth Rd / Earlsdon Avenue South => Kenilworth Rd / Davenport Rd",
      "length": 0.007036728615628068,
      "speed": {
        "0:00": 30
      },
      "startid": 370819116,
      "endid": 370819138
    },
    {
      "id": 2319,
      "name": "Kenilworth Rd / Davenport Rd => Kenilworth Rd / Davenport Rd",
      "length": 0.000915686103422053,
      "speed": {
        "0:00": 30
      },
      "startid": 370819138,
      "endid": 370819141
    },
    {
      "id": 2320,
      "name": "Kenilworth Rd / Davenport Rd => Warwick Road / Leamington Rd",
      "length": 0.003584891552053543,
      "speed": {
        "0:00": 30
      },
      "startid": 370819141,
      "endid": 370818568
    },
    {
      "id": 2321,
      "name": "Warwick Road / Leamington Rd => Warwick Road / Leamington Rd",
      "length": 0.000625492965591671,
      "speed": {
        "0:00": 30
      },
      "startid": 370818568,
      "endid": 370818566
    },
    {
      "id": 2322,
      "name": "Warwick Road / Leamington Rd => WR5",
      "length": 0.0026801527288538595,
      "speed": {
        "0:00": 30
      },
      "startid": 370818566,
      "endid": 370817793
    },
    {
      "id": 2323,
      "name": "WR5 => WR6",
      "length": 0.0004939037153162216,
      "speed": {
        "0:00": 30
      },
      "startid": 370817793,
      "endid": 370817791
    },
    {
      "id": 2324,
      "name": "WR6 => BY4",
      "length": 0.006062511646170546,
      "speed": {
        "0:00": 30
      },
      "startid": 370817791,
      "endid": 370817678
    },
    {
      "id": 2325,
      "name": "BY4 => LP1",
      "length": 0.0033431793505580404,
      "speed": {
        "0:00": 30
      },
      "startid": 370817678,
      "endid": 370817776
    },
    {
      "id": 2326,
      "name": "LP1 => ES1",
      "length": 0.0016872650799448009,
      "speed": {
        "0:00": 30
      },
      "startid": 370817776,
      "endid": 370817774
    },
    {
      "id": 2327,
      "name": "ES1 => CU3",
      "length": 0.0030794748545815336,
      "speed": {
        "0:00": 30
      },
      "startid": 370817774,
      "endid": 370817767
    },
    {
      "id": 2328,
      "name": "CU3 => CU5",
      "length": 0.000888082090805107,
      "speed": {
        "0:00": 30
      },
      "startid": 370817767,
      "endid": 370819676
    },
    {
      "id": 2329,
      "name": "CU5 => FX1",
      "length": 0.001435590516124241,
      "speed": {
        "0:00": 30
      },
      "startid": 370819676,
      "endid": 370817768
    },
    {
      "id": 2330,
      "name": "FX1 => Sheriff Ave / Prior Deram Walk",
      "length": 0.058162475937754726,
      "speed": {
        "0:00": 30
      },
      "startid": 370817768,
      "endid": 370819155
    },
    {
      "id": 2331,
      "name": "Sheriff Ave / Prior Deram Walk => Sheriff Ave / Freeburn Causeway",
      "length": 0.0020251922402616,
      "speed": {
        "0:00": 30
      },
      "startid": 370819155,
      "endid": 370817976
    },
    {
      "id": 2332,
      "name": "Sheriff Ave / Freeburn Causeway => Charter Ave / Northfolk Terrace",
      "length": 0.0014988698309016128,
      "speed": {
        "0:00": 30
      },
      "startid": 370817976,
      "endid": 370817974
    },
    {
      "id": 2333,
      "name": "Charter Ave / Northfolk Terrace => Charter Ave / Freeburn Causeway",
      "length": 0.0037046316861463384,
      "speed": {
        "0:00": 30
      },
      "startid": 370817974,
      "endid": 370817969
    },
    {
      "id": 2334,
      "name": "Charter Ave / Freeburn Causeway => Kirby Corner Rd / Lynchgate Rd",
      "length": 0.0010876794564562144,
      "speed": {
        "0:00": 30
      },
      "startid": 370817969,
      "endid": 370817927
    },
    {
      "id": 2335,
      "name": "Kirby Corner Rd / Lynchgate Rd => Kirby Corner Rd / Lynchgate Rd",
      "length": 0.00029797681117596606,
      "speed": {
        "0:00": 30
      },
      "startid": 370817927,
      "endid": 370817929
    },
    {
      "id": 2336,
      "name": "Kirby Corner Rd / Lynchgate Rd => Kirby Corner Rd / University Westwood Site",
      "length": 0.005184185461573927,
      "speed": {
        "0:00": 30
      },
      "startid": 370817929,
      "endid": 370817930
    },
    {
      "id": 2337,
      "name": "Kirby Corner Rd / University Westwood Site => Kirby Corner Rd / University Westwood Site",
      "length": 0.0008440280208634823,
      "speed": {
        "0:00": 30
      },
      "startid": 370817930,
      "endid": 370817931
    },
    {
      "id": 2338,
      "name": "Kirby Corner Rd / University Westwood Site => Kirby Corner Rd / Gibbet Hill Rd",
      "length": 0.004738827116489978,
      "speed": {
        "0:00": 30
      },
      "startid": 370817931,
      "endid": 370819749
    },
    {
      "id": 2339,
      "name": "Kirby Corner Rd / Gibbet Hill Rd => Gibbet Hill Rd / Kirby Corner Rd",
      "length": 0.0012235206945547885,
      "speed": {
        "0:00": 30
      },
      "startid": 370819749,
      "endid": 370817948
    },
    {
      "id": 2340,
      "name": "Gibbet Hill Rd / Kirby Corner Rd => GH1",
      "length": 0.00028726186659678205,
      "speed": {
        "0:00": 30
      },
      "startid": 370817948,
      "endid": 370817946
    },
    {
      "id": 2341,
      "name": "GH1 => Gibbet Hill Rd / Scarman Rd",
      "length": 0.001683870553218648,
      "speed": {
        "0:00": 30
      },
      "startid": 370817946,
      "endid": 3731548201
    },
    {
      "id": 2342,
      "name": "Gibbet Hill Rd / Scarman Rd => Gibbet Hill Rd / Scarman Rd",
      "length": 0.0013853324113731547,
      "speed": {
        "0:00": 30
      },
      "startid": 3731548201,
      "endid": 3731548192
    },
    {
      "id": 2343,
      "name": "Gibbet Hill Rd / Scarman Rd => UW4",
      "length": 0.003676536093934589,
      "speed": {
        "0:00": 30
      },
      "startid": 3731548192,
      "endid": 3731158214
    },
    {
      "id": 2344,
      "name": "UW4 => UW2",
      "length": 0.0001585356111384327,
      "speed": {
        "0:00": 30
      },
      "startid": 3731158214,
      "endid": 3731158221
    },
    {
      "id": 2345,
      "name": "UW2 => SJ1",
      "length": 0.0601769362782768,
      "speed": {
        "0:00": 30
      },
      "startid": 3731158221,
      "endid": 4815869810
    },
    {
      "id": 2346,
      "name": "SJ1 => MP1",
      "length": 0.0026203276512693527,
      "speed": {
        "0:00": 30
      },
      "startid": 4815869810,
      "endid": 4815869811
    },
    {
      "id": 2347,
      "name": "MP1 => K",
      "length": 0.0039233274168770284,
      "speed": {
        "0:00": 30
      },
      "startid": 4815869811,
      "endid": 4815881224
    },
    {
      "id": 2348,
      "name": "K => BY2",
      "length": 0.006710630889118878,
      "speed": {
        "0:00": 30
      },
      "startid": 4815881224,
      "endid": 370817685
    },
    {
      "id": 2349,
      "name": "BY2 => Sir Henry Parkes Rd / Centenary Rd",
      "length": 0.04372023887960915,
      "speed": {
        "0:00": 30
      },
      "startid": 370817685,
      "endid": 370817913
    },
    {
      "id": 2350,
      "name": "Sir Henry Parkes Rd / Centenary Rd => Prior Deram Walk / Fletchamstead Highway",
      "length": 0.004380416794095476,
      "speed": {
        "0:00": 30
      },
      "startid": 370817913,
      "endid": 4815876523
    },
    {
      "id": 2351,
      "name": "Prior Deram Walk / Fletchamstead Highway => Kenilworth Rd / Earlsdon Avenue South",
      "length": 0.031583567408543164,
      "speed": {
        "0:00": 30
      },
      "startid": 4815876523,
      "endid": 4815880396
    },
    {
      "id": 2352,
      "name": "Brinklow Rd / Coombe Court => Brinklow Rd / Porchester Close",
      "length": 0.0018598436923576822,
      "speed": {
        "0:00": 30
      },
      "startid": 370819174,
      "endid": 370818428
    },
    {
      "id": 2353,
      "name": "Brinklow Rd / Porchester Close => Brinklow Rd / Porchester Close",
      "length": 0.0019948509367861797,
      "speed": {
        "0:00": 30
      },
      "startid": 370818428,
      "endid": 370818424
    },
    {
      "id": 2354,
      "name": "Brinklow Rd / Porchester Close => Clifford Bridge Rd / Coombe Park Rd",
      "length": 0.003751182184325483,
      "speed": {
        "0:00": 30
      },
      "startid": 370818424,
      "endid": 370818409
    },
    {
      "id": 2355,
      "name": "Clifford Bridge Rd / Coombe Park Rd => Clifford Bridge Rd / Coombe Park Rd",
      "length": 0.0005575986459799535,
      "speed": {
        "0:00": 30
      },
      "startid": 370818409,
      "endid": 370818406
    },
    {
      "id": 2356,
      "name": "Clifford Bridge Rd / Coombe Park Rd => Clifford Bridge Rd / Bridgeacre Gardens",
      "length": 0.0025707344942616124,
      "speed": {
        "0:00": 30
      },
      "startid": 370818406,
      "endid": 370818410
    },
    {
      "id": 2357,
      "name": "Clifford Bridge Rd / Bridgeacre Gardens => Clifford Bridge Rd / Bridgeacre Gardens",
      "length": 0.00034793569808658665,
      "speed": {
        "0:00": 30
      },
      "startid": 370818410,
      "endid": 370818412
    },
    {
      "id": 2358,
      "name": "Clifford Bridge Rd / Bridgeacre Gardens => Clifford Bridge Rd / Gainford Rise",
      "length": 0.0010103507608701986,
      "speed": {
        "0:00": 30
      },
      "startid": 370818412,
      "endid": 370818415
    },
    {
      "id": 2359,
      "name": "Clifford Bridge Rd / Gainford Rise => Clifford Bridge Rd / Gainford Rise",
      "length": 0.0007986141120735769,
      "speed": {
        "0:00": 30
      },
      "startid": 370818415,
      "endid": 370818418
    },
    {
      "id": 2360,
      "name": "Clifford Bridge Rd / Gainford Rise => Clifford Bridge Rd / Tesco",
      "length": 0.0022040893856635595,
      "speed": {
        "0:00": 30
      },
      "startid": 370818418,
      "endid": 370817577
    },
    {
      "id": 2361,
      "name": "Clifford Bridge Rd / Tesco => Clifford Bridge Rd / Tesco",
      "length": 0.0011893140922393406,
      "speed": {
        "0:00": 30
      },
      "startid": 370817577,
      "endid": 370817575
    },
    {
      "id": 2362,
      "name": "Clifford Bridge Rd / Tesco => WG",
      "length": 0.007871720858873762,
      "speed": {
        "0:00": 30
      },
      "startid": 370817575,
      "endid": 370817730
    },
    {
      "id": 2363,
      "name": "WG => WH",
      "length": 0.000278365084014834,
      "speed": {
        "0:00": 30
      },
      "startid": 370817730,
      "endid": 370817732
    },
    {
      "id": 2364,
      "name": "WH => WF",
      "length": 0.00313308919119921,
      "speed": {
        "0:00": 30
      },
      "startid": 370817732,
      "endid": 370817729
    },
    {
      "id": 2365,
      "name": "WF => CU4",
      "length": 0.06393272887848582,
      "speed": {
        "0:00": 30
      },
      "startid": 370817729,
      "endid": 370819679
    },
    {
      "id": 2366,
      "name": "CU4 => CU5",
      "length": 0.0005253710783815626,
      "speed": {
        "0:00": 30
      },
      "startid": 370819679,
      "endid": 370819676
    },
    {
      "id": 2367,
      "name": "CU5 => CU1",
      "length": 0.0021117262535691986,
      "speed": {
        "0:00": 30
      },
      "startid": 370819676,
      "endid": 370817766
    },
    {
      "id": 2368,
      "name": "CU1 => CU2",
      "length": 0.00010206831045847219,
      "speed": {
        "0:00": 30
      },
      "startid": 370817766,
      "endid": 370819680
    },
    {
      "id": 2369,
      "name": "CU2 => Clifford Bridge Rd / Dorchester Way",
      "length": 0.05724264595605326,
      "speed": {
        "0:00": 30
      },
      "startid": 370819680,
      "endid": 370817578
    },
    {
      "id": 2370,
      "name": "Clifford Bridge Rd / Dorchester Way => FX1",
      "length": 0.05885796404948178,
      "speed": {
        "0:00": 30
      },
      "startid": 370817578,
      "endid": 370817768
    },
    {
      "id": 2371,
      "name": "FX1 => UH8",
      "length": 0.06670826585671405,
      "speed": {
        "0:00": 30
      },
      "startid": 370817768,
      "endid": 4062225928
    },
    {
      "id": 2372,
      "name": "UH8 => UH9",
      "length": 0.0002945095753964451,
      "speed": {
        "0:00": 30
      },
      "startid": 4062225928,
      "endid": 4062225927
    },
    {
      "id": 2373,
      "name": "UH9 => Sky Blue Way / Walkway To Gosford St",
      "length": 0.05856966329807571,
      "speed": {
        "0:00": 30
      },
      "startid": 4062225927,
      "endid": 4815874919
    },
    {
      "id": 2374,
      "name": "Sky Blue Way / Walkway To Gosford St => Sky Blue Way / Gosford Green",
      "length": 0.002963493080808429,
      "speed": {
        "0:00": 30
      },
      "startid": 4815874919,
      "endid": 4815880374
    },
    {
      "id": 2375,
      "name": "Sky Blue Way / Gosford Green => Brinklow Rd / Coombe Social Club",
      "length": 0.05058371016888745,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880374,
      "endid": 4815880370
    },
    {
      "id": 2376,
      "name": "Brinklow Rd / Coombe Social Club => Brinklow Rd / Rannock Close",
      "length": 0.0007116764222595206,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880370,
      "endid": 4815876529
    },
    {
      "id": 2377,
      "name": "Brinklow Rd / Rannock Close => F",
      "length": 0.06308781278860426,
      "speed": {
        "0:00": 30
      },
      "startid": 4815876529,
      "endid": 370817739
    },
    {
      "id": 2378,
      "name": "Belgrave Rd / Clifford Bridge Rd => Belgrave Rd / Clifford Bridge Rd",
      "length": 0.000413697050992378,
      "speed": {
        "0:00": 30
      },
      "startid": 370817707,
      "endid": 370817709
    },
    {
      "id": 2379,
      "name": "Belgrave Rd / Clifford Bridge Rd => Belgrave Rd / Westmorland Rd",
      "length": 0.0021349345118752226,
      "speed": {
        "0:00": 30
      },
      "startid": 370817709,
      "endid": 370817625
    },
    {
      "id": 2380,
      "name": "Belgrave Rd / Westmorland Rd => Belgrave Rd / Westmorland Rd",
      "length": 0.0001048001908401134,
      "speed": {
        "0:00": 30
      },
      "startid": 370817625,
      "endid": 370817627
    },
    {
      "id": 2381,
      "name": "Belgrave Rd / Westmorland Rd => Belgrave Rd / Arch Rd",
      "length": 0.003083393536349537,
      "speed": {
        "0:00": 30
      },
      "startid": 370817627,
      "endid": 370817572
    },
    {
      "id": 2382,
      "name": "Belgrave Rd / Arch Rd => Belgrave Rd / Arch Rd",
      "length": 0.00045216626366826956,
      "speed": {
        "0:00": 30
      },
      "startid": 370817572,
      "endid": 370817571
    },
    {
      "id": 2383,
      "name": "Belgrave Rd / Arch Rd => Belgrave Rd / Attoxhall Rd",
      "length": 0.0035260788207304087,
      "speed": {
        "0:00": 30
      },
      "startid": 370817571,
      "endid": 370819303
    },
    {
      "id": 2384,
      "name": "Belgrave Rd / Attoxhall Rd => Belgrave Rd / Attoxhall Rd",
      "length": 0.00013086252328456342,
      "speed": {
        "0:00": 30
      },
      "startid": 370819303,
      "endid": 370819304
    },
    {
      "id": 2385,
      "name": "Belgrave Rd / Attoxhall Rd => Belgrave Rd / St Ives Rd",
      "length": 0.0022946951867313984,
      "speed": {
        "0:00": 30
      },
      "startid": 370819304,
      "endid": 370817706
    },
    {
      "id": 2386,
      "name": "Belgrave Rd / St Ives Rd => Hipswell Highway / Belgrave Rd",
      "length": 0.0006430308624006904,
      "speed": {
        "0:00": 30
      },
      "startid": 370817706,
      "endid": 370817518
    },
    {
      "id": 2387,
      "name": "Hipswell Highway / Belgrave Rd => Hipswell Highway / Middle",
      "length": 0.0018479660521746348,
      "speed": {
        "0:00": 30
      },
      "startid": 370817518,
      "endid": 370817515
    },
    {
      "id": 2388,
      "name": "Hipswell Highway / Middle => Hipswell Highway / Middle",
      "length": 0.0005154422567053818,
      "speed": {
        "0:00": 30
      },
      "startid": 370817515,
      "endid": 370817514
    },
    {
      "id": 2389,
      "name": "Hipswell Highway / Middle => Hipswell Highway / Longfellow Rd",
      "length": 0.0010147675300312047,
      "speed": {
        "0:00": 30
      },
      "startid": 370817514,
      "endid": 370817431
    },
    {
      "id": 2390,
      "name": "Hipswell Highway / Longfellow Rd => Hipswell Highway / Longfellow Rd",
      "length": 0.0013096059598217862,
      "speed": {
        "0:00": 30
      },
      "startid": 370817431,
      "endid": 370817430
    },
    {
      "id": 2391,
      "name": "Hipswell Highway / Longfellow Rd => Hipswell Highway / Meredith Rd",
      "length": 0.0014559813529020406,
      "speed": {
        "0:00": 30
      },
      "startid": 370817430,
      "endid": 370818376
    },
    {
      "id": 2392,
      "name": "Hipswell Highway / Meredith Rd => Hipswell Highway / Meredith Rd",
      "length": 0.00048271595167421127,
      "speed": {
        "0:00": 30
      },
      "startid": 370818376,
      "endid": 370818375
    },
    {
      "id": 2393,
      "name": "Hipswell Highway / Meredith Rd => Hipswell Highway / Binley Rd",
      "length": 0.002199205922597769,
      "speed": {
        "0:00": 30
      },
      "startid": 370818375,
      "endid": 370818493
    },
    {
      "id": 2394,
      "name": "Hipswell Highway / Binley Rd => Binley Rd / Bromleigh Drive",
      "length": 0.007305056129832307,
      "speed": {
        "0:00": 30
      },
      "startid": 370818493,
      "endid": 370818360
    },
    {
      "id": 2395,
      "name": "Binley Rd / Bromleigh Drive => Binley Rd / Uxbridge Avenue",
      "length": 0.001940932984416144,
      "speed": {
        "0:00": 30
      },
      "startid": 370818360,
      "endid": 370818356
    },
    {
      "id": 2396,
      "name": "Binley Rd / Uxbridge Avenue => Binley Rd / Uxbridge Avenue",
      "length": 0.0016673498283206552,
      "speed": {
        "0:00": 30
      },
      "startid": 370818356,
      "endid": 370818357
    },
    {
      "id": 2397,
      "name": "Binley Rd / Uxbridge Avenue => Binley Rd / Raleigh Rd",
      "length": 0.002453510279171192,
      "speed": {
        "0:00": 30
      },
      "startid": 370818357,
      "endid": 370818354
    },
    {
      "id": 2398,
      "name": "Binley Rd / Raleigh Rd => Binley Rd / Raleigh Rd",
      "length": 0.00018749146647080057,
      "speed": {
        "0:00": 30
      },
      "startid": 370818354,
      "endid": 370818353
    },
    {
      "id": 2399,
      "name": "Binley Rd / Raleigh Rd => Binley Rd / Bulls Head Lane",
      "length": 0.004474147677491692,
      "speed": {
        "0:00": 30
      },
      "startid": 370818353,
      "endid": 370818335
    },
    {
      "id": 2400,
      "name": "Binley Rd / Bulls Head Lane => Binley Rd / Bulls Head Lane",
      "length": 0.00028935241488505436,
      "speed": {
        "0:00": 30
      },
      "startid": 370818335,
      "endid": 370818334
    },
    {
      "id": 2401,
      "name": "Binley Rd / Bulls Head Lane => Binley Rd / Kingsway",
      "length": 0.00749600886939167,
      "speed": {
        "0:00": 30
      },
      "startid": 370818334,
      "endid": 370818333
    },
    {
      "id": 2402,
      "name": "Binley Rd / Kingsway => Binley Rd / Kingsway",
      "length": 0.00018105593058337426,
      "speed": {
        "0:00": 30
      },
      "startid": 370818333,
      "endid": 370818331
    },
    {
      "id": 2403,
      "name": "Binley Rd / Kingsway => Far Gosford St / Gosford Green",
      "length": 0.007543255666488108,
      "speed": {
        "0:00": 30
      },
      "startid": 370818331,
      "endid": 4815880406
    },
    {
      "id": 2404,
      "name": "Far Gosford St / Gosford Green => Far Gosford St / Bramble St",
      "length": 0.004033183017171992,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880406,
      "endid": 4815880407
    },
    {
      "id": 2405,
      "name": "Brinklow Rd / Coombe Court => Brinklow Rd / Porchester Close",
      "length": 0.0018598436923576822,
      "speed": {
        "0:00": 30
      },
      "startid": 370819174,
      "endid": 370818428
    },
    {
      "id": 2406,
      "name": "Brinklow Rd / Porchester Close => Brinklow Rd / Porchester Close",
      "length": 0.0019948509367861797,
      "speed": {
        "0:00": 30
      },
      "startid": 370818428,
      "endid": 370818424
    },
    {
      "id": 2407,
      "name": "Brinklow Rd / Porchester Close => Clifford Bridge Rd / Coombe Park Rd",
      "length": 0.003751182184325483,
      "speed": {
        "0:00": 30
      },
      "startid": 370818424,
      "endid": 370818409
    },
    {
      "id": 2408,
      "name": "Clifford Bridge Rd / Coombe Park Rd => Clifford Bridge Rd / Coombe Park Rd",
      "length": 0.0005575986459799535,
      "speed": {
        "0:00": 30
      },
      "startid": 370818409,
      "endid": 370818406
    },
    {
      "id": 2409,
      "name": "Clifford Bridge Rd / Coombe Park Rd => Clifford Bridge Rd / Bridgeacre Gardens",
      "length": 0.0025707344942616124,
      "speed": {
        "0:00": 30
      },
      "startid": 370818406,
      "endid": 370818410
    },
    {
      "id": 2410,
      "name": "Clifford Bridge Rd / Bridgeacre Gardens => Clifford Bridge Rd / Bridgeacre Gardens",
      "length": 0.00034793569808658665,
      "speed": {
        "0:00": 30
      },
      "startid": 370818410,
      "endid": 370818412
    },
    {
      "id": 2411,
      "name": "Clifford Bridge Rd / Bridgeacre Gardens => Clifford Bridge Rd / Gainford Rise",
      "length": 0.0010103507608701986,
      "speed": {
        "0:00": 30
      },
      "startid": 370818412,
      "endid": 370818415
    },
    {
      "id": 2412,
      "name": "Clifford Bridge Rd / Gainford Rise => Clifford Bridge Rd / Gainford Rise",
      "length": 0.0007986141120735769,
      "speed": {
        "0:00": 30
      },
      "startid": 370818415,
      "endid": 370818418
    },
    {
      "id": 2413,
      "name": "Clifford Bridge Rd / Gainford Rise => Clifford Bridge Rd / Tesco",
      "length": 0.0022040893856635595,
      "speed": {
        "0:00": 30
      },
      "startid": 370818418,
      "endid": 370817577
    },
    {
      "id": 2414,
      "name": "Clifford Bridge Rd / Tesco => Clifford Bridge Rd / Tesco",
      "length": 0.0011893140922393406,
      "speed": {
        "0:00": 30
      },
      "startid": 370817577,
      "endid": 370817575
    },
    {
      "id": 2415,
      "name": "Clifford Bridge Rd / Tesco => WG",
      "length": 0.007871720858873762,
      "speed": {
        "0:00": 30
      },
      "startid": 370817575,
      "endid": 370817730
    },
    {
      "id": 2416,
      "name": "WG => WH",
      "length": 0.000278365084014834,
      "speed": {
        "0:00": 30
      },
      "startid": 370817730,
      "endid": 370817732
    },
    {
      "id": 2417,
      "name": "WH => WF",
      "length": 0.00313308919119921,
      "speed": {
        "0:00": 30
      },
      "startid": 370817732,
      "endid": 370817729
    },
    {
      "id": 2418,
      "name": "WF => CU4",
      "length": 0.06393272887848582,
      "speed": {
        "0:00": 30
      },
      "startid": 370817729,
      "endid": 370819679
    },
    {
      "id": 2419,
      "name": "CU4 => CU5",
      "length": 0.0005253710783815626,
      "speed": {
        "0:00": 30
      },
      "startid": 370819679,
      "endid": 370819676
    },
    {
      "id": 2420,
      "name": "CU5 => CU1",
      "length": 0.0021117262535691986,
      "speed": {
        "0:00": 30
      },
      "startid": 370819676,
      "endid": 370817766
    },
    {
      "id": 2421,
      "name": "CU1 => CU2",
      "length": 0.00010206831045847219,
      "speed": {
        "0:00": 30
      },
      "startid": 370817766,
      "endid": 370819680
    },
    {
      "id": 2422,
      "name": "CU2 => Clifford Bridge Rd / Dorchester Way",
      "length": 0.05724264595605326,
      "speed": {
        "0:00": 30
      },
      "startid": 370819680,
      "endid": 370817578
    },
    {
      "id": 2423,
      "name": "Clifford Bridge Rd / Dorchester Way => FX1",
      "length": 0.05885796404948178,
      "speed": {
        "0:00": 30
      },
      "startid": 370817578,
      "endid": 370817768
    },
    {
      "id": 2424,
      "name": "FX1 => UH8",
      "length": 0.06670826585671405,
      "speed": {
        "0:00": 30
      },
      "startid": 370817768,
      "endid": 4062225928
    },
    {
      "id": 2425,
      "name": "UH8 => UH9",
      "length": 0.0002945095753964451,
      "speed": {
        "0:00": 30
      },
      "startid": 4062225928,
      "endid": 4062225927
    },
    {
      "id": 2426,
      "name": "UH9 => Sky Blue Way / Walkway To Gosford St",
      "length": 0.05856966329807571,
      "speed": {
        "0:00": 30
      },
      "startid": 4062225927,
      "endid": 4815874919
    },
    {
      "id": 2427,
      "name": "Sky Blue Way / Walkway To Gosford St => Sky Blue Way / Gosford Green",
      "length": 0.002963493080808429,
      "speed": {
        "0:00": 30
      },
      "startid": 4815874919,
      "endid": 4815880374
    },
    {
      "id": 2428,
      "name": "Sky Blue Way / Gosford Green => Brinklow Rd / Coombe Social Club",
      "length": 0.05058371016888745,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880374,
      "endid": 4815880370
    },
    {
      "id": 2429,
      "name": "Brinklow Rd / Coombe Social Club => Brinklow Rd / Rannock Close",
      "length": 0.0007116764222595206,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880370,
      "endid": 4815876529
    },
    {
      "id": 2430,
      "name": "Brinklow Rd / Rannock Close => F",
      "length": 0.06308781278860426,
      "speed": {
        "0:00": 30
      },
      "startid": 4815876529,
      "endid": 370817739
    },
    {
      "id": 2431,
      "name": "Belgrave Rd / Clifford Bridge Rd => Belgrave Rd / Clifford Bridge Rd",
      "length": 0.000413697050992378,
      "speed": {
        "0:00": 30
      },
      "startid": 370817707,
      "endid": 370817709
    },
    {
      "id": 2432,
      "name": "Belgrave Rd / Clifford Bridge Rd => Belgrave Rd / Westmorland Rd",
      "length": 0.0021349345118752226,
      "speed": {
        "0:00": 30
      },
      "startid": 370817709,
      "endid": 370817625
    },
    {
      "id": 2433,
      "name": "Belgrave Rd / Westmorland Rd => Belgrave Rd / Westmorland Rd",
      "length": 0.0001048001908401134,
      "speed": {
        "0:00": 30
      },
      "startid": 370817625,
      "endid": 370817627
    },
    {
      "id": 2434,
      "name": "Belgrave Rd / Westmorland Rd => Belgrave Rd / Arch Rd",
      "length": 0.003083393536349537,
      "speed": {
        "0:00": 30
      },
      "startid": 370817627,
      "endid": 370817572
    },
    {
      "id": 2435,
      "name": "Belgrave Rd / Arch Rd => Belgrave Rd / Arch Rd",
      "length": 0.00045216626366826956,
      "speed": {
        "0:00": 30
      },
      "startid": 370817572,
      "endid": 370817571
    },
    {
      "id": 2436,
      "name": "Belgrave Rd / Arch Rd => Belgrave Rd / Attoxhall Rd",
      "length": 0.0035260788207304087,
      "speed": {
        "0:00": 30
      },
      "startid": 370817571,
      "endid": 370819303
    },
    {
      "id": 2437,
      "name": "Belgrave Rd / Attoxhall Rd => Belgrave Rd / Attoxhall Rd",
      "length": 0.00013086252328456342,
      "speed": {
        "0:00": 30
      },
      "startid": 370819303,
      "endid": 370819304
    },
    {
      "id": 2438,
      "name": "Belgrave Rd / Attoxhall Rd => Belgrave Rd / St Ives Rd",
      "length": 0.0022946951867313984,
      "speed": {
        "0:00": 30
      },
      "startid": 370819304,
      "endid": 370817706
    },
    {
      "id": 2439,
      "name": "Belgrave Rd / St Ives Rd => Hipswell Highway / Belgrave Rd",
      "length": 0.0006430308624006904,
      "speed": {
        "0:00": 30
      },
      "startid": 370817706,
      "endid": 370817518
    },
    {
      "id": 2440,
      "name": "Hipswell Highway / Belgrave Rd => Hipswell Highway / Middle",
      "length": 0.0018479660521746348,
      "speed": {
        "0:00": 30
      },
      "startid": 370817518,
      "endid": 370817515
    },
    {
      "id": 2441,
      "name": "Hipswell Highway / Middle => Hipswell Highway / Middle",
      "length": 0.0005154422567053818,
      "speed": {
        "0:00": 30
      },
      "startid": 370817515,
      "endid": 370817514
    },
    {
      "id": 2442,
      "name": "Hipswell Highway / Middle => Hipswell Highway / Longfellow Rd",
      "length": 0.0010147675300312047,
      "speed": {
        "0:00": 30
      },
      "startid": 370817514,
      "endid": 370817431
    },
    {
      "id": 2443,
      "name": "Hipswell Highway / Longfellow Rd => Hipswell Highway / Longfellow Rd",
      "length": 0.0013096059598217862,
      "speed": {
        "0:00": 30
      },
      "startid": 370817431,
      "endid": 370817430
    },
    {
      "id": 2444,
      "name": "Hipswell Highway / Longfellow Rd => Hipswell Highway / Meredith Rd",
      "length": 0.0014559813529020406,
      "speed": {
        "0:00": 30
      },
      "startid": 370817430,
      "endid": 370818376
    },
    {
      "id": 2445,
      "name": "Hipswell Highway / Meredith Rd => Hipswell Highway / Meredith Rd",
      "length": 0.00048271595167421127,
      "speed": {
        "0:00": 30
      },
      "startid": 370818376,
      "endid": 370818375
    },
    {
      "id": 2446,
      "name": "Hipswell Highway / Meredith Rd => Hipswell Highway / Binley Rd",
      "length": 0.002199205922597769,
      "speed": {
        "0:00": 30
      },
      "startid": 370818375,
      "endid": 370818493
    },
    {
      "id": 2447,
      "name": "Hipswell Highway / Binley Rd => Binley Rd / Bromleigh Drive",
      "length": 0.007305056129832307,
      "speed": {
        "0:00": 30
      },
      "startid": 370818493,
      "endid": 370818360
    },
    {
      "id": 2448,
      "name": "Binley Rd / Bromleigh Drive => Binley Rd / Uxbridge Avenue",
      "length": 0.001940932984416144,
      "speed": {
        "0:00": 30
      },
      "startid": 370818360,
      "endid": 370818356
    },
    {
      "id": 2449,
      "name": "Binley Rd / Uxbridge Avenue => Binley Rd / Uxbridge Avenue",
      "length": 0.0016673498283206552,
      "speed": {
        "0:00": 30
      },
      "startid": 370818356,
      "endid": 370818357
    },
    {
      "id": 2450,
      "name": "Binley Rd / Uxbridge Avenue => Binley Rd / Raleigh Rd",
      "length": 0.002453510279171192,
      "speed": {
        "0:00": 30
      },
      "startid": 370818357,
      "endid": 370818354
    },
    {
      "id": 2451,
      "name": "Binley Rd / Raleigh Rd => Binley Rd / Raleigh Rd",
      "length": 0.00018749146647080057,
      "speed": {
        "0:00": 30
      },
      "startid": 370818354,
      "endid": 370818353
    },
    {
      "id": 2452,
      "name": "Binley Rd / Raleigh Rd => Binley Rd / Bulls Head Lane",
      "length": 0.004474147677491692,
      "speed": {
        "0:00": 30
      },
      "startid": 370818353,
      "endid": 370818335
    },
    {
      "id": 2453,
      "name": "Binley Rd / Bulls Head Lane => Binley Rd / Bulls Head Lane",
      "length": 0.00028935241488505436,
      "speed": {
        "0:00": 30
      },
      "startid": 370818335,
      "endid": 370818334
    },
    {
      "id": 2454,
      "name": "Binley Rd / Bulls Head Lane => Binley Rd / Kingsway",
      "length": 0.00749600886939167,
      "speed": {
        "0:00": 30
      },
      "startid": 370818334,
      "endid": 370818333
    },
    {
      "id": 2455,
      "name": "Binley Rd / Kingsway => Binley Rd / Kingsway",
      "length": 0.00018105593058337426,
      "speed": {
        "0:00": 30
      },
      "startid": 370818333,
      "endid": 370818331
    },
    {
      "id": 2456,
      "name": "Binley Rd / Kingsway => Far Gosford St / Gosford Green",
      "length": 0.007543255666488108,
      "speed": {
        "0:00": 30
      },
      "startid": 370818331,
      "endid": 4815880406
    },
    {
      "id": 2457,
      "name": "Far Gosford St / Gosford Green => Far Gosford St / Bramble St",
      "length": 0.004033183017171992,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880406,
      "endid": 4815880407
    },
    {
      "id": 2458,
      "name": "T => BS7",
      "length": 0.004741096164390558,
      "speed": {
        "0:00": 30
      },
      "startid": 370817752,
      "endid": 7620250858
    },
    {
      "id": 2459,
      "name": "BS7 => BS3",
      "length": 0.00013405539899585386,
      "speed": {
        "0:00": 30
      },
      "startid": 7620250858,
      "endid": 370817695
    },
    {
      "id": 2460,
      "name": "BS3 => CS1",
      "length": 0.0029627712466539736,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 370817698
    },
    {
      "id": 2461,
      "name": "CS1 => CS4",
      "length": 0.00019329627518438407,
      "speed": {
        "0:00": 30
      },
      "startid": 370817698,
      "endid": 370817702
    },
    {
      "id": 2462,
      "name": "CS4 => VR3",
      "length": 0.002391225267514317,
      "speed": {
        "0:00": 30
      },
      "startid": 370817702,
      "endid": 370817718
    },
    {
      "id": 2463,
      "name": "VR3 => Butts Radial Link / Albany Rd",
      "length": 0.005936819708395398,
      "speed": {
        "0:00": 30
      },
      "startid": 370817718,
      "endid": 370817816
    },
    {
      "id": 2464,
      "name": "Butts Radial Link / Albany Rd => Butts Radial Link / Albany Rd",
      "length": 0.0017027777688234339,
      "speed": {
        "0:00": 30
      },
      "startid": 370817816,
      "endid": 370817814
    },
    {
      "id": 2465,
      "name": "Butts Radial Link / Albany Rd => CR4",
      "length": 0.006404540102146532,
      "speed": {
        "0:00": 30
      },
      "startid": 370817814,
      "endid": 370817813
    },
    {
      "id": 2466,
      "name": "CR4 => Spon End / The Arches",
      "length": 0.010638475949589828,
      "speed": {
        "0:00": 30
      },
      "startid": 370817813,
      "endid": 370818021
    },
    {
      "id": 2467,
      "name": "Spon End / The Arches => Spon End / The Arches",
      "length": 0.00015506108474010497,
      "speed": {
        "0:00": 30
      },
      "startid": 370818021,
      "endid": 370818019
    },
    {
      "id": 2468,
      "name": "Spon End / The Arches => UW1",
      "length": 0.045555557398520706,
      "speed": {
        "0:00": 30
      },
      "startid": 370818019,
      "endid": 3731158223
    },
    {
      "id": 2469,
      "name": "UW1 => Charter Ave / Mitchell Ave",
      "length": 0.01398854458655519,
      "speed": {
        "0:00": 30
      },
      "startid": 3731158223,
      "endid": 370817985
    },
    {
      "id": 2470,
      "name": "Charter Ave / Mitchell Ave => Charter Ave / John Rous Ave",
      "length": 0.0035931093401127476,
      "speed": {
        "0:00": 30
      },
      "startid": 370817985,
      "endid": 370817982
    },
    {
      "id": 2471,
      "name": "Charter Ave / John Rous Ave => Charter Ave / Sheriff Avenue",
      "length": 0.0021886123114886994,
      "speed": {
        "0:00": 30
      },
      "startid": 370817982,
      "endid": 370819684
    },
    {
      "id": 2472,
      "name": "Charter Ave / Sheriff Avenue => Charter Ave / Northfolk Terrace",
      "length": 0.0023981234768036728,
      "speed": {
        "0:00": 30
      },
      "startid": 370819684,
      "endid": 370817974
    },
    {
      "id": 2473,
      "name": "Charter Ave / Northfolk Terrace => Charter Ave / Freeburn Causeway",
      "length": 0.0037046316861463384,
      "speed": {
        "0:00": 30
      },
      "startid": 370817974,
      "endid": 370817969
    },
    {
      "id": 2474,
      "name": "Charter Ave / Freeburn Causeway => Kirby Corner Rd / Lynchgate Rd",
      "length": 0.0010876794564562144,
      "speed": {
        "0:00": 30
      },
      "startid": 370817969,
      "endid": 370817927
    },
    {
      "id": 2475,
      "name": "Kirby Corner Rd / Lynchgate Rd => Kirby Corner Rd / University Westwood Site",
      "length": 0.005740582536643942,
      "speed": {
        "0:00": 30
      },
      "startid": 370817927,
      "endid": 370817931
    },
    {
      "id": 2476,
      "name": "Kirby Corner Rd / University Westwood Site => Kirby Corner Rd / Gibbet Hill Rd",
      "length": 0.004738827116489978,
      "speed": {
        "0:00": 30
      },
      "startid": 370817931,
      "endid": 370819749
    },
    {
      "id": 2477,
      "name": "Kirby Corner Rd / Gibbet Hill Rd => GH1",
      "length": 0.0011167891878107667,
      "speed": {
        "0:00": 30
      },
      "startid": 370819749,
      "endid": 370817946
    },
    {
      "id": 2478,
      "name": "GH1 => Gibbet Hill Rd / Scarman Rd",
      "length": 0.0030671319844435773,
      "speed": {
        "0:00": 30
      },
      "startid": 370817946,
      "endid": 3731548192
    },
    {
      "id": 2479,
      "name": "Gibbet Hill Rd / Scarman Rd => Lynchgate Rd / Leeming Close",
      "length": 0.0098869213979884,
      "speed": {
        "0:00": 30
      },
      "startid": 3731548192,
      "endid": 370819152
    },
    {
      "id": 2480,
      "name": "Lynchgate Rd / Leeming Close => De Montfort Way / Cannon Park Shops",
      "length": 0.0023546683949164826,
      "speed": {
        "0:00": 30
      },
      "startid": 370819152,
      "endid": 370817920
    },
    {
      "id": 2481,
      "name": "De Montfort Way / Cannon Park Shops => Gibbet Hill Rd / Kirby Corner Rd",
      "length": 0.01392790865026104,
      "speed": {
        "0:00": 30
      },
      "startid": 370817920,
      "endid": 370817948
    },
    {
      "id": 2482,
      "name": "Gibbet Hill Rd / Kirby Corner Rd => Gibbet Hill Rd / Scarman Rd",
      "length": 0.0019545614597666463,
      "speed": {
        "0:00": 30
      },
      "startid": 370817948,
      "endid": 3731548201
    },
    {
      "id": 2483,
      "name": "Gibbet Hill Rd / Scarman Rd => Mitchell Avenue / Westwood School",
      "length": 0.0074904427752993585,
      "speed": {
        "0:00": 30
      },
      "startid": 3731548201,
      "endid": 370819688
    },
    {
      "id": 2484,
      "name": "Mitchell Avenue / Westwood School => Charter Ave / Ten Shilling Wood",
      "length": 0.004217384651650882,
      "speed": {
        "0:00": 30
      },
      "startid": 370819688,
      "endid": 370817987
    },
    {
      "id": 2485,
      "name": "Charter Ave / Ten Shilling Wood => Charter Ave / Ten Shilling Wood",
      "length": 0.0008599757264015652,
      "speed": {
        "0:00": 30
      },
      "startid": 370817987,
      "endid": 370817986
    },
    {
      "id": 2486,
      "name": "Charter Ave / Ten Shilling Wood => Charter Ave / Wolfe Rd",
      "length": 0.0024701140398776956,
      "speed": {
        "0:00": 30
      },
      "startid": 370817986,
      "endid": 370817991
    },
    {
      "id": 2487,
      "name": "Charter Ave / Wolfe Rd => Charter Ave / Wolfe Rd",
      "length": 0.00106623742665507,
      "speed": {
        "0:00": 30
      },
      "startid": 370817991,
      "endid": 370817990
    },
    {
      "id": 2488,
      "name": "Charter Ave / Wolfe Rd => Charter Ave / Marler Rd",
      "length": 0.002026663484646584,
      "speed": {
        "0:00": 30
      },
      "startid": 370817990,
      "endid": 370817996
    },
    {
      "id": 2489,
      "name": "Charter Ave / Marler Rd => Charter Ave / Marler Rd",
      "length": 0.0005352118552501463,
      "speed": {
        "0:00": 30
      },
      "startid": 370817996,
      "endid": 370817994
    },
    {
      "id": 2490,
      "name": "Charter Ave / Marler Rd => Charter Ave / Warren Green",
      "length": 0.0027842320090105534,
      "speed": {
        "0:00": 30
      },
      "startid": 370817994,
      "endid": 370817997
    },
    {
      "id": 2491,
      "name": "Charter Ave / Warren Green => Charter Ave / Warren Green",
      "length": 0.0006786605115951983,
      "speed": {
        "0:00": 30
      },
      "startid": 370817997,
      "endid": 370817999
    },
    {
      "id": 2492,
      "name": "Charter Ave / Warren Green => Charter Ave / Bradney Green",
      "length": 0.003230744570528456,
      "speed": {
        "0:00": 30
      },
      "startid": 370817999,
      "endid": 370818003
    },
    {
      "id": 2493,
      "name": "Charter Ave / Bradney Green => Charter Ave / Bradney Green",
      "length": 0.0007407507813021757,
      "speed": {
        "0:00": 30
      },
      "startid": 370818003,
      "endid": 370818000
    },
    {
      "id": 2494,
      "name": "Charter Ave / Bradney Green => Charter Ave / Marina Close",
      "length": 0.003515984955883761,
      "speed": {
        "0:00": 30
      },
      "startid": 370818000,
      "endid": 370818006
    },
    {
      "id": 2495,
      "name": "Charter Ave / Marina Close => Charter Ave / Marina Close",
      "length": 0.0005919281206352491,
      "speed": {
        "0:00": 30
      },
      "startid": 370818006,
      "endid": 370818005
    },
    {
      "id": 2496,
      "name": "Charter Ave / Marina Close => Charter Ave / Dalmeny Rd",
      "length": 0.005004857269692999,
      "speed": {
        "0:00": 30
      },
      "startid": 370818005,
      "endid": 370818017
    },
    {
      "id": 2497,
      "name": "Charter Ave / Dalmeny Rd => Charter Ave / Dalmeny Rd",
      "length": 0.0014327701281086536,
      "speed": {
        "0:00": 30
      },
      "startid": 370818017,
      "endid": 370818016
    },
    {
      "id": 2498,
      "name": "Charter Ave / Dalmeny Rd => Cromwell Lane / Tile Hill Rail Station",
      "length": 0.0009517469253945578,
      "speed": {
        "0:00": 30
      },
      "startid": 370818016,
      "endid": 370818008
    },
    {
      "id": 2499,
      "name": "Cromwell Lane / Tile Hill Rail Station => Cromwell Lane / Tile Hill Rail Station",
      "length": 0.00012686378521843434,
      "speed": {
        "0:00": 30
      },
      "startid": 370818008,
      "endid": 370818007
    },
    {
      "id": 2500,
      "name": "Cromwell Lane / Tile Hill Rail Station => Station Ave / Torrington Ave",
      "length": 0.004016656974401514,
      "speed": {
        "0:00": 30
      },
      "startid": 370818007,
      "endid": 4316311353
    },
    {
      "id": 2501,
      "name": "Station Ave / Torrington Ave => Station Ave / Torrington Ave",
      "length": 0.0008643032858886586,
      "speed": {
        "0:00": 30
      },
      "startid": 4316311353,
      "endid": 4316311354
    },
    {
      "id": 2502,
      "name": "Station Ave / Torrington Ave => Station Ave / Tanners Lane",
      "length": 0.0018260085980142168,
      "speed": {
        "0:00": 30
      },
      "startid": 4316311354,
      "endid": 370819332
    },
    {
      "id": 2503,
      "name": "Station Ave / Tanners Lane => Station Ave / Tanners Lane",
      "length": 0.00027278372385249316,
      "speed": {
        "0:00": 30
      },
      "startid": 370819332,
      "endid": 370819331
    },
    {
      "id": 2504,
      "name": "Station Ave / Tanners Lane => Banner Lane / Tile Hill Lane",
      "length": 0.0012298394204141845,
      "speed": {
        "0:00": 30
      },
      "startid": 370819331,
      "endid": 370819318
    },
    {
      "id": 2505,
      "name": "Banner Lane / Tile Hill Lane => Banner Lane / Tile Hill Lane",
      "length": 0.00017872585151608396,
      "speed": {
        "0:00": 30
      },
      "startid": 370819318,
      "endid": 370819314
    },
    {
      "id": 2506,
      "name": "Banner Lane / Tile Hill Lane => Banner Lane / Goodman Way",
      "length": 0.0017725446933755864,
      "speed": {
        "0:00": 30
      },
      "startid": 370819314,
      "endid": 4815875261
    },
    {
      "id": 2507,
      "name": "Banner Lane / Goodman Way => Banner Lane / Wickman'S",
      "length": 0.0030061455353952585,
      "speed": {
        "0:00": 30
      },
      "startid": 4815875261,
      "endid": 370819324
    },
    {
      "id": 2508,
      "name": "Banner Lane / Wickman'S => Banner Lane / Wickman'S",
      "length": 0.00040896483956532486,
      "speed": {
        "0:00": 30
      },
      "startid": 370819324,
      "endid": 370819325
    },
    {
      "id": 2509,
      "name": "Banner Lane / Wickman'S => Banner Lane / Bannerbrook Park",
      "length": 0.002976322712675995,
      "speed": {
        "0:00": 30
      },
      "startid": 370819325,
      "endid": 370819326
    },
    {
      "id": 2510,
      "name": "Banner Lane / Bannerbrook Park => Banner Lane / Bannerbrook Park",
      "length": 0.0003876625465527169,
      "speed": {
        "0:00": 30
      },
      "startid": 370819326,
      "endid": 370819328
    },
    {
      "id": 2511,
      "name": "Banner Lane / Bannerbrook Park => Banner Lane / Astoria Drive",
      "length": 0.00168801791459928,
      "speed": {
        "0:00": 30
      },
      "startid": 370819328,
      "endid": 370819330
    },
    {
      "id": 2512,
      "name": "Banner Lane / Astoria Drive => Banner Lane / Astoria Drive",
      "length": 0.0007953226074998468,
      "speed": {
        "0:00": 30
      },
      "startid": 370819330,
      "endid": 370819329
    },
    {
      "id": 2513,
      "name": "Banner Lane / Astoria Drive => Banner Lane / Broad Lane",
      "length": 0.0007634622321989104,
      "speed": {
        "0:00": 30
      },
      "startid": 370819329,
      "endid": 370819696
    },
    {
      "id": 2514,
      "name": "Banner Lane / Broad Lane => Banner Lane / Broad Lane",
      "length": 0.0007271705439559529,
      "speed": {
        "0:00": 30
      },
      "startid": 370819696,
      "endid": 370819695
    },
    {
      "id": 2515,
      "name": "Banner Lane / Broad Lane => Broad Lane / Farcroft Ave",
      "length": 0.0021461271747037418,
      "speed": {
        "0:00": 30
      },
      "startid": 370819695,
      "endid": 370818270
    },
    {
      "id": 2516,
      "name": "Broad Lane / Farcroft Ave => Farcroft Avenue / Sutton Avenue",
      "length": 0.0029054398978469492,
      "speed": {
        "0:00": 30
      },
      "startid": 370818270,
      "endid": 370819349
    },
    {
      "id": 2517,
      "name": "Farcroft Avenue / Sutton Avenue => Farcroft Avenue / Sutton Avenue",
      "length": 0.00014376327764693898,
      "speed": {
        "0:00": 30
      },
      "startid": 370819349,
      "endid": 370819348
    },
    {
      "id": 2518,
      "name": "Farcroft Avenue / Sutton Avenue => Sutton Ave / Thornton Close",
      "length": 0.00424373134045958,
      "speed": {
        "0:00": 30
      },
      "startid": 370819348,
      "endid": 620104224
    },
    {
      "id": 2519,
      "name": "Sutton Ave / Thornton Close => Sutton Ave / Thornton Close",
      "length": 0.00071690806244641,
      "speed": {
        "0:00": 30
      },
      "startid": 620104224,
      "endid": 620104226
    },
    {
      "id": 2520,
      "name": "Sutton Ave / Thornton Close => Sutton Ave / Hockley Lane",
      "length": 0.00260199004610002,
      "speed": {
        "0:00": 30
      },
      "startid": 620104226,
      "endid": 2193151733
    },
    {
      "id": 2521,
      "name": "Sutton Ave / Hockley Lane => Sutton Ave / Hockley Lane",
      "length": 0.00007676099269520049,
      "speed": {
        "0:00": 30
      },
      "startid": 2193151733,
      "endid": 4739802319
    },
    {
      "id": 2522,
      "name": "Sutton Ave / Hockley Lane => Hockley Lane / Church Lane",
      "length": 0.001552779459550233,
      "speed": {
        "0:00": 30
      },
      "startid": 4739802319,
      "endid": 370818277
    },
    {
      "id": 2523,
      "name": "Hockley Lane / Church Lane => Hockley Lane / Church Lane",
      "length": 0.00017256210476256428,
      "speed": {
        "0:00": 30
      },
      "startid": 370818277,
      "endid": 370819306
    },
    {
      "id": 2524,
      "name": "Hockley Lane / Church Lane => Upper Eastern Green Lane / Despard Rd",
      "length": 0.004857525708629854,
      "speed": {
        "0:00": 30
      },
      "startid": 370819306,
      "endid": 370818276
    },
    {
      "id": 2525,
      "name": "Upper Eastern Green Lane / Despard Rd => Upper Eastern Green Lane / Despard Rd",
      "length": 0.0007005742216212578,
      "speed": {
        "0:00": 30
      },
      "startid": 370818276,
      "endid": 370818275
    },
    {
      "id": 2526,
      "name": "Upper Eastern Green Lane / Despard Rd => Upper Eastern Green Lane / Rose Cottage Flats",
      "length": 0.003395288411902089,
      "speed": {
        "0:00": 30
      },
      "startid": 370818275,
      "endid": 370819819
    },
    {
      "id": 2527,
      "name": "Upper Eastern Green Lane / Rose Cottage Flats => Upper Eastern Green Lane / Rose Cottage Flats",
      "length": 0.0005537920187228133,
      "speed": {
        "0:00": 30
      },
      "startid": 370819819,
      "endid": 370819818
    },
    {
      "id": 2528,
      "name": "Upper Eastern Green Lane / Rose Cottage Flats => Upper Eastern Green Lane / Sutton Ave",
      "length": 0.004149694159815196,
      "speed": {
        "0:00": 30
      },
      "startid": 370819818,
      "endid": 370818272
    },
    {
      "id": 2529,
      "name": "Upper Eastern Green Lane / Sutton Ave => Upper Eastern Green Lane / Sutton Avenue",
      "length": 0.00040788549863907754,
      "speed": {
        "0:00": 30
      },
      "startid": 370818272,
      "endid": 370818274
    },
    {
      "id": 2530,
      "name": "Upper Eastern Green Lane / Sutton Avenue => Upper Eastern Green Lane / Windermere Ave",
      "length": 0.0020916863268663818,
      "speed": {
        "0:00": 30
      },
      "startid": 370818274,
      "endid": 370818223
    },
    {
      "id": 2531,
      "name": "Upper Eastern Green Lane / Windermere Ave => Upper Eastern Green Lane / Windermere Ave",
      "length": 0.0011930800853253434,
      "speed": {
        "0:00": 30
      },
      "startid": 370818223,
      "endid": 370818225
    },
    {
      "id": 2532,
      "name": "Upper Eastern Green Lane / Windermere Ave => Lower Eastern Green Lane / Alspath Lane",
      "length": 0.003735028149827388,
      "speed": {
        "0:00": 30
      },
      "startid": 370818225,
      "endid": 370818221
    },
    {
      "id": 2533,
      "name": "Lower Eastern Green Lane / Alspath Lane => Lower Eastern Green Lane / Alspath Lane",
      "length": 0.0009069872876719378,
      "speed": {
        "0:00": 30
      },
      "startid": 370818221,
      "endid": 370818222
    },
    {
      "id": 2534,
      "name": "Lower Eastern Green Lane / Alspath Lane => Lower Eastern Green Lane / Sutherland Ave",
      "length": 0.004146427779427151,
      "speed": {
        "0:00": 30
      },
      "startid": 370818222,
      "endid": 370819775
    },
    {
      "id": 2535,
      "name": "Lower Eastern Green Lane / Sutherland Ave => Alderminister Rd / Caithness Close",
      "length": 0.0024882131942419936,
      "speed": {
        "0:00": 30
      },
      "startid": 370819775,
      "endid": 370818220
    },
    {
      "id": 2536,
      "name": "Alderminister Rd / Caithness Close => Alderminister Rd / Caithness Close",
      "length": 0.00020121158018548583,
      "speed": {
        "0:00": 30
      },
      "startid": 370818220,
      "endid": 370818218
    },
    {
      "id": 2537,
      "name": "Alderminister Rd / Caithness Close => Alderminister Rd / Ladbrook Rd",
      "length": 0.0022172149580059397,
      "speed": {
        "0:00": 30
      },
      "startid": 370818218,
      "endid": 370819310
    },
    {
      "id": 2538,
      "name": "Alderminister Rd / Ladbrook Rd => Alderminister Rd / Ladbrook Rd",
      "length": 0.00018898238012798993,
      "speed": {
        "0:00": 30
      },
      "startid": 370819310,
      "endid": 370819311
    },
    {
      "id": 2539,
      "name": "Alderminister Rd / Ladbrook Rd => Alderminister Rd / Wilmcote Green Shops",
      "length": 0.0025165763270770065,
      "speed": {
        "0:00": 30
      },
      "startid": 370819311,
      "endid": 370818216
    },
    {
      "id": 2540,
      "name": "Alderminister Rd / Wilmcote Green Shops => Alderminister Rd / Wilmcote Green Shops",
      "length": 0.0006658693039946445,
      "speed": {
        "0:00": 30
      },
      "startid": 370818216,
      "endid": 370818214
    },
    {
      "id": 2541,
      "name": "Alderminister Rd / Wilmcote Green Shops => Alderminster Rd / Broad Lane",
      "length": 0.0023346361365305206,
      "speed": {
        "0:00": 30
      },
      "startid": 370818214,
      "endid": 370819774
    },
    {
      "id": 2542,
      "name": "Alderminster Rd / Broad Lane => Broad Lane / Alderminster Rd",
      "length": 0.0009849793500381705,
      "speed": {
        "0:00": 30
      },
      "startid": 370819774,
      "endid": 370818212
    },
    {
      "id": 2543,
      "name": "Broad Lane / Alderminster Rd => Broad Lane / Larch Tree Avenue",
      "length": 0.0021181322645202542,
      "speed": {
        "0:00": 30
      },
      "startid": 370818212,
      "endid": 370818210
    },
    {
      "id": 2544,
      "name": "Broad Lane / Larch Tree Avenue => Broad Lane / Larch Tree Avenue",
      "length": 0.0006163794042631228,
      "speed": {
        "0:00": 30
      },
      "startid": 370818210,
      "endid": 370818208
    },
    {
      "id": 2545,
      "name": "Broad Lane / Larch Tree Avenue => Broad Lane / Beech Tree Avenue",
      "length": 0.004840212044942724,
      "speed": {
        "0:00": 30
      },
      "startid": 370818208,
      "endid": 370818207
    },
    {
      "id": 2546,
      "name": "Broad Lane / Beech Tree Avenue => Broad Lane / Beech Tree Avenue",
      "length": 0.000665227058980418,
      "speed": {
        "0:00": 30
      },
      "startid": 370818207,
      "endid": 370818205
    },
    {
      "id": 2547,
      "name": "Broad Lane / Beech Tree Avenue => Broad Lane / Fletchamstead Highway",
      "length": 0.003723866176435228,
      "speed": {
        "0:00": 30
      },
      "startid": 370818205,
      "endid": 370818261
    },
    {
      "id": 2548,
      "name": "Broad Lane / Fletchamstead Highway => Broad Lane / Fletchamstead Highway",
      "length": 0.0011147375296455522,
      "speed": {
        "0:00": 30
      },
      "startid": 370818261,
      "endid": 370818259
    },
    {
      "id": 2549,
      "name": "Broad Lane / Fletchamstead Highway => Broad Lane / Wildcroft Rd",
      "length": 0.0035492343878633275,
      "speed": {
        "0:00": 30
      },
      "startid": 370818259,
      "endid": 370818167
    },
    {
      "id": 2550,
      "name": "Broad Lane / Wildcroft Rd => Wildcroft Rd / Broad Lane",
      "length": 0.0014280172617981506,
      "speed": {
        "0:00": 30
      },
      "startid": 370818167,
      "endid": 370819770
    },
    {
      "id": 2551,
      "name": "Wildcroft Rd / Broad Lane => Wildcroft Rd / Broad Lane",
      "length": 0.00019888169850283384,
      "speed": {
        "0:00": 30
      },
      "startid": 370819770,
      "endid": 370819771
    },
    {
      "id": 2552,
      "name": "Wildcroft Rd / Broad Lane => Wildcroft Rd / Gorseway",
      "length": 0.0016811075069690657,
      "speed": {
        "0:00": 30
      },
      "startid": 370819771,
      "endid": 370818149
    },
    {
      "id": 2553,
      "name": "Wildcroft Rd / Gorseway => Wildcroft Rd / Gorseway",
      "length": 0.00012721874861883027,
      "speed": {
        "0:00": 30
      },
      "startid": 370818149,
      "endid": 370818146
    },
    {
      "id": 2554,
      "name": "Wildcroft Rd / Gorseway => Lyndale Rd / Overdale Rd",
      "length": 0.0019218129825758785,
      "speed": {
        "0:00": 30
      },
      "startid": 370818146,
      "endid": 370819393
    },
    {
      "id": 2555,
      "name": "Lyndale Rd / Overdale Rd => Lyndale Rd / Overdale Rd",
      "length": 0.00021870715580570176,
      "speed": {
        "0:00": 30
      },
      "startid": 370819393,
      "endid": 370819394
    },
    {
      "id": 2556,
      "name": "Lyndale Rd / Overdale Rd => Whoberley Ave / Glendower Avenue",
      "length": 0.002571174939594763,
      "speed": {
        "0:00": 30
      },
      "startid": 370819394,
      "endid": 370818129
    },
    {
      "id": 2557,
      "name": "Whoberley Ave / Glendower Avenue => Whoberley Ave / Glendower Avenue",
      "length": 0.0006794678064488404,
      "speed": {
        "0:00": 30
      },
      "startid": 370818129,
      "endid": 370818133
    },
    {
      "id": 2558,
      "name": "Whoberley Ave / Glendower Avenue => Whoberley Ave / Billing Rd",
      "length": 0.001851570976227236,
      "speed": {
        "0:00": 30
      },
      "startid": 370818133,
      "endid": 370819416
    },
    {
      "id": 2559,
      "name": "Whoberley Ave / Billing Rd => Whoberley Ave / Billing Rd",
      "length": 0.0011712777168545756,
      "speed": {
        "0:00": 30
      },
      "startid": 370819416,
      "endid": 370819417
    },
    {
      "id": 2560,
      "name": "Whoberley Ave / Billing Rd => Whoberley Ave / Maudslay Rd",
      "length": 0.0014291600785080903,
      "speed": {
        "0:00": 30
      },
      "startid": 370819417,
      "endid": 370818142
    },
    {
      "id": 2561,
      "name": "Whoberley Ave / Maudslay Rd => Whoberley Ave / Maudslay Rd",
      "length": 0.0004539339269086163,
      "speed": {
        "0:00": 30
      },
      "startid": 370818142,
      "endid": 370818145
    },
    {
      "id": 2562,
      "name": "Whoberley Ave / Maudslay Rd => Maudslay Rd / Madeira Croft",
      "length": 0.0030242215064378436,
      "speed": {
        "0:00": 30
      },
      "startid": 370818145,
      "endid": 370818138
    },
    {
      "id": 2563,
      "name": "Maudslay Rd / Madeira Croft => Maudslay Rd / Madeira Croft",
      "length": 0.0003836421509692122,
      "speed": {
        "0:00": 30
      },
      "startid": 370818138,
      "endid": 370818140
    },
    {
      "id": 2564,
      "name": "Maudslay Rd / Madeira Croft => Maudslay Rd / Allesley Old Rd",
      "length": 0.0034464744087232065,
      "speed": {
        "0:00": 30
      },
      "startid": 370818140,
      "endid": 370819777
    },
    {
      "id": 2565,
      "name": "Maudslay Rd / Allesley Old Rd => Maudslay Rd / Allesley Old Rd",
      "length": 0.0003354752002761886,
      "speed": {
        "0:00": 30
      },
      "startid": 370819777,
      "endid": 370819778
    },
    {
      "id": 2566,
      "name": "Maudslay Rd / Allesley Old Rd => Allesley Old Rd / Mount St",
      "length": 0.004301136605596423,
      "speed": {
        "0:00": 30
      },
      "startid": 370819778,
      "endid": 370818030
    },
    {
      "id": 2567,
      "name": "Allesley Old Rd / Mount St => Allesley Old Rd / Mount St",
      "length": 0.00045158033615286605,
      "speed": {
        "0:00": 30
      },
      "startid": 370818030,
      "endid": 370818029
    },
    {
      "id": 2568,
      "name": "Allesley Old Rd / Mount St => Allesley Old Rd / Craven St",
      "length": 0.0034322825597551234,
      "speed": {
        "0:00": 30
      },
      "startid": 370818029,
      "endid": 370818027
    },
    {
      "id": 2569,
      "name": "Allesley Old Rd / Craven St => Allesley Old Rd / Craven St",
      "length": 0.0005056624368094169,
      "speed": {
        "0:00": 30
      },
      "startid": 370818027,
      "endid": 370818026
    },
    {
      "id": 2570,
      "name": "T => BS7",
      "length": 0.004741096164390558,
      "speed": {
        "0:00": 30
      },
      "startid": 370817752,
      "endid": 7620250858
    },
    {
      "id": 2571,
      "name": "BS7 => CS1",
      "length": 0.0030421205712464617,
      "speed": {
        "0:00": 30
      },
      "startid": 7620250858,
      "endid": 370817698
    },
    {
      "id": 2572,
      "name": "CS1 => Butts Radial Link / Albany Rd",
      "length": 0.009523948349817077,
      "speed": {
        "0:00": 30
      },
      "startid": 370817698,
      "endid": 370817814
    },
    {
      "id": 2573,
      "name": "Butts Radial Link / Albany Rd => CR4",
      "length": 0.006404540102146532,
      "speed": {
        "0:00": 30
      },
      "startid": 370817814,
      "endid": 370817813
    },
    {
      "id": 2574,
      "name": "CR4 => Spon End / The Arches",
      "length": 0.010707072778775164,
      "speed": {
        "0:00": 30
      },
      "startid": 370817813,
      "endid": 370818019
    },
    {
      "id": 2575,
      "name": "Spon End / The Arches => Charter Ave / Mitchell Ave",
      "length": 0.044403558087386344,
      "speed": {
        "0:00": 30
      },
      "startid": 370818019,
      "endid": 370817985
    },
    {
      "id": 2576,
      "name": "Charter Ave / Mitchell Ave => Charter Ave / John Rous Ave",
      "length": 0.0035931093401127476,
      "speed": {
        "0:00": 30
      },
      "startid": 370817985,
      "endid": 370817982
    },
    {
      "id": 2577,
      "name": "Charter Ave / John Rous Ave => Charter Ave / Sheriff Avenue",
      "length": 0.0021886123114886994,
      "speed": {
        "0:00": 30
      },
      "startid": 370817982,
      "endid": 370819684
    },
    {
      "id": 2578,
      "name": "Charter Ave / Sheriff Avenue => Charter Ave / Northfolk Terrace",
      "length": 0.0023981234768036728,
      "speed": {
        "0:00": 30
      },
      "startid": 370819684,
      "endid": 370817974
    },
    {
      "id": 2579,
      "name": "Charter Ave / Northfolk Terrace => Charter Ave / Freeburn Causeway",
      "length": 0.0037046316861463384,
      "speed": {
        "0:00": 30
      },
      "startid": 370817974,
      "endid": 370817969
    },
    {
      "id": 2580,
      "name": "Charter Ave / Freeburn Causeway => Kirby Corner Rd / Lynchgate Rd",
      "length": 0.0010876794564562144,
      "speed": {
        "0:00": 30
      },
      "startid": 370817969,
      "endid": 370817927
    },
    {
      "id": 2581,
      "name": "Kirby Corner Rd / Lynchgate Rd => Kirby Corner Rd / University Westwood Site",
      "length": 0.005740582536643942,
      "speed": {
        "0:00": 30
      },
      "startid": 370817927,
      "endid": 370817931
    },
    {
      "id": 2582,
      "name": "Kirby Corner Rd / University Westwood Site => Kirby Corner Rd / Gibbet Hill Rd",
      "length": 0.004738827116489978,
      "speed": {
        "0:00": 30
      },
      "startid": 370817931,
      "endid": 370819749
    },
    {
      "id": 2583,
      "name": "Kirby Corner Rd / Gibbet Hill Rd => GH1",
      "length": 0.0011167891878107667,
      "speed": {
        "0:00": 30
      },
      "startid": 370819749,
      "endid": 370817946
    },
    {
      "id": 2584,
      "name": "GH1 => Gibbet Hill Rd / Scarman Rd",
      "length": 0.0030671319844435773,
      "speed": {
        "0:00": 30
      },
      "startid": 370817946,
      "endid": 3731548192
    },
    {
      "id": 2585,
      "name": "Gibbet Hill Rd / Scarman Rd => Charter Ave / Ten Shilling Wood",
      "length": 0.012963780752542897,
      "speed": {
        "0:00": 30
      },
      "startid": 3731548192,
      "endid": 370817987
    },
    {
      "id": 2586,
      "name": "Charter Ave / Ten Shilling Wood => Charter Ave / Wolfe Rd",
      "length": 0.003319566869337238,
      "speed": {
        "0:00": 30
      },
      "startid": 370817987,
      "endid": 370817991
    },
    {
      "id": 2587,
      "name": "Charter Ave / Wolfe Rd => Charter Ave / Marler Rd",
      "length": 0.003085185979807345,
      "speed": {
        "0:00": 30
      },
      "startid": 370817991,
      "endid": 370817996
    },
    {
      "id": 2588,
      "name": "Charter Ave / Marler Rd => Charter Ave / Warren Green",
      "length": 0.002650100424512346,
      "speed": {
        "0:00": 30
      },
      "startid": 370817996,
      "endid": 370817999
    },
    {
      "id": 2589,
      "name": "Charter Ave / Warren Green => Charter Ave / Bradney Green",
      "length": 0.003230744570528456,
      "speed": {
        "0:00": 30
      },
      "startid": 370817999,
      "endid": 370818003
    },
    {
      "id": 2590,
      "name": "Charter Ave / Bradney Green => Charter Ave / Marina Close",
      "length": 0.00425260104524283,
      "speed": {
        "0:00": 30
      },
      "startid": 370818003,
      "endid": 370818006
    },
    {
      "id": 2591,
      "name": "Charter Ave / Marina Close => Charter Ave / Dalmeny Rd",
      "length": 0.006988426101061683,
      "speed": {
        "0:00": 30
      },
      "startid": 370818006,
      "endid": 370818016
    },
    {
      "id": 2592,
      "name": "Charter Ave / Dalmeny Rd => Cromwell Lane / Tile Hill Rail Station",
      "length": 0.0009517469253945578,
      "speed": {
        "0:00": 30
      },
      "startid": 370818016,
      "endid": 370818008
    },
    {
      "id": 2593,
      "name": "Cromwell Lane / Tile Hill Rail Station => Station Ave / Torrington Ave",
      "length": 0.003986429501446275,
      "speed": {
        "0:00": 30
      },
      "startid": 370818008,
      "endid": 4316311353
    },
    {
      "id": 2594,
      "name": "Station Ave / Torrington Ave => Station Ave / Tanners Lane",
      "length": 0.00288363016526207,
      "speed": {
        "0:00": 30
      },
      "startid": 4316311353,
      "endid": 370819331
    },
    {
      "id": 2595,
      "name": "Station Ave / Tanners Lane => Banner Lane / Tile Hill Lane",
      "length": 0.0011733240174801795,
      "speed": {
        "0:00": 30
      },
      "startid": 370819331,
      "endid": 370819314
    },
    {
      "id": 2596,
      "name": "Banner Lane / Tile Hill Lane => Banner Lane / Wickman'S",
      "length": 0.004766785211229868,
      "speed": {
        "0:00": 30
      },
      "startid": 370819314,
      "endid": 370819324
    },
    {
      "id": 2597,
      "name": "Banner Lane / Wickman'S => Banner Lane / Bannerbrook Park",
      "length": 0.0031191799130561074,
      "speed": {
        "0:00": 30
      },
      "startid": 370819324,
      "endid": 370819326
    },
    {
      "id": 2598,
      "name": "Banner Lane / Bannerbrook Park => Banner Lane / Astoria Drive",
      "length": 0.0019966504576434283,
      "speed": {
        "0:00": 30
      },
      "startid": 370819326,
      "endid": 370819330
    },
    {
      "id": 2599,
      "name": "Banner Lane / Astoria Drive => Banner Lane / Broad Lane",
      "length": 0.0015019449290800263,
      "speed": {
        "0:00": 30
      },
      "startid": 370819330,
      "endid": 370819696
    },
    {
      "id": 2600,
      "name": "Banner Lane / Broad Lane => Broad Lane / Farcroft Ave",
      "length": 0.0020187236685602758,
      "speed": {
        "0:00": 30
      },
      "startid": 370819696,
      "endid": 370818270
    },
    {
      "id": 2601,
      "name": "Broad Lane / Farcroft Ave => Farcroft Avenue / Sutton Avenue",
      "length": 0.0030463066424761247,
      "speed": {
        "0:00": 30
      },
      "startid": 370818270,
      "endid": 370819348
    },
    {
      "id": 2602,
      "name": "Farcroft Avenue / Sutton Avenue => Sutton Ave / Thornton Close",
      "length": 0.004446161638986881,
      "speed": {
        "0:00": 30
      },
      "startid": 370819348,
      "endid": 620104226
    },
    {
      "id": 2603,
      "name": "Sutton Ave / Thornton Close => Sutton Ave / Hockley Lane",
      "length": 0.002599758859970464,
      "speed": {
        "0:00": 30
      },
      "startid": 620104226,
      "endid": 4739802319
    },
    {
      "id": 2604,
      "name": "Sutton Ave / Hockley Lane => Hockley Lane / Church Lane",
      "length": 0.001552779459550233,
      "speed": {
        "0:00": 30
      },
      "startid": 4739802319,
      "endid": 370818277
    },
    {
      "id": 2605,
      "name": "Hockley Lane / Church Lane => Upper Eastern Green Lane / Despard Rd",
      "length": 0.004717446017709008,
      "speed": {
        "0:00": 30
      },
      "startid": 370818277,
      "endid": 370818276
    },
    {
      "id": 2606,
      "name": "Upper Eastern Green Lane / Despard Rd => Upper Eastern Green Lane / Rose Cottage Flats",
      "length": 0.004092527360934541,
      "speed": {
        "0:00": 30
      },
      "startid": 370818276,
      "endid": 370819819
    },
    {
      "id": 2607,
      "name": "Upper Eastern Green Lane / Rose Cottage Flats => Upper Eastern Green Lane / Sutton Ave",
      "length": 0.0036026294091953638,
      "speed": {
        "0:00": 30
      },
      "startid": 370819819,
      "endid": 370818272
    },
    {
      "id": 2608,
      "name": "Upper Eastern Green Lane / Sutton Ave => Upper Eastern Green Lane / Windermere Ave",
      "length": 0.0036853627067087056,
      "speed": {
        "0:00": 30
      },
      "startid": 370818272,
      "endid": 370818225
    },
    {
      "id": 2609,
      "name": "Upper Eastern Green Lane / Windermere Ave => Lower Eastern Green Lane / Alspath Lane",
      "length": 0.003735028149827388,
      "speed": {
        "0:00": 30
      },
      "startid": 370818225,
      "endid": 370818221
    },
    {
      "id": 2610,
      "name": "Lower Eastern Green Lane / Alspath Lane => Lower Eastern Green Lane / Sutherland Ave",
      "length": 0.005053178331505746,
      "speed": {
        "0:00": 30
      },
      "startid": 370818221,
      "endid": 370819775
    },
    {
      "id": 2611,
      "name": "Lower Eastern Green Lane / Sutherland Ave => Alderminister Rd / Caithness Close",
      "length": 0.0024882131942419936,
      "speed": {
        "0:00": 30
      },
      "startid": 370819775,
      "endid": 370818220
    },
    {
      "id": 2612,
      "name": "Alderminister Rd / Caithness Close => Alderminister Rd / Ladbrook Rd",
      "length": 0.002119574799337777,
      "speed": {
        "0:00": 30
      },
      "startid": 370818220,
      "endid": 370819311
    },
    {
      "id": 2613,
      "name": "Alderminister Rd / Ladbrook Rd => Alderminister Rd / Wilmcote Green Shops",
      "length": 0.0025165763270770065,
      "speed": {
        "0:00": 30
      },
      "startid": 370819311,
      "endid": 370818216
    },
    {
      "id": 2614,
      "name": "Alderminister Rd / Wilmcote Green Shops => Alderminster Rd / Broad Lane",
      "length": 0.00296729793583255,
      "speed": {
        "0:00": 30
      },
      "startid": 370818216,
      "endid": 370819774
    },
    {
      "id": 2615,
      "name": "Alderminster Rd / Broad Lane => Broad Lane / Larch Tree Avenue",
      "length": 0.0030754263395513654,
      "speed": {
        "0:00": 30
      },
      "startid": 370819774,
      "endid": 370818210
    },
    {
      "id": 2616,
      "name": "Broad Lane / Larch Tree Avenue => Broad Lane / Beech Tree Avenue",
      "length": 0.005452730439880875,
      "speed": {
        "0:00": 30
      },
      "startid": 370818210,
      "endid": 370818207
    },
    {
      "id": 2617,
      "name": "Broad Lane / Beech Tree Avenue => Broad Lane / Fletchamstead Highway",
      "length": 0.004382425093483953,
      "speed": {
        "0:00": 30
      },
      "startid": 370818207,
      "endid": 370818261
    },
    {
      "id": 2618,
      "name": "Broad Lane / Fletchamstead Highway => Broad Lane / Wildcroft Rd",
      "length": 0.004654586033150057,
      "speed": {
        "0:00": 30
      },
      "startid": 370818261,
      "endid": 370818167
    },
    {
      "id": 2619,
      "name": "Broad Lane / Wildcroft Rd => Wildcroft Rd / Broad Lane",
      "length": 0.0014280172617981506,
      "speed": {
        "0:00": 30
      },
      "startid": 370818167,
      "endid": 370819770
    },
    {
      "id": 2620,
      "name": "Wildcroft Rd / Broad Lane => Wildcroft Rd / Gorseway",
      "length": 0.0015897495054305597,
      "speed": {
        "0:00": 30
      },
      "startid": 370819770,
      "endid": 370818146
    },
    {
      "id": 2621,
      "name": "Wildcroft Rd / Gorseway => Lyndale Rd / Overdale Rd",
      "length": 0.0019218129825758785,
      "speed": {
        "0:00": 30
      },
      "startid": 370818146,
      "endid": 370819393
    },
    {
      "id": 2622,
      "name": "Lyndale Rd / Overdale Rd => Whoberley Ave / Glendower Avenue",
      "length": 0.0027789651904981095,
      "speed": {
        "0:00": 30
      },
      "startid": 370819393,
      "endid": 370818129
    },
    {
      "id": 2623,
      "name": "Whoberley Ave / Glendower Avenue => Whoberley Ave / Billing Rd",
      "length": 0.002516172048968607,
      "speed": {
        "0:00": 30
      },
      "startid": 370818129,
      "endid": 370819416
    },
    {
      "id": 2624,
      "name": "Whoberley Ave / Billing Rd => Whoberley Ave / Maudslay Rd",
      "length": 0.002570380057501705,
      "speed": {
        "0:00": 30
      },
      "startid": 370819416,
      "endid": 370818142
    },
    {
      "id": 2625,
      "name": "Whoberley Ave / Maudslay Rd => Maudslay Rd / Madeira Croft",
      "length": 0.003478089534498876,
      "speed": {
        "0:00": 30
      },
      "startid": 370818142,
      "endid": 370818138
    },
    {
      "id": 2626,
      "name": "Maudslay Rd / Madeira Croft => Maudslay Rd / Allesley Old Rd",
      "length": 0.004117767737499354,
      "speed": {
        "0:00": 30
      },
      "startid": 370818138,
      "endid": 370819778
    },
    {
      "id": 2627,
      "name": "Maudslay Rd / Allesley Old Rd => Allesley Old Rd / Mount St",
      "length": 0.004301136605596423,
      "speed": {
        "0:00": 30
      },
      "startid": 370819778,
      "endid": 370818030
    },
    {
      "id": 2628,
      "name": "Allesley Old Rd / Mount St => Allesley Old Rd / Craven St",
      "length": 0.0038627273641821465,
      "speed": {
        "0:00": 30
      },
      "startid": 370818030,
      "endid": 370818027
    },
    {
      "id": 2629,
      "name": "Allesley Old Rd / Craven St => UW1",
      "length": 0.04246754209805522,
      "speed": {
        "0:00": 30
      },
      "startid": 370818027,
      "endid": 3731158223
    },
    {
      "id": 2630,
      "name": "E => UH3",
      "length": 0.06848654388454738,
      "speed": {
        "0:00": 30
      },
      "startid": 370817737,
      "endid": 370817649
    },
    {
      "id": 2631,
      "name": "UH3 => UH8",
      "length": 0.00019671697944123576,
      "speed": {
        "0:00": 30
      },
      "startid": 370817649,
      "endid": 4062225928
    },
    {
      "id": 2632,
      "name": "E => UH3",
      "length": 0.06848654388454738,
      "speed": {
        "0:00": 30
      },
      "startid": 370817737,
      "endid": 370817649
    },
    {
      "id": 2633,
      "name": "UH3 => UH8",
      "length": 0.00019671697944123576,
      "speed": {
        "0:00": 30
      },
      "startid": 370817649,
      "endid": 4062225928
    },
    {
      "id": 2634,
      "name": "Hillmorton Rd / Lillington Rd => Hillmorton Rd / Deedmore Rd",
      "length": 0.002628263769106573,
      "speed": {
        "0:00": 30
      },
      "startid": 370817624,
      "endid": 370819178
    },
    {
      "id": 2635,
      "name": "Hillmorton Rd / Deedmore Rd => Hillmorton Rd / Deedmore Rd",
      "length": 0.0001535305181388248,
      "speed": {
        "0:00": 30
      },
      "startid": 370819178,
      "endid": 370819180
    },
    {
      "id": 2636,
      "name": "Hillmorton Rd / Deedmore Rd => UH2",
      "length": 0.02970093417470276,
      "speed": {
        "0:00": 30
      },
      "startid": 370819180,
      "endid": 370817645
    },
    {
      "id": 2637,
      "name": "Birmingham Rd / Brickhill Lane => Birmingham Rd / Brickhill Lane",
      "length": 0.0006062756633735554,
      "speed": {
        "0:00": 30
      },
      "startid": 370819527,
      "endid": 370819530
    },
    {
      "id": 2638,
      "name": "Birmingham Rd / Brickhill Lane => Birmingham Rd / Windmill Farm",
      "length": 0.012881388064957972,
      "speed": {
        "0:00": 30
      },
      "startid": 370819530,
      "endid": 370819525
    },
    {
      "id": 2639,
      "name": "Birmingham Rd / Windmill Farm => Parkhill Dr / Parkhill Estate Terminus",
      "length": 0.008745833371377748,
      "speed": {
        "0:00": 30
      },
      "startid": 370819525,
      "endid": 370818229
    },
    {
      "id": 2640,
      "name": "Parkhill Dr / Parkhill Estate Terminus => Birmingham Rd / Neale Avenue",
      "length": 0.006306014482219508,
      "speed": {
        "0:00": 30
      },
      "startid": 370818229,
      "endid": 370819493
    },
    {
      "id": 2641,
      "name": "Birmingham Rd / Neale Avenue => Birmingham Rd / Neale Avenue",
      "length": 0.0014933214590289524,
      "speed": {
        "0:00": 30
      },
      "startid": 370819493,
      "endid": 370819494
    },
    {
      "id": 2642,
      "name": "Birmingham Rd / Neale Avenue => Birmingham Rd / Allesley Post Office",
      "length": 0.0015646175379312936,
      "speed": {
        "0:00": 30
      },
      "startid": 370819494,
      "endid": 370819489
    },
    {
      "id": 2643,
      "name": "Birmingham Rd / Allesley Post Office => Birmingham Rd / Allesley Post Office",
      "length": 0.0008820798716671872,
      "speed": {
        "0:00": 30
      },
      "startid": 370819489,
      "endid": 370819490
    },
    {
      "id": 2644,
      "name": "Birmingham Rd / Allesley Post Office => Birmingham Rd / Butchers Lane",
      "length": 0.002760424034455538,
      "speed": {
        "0:00": 30
      },
      "startid": 370819490,
      "endid": 370819486
    },
    {
      "id": 2645,
      "name": "Birmingham Rd / Butchers Lane => Birmingham Rd / Butchers Lane",
      "length": 0.002666668160832974,
      "speed": {
        "0:00": 30
      },
      "startid": 370819486,
      "endid": 370819484
    },
    {
      "id": 2646,
      "name": "Birmingham Rd / Butchers Lane => Birmingham Rd / Norton Grange",
      "length": 0.0032394266313661847,
      "speed": {
        "0:00": 30
      },
      "startid": 370819484,
      "endid": 370819481
    },
    {
      "id": 2647,
      "name": "Birmingham Rd / Norton Grange => Birmingham Rd / Norton Grange",
      "length": 0.00018735042033075414,
      "speed": {
        "0:00": 30
      },
      "startid": 370819481,
      "endid": 370819482
    },
    {
      "id": 2648,
      "name": "Birmingham Rd / Norton Grange => Holyhead Rd / Dulverton Avenue",
      "length": 0.005333658446132934,
      "speed": {
        "0:00": 30
      },
      "startid": 370819482,
      "endid": 370819479
    },
    {
      "id": 2649,
      "name": "Holyhead Rd / Dulverton Avenue => Holyhead Rd / Dulverton Avenue",
      "length": 0.0004808124894384671,
      "speed": {
        "0:00": 30
      },
      "startid": 370819479,
      "endid": 370819480
    },
    {
      "id": 2650,
      "name": "Holyhead Rd / Dulverton Avenue => Holyhead Rd / Grayswood Avenue",
      "length": 0.005298354314313946,
      "speed": {
        "0:00": 30
      },
      "startid": 370819480,
      "endid": 370819453
    },
    {
      "id": 2651,
      "name": "Holyhead Rd / Grayswood Avenue => Holyhead Rd / Grayswood Avenue",
      "length": 0.0015367593988653307,
      "speed": {
        "0:00": 30
      },
      "startid": 370819453,
      "endid": 370819454
    },
    {
      "id": 2652,
      "name": "Holyhead Rd / Grayswood Avenue => Holyhead Rd / Southbank Rd",
      "length": 0.0018399552304324976,
      "speed": {
        "0:00": 30
      },
      "startid": 370819454,
      "endid": 370819450
    },
    {
      "id": 2653,
      "name": "Holyhead Rd / Southbank Rd => Holyhead Rd / Southbank Rd",
      "length": 0.0020147104010257858,
      "speed": {
        "0:00": 30
      },
      "startid": 370819450,
      "endid": 370819452
    },
    {
      "id": 2654,
      "name": "Holyhead Rd / Southbank Rd => Holyhead Rd / Redesdale Avenue",
      "length": 0.0032341260334133653,
      "speed": {
        "0:00": 30
      },
      "startid": 370819452,
      "endid": 370819398
    },
    {
      "id": 2655,
      "name": "Holyhead Rd / Redesdale Avenue => Holyhead Rd / Redesdale Avenue",
      "length": 0.0006598299856777957,
      "speed": {
        "0:00": 30
      },
      "startid": 370819398,
      "endid": 370819399
    },
    {
      "id": 2656,
      "name": "Holyhead Rd / Redesdale Avenue => Holyhead Rd / Moseley Avenue",
      "length": 0.003837463750968571,
      "speed": {
        "0:00": 30
      },
      "startid": 370819399,
      "endid": 370819395
    },
    {
      "id": 2657,
      "name": "Holyhead Rd / Moseley Avenue => Holyhead Rd / Moseley Avenue",
      "length": 0.0008869628740820093,
      "speed": {
        "0:00": 30
      },
      "startid": 370819395,
      "endid": 370819397
    },
    {
      "id": 2658,
      "name": "Holyhead Rd / Moseley Avenue => Holyhead Rd / Alvis Retail Park",
      "length": 0.0043102225893796985,
      "speed": {
        "0:00": 30
      },
      "startid": 370819397,
      "endid": 370819361
    },
    {
      "id": 2659,
      "name": "Holyhead Rd / Alvis Retail Park => Holyhead Rd / Alvis Retail Park",
      "length": 0.0002442421953716176,
      "speed": {
        "0:00": 30
      },
      "startid": 370819361,
      "endid": 370819363
    },
    {
      "id": 2660,
      "name": "Holyhead Rd / Alvis Retail Park => Holyhead Rd / Meriden St",
      "length": 0.006867083871630511,
      "speed": {
        "0:00": 30
      },
      "startid": 370819363,
      "endid": 370819360
    },
    {
      "id": 2661,
      "name": "Holyhead Rd / Meriden St => Holyhead Rd / Meriden St",
      "length": 0.0008530438792932072,
      "speed": {
        "0:00": 30
      },
      "startid": 370819360,
      "endid": 370819359
    },
    {
      "id": 2662,
      "name": "Holyhead Rd / Meriden St => Holyhead Rd / Ringway",
      "length": 0.0034018527613649606,
      "speed": {
        "0:00": 30
      },
      "startid": 370819359,
      "endid": 370819355
    },
    {
      "id": 2663,
      "name": "Holyhead Rd / Ringway => Holyhead Rd / Ringway",
      "length": 0.0001523425416673504,
      "speed": {
        "0:00": 30
      },
      "startid": 370819355,
      "endid": 370819357
    },
    {
      "id": 2664,
      "name": "Holyhead Rd / Ringway => UL3",
      "length": 0.0059757926938607455,
      "speed": {
        "0:00": 30
      },
      "startid": 370819357,
      "endid": 370817723
    },
    {
      "id": 2665,
      "name": "UL4 => BS3",
      "length": 0.002031303665137189,
      "speed": {
        "0:00": 30
      },
      "startid": 370817719,
      "endid": 370817695
    },
    {
      "id": 2666,
      "name": "Roseberry Ave / Riley Square => UL4",
      "length": 0.050126817996358125,
      "speed": {
        "0:00": 30
      },
      "startid": 370817349,
      "endid": 370817719
    },
    {
      "id": 2667,
      "name": "UL4 => UL3",
      "length": 0.00031591698276652307,
      "speed": {
        "0:00": 30
      },
      "startid": 370817719,
      "endid": 370817723
    },
    {
      "id": 2668,
      "name": "UL3 => BS3",
      "length": 0.0023332105005764514,
      "speed": {
        "0:00": 30
      },
      "startid": 370817723,
      "endid": 370817695
    },
    {
      "id": 2669,
      "name": "BS3 => BS5",
      "length": 0.0010715734832442273,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 370817666
    },
    {
      "id": 2670,
      "name": "BS5 => N",
      "length": 0.003582887140281883,
      "speed": {
        "0:00": 30
      },
      "startid": 370817666,
      "endid": 370817746
    },
    {
      "id": 2671,
      "name": "N => G",
      "length": 0.0008477681994510137,
      "speed": {
        "0:00": 30
      },
      "startid": 370817746,
      "endid": 370817740
    },
    {
      "id": 2672,
      "name": "G => FX1",
      "length": 0.0020614218127312416,
      "speed": {
        "0:00": 30
      },
      "startid": 370817740,
      "endid": 370817768
    },
    {
      "id": 2673,
      "name": "FX1 => CU4",
      "length": 0.001230879766667563,
      "speed": {
        "0:00": 30
      },
      "startid": 370817768,
      "endid": 370819679
    },
    {
      "id": 2674,
      "name": "CU4 => CU5",
      "length": 0.0005253710783815626,
      "speed": {
        "0:00": 30
      },
      "startid": 370819679,
      "endid": 370819676
    },
    {
      "id": 2675,
      "name": "CU5 => CU1",
      "length": 0.0021117262535691986,
      "speed": {
        "0:00": 30
      },
      "startid": 370819676,
      "endid": 370817766
    },
    {
      "id": 2676,
      "name": "CU1 => CU2",
      "length": 0.00010206831045847219,
      "speed": {
        "0:00": 30
      },
      "startid": 370817766,
      "endid": 370819680
    },
    {
      "id": 2677,
      "name": "CU2 => Sky Blue Way / Walkway To Gosford St",
      "length": 0.006305733683720618,
      "speed": {
        "0:00": 30
      },
      "startid": 370819680,
      "endid": 4815874919
    },
    {
      "id": 2678,
      "name": "Sky Blue Way / Walkway To Gosford St => Sky Blue Way / Gosford Green",
      "length": 0.0029580316495925675,
      "speed": {
        "0:00": 30
      },
      "startid": 4815874919,
      "endid": 4815880373
    },
    {
      "id": 2679,
      "name": "Sky Blue Way / Gosford Green => Sky Blue Way / Gosford Green",
      "length": 0.0003139044440539605,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880373,
      "endid": 4815880374
    },
    {
      "id": 2680,
      "name": "Sky Blue Way / Gosford Green => Walsgrave Rd / Swan Lane",
      "length": 0.0038133658229965737,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880374,
      "endid": 370817464
    },
    {
      "id": 2681,
      "name": "Walsgrave Rd / Swan Lane => Walsgrave Rd / Swan Lane",
      "length": 0.0017645372707868672,
      "speed": {
        "0:00": 30
      },
      "startid": 370817464,
      "endid": 370817463
    },
    {
      "id": 2682,
      "name": "Walsgrave Rd / Swan Lane => Walsgrave Rd / Clements St",
      "length": 0.0030988222827398773,
      "speed": {
        "0:00": 30
      },
      "startid": 370817463,
      "endid": 370817467
    },
    {
      "id": 2683,
      "name": "Walsgrave Rd / Clements St => Walsgrave Rd / Clements St",
      "length": 0.0005896212004330483,
      "speed": {
        "0:00": 30
      },
      "startid": 370817467,
      "endid": 370817465
    },
    {
      "id": 2684,
      "name": "Walsgrave Rd / Clements St => Clay Lane / Villiers St",
      "length": 0.002018121963607191,
      "speed": {
        "0:00": 30
      },
      "startid": 370817465,
      "endid": 370817469
    },
    {
      "id": 2685,
      "name": "Clay Lane / Villiers St => Clay Lane / Villiers St",
      "length": 0.0004209312770510226,
      "speed": {
        "0:00": 30
      },
      "startid": 370817469,
      "endid": 370817470
    },
    {
      "id": 2686,
      "name": "Clay Lane / Villiers St => Clay Lane / Caludon Rd",
      "length": 0.0013332352230586053,
      "speed": {
        "0:00": 30
      },
      "startid": 370817470,
      "endid": 370817472
    },
    {
      "id": 2687,
      "name": "Clay Lane / Caludon Rd => Clay Lane / Caludon Rd",
      "length": 0.00023488720697729067,
      "speed": {
        "0:00": 30
      },
      "startid": 370817472,
      "endid": 370817474
    },
    {
      "id": 2688,
      "name": "Clay Lane / Caludon Rd => Barras Green / Coventry St",
      "length": 0.0021808694137867867,
      "speed": {
        "0:00": 30
      },
      "startid": 370817474,
      "endid": 370817477
    },
    {
      "id": 2689,
      "name": "Barras Green / Coventry St => Barras Green / Coventry St",
      "length": 0.0002759794195227487,
      "speed": {
        "0:00": 30
      },
      "startid": 370817477,
      "endid": 370817479
    },
    {
      "id": 2690,
      "name": "Barras Green / Coventry St => Mercer Ave / North St",
      "length": 0.002349813177682842,
      "speed": {
        "0:00": 30
      },
      "startid": 370817479,
      "endid": 370817480
    },
    {
      "id": 2691,
      "name": "Mercer Ave / North St => Mercer Ave / North St",
      "length": 0.00022498899973042542,
      "speed": {
        "0:00": 30
      },
      "startid": 370817480,
      "endid": 370817481
    },
    {
      "id": 2692,
      "name": "Mercer Ave / North St => Alfall Rd / Stubbs Grove",
      "length": 0.004840595362142863,
      "speed": {
        "0:00": 30
      },
      "startid": 370817481,
      "endid": 370819566
    },
    {
      "id": 2693,
      "name": "Alfall Rd / Stubbs Grove => Alfall Rd / Stubbs Grove",
      "length": 0.0005282783830510509,
      "speed": {
        "0:00": 30
      },
      "startid": 370819566,
      "endid": 370819567
    },
    {
      "id": 2694,
      "name": "Alfall Rd / Stubbs Grove => Alfall Rd / Dennis Rd",
      "length": 0.002337872400281609,
      "speed": {
        "0:00": 30
      },
      "startid": 370819567,
      "endid": 370819643
    },
    {
      "id": 2695,
      "name": "Alfall Rd / Dennis Rd => Alfall Rd / Dennis Rd",
      "length": 0.001948143662567895,
      "speed": {
        "0:00": 30
      },
      "startid": 370819643,
      "endid": 370819644
    },
    {
      "id": 2696,
      "name": "Alfall Rd / Dennis Rd => Avon St / Alfall Rd",
      "length": 0.0007244049972218178,
      "speed": {
        "0:00": 30
      },
      "startid": 370819644,
      "endid": 370817483
    },
    {
      "id": 2697,
      "name": "Avon St / Alfall Rd => Avon St / Honiton Rd",
      "length": 0.0019748620610052668,
      "speed": {
        "0:00": 30
      },
      "startid": 370817483,
      "endid": 370817485
    },
    {
      "id": 2698,
      "name": "Avon St / Honiton Rd => Avon St / Honiton Rd",
      "length": 0.00046808773750384527,
      "speed": {
        "0:00": 30
      },
      "startid": 370817485,
      "endid": 370817484
    },
    {
      "id": 2699,
      "name": "Avon St / Honiton Rd => Torcross Ave / Sewall Highway",
      "length": 0.0016491798476805893,
      "speed": {
        "0:00": 30
      },
      "startid": 370817484,
      "endid": 370817488
    },
    {
      "id": 2700,
      "name": "Torcross Ave / Sewall Highway => Torcross Ave / Sewall Highway",
      "length": 0.0003655913018657318,
      "speed": {
        "0:00": 30
      },
      "startid": 370817488,
      "endid": 370817486
    },
    {
      "id": 2701,
      "name": "Torcross Ave / Sewall Highway => Sewall Highway / Middle",
      "length": 0.003031260175240516,
      "speed": {
        "0:00": 30
      },
      "startid": 370817486,
      "endid": 370819641
    },
    {
      "id": 2702,
      "name": "Sewall Highway / Middle => Sewall Highway / Dennis Rd",
      "length": 0.002706378391876186,
      "speed": {
        "0:00": 30
      },
      "startid": 370819641,
      "endid": 370819640
    },
    {
      "id": 2703,
      "name": "Sewall Highway / Dennis Rd => Sewall Highway / Dennis Rd",
      "length": 0.0006107787897418022,
      "speed": {
        "0:00": 30
      },
      "startid": 370819640,
      "endid": 370819639
    },
    {
      "id": 2704,
      "name": "Sewall Highway / Dennis Rd => Blackberry Lane / Brixham Drive",
      "length": 0.004937185053247094,
      "speed": {
        "0:00": 30
      },
      "startid": 370819639,
      "endid": 370817641
    },
    {
      "id": 2705,
      "name": "Blackberry Lane / Brixham Drive => Blackberry Lane / Brixham Drive",
      "length": 0.0001440904229983649,
      "speed": {
        "0:00": 30
      },
      "startid": 370817641,
      "endid": 370817639
    },
    {
      "id": 2706,
      "name": "Blackberry Lane / Brixham Drive => Blackberry Lane / Attwood Crescent",
      "length": 0.004738575104395738,
      "speed": {
        "0:00": 30
      },
      "startid": 370817639,
      "endid": 370817651
    },
    {
      "id": 2707,
      "name": "Blackberry Lane / Attwood Crescent => Wyken Croft / Blackberry Lane",
      "length": 0.001917655756385987,
      "speed": {
        "0:00": 30
      },
      "startid": 370817651,
      "endid": 370817489
    },
    {
      "id": 2708,
      "name": "Wyken Croft / Blackberry Lane => Wyken Croft / Hermes Crescent",
      "length": 0.0011307992969597162,
      "speed": {
        "0:00": 30
      },
      "startid": 370817489,
      "endid": 370817653
    },
    {
      "id": 2709,
      "name": "Wyken Croft / Hermes Crescent => Wyken Croft / Hermes Crescent",
      "length": 0.0011230694546673055,
      "speed": {
        "0:00": 30
      },
      "startid": 370817653,
      "endid": 4815881234
    },
    {
      "id": 2710,
      "name": "Wyken Croft / Hermes Crescent => Wyken Croft / Doncaster Close",
      "length": 0.0010068258886211014,
      "speed": {
        "0:00": 30
      },
      "startid": 4815881234,
      "endid": 370817533
    },
    {
      "id": 2711,
      "name": "Wyken Croft / Doncaster Close => Wyken Croft / Doncaster Close",
      "length": 0.0002922190958847474,
      "speed": {
        "0:00": 30
      },
      "startid": 370817533,
      "endid": 370817535
    },
    {
      "id": 2712,
      "name": "Wyken Croft / Doncaster Close => Henley Rd / Broad Park Rd",
      "length": 0.0031911319700053263,
      "speed": {
        "0:00": 30
      },
      "startid": 370817535,
      "endid": 370817560
    },
    {
      "id": 2713,
      "name": "Henley Rd / Broad Park Rd => Broad Park Rd / Logan Rd",
      "length": 0.0009178312045262597,
      "speed": {
        "0:00": 30
      },
      "startid": 370817560,
      "endid": 4815876530
    },
    {
      "id": 2714,
      "name": "Broad Park Rd / Logan Rd => Broad Park Rd / Broad Park Shops",
      "length": 0.0008362044726040847,
      "speed": {
        "0:00": 30
      },
      "startid": 4815876530,
      "endid": 370817536
    },
    {
      "id": 2715,
      "name": "Broad Park Rd / Broad Park Shops => Broad Park Rd / Broad Park Shops",
      "length": 0.000692580103667792,
      "speed": {
        "0:00": 30
      },
      "startid": 370817536,
      "endid": 370817539
    },
    {
      "id": 2716,
      "name": "Broad Park Rd / Broad Park Shops => Winston Avenue / Clennon Rise",
      "length": 0.0031214824298725925,
      "speed": {
        "0:00": 30
      },
      "startid": 370817539,
      "endid": 370817543
    },
    {
      "id": 2717,
      "name": "Winston Avenue / Clennon Rise => Winston Avenue / Clennon Rise",
      "length": 0.0006219700314324196,
      "speed": {
        "0:00": 30
      },
      "startid": 370817543,
      "endid": 370817541
    },
    {
      "id": 2718,
      "name": "Winston Avenue / Clennon Rise => Winston Avenue / Deedmore Rd",
      "length": 0.004886732295717704,
      "speed": {
        "0:00": 30
      },
      "startid": 370817541,
      "endid": 370817545
    },
    {
      "id": 2719,
      "name": "Winston Avenue / Deedmore Rd => Winston Avenue / Deedmore Rd",
      "length": 0.0004305618886989429,
      "speed": {
        "0:00": 30
      },
      "startid": 370817545,
      "endid": 370817546
    },
    {
      "id": 2720,
      "name": "Winston Avenue / Deedmore Rd => Deedmore Rd / Henley Rd",
      "length": 0.003181467015389691,
      "speed": {
        "0:00": 30
      },
      "startid": 370817546,
      "endid": 370817426
    },
    {
      "id": 2721,
      "name": "Deedmore Rd / Henley Rd => Henley Rd / Deedmore Rd",
      "length": 0.0011486461334971625,
      "speed": {
        "0:00": 30
      },
      "startid": 370817426,
      "endid": 370817566
    },
    {
      "id": 2722,
      "name": "Henley Rd / Deedmore Rd => Henley Rd / Dame Agnes Grove",
      "length": 0.005039856365016028,
      "speed": {
        "0:00": 30
      },
      "startid": 370817566,
      "endid": 370817365
    },
    {
      "id": 2723,
      "name": "Henley Rd / Dame Agnes Grove => Henley Rd / Dame Agnes Grove",
      "length": 0.0008064862057111586,
      "speed": {
        "0:00": 30
      },
      "startid": 370817365,
      "endid": 370817363
    },
    {
      "id": 2724,
      "name": "Kingsbury Rd / Morfa Gardens => Kingsbury Rd / Morfa Gardens",
      "length": 0.0002346570476252687,
      "speed": {
        "0:00": 30
      },
      "startid": 370818814,
      "endid": 370818815
    },
    {
      "id": 2725,
      "name": "Kingsbury Rd / Morfa Gardens => Kingsbury Rd / Forfield Rd",
      "length": 0.002124688071222401,
      "speed": {
        "0:00": 30
      },
      "startid": 370818815,
      "endid": 370819531
    },
    {
      "id": 2726,
      "name": "Kingsbury Rd / Forfield Rd => Forfield Rd / Kingsbury Rd",
      "length": 0.0006363882148532272,
      "speed": {
        "0:00": 30
      },
      "startid": 370819531,
      "endid": 370819476
    },
    {
      "id": 2727,
      "name": "Forfield Rd / Kingsbury Rd => Forfield Rd / Donnington Avenue",
      "length": 0.0039029464203348737,
      "speed": {
        "0:00": 30
      },
      "startid": 370819476,
      "endid": 370819474
    },
    {
      "id": 2728,
      "name": "Forfield Rd / Donnington Avenue => Forfield Rd / Donnington Avenue",
      "length": 0.0007997796258971145,
      "speed": {
        "0:00": 30
      },
      "startid": 370819474,
      "endid": 370819475
    },
    {
      "id": 2729,
      "name": "Forfield Rd / Donnington Avenue => Forfield Rd / Coundon Jun & Inf School",
      "length": 0.0018597823367256243,
      "speed": {
        "0:00": 30
      },
      "startid": 370819475,
      "endid": 370819781
    },
    {
      "id": 2730,
      "name": "Forfield Rd / Coundon Jun & Inf School => Courtland Ave / Evenlode Crescent",
      "length": 0.0012915526508817362,
      "speed": {
        "0:00": 30
      },
      "startid": 370819781,
      "endid": 370819468
    },
    {
      "id": 2731,
      "name": "Courtland Ave / Evenlode Crescent => Courtland Ave / Westhill Rd",
      "length": 0.0022943387108270504,
      "speed": {
        "0:00": 30
      },
      "startid": 370819468,
      "endid": 370819779
    },
    {
      "id": 2732,
      "name": "Courtland Ave / Westhill Rd => Westhill Rd / Courtland Avenue",
      "length": 0.0011599790429136195,
      "speed": {
        "0:00": 30
      },
      "startid": 370819779,
      "endid": 370819456
    },
    {
      "id": 2733,
      "name": "Westhill Rd / Courtland Avenue => Barkers Butts Lane / Ashwood Avenue",
      "length": 0.0026122990429900124,
      "speed": {
        "0:00": 30
      },
      "startid": 370819456,
      "endid": 370819411
    },
    {
      "id": 2734,
      "name": "Barkers Butts Lane / Ashwood Avenue => Barkers Butts Lane / Ashwood Avenue",
      "length": 0.0005091038400957758,
      "speed": {
        "0:00": 30
      },
      "startid": 370819411,
      "endid": 370819409
    },
    {
      "id": 2735,
      "name": "Barkers Butts Lane / Ashwood Avenue => Barkers Butts Lane / Browett Rd",
      "length": 0.002404771743846582,
      "speed": {
        "0:00": 30
      },
      "startid": 370819409,
      "endid": 370819408
    },
    {
      "id": 2736,
      "name": "Barkers Butts Lane / Browett Rd => Barkers Butts Lane / Browett Rd",
      "length": 0.0009830320442389589,
      "speed": {
        "0:00": 30
      },
      "startid": 370819408,
      "endid": 370819407
    },
    {
      "id": 2737,
      "name": "Barkers Butts Lane / Browett Rd => Barkers Butts Lane / Moseley Avenue",
      "length": 0.0017103410946331416,
      "speed": {
        "0:00": 30
      },
      "startid": 370819407,
      "endid": 370819382
    },
    {
      "id": 2738,
      "name": "Barkers Butts Lane / Moseley Avenue => Barkers Butts Lane / Moseley Avenue",
      "length": 0.0013327606911980824,
      "speed": {
        "0:00": 30
      },
      "startid": 370819382,
      "endid": 370819379
    },
    {
      "id": 2739,
      "name": "Barkers Butts Lane / Moseley Avenue => Barkers Butts Lane / Tomson Avenue",
      "length": 0.0033757849516812726,
      "speed": {
        "0:00": 30
      },
      "startid": 370819379,
      "endid": 370819376
    },
    {
      "id": 2740,
      "name": "Barkers Butts Lane / Tomson Avenue => Barkers Butts Lane / Tomson Avenue",
      "length": 0.00030290600852587226,
      "speed": {
        "0:00": 30
      },
      "startid": 370819376,
      "endid": 370819377
    },
    {
      "id": 2741,
      "name": "Barkers Butts Lane / Tomson Avenue => Coundon Rd / Middleborough Rd",
      "length": 0.004570993845978481,
      "speed": {
        "0:00": 30
      },
      "startid": 370819377,
      "endid": 370819372
    },
    {
      "id": 2742,
      "name": "Coundon Rd / Middleborough Rd => Coundon Rd / Middleborough Rd",
      "length": 0.00015459912677892894,
      "speed": {
        "0:00": 30
      },
      "startid": 370819372,
      "endid": 370819375
    },
    {
      "id": 2743,
      "name": "Coundon Rd / Middleborough Rd => Holyhead Rd / Ringway",
      "length": 0.0015711524750984024,
      "speed": {
        "0:00": 30
      },
      "startid": 370819375,
      "endid": 370819355
    },
    {
      "id": 2744,
      "name": "Holyhead Rd / Ringway => Holyhead Rd / Ringway",
      "length": 0.0001523425416673504,
      "speed": {
        "0:00": 30
      },
      "startid": 370819355,
      "endid": 370819357
    },
    {
      "id": 2745,
      "name": "Holyhead Rd / Ringway => UL4",
      "length": 0.0062750762561103,
      "speed": {
        "0:00": 30
      },
      "startid": 370819357,
      "endid": 370817719
    },
    {
      "id": 2746,
      "name": "UL4 => UL3",
      "length": 0.00031591698276652307,
      "speed": {
        "0:00": 30
      },
      "startid": 370817719,
      "endid": 370817723
    },
    {
      "id": 2747,
      "name": "UL3 => BS3",
      "length": 0.0023332105005764514,
      "speed": {
        "0:00": 30
      },
      "startid": 370817723,
      "endid": 370817695
    },
    {
      "id": 2748,
      "name": "BS3 => BS5",
      "length": 0.0010715734832442273,
      "speed": {
        "0:00": 30
      },
      "startid": 370817695,
      "endid": 370817666
    },
    {
      "id": 2749,
      "name": "BS5 => G",
      "length": 0.00440915935978715,
      "speed": {
        "0:00": 30
      },
      "startid": 370817666,
      "endid": 370817740
    },
    {
      "id": 2750,
      "name": "Holly Walk => Holly Walk",
      "length": 0.00042105334579031165,
      "speed": {
        "0:00": 30
      },
      "startid": 487166966,
      "endid": 487166961
    },
    {
      "id": 2751,
      "name": "Holly Walk => Old Mill Inn",
      "length": 0.006659676428325368,
      "speed": {
        "0:00": 30
      },
      "startid": 487166961,
      "endid": 487166975
    },
    {
      "id": 2752,
      "name": "Old Mill Inn => Old Mill Inn",
      "length": 0.00025494903412259746,
      "speed": {
        "0:00": 30
      },
      "startid": 487166975,
      "endid": 487166972
    },
    {
      "id": 2753,
      "name": "Old Mill Inn => Mill Hill / Howes Lane",
      "length": 0.0036200541335719345,
      "speed": {
        "0:00": 30
      },
      "startid": 487166972,
      "endid": 370819803
    },
    {
      "id": 2754,
      "name": "Mill Hill / Howes Lane => Mill Hill / Howes Lane",
      "length": 0.0002920659172212636,
      "speed": {
        "0:00": 30
      },
      "startid": 370819803,
      "endid": 370819804
    },
    {
      "id": 2755,
      "name": "Mill Hill / Howes Lane => Brentwood Avenue / Alfriston Rd",
      "length": 0.00540579816863295,
      "speed": {
        "0:00": 30
      },
      "startid": 370819804,
      "endid": 370818943
    },
    {
      "id": 2756,
      "name": "Brentwood Avenue / Alfriston Rd => Brentwood Avenue / Alfriston Rd",
      "length": 0.00031848089424333243,
      "speed": {
        "0:00": 30
      },
      "startid": 370818943,
      "endid": 370818944
    },
    {
      "id": 2757,
      "name": "Brentwood Avenue / Alfriston Rd => Hadleigh Rd / St Martins Rd",
      "length": 0.004172986332351912,
      "speed": {
        "0:00": 30
      },
      "startid": 370818944,
      "endid": 370818942
    },
    {
      "id": 2758,
      "name": "Hadleigh Rd / St Martins Rd => Hadleigh Rd / St Martins Rd",
      "length": 0.00010549090007743969,
      "speed": {
        "0:00": 30
      },
      "startid": 370818942,
      "endid": 370818940
    },
    {
      "id": 2759,
      "name": "Hadleigh Rd / St Martins Rd => St Martins Rd / Erithway Rd",
      "length": 0.0021740875166395787,
      "speed": {
        "0:00": 30
      },
      "startid": 370818940,
      "endid": 370818938
    },
    {
      "id": 2760,
      "name": "St Martins Rd / Erithway Rd => St Martins Rd / Erithway Rd",
      "length": 0.0004672167912177775,
      "speed": {
        "0:00": 30
      },
      "startid": 370818938,
      "endid": 370818937
    },
    {
      "id": 2761,
      "name": "St Martins Rd / Erithway Rd => Leamington Rd / Stonebridge Highway",
      "length": 0.002346814106405063,
      "speed": {
        "0:00": 30
      },
      "startid": 370818937,
      "endid": 370818933
    },
    {
      "id": 2762,
      "name": "Leamington Rd / Stonebridge Highway => Leamington Rd / Stonebridge Highway",
      "length": 0.00028445586652267,
      "speed": {
        "0:00": 30
      },
      "startid": 370818933,
      "endid": 370818935
    },
    {
      "id": 2763,
      "name": "Leamington Rd / Stonebridge Highway => Leamington Rd / Dewsbury Avenue",
      "length": 0.002528549546679714,
      "speed": {
        "0:00": 30
      },
      "startid": 370818935,
      "endid": 370818579
    },
    {
      "id": 2764,
      "name": "Leamington Rd / Dewsbury Avenue => Leamington Rd / Dewsbury Avenue",
      "length": 0.00026672916975609856,
      "speed": {
        "0:00": 30
      },
      "startid": 370818579,
      "endid": 370818578
    },
    {
      "id": 2765,
      "name": "Leamington Rd / Dewsbury Avenue => Leamington Rd / Baginton Rd",
      "length": 0.0008850576478397776,
      "speed": {
        "0:00": 30
      },
      "startid": 370818578,
      "endid": 370818575
    },
    {
      "id": 2766,
      "name": "Leamington Rd / Baginton Rd => Leamington Rd / Baginton Rd",
      "length": 0.001640813886464955,
      "speed": {
        "0:00": 30
      },
      "startid": 370818575,
      "endid": 370818577
    },
    {
      "id": 2767,
      "name": "Leamington Rd / Baginton Rd => Leamington Rd / Stivichall Croft",
      "length": 0.0031634906432593717,
      "speed": {
        "0:00": 30
      },
      "startid": 370818577,
      "endid": 370818574
    },
    {
      "id": 2768,
      "name": "Leamington Rd / Stivichall Croft => Leamington Rd / Stivichall Croft",
      "length": 0.00039644168549778086,
      "speed": {
        "0:00": 30
      },
      "startid": 370818574,
      "endid": 370818572
    },
    {
      "id": 2769,
      "name": "Leamington Rd / Stivichall Croft => Leamington Rd / Armorial Rd",
      "length": 0.0023907359808194324,
      "speed": {
        "0:00": 30
      },
      "startid": 370818572,
      "endid": 370818559
    },
    {
      "id": 2770,
      "name": "Leamington Rd / Armorial Rd => Leamington Rd / Armorial Rd",
      "length": 0.0003211603026512689,
      "speed": {
        "0:00": 30
      },
      "startid": 370818559,
      "endid": 370818562
    },
    {
      "id": 2771,
      "name": "Leamington Rd / Armorial Rd => Leamington Rd / War Memorial Park",
      "length": 0.0021197752262931174,
      "speed": {
        "0:00": 30
      },
      "startid": 370818562,
      "endid": 370818570
    },
    {
      "id": 2772,
      "name": "Leamington Rd / War Memorial Park => Leamington Rd / War Memorial Park",
      "length": 0.00032981820750473,
      "speed": {
        "0:00": 30
      },
      "startid": 370818570,
      "endid": 370818569
    },
    {
      "id": 2773,
      "name": "Leamington Rd / War Memorial Park => Warwick Road / Leamington Rd",
      "length": 0.0030726059054120613,
      "speed": {
        "0:00": 30
      },
      "startid": 370818569,
      "endid": 370818568
    },
    {
      "id": 2774,
      "name": "Warwick Road / Leamington Rd => Warwick Road / Leamington Rd",
      "length": 0.000625492965591671,
      "speed": {
        "0:00": 30
      },
      "startid": 370818568,
      "endid": 370818566
    },
    {
      "id": 2775,
      "name": "Warwick Road / Leamington Rd => WR5",
      "length": 0.0026801527288538595,
      "speed": {
        "0:00": 30
      },
      "startid": 370818566,
      "endid": 370817793
    },
    {
      "id": 2776,
      "name": "WR5 => WR6",
      "length": 0.0004939037153162216,
      "speed": {
        "0:00": 30
      },
      "startid": 370817793,
      "endid": 370817791
    },
    {
      "id": 2777,
      "name": "WR6 => BY2",
      "length": 0.006360279312262274,
      "speed": {
        "0:00": 30
      },
      "startid": 370817791,
      "endid": 370817685
    },
    {
      "id": 2778,
      "name": "BY2 => BY5",
      "length": 0.000648345224398062,
      "speed": {
        "0:00": 30
      },
      "startid": 370817685,
      "endid": 370817679
    },
    {
      "id": 2779,
      "name": "BY5 => SJ1",
      "length": 0.0037519047429273086,
      "speed": {
        "0:00": 30
      },
      "startid": 370817679,
      "endid": 4815869810
    },
    {
      "id": 2780,
      "name": "SJ1 => LP1",
      "length": 0.001256202392133201,
      "speed": {
        "0:00": 30
      },
      "startid": 4815869810,
      "endid": 370817776
    },
    {
      "id": 2781,
      "name": "LP1 => ES1",
      "length": 0.0016872650799448009,
      "speed": {
        "0:00": 30
      },
      "startid": 370817776,
      "endid": 370817774
    },
    {
      "id": 2782,
      "name": "ES1 => MP1",
      "length": 0.0010158778371435512,
      "speed": {
        "0:00": 30
      },
      "startid": 370817774,
      "endid": 4815869811
    },
    {
      "id": 2783,
      "name": "MP1 => CU5",
      "length": 0.0026715607423398167,
      "speed": {
        "0:00": 30
      },
      "startid": 4815869811,
      "endid": 370819676
    },
    {
      "id": 2784,
      "name": "CU5 => FX1",
      "length": 0.001435590516124241,
      "speed": {
        "0:00": 30
      },
      "startid": 370819676,
      "endid": 370817768
    },
    {
      "id": 2785,
      "name": "FX1 => F",
      "length": 0.0020783494845687056,
      "speed": {
        "0:00": 30
      },
      "startid": 370817768,
      "endid": 370817739
    },
    {
      "id": 2786,
      "name": "F => Baginton, Kimberley Road.",
      "length": 0.04165787759356178,
      "speed": {
        "0:00": 30
      },
      "startid": 370817739,
      "endid": 944102324
    },
    {
      "id": 2787,
      "name": "Baginton, Kimberley Road. => Post Office",
      "length": 0.00042695110961433146,
      "speed": {
        "0:00": 30
      },
      "startid": 944102324,
      "endid": 487160157
    },
    {
      "id": 2788,
      "name": "Post Office => Church Road",
      "length": 0.002703608481269057,
      "speed": {
        "0:00": 30
      },
      "startid": 487160157,
      "endid": 487160158
    },
    {
      "id": 2789,
      "name": "Church Road => Church Road",
      "length": 0.0002520307322529971,
      "speed": {
        "0:00": 30
      },
      "startid": 487160158,
      "endid": 487160160
    },
    {
      "id": 2790,
      "name": "Cromwell Lane / Westwood Heath Rd => Westwood Heath Rd / Cromwell Lane",
      "length": 0.0008921814277368043,
      "speed": {
        "0:00": 30
      },
      "startid": 370818011,
      "endid": 370818014
    },
    {
      "id": 2791,
      "name": "Westwood Heath Rd / Cromwell Lane => Westwood Heath Rd / Cromwell Lane",
      "length": 0.00022379387837956485,
      "speed": {
        "0:00": 30
      },
      "startid": 370818014,
      "endid": 370818013
    },
    {
      "id": 2792,
      "name": "Westwood Heath Rd / Cromwell Lane => Westwood Heath Rd / Bockendon Rd",
      "length": 0.007790139626477543,
      "speed": {
        "0:00": 30
      },
      "startid": 370818013,
      "endid": 370817958
    },
    {
      "id": 2793,
      "name": "Westwood Heath Rd / Bockendon Rd => Westwood Heath Rd / Bockendon Rd",
      "length": 0.0033676133032156754,
      "speed": {
        "0:00": 30
      },
      "startid": 370817958,
      "endid": 370817957
    },
    {
      "id": 2794,
      "name": "Westwood Heath Rd / Bockendon Rd => Westwood Heath Rd / Woodleigh Rd",
      "length": 0.0058215167370711755,
      "speed": {
        "0:00": 30
      },
      "startid": 370817957,
      "endid": 370817960
    },
    {
      "id": 2795,
      "name": "Westwood Heath Rd / Woodleigh Rd => Westwood Heath Rd / Broadwells Crescent",
      "length": 0.006716951541436058,
      "speed": {
        "0:00": 30
      },
      "startid": 370817960,
      "endid": 370817993
    },
    {
      "id": 2796,
      "name": "Westwood Heath Rd / Broadwells Crescent => Westwood Heath Rd / Broadwells Crescent",
      "length": 0.0004890352339050721,
      "speed": {
        "0:00": 30
      },
      "startid": 370817993,
      "endid": 370817992
    },
    {
      "id": 2797,
      "name": "Westwood Heath Rd / Broadwells Crescent => Westwood Heath Rd / Westwood Church",
      "length": 0.003214200542903373,
      "speed": {
        "0:00": 30
      },
      "startid": 370817992,
      "endid": 370817655
    },
    {
      "id": 2798,
      "name": "Westwood Heath Rd / Westwood Church => Westwood Heath Rd / Gibbet Hill Rd",
      "length": 0.002089032465041632,
      "speed": {
        "0:00": 30
      },
      "startid": 370817655,
      "endid": 370817657
    },
    {
      "id": 2799,
      "name": "Westwood Heath Rd / Gibbet Hill Rd => Kirby Corner Rd / Gibbet Hill Rd",
      "length": 0.0027864212208499784,
      "speed": {
        "0:00": 30
      },
      "startid": 370817657,
      "endid": 370819749
    },
    {
      "id": 2800,
      "name": "Kirby Corner Rd / Gibbet Hill Rd => Kirby Corner Rd / University Westwood Site",
      "length": 0.004738827116489978,
      "speed": {
        "0:00": 30
      },
      "startid": 370819749,
      "endid": 370817931
    },
    {
      "id": 2801,
      "name": "Kirby Corner Rd / University Westwood Site => Kirby Corner Rd / University Westwood Site",
      "length": 0.0008440280208634823,
      "speed": {
        "0:00": 30
      },
      "startid": 370817931,
      "endid": 370817930
    },
    {
      "id": 2802,
      "name": "Kirby Corner Rd / University Westwood Site => Kirby Corner Rd / Lynchgate Rd",
      "length": 0.005184185461573927,
      "speed": {
        "0:00": 30
      },
      "startid": 370817930,
      "endid": 370817929
    },
    {
      "id": 2803,
      "name": "Kirby Corner Rd / Lynchgate Rd => Kirby Corner Rd / Lynchgate Rd",
      "length": 0.00029797681117596606,
      "speed": {
        "0:00": 30
      },
      "startid": 370817929,
      "endid": 370817927
    },
    {
      "id": 2804,
      "name": "Kirby Corner Rd / Lynchgate Rd => Lynchgate Rd / Leeming Close",
      "length": 0.0039043109366500898,
      "speed": {
        "0:00": 30
      },
      "startid": 370817927,
      "endid": 370819152
    },
    {
      "id": 2805,
      "name": "Lynchgate Rd / Leeming Close => De Montfort Way / Cannon Park Shops",
      "length": 0.0023546683949164826,
      "speed": {
        "0:00": 30
      },
      "startid": 370819152,
      "endid": 370817920
    },
    {
      "id": 2806,
      "name": "De Montfort Way / Cannon Park Shops => Sir Henry Parkes Rd / Centenary Rd",
      "length": 0.004222512670197375,
      "speed": {
        "0:00": 30
      },
      "startid": 370817920,
      "endid": 370817913
    },
    {
      "id": 2807,
      "name": "Sir Henry Parkes Rd / Centenary Rd => Charter Ave / Sir Henry Parkes Rd",
      "length": 0.001759790942127883,
      "speed": {
        "0:00": 30
      },
      "startid": 370817913,
      "endid": 370817940
    },
    {
      "id": 2808,
      "name": "Charter Ave / Sir Henry Parkes Rd => Charter Ave / Centenary Rd",
      "length": 0.0023897088190822846,
      "speed": {
        "0:00": 30
      },
      "startid": 370817940,
      "endid": 370817918
    },
    {
      "id": 2809,
      "name": "Charter Ave / Centenary Rd => Charter Ave / Fletchamstead Highway",
      "length": 0.0031323945361338627,
      "speed": {
        "0:00": 30
      },
      "startid": 370817918,
      "endid": 466384984
    },
    {
      "id": 2810,
      "name": "Charter Ave / Fletchamstead Highway => Fletchamstead Highway / Canley Rd",
      "length": 0.0009373778853794403,
      "speed": {
        "0:00": 30
      },
      "startid": 466384984,
      "endid": 370819754
    },
    {
      "id": 2811,
      "name": "Fletchamstead Highway / Canley Rd => Fletchamstead Highway / Cannon Park Rd",
      "length": 0.008883542424618952,
      "speed": {
        "0:00": 30
      },
      "startid": 370819754,
      "endid": 370817893
    },
    {
      "id": 2812,
      "name": "Fletchamstead Highway / Cannon Park Rd => Fletchamstead Highway / Cannon Park Rd",
      "length": 0.0025635280942480913,
      "speed": {
        "0:00": 30
      },
      "startid": 370817893,
      "endid": 370817894
    },
    {
      "id": 2813,
      "name": "Fletchamstead Highway / Cannon Park Rd => Kenilworth Rd / Fletchamstead Highway",
      "length": 0.0026321823379088934,
      "speed": {
        "0:00": 30
      },
      "startid": 370817894,
      "endid": 370819143
    },
    {
      "id": 2814,
      "name": "Kenilworth Rd / Fletchamstead Highway => Kenilworth Rd / Fletchamstead Highway",
      "length": 0.0003271508062040479,
      "speed": {
        "0:00": 30
      },
      "startid": 370819143,
      "endid": 370817878
    },
    {
      "id": 2815,
      "name": "Kenilworth Rd / Fletchamstead Highway => Kenilworth Rd / Coat Of Arms Bridge Rd",
      "length": 0.0032329641259982583,
      "speed": {
        "0:00": 30
      },
      "startid": 370817878,
      "endid": 370819121
    },
    {
      "id": 2816,
      "name": "Kenilworth Rd / Coat Of Arms Bridge Rd => Kenilworth Rd / Coat Of Arms Bridge Rd",
      "length": 0.0008588363348187505,
      "speed": {
        "0:00": 30
      },
      "startid": 370819121,
      "endid": 370819120
    },
    {
      "id": 2817,
      "name": "Kenilworth Rd / Coat Of Arms Bridge Rd => Kenilworth Rd / Beechwood Avenue",
      "length": 0.0027098195105921007,
      "speed": {
        "0:00": 30
      },
      "startid": 370819120,
      "endid": 370819119
    },
    {
      "id": 2818,
      "name": "Kenilworth Rd / Beechwood Avenue => Kenilworth Rd / Beechwood Avenue",
      "length": 0.00217378832916246,
      "speed": {
        "0:00": 30
      },
      "startid": 370819119,
      "endid": 370819118
    },
    {
      "id": 2819,
      "name": "Kenilworth Rd / Beechwood Avenue => Kenilworth Rd / Earlsdon Avenue South",
      "length": 0.0019592283072683227,
      "speed": {
        "0:00": 30
      },
      "startid": 370819118,
      "endid": 370819116
    },
    {
      "id": 2820,
      "name": "Kenilworth Rd / Earlsdon Avenue South => Kenilworth Rd / Davenport Rd",
      "length": 0.007036728615628068,
      "speed": {
        "0:00": 30
      },
      "startid": 370819116,
      "endid": 370819138
    },
    {
      "id": 2821,
      "name": "Kenilworth Rd / Davenport Rd => Kenilworth Rd / Davenport Rd",
      "length": 0.000915686103422053,
      "speed": {
        "0:00": 30
      },
      "startid": 370819138,
      "endid": 370819141
    },
    {
      "id": 2822,
      "name": "Kenilworth Rd / Davenport Rd => Warwick Road / Leamington Rd",
      "length": 0.003584891552053543,
      "speed": {
        "0:00": 30
      },
      "startid": 370819141,
      "endid": 370818568
    },
    {
      "id": 2823,
      "name": "Warwick Road / Leamington Rd => Warwick Road / Leamington Rd",
      "length": 0.000625492965591671,
      "speed": {
        "0:00": 30
      },
      "startid": 370818568,
      "endid": 370818566
    },
    {
      "id": 2824,
      "name": "Warwick Road / Leamington Rd => WR5",
      "length": 0.0026801527288538595,
      "speed": {
        "0:00": 30
      },
      "startid": 370818566,
      "endid": 370817793
    },
    {
      "id": 2825,
      "name": "WR5 => Burton Green",
      "length": 0.08609227829236407,
      "speed": {
        "0:00": 30
      },
      "startid": 370817793,
      "endid": 2629273401
    },
    {
      "id": 2826,
      "name": "Burton Green => Burton green",
      "length": 0.000265942192971362,
      "speed": {
        "0:00": 30
      },
      "startid": 2629273401,
      "endid": 2629273407
    },
    {
      "id": 2827,
      "name": "Westwood Heath Rd / Woodleigh Rd => Kenilworth Rd / Earlsdon Avenue South",
      "length": 0.05979805309949543,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880390,
      "endid": 4815880396
    },
    {
      "id": 2828,
      "name": "Kenilworth Rd / Earlsdon Avenue South => WR6",
      "length": 0.010441155587386949,
      "speed": {
        "0:00": 30
      },
      "startid": 4815880396,
      "endid": 370817791
    },
    {
      "id": 2829,
      "name": "WR6 => WR3",
      "length": 0.001157136020523468,
      "speed": {
        "0:00": 30
      },
      "startid": 370817791,
      "endid": 9416517351
    },
    {
      "id": 2830,
      "name": "WR3 => WR1",
      "length": 0.0005164773179946906,
      "speed": {
        "0:00": 30
      },
      "startid": 9416517351,
      "endid": 9590566165
    },
    {
      "id": 2831,
      "name": "Cedars Road => Cedars Road",
      "length": 0.00009587251952832346,
      "speed": {
        "0:00": 30
      },
      "startid": 487166699,
      "endid": 487166701
    },
    {
      "id": 2832,
      "name": "Cedars Road => Field View Close",
      "length": 0.002068134205025566,
      "speed": {
        "0:00": 30
      },
      "startid": 487166701,
      "endid": 487169363
    },
    {
      "id": 2833,
      "name": "Field View Close => Field View Close",
      "length": 0.0005728722894345266,
      "speed": {
        "0:00": 30
      },
      "startid": 487169363,
      "endid": 487169354
    },
    {
      "id": 2834,
      "name": "Field View Close => Hayes Lane",
      "length": 0.0008336227264145015,
      "speed": {
        "0:00": 30
      },
      "startid": 487169354,
      "endid": 487174464
    },
    {
      "id": 2835,
      "name": "Hayes Lane => Hayes Lane",
      "length": 0.0007126821732062443,
      "speed": {
        "0:00": 30
      },
      "startid": 487174464,
      "endid": 487169359
    },
    {
      "id": 2836,
      "name": "Hayes Lane => Heckley Road",
      "length": 0.0019734361149991134,
      "speed": {
        "0:00": 30
      },
      "startid": 487169359,
      "endid": 487174461
    },
    {
      "id": 2837,
      "name": "Heckley Road => Trelawney Road",
      "length": 0.0009165142933970633,
      "speed": {
        "0:00": 30
      },
      "startid": 487174461,
      "endid": 487169366
    },
    {
      "id": 2838,
      "name": "Trelawney Road => Lord Raglan",
      "length": 0.0008222157867605711,
      "speed": {
        "0:00": 30
      },
      "startid": 487169366,
      "endid": 487174457
    },
    {
      "id": 2839,
      "name": "Lord Raglan => Blackhorse Road",
      "length": 0.001911582135301548,
      "speed": {
        "0:00": 30
      },
      "startid": 487174457,
      "endid": 487169369
    },
    {
      "id": 2840,
      "name": "Blackhorse Road => Black Horse",
      "length": 0.001370454088983439,
      "speed": {
        "0:00": 30
      },
      "startid": 487169369,
      "endid": 487169349
    },
    {
      "id": 2841,
      "name": "Black Horse => Black Horse",
      "length": 0.00041012888217990085,
      "speed": {
        "0:00": 30
      },
      "startid": 487169349,
      "endid": 487169388
    },
    {
      "id": 2842,
      "name": "Black Horse => Bedworth Rd / Oban Rd",
      "length": 0.007028217129543348,
      "speed": {
        "0:00": 30
      },
      "startid": 487169388,
      "endid": 370818876
    },
    {
      "id": 2843,
      "name": "Bedworth Rd / Oban Rd => Bedworth Rd / Ibstock Rd",
      "length": 0.002246773317446427,
      "speed": {
        "0:00": 30
      },
      "startid": 370818876,
      "endid": 370818878
    },
    {
      "id": 2844,
      "name": "Bedworth Rd / Ibstock Rd => Bedworth Rd / Ibstock Rd",
      "length": 0.00033837257572197685,
      "speed": {
        "0:00": 30
      },
      "startid": 370818878,
      "endid": 370818879
    },
    {
      "id": 2845,
      "name": "Bedworth Rd / Ibstock Rd => Bedworth Rd / Oban Rd",
      "length": 0.0033466396594159123,
      "speed": {
        "0:00": 30
      },
      "startid": 370818879,
      "endid": 370818877
    },
    {
      "id": 2846,
      "name": "Bedworth Rd / Oban Rd => Longford Rd / Longford Square",
      "length": 0.0026911415013017555,
      "speed": {
        "0:00": 30
      },
      "startid": 370818877,
      "endid": 370818874
    },
    {
      "id": 2847,
      "name": "Longford Rd / Longford Square => Longford Rd / Longford Square",
      "length": 0.0003155618639778003,
      "speed": {
        "0:00": 30
      },
      "startid": 370818874,
      "endid": 370818873
    },
    {
      "id": 2848,
      "name": "Longford Rd / Longford Square => Longford Rd / Vinecote Rd",
      "length": 0.0027949190256651227,
      "speed": {
        "0:00": 30
      },
      "startid": 370818873,
      "endid": 370818872
    },
    {
      "id": 2849,
      "name": "Longford Rd / Vinecote Rd => Longford Rd / Oakmoor Rd",
      "length": 0.0011475531403839034,
      "speed": {
        "0:00": 30
      },
      "startid": 370818872,
      "endid": 370818871
    },
    {
      "id": 2850,
      "name": "Longford Rd / Oakmoor Rd => Longford Rd / Longford Bridge",
      "length": 0.0032066862163273296,
      "speed": {
        "0:00": 30
      },
      "startid": 370818871,
      "endid": 370819748
    },
    {
      "id": 2851,
      "name": "Longford Rd / Longford Bridge => Longford Rd / Windmill Rd",
      "length": 0.0014970952808711533,
      "speed": {
        "0:00": 30
      },
      "startid": 370819748,
      "endid": 370819732
    },
    {
      "id": 2852,
      "name": "Longford Rd / Windmill Rd => Longford Rd / Dovedale Avenue",
      "length": 0.0010496597639259562,
      "speed": {
        "0:00": 30
      },
      "startid": 370819732,
      "endid": 370818870
    },
    {
      "id": 2853,
      "name": "Longford Rd / Dovedale Avenue => AG",
      "length": 0.0021072323103976083,
      "speed": {
        "0:00": 30
      },
      "startid": 370818870,
      "endid": 370818869
    },
    {
      "id": 2854,
      "name": "AG => AF",
      "length": 0.0008466729474816734,
      "speed": {
        "0:00": 30
      },
      "startid": 370818869,
      "endid": 370818867
    },
    {
      "id": 2855,
      "name": "AF => Foleshill Rd / The Wheatsheaf",
      "length": 0.001456813598235208,
      "speed": {
        "0:00": 30
      },
      "startid": 370818867,
      "endid": 370818864
    },
    {
      "id": 2856,
      "name": "Foleshill Rd / The Wheatsheaf => Foleshill Rd / The Wheatsheaf",
      "length": 0.00031738230889481126,
      "speed": {
        "0:00": 30
      },
      "startid": 370818864,
      "endid": 370818865
    },
    {
      "id": 2857,
      "name": "Foleshill Rd / The Wheatsheaf => Foleshill Rd / Old Church Rd",
      "length": 0.0031598401984935013,
      "speed": {
        "0:00": 30
      },
      "startid": 370818865,
      "endid": 370818863
    },
    {
      "id": 2858,
      "name": "Foleshill Rd / Old Church Rd => Foleshill Rd / Old Church Rd",
      "length": 0.0003347000000000211,
      "speed": {
        "0:00": 30
      },
      "startid": 370818863,
      "endid": 370818862
    },
    {
      "id": 2859,
      "name": "Foleshill Rd / Old Church Rd => Foleshill Rd / Phoenix Way",
      "length": 0.0035533042270538776,
      "speed": {
        "0:00": 30
      },
      "startid": 370818862,
      "endid": 370818832
    },
    {
      "id": 2860,
      "name": "Foleshill Rd / Phoenix Way => Foleshill Rd / Phoenix Way",
      "length": 0.0002803520108717694,
      "speed": {
        "0:00": 30
      },
      "startid": 370818832,
      "endid": 370818834
    },
    {
      "id": 2861,
      "name": "Foleshill Rd / Phoenix Way => Foleshill Rd / Cross Rd",
      "length": 0.0016837137820924367,
      "speed": {
        "0:00": 30
      },
      "startid": 370818834,
      "endid": 370818830
    },
    {
      "id": 2862,
      "name": "Foleshill Rd / Cross Rd => Foleshill Rd / Cross Rd",
      "length": 0.0004945206264681952,
      "speed": {
        "0:00": 30
      },
      "startid": 370818830,
      "endid": 370818831
    },
    {
      "id": 2863,
      "name": "Foleshill Rd / Cross Rd => Foleshill Rd / Family Centre",
      "length": 0.0026930447174148245,
      "speed": {
        "0:00": 30
      },
      "startid": 370818831,
      "endid": 370819702
    },
    {
      "id": 2864,
      "name": "Foleshill Rd / Family Centre => Foleshill Rd / Family Centre",
      "length": 0.00016455625178377943,
      "speed": {
        "0:00": 30
      },
      "startid": 370819702,
      "endid": 370819703
    },
    {
      "id": 2865,
      "name": "Foleshill Rd / Family Centre => Foleshill Rd / Station St",
      "length": 0.0014088894953136236,
      "speed": {
        "0:00": 30
      },
      "startid": 370819703,
      "endid": 370818829
    },
    {
      "id": 2866,
      "name": "Foleshill Rd / Station St => Foleshill Rd / Station St",
      "length": 0.0013386575364890566,
      "speed": {
        "0:00": 30
      },
      "startid": 370818829,
      "endid": 370818827
    },
    {
      "id": 2867,
      "name": "Foleshill Rd / Station St => Foleshill Rd / Broad St",
      "length": 0.0028052413532526385,
      "speed": {
        "0:00": 30
      },
      "startid": 370818827,
      "endid": 370818825
    },
    {
      "id": 2868,
      "name": "Foleshill Rd / Broad St => Foleshill Rd / Broad St",
      "length": 0.00038016818646532426,
      "speed": {
        "0:00": 30
      },
      "startid": 370818825,
      "endid": 370818826
    },
    {
      "id": 2869,
      "name": "Foleshill Rd / Broad St => Foleshill Rd / Courtaulds Way",
      "length": 0.004239609710810101,
      "speed": {
        "0:00": 30
      },
      "startid": 370818826,
      "endid": 370818780
    },
    {
      "id": 2870,
      "name": "Foleshill Rd / Courtaulds Way => Foleshill Rd / Courtaulds Way",
      "length": 0.00035180778843009035,
      "speed": {
        "0:00": 30
      },
      "startid": 370818780,
      "endid": 370818784
    },
    {
      "id": 2871,
      "name": "Foleshill Rd / Courtaulds Way => Foleshill Rd / Cashs Lane",
      "length": 0.004273169018420262,
      "speed": {
        "0:00": 30
      },
      "startid": 370818784,
      "endid": 370818776
    },
    {
      "id": 2872,
      "name": "Foleshill Rd / Cashs Lane => Foleshill Rd / Cashs Lane",
      "length": 0.00022125555360341274,
      "speed": {
        "0:00": 30
      },
      "startid": 370818776,
      "endid": 370818774
    },
    {
      "id": 2873,
      "name": "Foleshill Rd / Cashs Lane => Foleshill Rd / Eagle St",
      "length": 0.0011237341055589636,
      "speed": {
        "0:00": 30
      },
      "startid": 370818774,
      "endid": 370818765
    },
    {
      "id": 2874,
      "name": "Foleshill Rd / Eagle St => Foleshill Rd / Eagle St",
      "length": 0.001522061907418469,
      "speed": {
        "0:00": 30
      },
      "startid": 370818765,
      "endid": 370818766
    },
    {
      "id": 2875,
      "name": "Foleshill Rd / Eagle St => Foleshill Rd / City Engineers",
      "length": 0.0027907170565999295,
      "speed": {
        "0:00": 30
      },
      "startid": 370818766,
      "endid": 370818762
    },
    {
      "id": 2876,
      "name": "Foleshill Rd / City Engineers => Foleshill Rd / City Engineers",
      "length": 0.00022393115013730707,
      "speed": {
        "0:00": 30
      },
      "startid": 370818762,
      "endid": 370818764
    },
    {
      "id": 2877,
      "name": "Foleshill Rd / City Engineers => Foleshill Rd / Leicester Row",
      "length": 0.0016005044017478598,
      "speed": {
        "0:00": 30
      },
      "startid": 370818764,
      "endid": 370818761
    },
    {
      "id": 2878,
      "name": "Foleshill Rd / Leicester Row => Foleshill Rd / Leicester Row",
      "length": 0.00040428367515873303,
      "speed": {
        "0:00": 30
      },
      "startid": 370818761,
      "endid": 370818758
    },
    {
      "id": 2879,
      "name": "Foleshill Rd / Leicester Row => BS1",
      "length": 0.003915537353925627,
      "speed": {
        "0:00": 30
      },
      "startid": 370818758,
      "endid": 370817728
    },
    {
      "id": 2880,
      "name": "BS1 => BS2",
      "length": 0.0006854744707142306,
      "speed": {
        "0:00": 30
      },
      "startid": 370817728,
      "endid": 370817727
    }
  ]
}""")


