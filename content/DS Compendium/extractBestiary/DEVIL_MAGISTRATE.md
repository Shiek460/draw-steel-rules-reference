# DEVIL MAGISTRATE
```statblock
name: "DEVIL MAGISTRATE"
level: 6
roles:
  - TROOP
  - HARRIER
ancestry:
  - Devil
  - Infernal
ev: 32
stamina: 160
immunities: Fire 5
speed: 7
size: 1M /
stability: 0
free_strike: 7
characteristics:
  - +1
  - +3
  - 0
  - +1
  - +2
actions:
  - name: "Edge of the Law"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 damage
      <br />★ 12–16 15 damage
      <br />✸ 17+ 18 damage; R<  3 [[dazed]] (save ends) 
      <br />**Effect:** The magistrate can shift up to 3 squares before or after using this ability, or between targets."
  - name: "Verdict"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature
      <br />✸ ≤11 11 damage
      <br />★ 12–16 17+ damage
      <br />`dice: 2d10 + 3`
      <br />✦ 17+ 21 damage 
      <br />**Effect:** This ability has a double edge if the magistrate was hidden before using this ability and deals an additional 5 damage if the target is [[dazed]]."
maneuvers:
  - name: "Justice Turns Its Gaze"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The magistrate becomes hidden, even if they are being observed."
ta:
  - name: "Devilish Charm"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Magic
      <br />**Distance** Ranged 5
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature targets the magistrate with a strike. 
      <br />**Effect:** The target makes a Might test.
      <br />✸ ≤11 The magistrate chooses a new target for the strike
      <br />★ 12–16 The magistrate halves the incoming damage
      <br />✦ 17+ The target is [[dazed]] (EoT) Leading If the magistrate moves away from an enemy who is adjacent to one of the magistrate’s allies, the movement is considered shifting."
traits:
  - name: "True Name"
    desc: "If a creature within 10 squares of the magistrate speaks the magistrate’s true name aloud, the magistrate loses their immunities, the additional effects on their signature action, and their Devilish Charm ability."


```
