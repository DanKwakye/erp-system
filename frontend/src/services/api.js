import axios from 'axios';

// Base API URL - your FastAPI backend
const API_BASE_URL = 'http://127.0.0.1:8000/api/v1';

// Create axios instance with base config
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// PRODUCT CATEGORIES
export const getCategories = () => api.get('/products/categories');
export const createCategory = (data) => api.post('/products/categories', data);

//PRODUCTS
export const getProducts = () => api.get('/products/');
export const getProduct = (id) => api.get(`/products/${id}`);
export const createProduct = (data) => api.post('/products/', data);
export const updateProduct = (id, data) => api.put(`/products/${id}`, data);
export const deleteProduct = (id) => api.delete(`/products/${id}`);


// SUPPLIERS
export const getSuppliers = () => api.get('/suppliers/');
export const getSupplier = (id) => api.get(`/suppliers/${id}`);
export const createSupplier = (data) => api.post('/suppliers/', data);
export const updateSupplier = (id, data) => api.put(`/suppliers/${id}`, data);
export const deleteSupplier = (id) => api.delete(`/suppliers/${id}`);

export default api;