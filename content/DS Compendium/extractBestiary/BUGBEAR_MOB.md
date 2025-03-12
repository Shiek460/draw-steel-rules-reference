# BUGBEAR MOB
```statblock
name: "BUGBEAR MOB"
level: 5
roles:
  - MINION
  - BRUTE
ancestry:
- Bugbear 
- Goblin 
- Humanoid 
- Fey 
- Swarm
ev: 7 for four minions
stamina: 10
speed: 6
size: 3 /
stability: 2
with-captain: Strike damage +2
free_strike: 3
characteristics:
  - +3
  - -1
  - 0
  - +1
  - 0
actions:
  - name: "Mug and Tear"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 damage; pull 2
      <br />★ 12–16 6 damage; pull 3
      <br />✸ 17+ 7 damage; pull 4; [[grabbed]] 
      <br />**Effect:** The target can be pulled into the mob without inflicting damage."
traits:
  - name: "Swarm"
    desc: "The mob can move through squares as if they were size -1M, and can occupy other creatures’ spaces. At the start of the mob’s turn, they can make a free strike against each creature they share a square with."


```
