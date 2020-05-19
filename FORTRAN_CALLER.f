      SUBROUTINE FORTRAN_CALLER( A1 )
C     .. Scalar Arguments ..
      INTEGER            A1
C     .. External Subroutines ..
      EXTERNAL           XERBLA
C     ..
      CALL XERBLA( 'FORTRAN_CALLER', A1 )
C
      RETURN
C
      END
