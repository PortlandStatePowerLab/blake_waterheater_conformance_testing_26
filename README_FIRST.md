# WH1 Master Staging

This folder is a staged clean master copy for manual inspection before any Pi copy
or GitHub push. It was assembled from the active Pi script dump and the hardware
documentation repository, but those original source folders were not edited.

Only files listed in `DEPLOY_MANIFEST.md` are intended to be copied to the
Raspberry Pi. Hardware documents, audit reports, reference-only documents,
generated material, and legacy scripts are not deployment payloads.

`legacy_deprecated/` is historical reference only. Do not run scripts from that
folder as part of the current WH1 PCB-ribbon deployment candidate.

Current hardware truth preserved in this staging folder:

- U11 is treated as MAX1238EEE+ unless physical board marking proves otherwise.
- U12 is TXS0104E level shifting Pi-side I2C to the MAX1238 I2C side.
- U13 is ACS37800 at I2C address 0x60.
- ADC channels are MAX1238 channels, not Raspberry Pi GPIO pins.
- GPIO17 is the valve relay control path through the ribbon cable.
