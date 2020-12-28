Number


Format


Output


Description

x = 3.1415926


print(f"{x:.2f}")


3.14


2 decimal places

x = 3.1415926


print(f"{x:+.2f}")


+3.14


2 decimal places with sign

x = -1


print(f"{x:+.2f}")


-1.00


2 decimal places with sign

x = 3.1415926


print(f"{x:.0f}")


3


No decimal places (will round)

x = 5


print(f"{x:0>2d}")


05


Pad with zeros on the left

x = 1000000


print(f"{x:,}")


1,000,000


Number format with comma separator

x = 0.25


print(f"{x:.2%}")


25.00%


Format percentage

x = 1000000000


print(f"{x:.2e}")


1.00e+09


Exponent notation

x = 11


print(f"{x:>10d}")


........11


Right aligned

x = 11


print(f"{x:<10d}")


11........


Left aligned

x = 11


print(f"{x:^10d}")


....11....


Center aligned
