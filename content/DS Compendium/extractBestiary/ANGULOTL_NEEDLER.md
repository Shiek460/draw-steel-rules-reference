```statblock
name: "ANGULOTL NEEDLER"
level: 1
roles:
  - BAND 
  - ARTILLERY 
ancestry:
  - Angulotl 
  - Humanoid 
ev: 3 
stamina: 10 
immunities: poison 2 
speed: 5 (swim, climb) 
size: 1S / 
stability: 0 
free_strike: 2 
characteristics: 
  - 0 
  - +2 
  - +1 
  - 0 
  - −1 
actions:
  - name: "Blowgun"
    desc: "
      <br />**Type** Signature 
      <br />**Keywords** Ranged, Strike, Weapon 
      <br />**Distance** Ranged 15 
      <br />**Target** 1 creature or object 
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 poison damage 
      <br />★ 12–16 6 poison damage 
      <br />✸ 17 7 poison damage 
      <br />**2 Malice** M< 2 weakened (save ends). The target takes 2 poison damage at the start of each of their turns while they are weakened by this ability."
maneuvers:
  - name: "Camoufroge" 
    desc: "
      <br />**Cost** 1 Malice 
      <br />**Keywords** — 
      <br />**Distance** Self 
      <br />**Target** Self (while Hiding) 
      <br />**Effect** The needler isn’t revealed after using their next action."
traits:
  - name: "Toxiferous"
    desc: "When an adjacent enemy grabs or uses a melee ability against the needler, they take 3 poison damage."
```