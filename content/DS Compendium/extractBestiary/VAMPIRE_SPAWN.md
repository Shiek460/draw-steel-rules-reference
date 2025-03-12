#+3
#Vampire
#+1
#name: "Exsanguinating Bite
#BAND
#Undead
#-1
#name: "Vampiric Celerity
#name: "Unslakable Bloodthirst
#HARRIER
#+2

# VAMPIRE SPAWN
```statblock
name: "VAMPIRE SPAWN"
level: 4
roles:
  - BAND
  - HARRIER
ancestry:
  - Undead
  - Vampire
ev: 6
stamina: 30
immunities: corruption 4, poison 4
speed: 5 (climb)
size: 1M /
stability: 0
free_strike: 2
characteristics:
  - +2
  - +3
  - -1
  - +1
  - +2
actions:
  - name: "Exsanguinating Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 corruption damage; M< 2 [[bleeding]] (save ends)
      <br />✸ 17+ 9 corruption damage; M< 3 [[bleeding]] (save ends) 
      <br />**Effect:** The vampire spawn regains stamina equal to the corruption damage they deal.
      <br />**1 Malice** The target takes an additional 3 corruption damage."
maneuvers:
  - name: "Vampiric Celerity"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The vampire spawn shifts 1 and then moves up to their speed. The next ability the vampire uses before the start of their next turn has an edge."
traits:
  - name: "Unslakable Bloodthirst"
    desc: "The vampire spawn has a speed of 10 while a creature is [[bleeding]] within 10. The vampire spawn must strike a [[bleeding]] creature on their turn if they are able to."

```
