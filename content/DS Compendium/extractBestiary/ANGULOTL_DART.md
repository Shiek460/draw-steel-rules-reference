```statblock
name: "ANGULOTL DART"
Level: "1" 
roles: 
  - MINION 
  - ARTILLERY 
ancestry: 
  - Angulotl
  - Humanoid 
ev: 3 for four minions 
stamina: 3 
immunities: poison 2 
speed: 5 (swim, climb) 
size: 1S / 
stability: 0 
with-captain: Ranged distance +4 
free_strike: 2 
characteristics:
  - 0 
  - +2 
  - +1 
  - 0 
  - 0 
actions:
  - name: "Poison Dart"
    desc: "
      <br />**Type** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 8 
      <br />**Target** 1 creature or object per minion 
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage 
      <br />★ 12–16 4 poison damage 
      <br />✸ 17 5 poison damage 
      <br />**Effect** This ability has an edge on targets that don’t have full stamina."
traits:
  - name: "Toxiferous"
    desc: "- When an adjacent enemy grabs or uses a melee ability against the dart, they take 2 poison damage."
```