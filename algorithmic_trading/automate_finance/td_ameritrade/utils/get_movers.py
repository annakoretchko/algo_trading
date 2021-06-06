import pandas as pd
import sys

def run(TDSession):

    # GET COMPX
    COMPX_down = pd.DataFrame(
                TDSession.get_movers(
                    market='$COMPX',
                    direction='down',
                    change='percent'
                ))

    COMPX_up = pd.DataFrame(
                TDSession.get_movers(
                    market='$COMPX',
                    direction='up',
                    change='percent'
                ))

    # GET DJI
    DJI_down = pd.DataFrame(
                TDSession.get_movers(
                    market='$DJI',
                    direction='down',
                    change='percent'
                ))
    DJI_up = pd.DataFrame(
                TDSession.get_movers(
                    market='$DJI',
                    direction='up',
                    change='percent'
                ))

    # GET SPX
    SPX_down = pd.DataFrame(
                TDSession.get_movers(
                    market='$SPX.X',
                    direction='down',
                    change='percent'
                ))
    SPX_up = pd.DataFrame(
                TDSession.get_movers(
                    market='$SPX.X',
                    direction='up',
                    change='percent'
                ))
    
    
    # COMPX combined
    COMPX_df = pd.concat([COMPX_up, COMPX_down])
    COMPX_df['change']  = (COMPX_df['change']  *100).round(1)    
    COMPX_df = COMPX_df.rename(columns={"change": "% change"})


    # DJI combined
    DJI_df = pd.concat([DJI_up, DJI_down])
    DJI_df['change']  = (DJI_df['change']  *100).round(1)    
    DJI_df = DJI_df.rename(columns={"change": "% change"})

    # SPX combined
    SPX_df = pd.concat([SPX_up, SPX_down])
    SPX_df['change']  = (SPX_df['change']  *100).round(1)    
    SPX_df = SPX_df.rename(columns={"change": "% change"})
   
    # print(COMPX_df)

    return COMPX_df ,DJI_df, SPX_df
    