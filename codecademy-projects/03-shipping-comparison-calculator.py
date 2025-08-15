weight = float(input("How much does the package weigh (lbs)? "))
ground_flat_charge = 20
premium_cost = 125

# Ground Shipping
if weight <= 2:
  ground_cost = weight * 1.5 + ground_flat_charge

elif weight <= 6:
  ground_cost = weight * 3 + ground_flat_charge

elif weight <= 10:
  ground_cost = weight * 4 + ground_flat_charge

else:
  ground_cost = weight * 4.75 + ground_flat_charge

print(f"Standard Ground Shipping Cost: ${ground_cost:.2f}")

# Premium Ground Shipping
print(f"Premium Ground Shipping Cost: ${premium_cost:.2f}")

# Drone Shipping
if weight <= 2:
  drone_cost = weight * 4.5

elif weight <= 6:
  drone_cost = weight * 9

elif weight <= 10:
  drone_cost = weight * 12

else:
  drone_cost = weight * 14.25

print(f"Drone Shipping Cost: ${drone_cost:.2f}")

cheapest = min(ground_cost, premium_cost, drone_cost)

if cheapest == ground_cost:
  print(f"Cheapest method: Standard Ground Shipping (${ground_cost:.2f})")

elif cheapest == premium_cost:
  print(f"Cheapest method: Premium Ground Shipping (${premium_cost:.2f})")

else:
  print(f"Cheapest method: Drone Shipping (${drone_cost:.2f})")
