# GOBLIN ASSASSIN
```statblock
name: "GOBLIN ASSASSIN"
level: 1
roles:
  - BAND
  - AMBUSHER
ancestry:
  - Goblin
  - Humanoid
ev: 3
stamina: 15
speed: 6 (climb)
size: 1S /
stability: 0
free_strike: 2
characteristics:
  - −2
  - +2
  - +0
  - +0
  - −2
actions:
  - name: "Sword Stab"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 6 damage
      <br />✸ 17+ 7 damage 
      <br />**Effect:** This ability deals an additional 2 damage if the scoundrel has an edge on the power roll."
  - name: "Shadow Chains"
    desc:
      "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** Three creatures
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 corruption damage; A< 0 [[restrained]] (save ends)
      <br />★ 12–16 4 corruption damage; A< 1 [[restrained]] (save ends)
      <br />✸ 17+ 5 corruption damage; A< 2 [[restrained]] (save ends)"
traits:
  - name: "Crafty"
    desc: "The goblin doesn’t provoke opportunity attacks by moving."
  - name: "Hide While Observed"
    desc: "The assassin can take the Hide maneuver even while observed, though they still must have cover or concealment."


```
