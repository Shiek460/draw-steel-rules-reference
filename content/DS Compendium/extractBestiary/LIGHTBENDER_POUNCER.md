# LIGHTBENDER POUNCER
```statblock
name: "LIGHTBENDER POUNCER"
level: 3
roles:
  - TROOP
  - HARRIER
ancestry:
  - Beast
  - Lightbender
ev: 20
stamina: 100
speed: 10
size: 2
stability: 1
free_strike: 5
characteristics:
  - +2
  - +2
  - −3
  - +1
  - −1
actions:
  - name: "Pounce"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage; A< 1 [[prone]]
      <br />✸ 17+ 14 damage; A< 2 [[prone]] 
      <br />**Effect:** The pouncer makes a free strike against each target they have knocked [[prone]]."
  - name: "Sparkling Tail Whip"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 2 burst
      <br />**Target** All enemies and objects in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 7 damage; A< 1 dazzled (save ends)
      <br />✸ 17+ 10 damage; A< 2 dazzled (save ends) 
      <br />**Effect:** A dazzled creature has a bane on strikes and can’t have [[Line of Effect]] to targets who aren’t adjacent to them."
maneuvers:
  - name: "Illusory Feint"
    desc: "
      <br />**Cost** 5 Malice
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 cube within 10
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 R< 0 [[dazed]] (save ends)
      <br />★ 12–16 R< 1 [[dazed]] (save ends)
      <br />✸ 17+ R< 2 [[dazed]] (save ends) 
      <br />**Effect:** Targets [[dazed]] by this ability have a speed of 0 while [[dazed]]. If a [[dazed]] target takes damage or if someone else spends an action to shake the creature out of their stupor, the condition ends."
ta:
  - name: "Striking Afterimage"
    desc: "
      <br />**Keywords** Magic 
      <br />**Trigger** The pouncer takes damage from a strike.
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The pouncer halves the damage, doesn’t suffer any effect associated with it, and teleports 5 squares. The pouncer makes a free strike if they teleport into a space adjacent to an enemy."
traits:
  - name: "Avoidance"
    desc: "The pouncer always treats a save ends effect as an EoT effect."

```
