# BUGBEAR COMMANDER
```statblock
name: "BUGBEAR COMMANDER"
level: 2
roles:
  - TROOP
  - SUPPORT
ancestry:
- Bugbear 
- Goblin 
- Humanoid 
- Fey
ev: 16
stamina: 80
speed: 5
size: 1L /
stability: 0
free_strike: 5
characteristics:
  - +2
  - +1
  - +2
  - 0
  - 0
actions:
  - name: "Inspiring Swordplay"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Attack, Melee, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 10 damage
      <br />✸ 17+ 13 damage; one target is [[grabbed]] 
      <br />**Effect:** 1 ally within 5 of the commander has an edge on their next attack until the start of the commander’s next turn."
  - name: "You Next!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 8
      <br />**Target** 1 ally 
      <br />**Effect:** The target moves up to their speed and uses a signature action."
  - name: "Fall Back!"
    desc:
      "
      <br />**Cost** 5 Malice
      <br />**Keywords** —
      <br />**Distance** Self and 5 burst
      <br />**Target** Self and all allies 
      <br />**Effect:** Each target shifts up to their speed. Each target can use the Throw maneuver if they are grabbing a creature or object."
maneuvers:
  - name: "Throw"
    desc: "
      <br />**Keywords** Attack, Melee
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object [[grabbed]] by the commander 
      <br />**Effect:** Vertical push 4. An ally target doesn’t take damage from being force moved."
ta:
  - name: "Catcher (Free Triggered Action)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** 1 size 1 creature or object 
      <br />**Trigger** The target is force moved into a square adjacent to the commander. 
      <br />**Effect:** The target is [[grabbed]] by the commander."
traits:
  - name: "The Commander’s Watching"
    desc: "While an ally has [[Line of Effect]] to the commander, the ally can end one condition afflicting them at the start of their turn."


```
