	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 12, 0	sdk_version 12, 3
	.section	__TEXT,__literal4,4byte_literals
	.p2align	2                               ## -- Begin function main
LCPI0_0:
	.long	0x3f800000                      ## float 1
	.section	__TEXT,__text,regular,pure_instructions
	.globl	_main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$16, %rsp
	movl	$0, -4(%rbp)
	leaq	L_.str(%rip), %rdi
	movb	$0, %al
	callq	_printf
	leaq	L_.str.1(%rip), %rdi
	movb	$0, %al
	callq	_printf
	leaq	L_.str.2(%rip), %rdi
	leaq	-8(%rbp), %rsi
	movb	$0, %al
	callq	_scanf
	movl	%eax, %ecx
	xorl	%eax, %eax
	cmpl	%ecx, %eax
	jne	LBB0_2
## %bb.1:
	xorps	%xmm0, %xmm0
	movss	%xmm0, -8(%rbp)
	leaq	L_.str.3(%rip), %rdi
	movb	$0, %al
	callq	_scanf
LBB0_2:
	xorps	%xmm0, %xmm0
	movss	%xmm0, -12(%rbp)
LBB0_3:                                 ## =>This Inner Loop Header: Depth=1
	movss	-12(%rbp), %xmm1                ## xmm1 = mem[0],zero,zero,zero
	movss	-8(%rbp), %xmm0                 ## xmm0 = mem[0],zero,zero,zero
	ucomiss	%xmm1, %xmm0
	jbe	LBB0_5
## %bb.4:                               ##   in Loop: Header=BB0_3 Depth=1
	leaq	L_.str.4(%rip), %rdi
	movb	$0, %al
	callq	_printf
	movss	LCPI0_0(%rip), %xmm0            ## xmm0 = mem[0],zero,zero,zero
	addss	-12(%rbp), %xmm0
	movss	%xmm0, -12(%rbp)
	jmp	LBB0_3
LBB0_5:
	leaq	L_.str.5(%rip), %rdi
	movb	$0, %al
	callq	_printf
	xorl	%eax, %eax
	addq	$16, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"Compilador pro\n"

L_.str.1:                               ## @.str.1
	.asciz	"cuantas veces quiere ser saludado?\n"

L_.str.2:                               ## @.str.2
	.asciz	"%f"

L_.str.3:                               ## @.str.3
	.asciz	"%*s"

L_.str.4:                               ## @.str.4
	.asciz	"Hola\n"

L_.str.5:                               ## @.str.5
	.asciz	"Fin del programa\n"

.subsections_via_symbols
