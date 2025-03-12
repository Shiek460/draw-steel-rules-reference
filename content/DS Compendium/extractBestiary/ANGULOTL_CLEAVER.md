```statblock
name: "ANGULOTL CLEAVER" 
level: 1 
roles:
  - MINION 
  - AMBUSHER 
ancestry:
  - Angulotl 
  - Humanoid
ev: 3 for four minions 
stamina: 4 
immunities: poison 2 
speed: 6 (swim, climb) 
size: 1S / 
stability: 0 
with-captain: Strike damage +1 
free_strike: 2 
characteristics:
  - 0 
  - +2 
  - 0 
  - +1 
  - 0 
actions:
  - name: "Hop & Chop"
    desc: "
      <br />**Type** Signature 
      <br />**Keywords** Melee, Strike, Weapon 
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion 
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage 
      <br />★ 12–16 4 damage 
      <br />✸ 17 5 damage 
      <br />Effect The cleaver jumps 4 squares before or after attacking. "
traits:
  - name: "Toxiferous"
    desc: "- When an adjacent enemy grabs or uses a melee ability against the cleaver, they take 2 poison damage."
```