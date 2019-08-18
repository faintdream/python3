#!/usr/bin/env python

# this program demonstrates getting ENVIRONMENT_VARIABLE from the os and doing some acttion based on that.

import os 

def get_stage_status():
    stage = os.getenv("STAGE", default="dev").upper()
    output = "We are in " + stage + " server."
    if stage.startswith("PROD"):
        output = "DANGER!!!!!" + output 

    return output

result = get_stage_status()
print(result)

    
