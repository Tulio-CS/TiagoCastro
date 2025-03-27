    printf("Digite a ordem da matriz");
    scanf("%d",&n);
    int A[n][n],B[n][n],C[n][n];

    printf("Digite os elementos da primeira matriz");
    for (i=0;i<n;i++){
            for (j=0;j<n;j++){
                    scanf("%d",&A[i][j]);
                };
        };

    printf("Digite os elementos da segunda matriz");
    for (i=0;i<n;i++){
            for (j=0;j<n;j++){
                    scanf("%d",&B[i][j]);
                };
        };
    multiplicaMatriz(A,B,C);
    printf("Resultado da multiplicação de matrizes:\n")
    imprimeMatriz(C);
    return 0;
}