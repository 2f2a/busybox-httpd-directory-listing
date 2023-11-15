#!/bin/sh

posix_compliant() {
    strg="${*}"
    printf '%s' "${strg%%[%+]*}"
    j="${strg#"${strg%%[%+]*}"}"
    strg="${j#?}"
    case "${j}" in "%"* )
        printf '%b' "\\0$(printf '%o' "0x${strg%"${strg#??}"}")"
   	strg="${strg#??}"
        ;; "+"* ) printf ' '
        ;;    * ) return
    esac
    if [ -n "${strg}" ] ; then posix_compliant "${strg}"; fi
}

posix_compliant "${*}"