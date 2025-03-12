```statblock
name: "ANGULOTL SLINK"
level: 1 
roles:
  - BAND 
  - AMBUSHER 
ancestry:
  - Angulotl
  - Humanoid 
ev: 3 
stamina: 15 
immunities: poison 2 
speed: 7 (swim, climb) 
size: 1S / 
stability: 0 
free_strike: 2 
characteristics: 
  - +1 
  - +2 
  - 0 
  - 0 
  - 0 
actions:
  - name: "Tonguelash"
    desc: " 
      <br />**Signature** 
      <br />**Keywords** Attack, Melee, Weapon 
      <br />**Distance** Melee 6 
      <br />**Target** 1 creature or object 
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage; pull 2 
      <br />★ 12–16 6 damage; pull 4 
      <br />✸ 17 7 damage; pull 6 
      <br />**Effect** The target is wet (save ends) (see Wet). Allies targeted by this ability take no damage and are pulled 6, ignoring stability."
maneuvers:
  - name: "Hop To It (Free Maneuver)"
    desc: "
      <br />**Cost** 1 Malice 
      <br />**Keywords** — 
      <br />**Distance** Self 
      <br />**Target** Self 
      <br />**Effect** The slink jumps 3 squares. If the slink lands in cover or concealment, they can immediately Hide."
traits:
  - name: "Toxiferous" 
    desc: "When an adjacent enemy grabs or uses a melee ability against the slink, they take 3 poison damage."
  - name: "Adhesive"
    desc: "The slink excretes residue into their square at the end of each of their turns. A non-angulotl creature or object that enters or leaves the square must use a maneuver to withstand the adhesive or be restrained (EoT). "
```