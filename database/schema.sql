-- Criação das tabelas principais para a Startup Loja Online + IA

-- Tabela de Clientes
CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100),
    endereco TEXT
);

-- Tabela de Fornecedores   
CREATE TABLE fornecedores (
    id_fornecedor SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100)
);

-- Tabela de Funcionários
CREATE TABLE funcionarios (
    id_funcionario SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(50),
    email VARCHAR(100),
    senha_hash TEXT
);

-- Tabela de Produtos
CREATE TABLE produtos (
    id_produto SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10, 2) NOT NULL,
    id_fornecedor INTEGER REFERENCES fornecedores(id_fornecedor)
);

-- Tabela de Estoque
CREATE TABLE estoque (
    id_estoque SERIAL PRIMARY KEY,
    id_produto INTEGER REFERENCES produtos(id_produto),
    quantidade_estoque INTEGER DEFAULT 0,
    quantidade_minima INTEGER DEFAULT 0
);

-- Tabela de Pedidos
CREATE TABLE pedidos (
    id_pedido SERIAL PRIMARY KEY,
    id_cliente INTEGER REFERENCES clientes(id_cliente),
    data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) DEFAULT 'Em andamento'
);

-- Tabela de Itens do Pedido
CREATE TABLE itens_pedido (
    id_item SERIAL PRIMARY KEY,
    id_pedido INTEGER REFERENCES pedidos(id_pedido),
    id_produto INTEGER REFERENCES produtos(id_produto),
    quantidade INTEGER DEFAULT 1,
    preco_unitario DECIMAL(10, 2)
);

-- Tabela de Notas Fiscais
CREATE TABLE notas_fiscais (
    id_nf SERIAL PRIMARY KEY,
    tipo VARCHAR(10) CHECK (tipo IN ('entrada', 'saida')),
    id_pedido INTEGER REFERENCES pedidos(id_pedido),
    data_emissao DATE DEFAULT CURRENT_DATE,
    valor_total DECIMAL(12, 2)
);

-- Tabela Financeira
CREATE TABLE financeiro (
    id_lancamento SERIAL PRIMARY KEY,
    tipo VARCHAR(10) CHECK (tipo IN ('receita', 'despesa')),
    descricao TEXT,
    valor DECIMAL(12, 2),
    data DATE DEFAULT CURRENT_DATE
);

-- Tabela de Mensagens WhatsApp
CREATE TABLE mensagens (
    id_mensagem SERIAL PRIMARY KEY,
    id_cliente INTEGER REFERENCES clientes(id_cliente),
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    conteudo TEXT,
    status_atendimento VARCHAR(50) DEFAULT 'aberto'
);

CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    usuario VARCHAR(50) UNIQUE,
    senha_hash TEXT NOT NULL,
    tipo VARCHAR(20) DEFAULT 'funcionario' -- ou 'admin'
);
