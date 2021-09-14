# Ansible

Some Ansible examples:
```
- name: Sync two dirs ...
  synchronize:
    src: '/secrets/envs/foobar'
    dest: '/secrets/envs/'
    delete: yes
    rsync_opts:
      - "--chmod=u=r,g=,o="
```
