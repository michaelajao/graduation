import csv
from collections import defaultdict

# Read CSV
with open('rsvp-michael-phd-celebration.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Group by name and find max guest count
people_max_guests = {}
for row in data:
    name = row['full-name'].strip()
    guest_count = int(row['guest-count'])
    
    if name not in people_max_guests:
        people_max_guests[name] = guest_count
    else:
        people_max_guests[name] = max(people_max_guests[name], guest_count)

# Sort by guest count descending
sorted_people = sorted(people_max_guests.items(), key=lambda x: x[1], reverse=True)

# Calculate totals
total_people = len(sorted_people)
total_guests = sum(people_max_guests.values())

print("=" * 60)
print(f"RSVP ANALYSIS - Michael's PhD Celebration")
print("=" * 60)
print(f"\nTotal unique attendees: {total_people}")
print(f"Total attendees coming: {total_guests}")
print(f"Average guests per person: {total_guests / total_people:.1f}")

print("\n" + "=" * 60)
print("ATTENDEES BY GUEST COUNT")
print("=" * 60)

for name, count in sorted_people:
    print(f"{name:<40} {count} guest(s)")

# Group by guest count
print("\n" + "=" * 60)
print("SUMMARY BY GROUP SIZE")
print("=" * 60)
group_counts = defaultdict(int)
for count in people_max_guests.values():
    group_counts[count] += 1

for count in sorted(group_counts.keys()):
    print(f"{count} guest(s):  {group_counts[count]} attendee(s)")

print("\n" + "=" * 60)
