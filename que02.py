import numpy as np
import matplotlib.pyplot as plt

# Function to calculate heat exchanger performance
def heat_exchanger(T_h_in, T_c_in, m_hot, m_cold):
    Cp = 4180  # Specific heat capacity of water (J/kg·K)
    
    # Maximum possible heat transfer
    Q_max = min(m_hot, m_cold) * Cp * (T_h_in - T_c_in)
    
    # Assume an efficiency (effectiveness)
    effectiveness = 0.85  # 85% efficient
    
    # Actual heat transfer
    Q_actual = effectiveness * Q_max
    
    # Outlet temperatures
    T_h_out = T_h_in - (Q_actual / (m_hot * Cp))
    T_c_out = T_c_in + (Q_actual / (m_cold * Cp))
    
    return T_h_out, T_c_out, Q_actual, effectiveness

# Function to plot temperature profiles
def plot_temperature_profile(T_h_in, T_c_in, T_h_out, T_c_out):
    x = np.linspace(0, 1, 100)  # Assume normalized exchanger length
    T_hot_profile = np.linspace(T_h_in, T_h_out, 100)
    T_cold_profile = np.linspace(T_c_in, T_c_out, 100)
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, T_hot_profile, label="Hot Fluid Temperature", color='r')
    plt.plot(x, T_cold_profile, label="Cold Fluid Temperature", color='b')
    plt.xlabel("Normalized Heat Exchanger Length")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Profiles in Heat Exchanger")
    plt.legend()
    plt.grid()
    plt.show()

# Example Inputs
T_h_in = 80  # Inlet temperature of hot fluid (°C)
T_c_in = 30  # Inlet temperature of cold fluid (°C)
m_hot = 0.5  # Mass flow rate of hot fluid (kg/s)
m_cold = 0.8  # Mass flow rate of cold fluid (kg/s)

# Compute heat exchanger performance
T_h_out, T_c_out, Q_actual, effectiveness = heat_exchanger(T_h_in, T_c_in, m_hot, m_cold)

# Print results
print(f"Hot Fluid Outlet Temperature: {T_h_out:.2f} °C")
print(f"Cold Fluid Outlet Temperature: {T_c_out:.2f} °C")
print(f"Actual Heat Transfer: {Q_actual:.2f} J")
print(f"Heat Exchanger Effectiveness: {effectiveness * 100:.2f}%")

# Plot temperature profiles
plot_temperature_profile(T_h_in, T_c_in, T_h_out, T_c_out)
