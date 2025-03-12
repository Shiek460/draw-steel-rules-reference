# WAR SPIDER
```statblock
name: "WAR SPIDER"
level: 1
roles:
  - TROOP
  - MOUNT
ancestry:
  - Animal
  - Goblin
ev: 12
stamina: 60
speed: 7 (climb)
size: 3 /
stability: 2
free_strike: 4
characteristics:
  - +2
  - +1
  - −4
  - +0
  - −3
actions:
  - name: "Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 poison damage
      <br />★ 12–16 11 poison damage
      <br />✸ 17+ 14 poison damage; M< 2 [[weakened]] (save ends) <br />**2 Malice** M< 3 [[weakened]] (save ends)."
  - name: "Leg Blade"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 12 damage"
  - name: "Trample"
    desc:
      "<br />**Cost** 5 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The spider shifts up to their speed and makes a Leg Blade strike against each creature who comes within 1 of the spider during the move. The spider makes one power roll against all targets."
maneuvers:
  - name: "Web"
    desc: "
      <br />**Keywords** Area, Weapon
      <br />**Distance** 3 cube within 1
      <br />**Target** All creatures in the cube
      <br />`dice: 2d10 +
      <br />✦ ≤11 A< 0 [[restrained]] (save ends)
      <br />★ 12–16 A< 1 [[restrained]] (save ends)
      <br />✸ 17+ A< 2 [[restrained]] (save ends)
      <br />**Distance** The affected area is considered difficult terrain for enemies."
ta:
  - name: "Skitter"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The spider or an ally riding the spider is targeted by an ability. 
      <br />**Effect:** The spider shifts 2. Any damage dealt by the triggering ability is halved."
traits:
  - name: "Ride Launcher"
    desc: "An ally who leaps off the back of the spider can jump up to 6 squares without a test, and takes no damage if they fall during the jump. After the jump, the first melee strike an ally makes on the same turn gains an edge."
  - name: "Wide Back"
    desc: "Two of the spider’s size: 1 allies can occupy the same space while riding the spider."


```
