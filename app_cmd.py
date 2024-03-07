import os
# Set your OpenAI API key
os.environ['OPENAI_API_KEY'] = "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"

from llama_index.core import StorageContext, load_index_from_storage

# Initialize the storage context and load the index
storage_context = StorageContext.from_defaults(persist_dir='./storage')
index = load_index_from_storage(storage_context)
# chat_engine = index.as_chat_engine(chat_mode="react", llm=llm, verbose=True)

query_engine = index.as_query_engine()

# Initialize an empty list to store the conversation history
conversation_history = []

# app = Flask(__name__)

# Interactive loop for querying the AI tutor
# @app.route('/query', methods=['GET'])
# def hello_world():
#     print("msg")
#     query = request.args.get('query') if request.method == 'GET' else request.form.get('query')
#     print(query)
#     while True:
#     # query = input()

#         if query.lower() == 'exit':
#             print("All the best! Happy studying.")
#             break

#     # 0Add the user's query to the conversation history
#         conversation_history.append({'query': query})

#     # Concatenate the conversation history to form the context for the query
#         context = " ".join(conversation_history)
#     # Get the response from the query engine
#         response = query_engine.query(context)

#     # Add the AI's response to the conversation history
#         conversation_history.append(f"AI Tutor: {response}")
#     # if query is not None:
#     #     conversation_history.append({'query': query})
#     #     query_engine = index.as_query_engine()
#     #     response = query_engine.query(context)
#     #     conversation_history.append({'response': response})
#         return jsonify({"response": str(response)})
#     else:
#         return jsonify({"error": "query field is missing"}), 400

# while True:
#     query = input()

#     if query.lower() == 'exit':
#         print("All the best! Happy studying.")
#         break

#     # 0Add the user's query to the conversation history
#     conversation_history.append(f"user: {query}")

#     # Concatenate the conversation history to form the context for the query
#     context = " ".join(conversation_history)
#     # Get the response from the query engine
#     response = query_engine.query(context)

#     # Add the AI's response to the conversation history
#     conversation_history.append(f"AI Tutor: {response}")

    
    
    # print("\nAI Tutor :)", response)
    # print(" ")

