import math

def jamming_range_calc(tx_power_watt, antenna_gain_dbi, target_sensitivity_dbm, frequency_mhz):
    """
    计算干扰信号的有效覆盖距离
    """
    # 将功率从瓦特转换为 dBm
    tx_power_dbm = 10 * math.log10(tx_power_watt * 1000)
    
    # 路径损耗常数
    c = 3e8
    lambda_val = c / (frequency_mhz * 1e6)
    
    # 基于 Friis 传输方程反推距离
    # Pr = Pt + Gt + Gr + 20log10(lambda / 4*pi*d)
    # 简化版：d = 10^((Pt + Gt + Gr - Pr - 22) / 20) / frequency
    
    # 假设天线增益为 10dBi
    dist = math.pow(10, (tx_power_dbm + antenna_gain_dbi - target_sensitivity_dbm - 32.4) / 20) / (frequency_mhz / 1000)
    
    return round(dist, 2)

if __name__ == "__main__":
    print("--- 无人机反制压制半径评估工具 ---")
    p_watt = 20  # 20W 发射功率
    freq = 2400  # 2.4GHz 频段
    gain = 12    # 定向天线增益
    sens = -90   # 无人机接收灵敏度
    
    range_m = jamming_range_calc(p_watt, gain, sens, freq)
    print(f"频率: {freq} MHz | 功率: {p_watt} W")
    print(f"理论最大压制距离: {range_m} 米")
    print(f"\n获取完整硬件方案，请访问: https://rf.sz-bgwx.com")
