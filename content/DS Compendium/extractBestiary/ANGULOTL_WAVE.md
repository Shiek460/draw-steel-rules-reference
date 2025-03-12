```statblock
name: "ANGULOTL WAVE" 
level: 1 
roles:
  - BAND 
  - CONTROLLER 
ancestry:
  - Angulotl
  - Humanoid 
ev: 3 
stamina: 10 
immunities: poison 2 
speed: 5 (swim, climb) 
size: 1S / 
stability: 0 
free_strike: 1 
characteristics: 
  - 0 
  - 0 
  - 0 
  - +2 
  - +2 
actions:
  - name: "Refulgent Beams"
    desc: "
      <br />**Type** Signature 
      <br />**Keywords** Magic, Ranged, Strike 
      <br />**Distance** Ranged 8 
      <br />**Target** 2 creatures or objects 
      <br />`dice: 2d10 + 2` 
      <br />✸ ≤11 3 holy damage 
      <br />★ 12–16 4 holy damage; R<1 illuminated (save ends) 
      <br />✦ 17 5 holy damage; R<2 illuminated (save ends) 
      <br />**Effect** Illuminated creatures and objects can’t Hide or turn invisible, and strikes made against them have an edge until the condition ends."
  - name: "Noxious Bubble"
    desc: "
      <br />**Cost** 3 Malice 
      <br />**Keywords** Area, Magic, Ranged 
      <br />**Distance** 3 Cube of unoccupied space within 10 
      <br />**Target** Special 
      <br />**Effect** A bubble of toxic gas fills the area that lasts until the end of the encounter. If a creature or object touches the bubble, it bursts and each enemy within 3 makes a Might test. 
      <br />✸ ≤11 5 poison damage; wet and weakened (save ends) 
      <br />★ 12–16 4 poison damage; wet (EoT) 
      <br />✦ 17 Wet (EoT) (see Wet)"
traits:
  - name: "Toxiferous"
    desc: "When an adjacent enemy grabs or uses a melee ability against the wave, they take 2 poison damage."
```