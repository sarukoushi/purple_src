# How I managed to fix some problem with `Grub` and triple boot on separate drives.
#### I installed `Ubuntu 24` on drive `sda` with `btrfs`, mounted on subvolumes `@`, `@home`, `@swap`, then I installed `Ubuntu 22.04.5` on drive `sdb` with `ext4`. And them I installed `Windows 11` on `sdc`. After I did it I couldn't boot into `Ubuntu 24`, `Ubuntu 22` was booting from `sda` bootable partition. There was no `Ubuntu 24` entry in `Grub` boot menu or in `bios` boot menu. I found nice tutorial with the fix:

https://youtu.be/Zr9oyWjD6IA?feature=shared
Big thanks to the author.

1. I had to boot to `Ubuntu` `live USB`
2. Then choose the `Try Ubuntu` option.
3. Open terminal and do this, first i will fix `grub` for the `Ubuntu 22`:
   * `sudo su -`
   * `mount /dev/sdb2 /mnt`
   * `mount /dev/sdb1 /mnt/boot/efi`
   * `for i in /dev /dev/pts /proc /sys /run; do mount -B $i /mnt$i; done`
   * `chroot /mnt`
   * `mount -t efivarfs none /sys/firmware/efi/efivars`
   * `grub-install /dev/sdb`
   * `update-grub`
   * `exit`
4. Then I couldn't unmount something so I rebooted again into `live USB`.
   Now I will revive `Grub` for `Ubuntu 24`.
   We will now mount specific subvolume with root directory from `btrfs` drive
   using `-o subvol=[subvolume_name]` option for `mount` command.
   * `sudo su -`
   * `mount /dev/sda2 /mnt -o subvol=@`
   * `mount /dev/sda1 /mnt/boot/efi`
   * `for i in /dev /dev/pts /proc /sys /run; do mount -B $i /mnt$i; done`
   * `chroot /mnt`
   * `mount -t efivarfs none /sys/firmware/efi/efivars`
   * `grub-install /dev/sda`
   * `update-grub`
   * `exit`
5. Now everything works fine! Big thanks again to the author of the tutorial.
