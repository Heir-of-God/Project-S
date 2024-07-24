teams = int(input())
home_uniforms_counter = {}
guest_uniforms_counter = {}
res = 0

for _ in range(teams):
    home, guest = input().split()
    home_uniforms_counter[home] = home_uniforms_counter.get(home, 0) + 1
    guest_uniforms_counter[guest] = guest_uniforms_counter.get(guest, 0) + 1


for home_uniform, n_teams in home_uniforms_counter.items():
    if home_uniform in guest_uniforms_counter:
        res += n_teams * guest_uniforms_counter[home_uniform]

print(res)
