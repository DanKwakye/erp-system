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


// CUSTOMERS
export const getCustomers = () => api.get('/customers/');
export const getCustomer = (id) => api.get(`/customers/${id}`);
export const createCustomer = (data) => api.post('/customers/', data);
export const updateCustomer = (id, data) => api.put(`/customers/${id}`, data);
export const deleteCustomer = (id) => api.delete(`/customers/${id}`);


// ORDERS
export const getOrders = () => api.get('/orders/');
export const getOrder = (id) => api.get(`/orders/${id}`);
export const createOrder = (data) => api.post('/orders/', data);
export const updateOrder = (id, data) => api.put(`/orders/${id}`, data);
export const deleteOrder = (id) => api.delete(`/orders/${id}`);


// INVENTORY
export const getInventoryMovements = () => api.get('/inventory/movements');
export const getInventoryMovement = (id) => api.get(`/inventory/movements/${id}`);
export const createInventoryMovement = (data) => api.post('/inventory/movements', data);
export const deleteInventoryMovement = (id) => api.delete(`/inventory/movements/${id}`);
export const getCurrentStock = (productId) => api.get(`/inventory/stock/${productId}`);



export default api;