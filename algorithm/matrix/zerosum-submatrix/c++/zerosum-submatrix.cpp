#include <iostream>
#include <stdio.h>

class ZeroSubMatrix
{
public:
	ZeroSubMatrix();
	~ZeroSubMatrix();

	int NFun;
	int test();
	int getZeroSubMatrix(int **matrix,int M, int N);
	int stupid(int **matrix, int m1, int m2, int n1, int n2);
	int recursionV1(int **matrix, int m1, int m2, int n1, int n2);
	int recursionV2(int **matrix, int m1, int m2, int n1, int n2);
private:
	int sumRightColumn(int **matrix, int m1, int m2, int n1, int n2);
	int sumLeftColumn(int **matrix, int m1, int m2, int n1, int n2);
	int sumDownRow(int **matrix, int m1, int m2, int n1, int n2);
	int sumUpRow(int **matrix, int m1, int m2, int n1, int n2);
};




int NT = 0;

int main(int argc, char const *argv[])
{
	/* code */
	int M = 4;
	int N = 4;
	int matrix0[M*N] = {
		9,	4,	6,	8,
		-6,	-8,	39,	0,
		0, 	14,	-45,9,
		5,	8,	9,	4};

	int **matrix;
	matrix = new int *[M];
	for(int i = 0; i < M; i ++)
	    matrix[i] = new int[N]; 

	for(int i=0; i<M; i++)
	{
		for (int j = 0; j < N; ++j)
		{
			matrix[i][j] = matrix0[i*N + j];	
			// printf("%d,%d,%d\n", i,j,matrix[i][j]);
		}
	}
	zeroSubMatrix(matrix,0,M-1,0,N-1);
	std::cout<<NT<<std::endl;
	return 0;
}


int zeroSubMatrix(int **matrix, int m1, int m2, int n1, int n2)
{
	// printf("#[(%d,%d),(%d,%d)]\n",m1,n1,m2,n2);
	// getchar();
	
	NT ++;
	int sum = 0;

	if((n1 == n2)&&(m1 == m2))
	{
		return matrix[m1][n1];
	}


	if(m2 > m1 + 1 && n2 > n1 +1) 
	{
		sum = zeroSubMatrix(matrix, m1+1, m2-1, n1+1, n2-1) + aroundMatrix(matrix, m1, m2, n1, n2);
		if(sum == 0)
		{
			printf("[(%d,%d),(%d,%d)]  %d + %d = %d \n",m1,n1,m2,n2,t1,t2,sum);
			for (int i = m1; i <= m2; ++i)
			{
				for (int j = n1; j <= n2; ++j)
				{
					printf("%d\t", matrix[i][j]);
				}
				printf("\n");
			}
		}

		zeroSubMatrix(matrix, m1+1, m2, n1, n2);
	}
	else if(m2 = m1 + 1 && n2 > n1 +1)
	{
		sum = zeroSubMatrix(matrix, m1, m2-1, n1+1, n2-1) + aroundMatrix(matrix, m1, m2, n1, n2) - sumDownRow(matrix, m1, m2, n1, n2);
		if(sum == 0)
		{
			printf("[(%d,%d),(%d,%d)]  %d + %d = %d \n",m1,n1,m2,n2,t1,t2,sum);
			for (int i = m1; i <= m2; ++i)
			{
				for (int j = n1; j <= n2; ++j)
				{
					printf("%d\t", matrix[i][j]);
				}
				printf("\n");
			}
		}
	}

	else if(m1 == m2)
	{
		sum = sumDownRow(matrix, m1, m2, n1, n2);
	}

	if(m1+1 < m2)
	{
		zeroSubMatrix(matrix, m1+1, m2, n1, n2);
	}


	if(n2 > n1)
	{
		zeroSubMatrix(matrix, m1, m2, n1, n2-1);
	}
	
	if(n1+1 < n2)
	{
		zeroSubMatrix(matrix, m1, m2, n1 +1, n2);
	}

	return sum;
}

int aroundMatrix(int **matrix, int m1, int m2, int n1, int n2)
{
	int sum = 0;
	for(int i=m1; i <=m2; i++)
	{
		sum += matrix[i][n2];
		sum += matrix[i][n1];
	}

	for(int i=n1+1; i <=n2-1; i++)
	{
		sum += matrix[m1][i];
		sum += matrix[m2][i];
	}
	return sum;
}

int sumRightColumn(int **matrix, int m1, int m2, int n1, int n2)
{
	int sum = 0;
	for(int i=m1; i <=m2; i++)
	{
		sum += matrix[i][n2];
	}
	return sum;
}

int sumDownRow(int **matrix, int m1, int m2, int n1, int n2)
{
	int sum = 0;
	for(int i=n1; i <=n2; i++)
	{
		sum += matrix[m2][i];
	}
	return sum;
}

int sumLeftColumn(int **matrix, int m1, int m2, int n1, int n2)
{
	int sum = 0;
	for(int i=m1; i <=m2; i++)
	{
		sum += matrix[i][n1];
	}
	return sum;
}

int sumUpRow(int **matrix, int m1, int m2, int n1, int n2)
{
	int sum = 0;
	for(int i=n1; i <=n2; i++)
	{
		sum += matrix[m1][i];
	}
	return sum;
}
