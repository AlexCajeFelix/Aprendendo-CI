package com.example.demo;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CalculatorServiceTests {

    private CalculatorService calculatorService;

    @BeforeEach
    void setUp() {
        calculatorService = new CalculatorService();
    }

    @Test
    void testAdd() {
        assertEquals(5, calculatorService.add(2, 3));
        assertEquals(0, calculatorService.add(-1, 1));
        assertEquals(-5, calculatorService.add(-2, -3));
    }

    @Test
    void testSubtract() {
        assertEquals(2, calculatorService.subtract(5, 3));
        assertEquals(-2, calculatorService.subtract(3, 5));
        assertEquals(0, calculatorService.subtract(5, 5));
    }

    @Test
    void testMultiply() {
        assertEquals(6, calculatorService.multiply(2, 3));
        assertEquals(0, calculatorService.multiply(0, 5));
        assertEquals(-10, calculatorService.multiply(-2, 5));
    }

    @Test
    void testDivide() {
        assertEquals(2.0, calculatorService.divide(6, 3));
        assertEquals(2.5, calculatorService.divide(5, 2));
        assertEquals(-2.0, calculatorService.divide(-6, 3));
    }

    @Test
    void testDivideByZero() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            calculatorService.divide(10, 0);
        });
        assertEquals("Cannot divide by zero", exception.getMessage());
    }

    @Test
    void testIsEven() {
        assertTrue(calculatorService.isEven(2));
        assertTrue(calculatorService.isEven(0));
        assertTrue(calculatorService.isEven(-4));
        assertFalse(calculatorService.isEven(3));
        assertFalse(calculatorService.isEven(-5));
    }

    @Test
    void testIsPrime() {
        assertTrue(calculatorService.isPrime(2));
        assertTrue(calculatorService.isPrime(3));
        assertTrue(calculatorService.isPrime(5));
        assertTrue(calculatorService.isPrime(7));
        assertTrue(calculatorService.isPrime(11));
        
        assertFalse(calculatorService.isPrime(0));
        assertFalse(calculatorService.isPrime(1));
        assertFalse(calculatorService.isPrime(4));
        assertFalse(calculatorService.isPrime(6));
        assertFalse(calculatorService.isPrime(9));
    }
}

