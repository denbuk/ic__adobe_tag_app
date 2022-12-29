from collections import namedtuple
from datetime import datetime as dt
from PIL import Image
import altair as alt
import math
import pandas as pd
import numpy as np
import streamlit as st
import requests
import json
import time

with st.echo(code_location='below'):
    with st.expander("Delete campaign"):
        if st.text_input("Enter passcode") == "OnlineMO2":
            if st.button('Delete campaign'):
                with st.spinner('Wait for it...'):
                    time.sleep(2)
    
