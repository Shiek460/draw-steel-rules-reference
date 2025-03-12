# LIGHTBENDER
```statblock
name: "LIGHTBENDER"
level: 3
roles:
  - TROOP
  - AMBUSHER
ancestry:
  - Beast
  - Lightbender
ev: 20
stamina: 100
speed: 10
size: 2 /
stability: 1
free_strike: 6
characteristics:
  - +2
  - +1
  - −3
  - +1
  - −1
actions:
  - name: "Flash Swipe"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 14 damage
      <br />✸ 17+ 18 damage 
      <br />**Effect:** The lightbender deals an additional 4 damage if they have an edge."
  - name: "Piercing Tails"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 damage
      <br />★ 12–16 12 damage; M< 1 [[bleeding]] (save ends)
      <br />✸ 17+ 15 damage; M< 2 [[bleeding]] (save ends) 
      <br />**Effect:** A creature who is [[bleeding]] from this ability has a bane on tests to search for the lightbender until the condition ends."
maneuvers:
  - name: "Hypnotic Mane"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 I< 0 [[dazed]] (save ends)
      <br />★ 12–16 I< 1 [[dazed]] (save ends)
      <br />✸ 17+ I< 2 [[dazed]] (save ends) 
      <br />**Effect:** Targets [[dazed]] by this ability have a speed of 0 while [[dazed]]. If a [[dazed]] target takes damage or if someone else spends an action to shake the creature out of their stupor, the condition ends."
ta:
  - name: "Stalker’s Afterimage"
    desc: "
      <br />**Keywords** Magic 
      <br />**Trigger** The lightbender takes damage from a strike.
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The lightbender halves the damage, doesn’t suffer any effect associated with it, and teleports 5 squares. The lightbender immediately hides if they teleport into cover or concealment."
traits:
  - name: "Avoidance"
    desc: "The lightbender always treats a save ends effect as an EoT effect."

```
