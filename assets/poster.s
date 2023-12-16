.global _start

.section .data
greeting: .asciz "Welcome to SVUCTF Winter 2023!\n"

.section .text
_start:
    li a0, 1
    la a1, greeting
    li a2, 31
    li a7, 64
    ecall
    
    li a0, 0
    li a7, 93
    ecall

