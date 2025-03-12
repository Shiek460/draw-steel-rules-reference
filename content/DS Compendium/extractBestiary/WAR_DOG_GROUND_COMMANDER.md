# WAR DOG GROUND COMMANDER
```statblock
name: "WAR DOG GROUND COMMANDER"
level: 3
roles:
  - LEADER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 20
stamina: 120
speed: 5
size: 1M /
stability: 2
free_strike: 5
characteristics:
  - +3
  - +2
  - +3
  - +2
  - +2
actions:
  - name: "Conditioning Spear"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; pull 1
      <br />★ 12–16 12 damage; pull 2
      <br />✸ 17+ 15 damage; pull 3 
      <br />**Effect:** One ally within 10 squares of the commander can make a free strike. 
      <br />**1 Malice** A target who is adjacent to the ground commander after this ability is resolved is I< 2 [[grabbed]] (save ends). This grab can’t be escaped using the Escape Grab maneuver. The ground commander can grab up to two creatures at a time."
maneuvers:
  - name: "Highest Posthumous Promotion"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 10 burst
      <br />**Target** Each war dog with a loyalty collar 
      <br />**Effect:** The ground commander selects any number of targets’ loyalty collars and detonates them, killing the target instantly."
ta:
  - name: "Final Orders"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One ally 
      <br />**Trigger** The target has a condition imposed on them, is force moved, or is killed. 
      <br />**Effect:** The target can move up to their speed and make a free strike before the triggering effect happens."
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the ground commander can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Loyalty Collar"
    desc: "When the ground commander dies, they explode, dealing 2d6 damage to each adjacent enemy."
va:
  - name: "Combined Arms (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** Each ally 
      <br />**Effect:** Each target can make a ranged free strike, then immediately use the Charge action."
  - name: "Make an Example of Them (Villain Action 2)"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One enemy 
      <br />**Effect:** Each ally within 5 squares of the target can move up to their speed and make a free strike against the target. The target is then I< 2 [[frightened]] of the ground commander (save ends)."
  - name: "Claim Them for the Body Banks (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 10 burst
      <br />**Target** Each ally 
      <br />**Effect:** Each target can shift 2 and use the Grab maneuver. For the rest of the encounter, each enemy has a bane on escaping grabs."


```
