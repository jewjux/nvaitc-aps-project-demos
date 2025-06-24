const express = require('express');
const cors = require('cors');
const { generateScore, generateSuggestion } = require('./controller/llm-chat-controller');

const router = express.Router();

router.use(cors()); // Enable CORS for all routes

router.post('/generate-score', generateScore);
router.post('/generate-suggestion', generateSuggestion);

module.exports = router;