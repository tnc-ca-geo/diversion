# Create a 'variable' table in the CUAHSI format
# For a full description of the tables, variables, and format, see: https://www.cuahsi.org/uploads/pages/img/Advanced_Formatting_Template.xlsx
import pandas as pd
import os.path


outname = os.path.join( os.getcwd(), '..', 'Variables.csv' )


columns = ["VariableCode",
          "VariableName",
          "Speciation",
          "VariableUnitsName",
          "SampleMedium",
          "ValueType",
          "IsRegular",
          "TimeSupport",
          "TimeUnitsName",
          "DataType",
          "GeneralCategory",
          "NoDataValue"]

row1 = [['GPM_5min',
        'Discharge',
        'Not Applicable',
        'gallons per minute',
        'Surface water',
        'Field Observation',
        'True',
        '5',
        'minute',
        'Continuous',
        'Hydrology',
        '-9999']]

df = pd.DataFrame(row1,columns=columns)
df.to_csv(outname, encoding='utf-8', index=False)
