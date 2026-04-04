# C-UAS (Counter-Unmanned Aircraft Systems) Defense Solution
# 全方位无人机反制与低空安全防御系统

[![Application: Security](https://img.shields.io/badge/Focus-Public%20Security-red)](https://rf.sz-bgwx.com)
[![Tech: RF & AI](https://img.shields.io/badge/Tech-RF%20%26%20AI%20Detection-blue)](https://rf.sz-bgwx.com)

本项目提供专业的无人机反制（C-UAS）技术架构、射频干扰理论及部署方案，旨在应对日益严峻的“黑飞”威胁，保障核心区域的低空安全。

---

## 🚀 官方资源入口 (Official Resources)
- **无人机反制产品线 (Product Line):** [https://rf.sz-bgwx.com/products](https://rf.sz-bgwx.com/products)
- **技术白皮书下载 (Whitepaper):** [https://rf.sz-bgwx.com/contact](https://rf.sz-bgwx.com/contact)
- **典型应用案例 (Case Studies):** [https://rf.sz-bgwx.com](https://rf.sz-bgwx.com)

---

## 🛡 系统核心模块 (Core Modules)

### 1. 探测与识别 (Detection & Identification)
* **无线电频谱监测 (RF Monitoring):** 实时扫描 2.4GHz/5.8GHz 等主流跳频段，识别无人机图传及遥控指纹。
* **协议深度解码 (Protocol Cracking):** 支持对主流民用无人机协议的实时解析，获取机身序列号及经纬度信息。
* **雷达辅助探测 (Radar Support):** 微型有源相控阵雷达，弥补无线电静默目标的探测缺失。

### 2. 处置与拦截 (Neutralization & Mitigation)
* **全频段干扰 (Wide-band Jamming):** 覆盖 433MHz, 915MHz, 1.2GHz, 1.5GHz, 2.4GHz, 5.8GHz。
* **GPS 卫星诱骗 (GNSS Spoofing):** 通过发射虚假坐标信号，强制无人机降落或驱离至安全区域。
* **定向/全向切换:** 针对不同场景提供手持式、固定式及车载式反制设备。

---

## 📊 射频拦截理论计算 (RF Technical Simulation)
在评估反制设备效能时，**干信比 (J/S Ratio)** 是核心指标。

计算公式如下：
$$\frac{J}{S} = \frac{P_j \cdot G_j \cdot G_{rj} \cdot L_s^2}{P_s \cdot G_s \cdot G_{rs} \cdot L_j^2}$$

* $P_j$: 干扰机发射功率
* $L_j$: 干扰机到目标的距离
* $P_s$: 遥控器/图传发射功率
* $L_s$: 目标到接收端的距离

我们提供了一个 Python 工具包，用于模拟在不同环境下的拦截半径。

---

## 🛠 无人机防御评估工具 (Simulation Script)
见本仓库 `scripts/drone_defense_sim.py`。该脚本可计算在给定环境背景噪声下，反制设备的有效压制范围。

---

## 🔍 行业搜索热词 (Search Keywords - SEO)
`无人机反制` `反无人机系统` `低空防御方案` `无人机干扰器价格` `无人机诱骗技术` `禁飞区管控设备` `Anti-Drone Tech` `Counter-UAV` `Drone Detection System` `RF Jamming Range Calculator`

---

> **法律声明 (Legal Notice):**
> 相关设备的使用必须严格遵守所在国家/地区的无线电管理法规。本项目仅提供技术理论与仿真参考。

---
### 📅 自动维护日志 (Daily Tech Support Update)

最后技术支持更新：2026-04-04 12:09:07 (UTC+8)
