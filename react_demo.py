#!/usr/bin/env python3
"""
ReAct Agent Demo for Pine Labs Integration
This script demonstrates the ReAct agent's capabilities in action
"""

import os
import json
from colorama import Fore, Style, init
from app.services.react_agent import ReActAgent

# Initialize colorama for colored output
init(autoreset=True)

def print_section(title):
    """Print a section header"""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}{title}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")

def print_agent_response(response, step_name):
    """Print agent response with formatting"""
    print(f"\n{Fore.GREEN}🤖 {step_name}:{Style.RESET_ALL}")
    print(f"   Response: {response.get('response', 'N/A')}")
    print(f"   Action Taken: {response.get('action_taken', 'None')}")
    print(f"   Success: {response.get('success', False)}")
    
    if response.get('reasoning'):
        print(f"   Reasoning: {response.get('reasoning')[:100]}...")
    
    if response.get('result'):
        print(f"   Result Keys: {list(response.get('result', {}).keys())}")

def demo_react_agent():
    """Demonstrate the ReAct agent capabilities"""
    
    print(f"{Fore.YELLOW}🚀 Starting Pine Labs ReAct Agent Demo{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}This demo shows how the agent reasons and acts on integration tasks{Style.RESET_ALL}")
    
    # Create ReAct agent
    agent = ReActAgent()
    
    # Demo scenarios
    scenarios = [
        {
            "title": "Code Generation Request",
            "message": "Generate Python code for payment integration with Pine Labs API",
            "expected_action": "generate_code"
        },
        {
            "title": "Payload Validation",
            "message": "Validate this payment payload",
            "context": {
                "payload": {
                    "type": "payment",
                    "amount": "10000",
                    "currency": "INR",
                    "merchant_order_id": "ORD_123456"
                }
            },
            "expected_action": "validate_payload"
        },
        {
            "title": "Integration Testing",
            "message": "Test this payment integration",
            "context": {
                "payload": {
                    "type": "payment",
                    "amount": "10000",
                    "currency": "INR",
                    "merchant_order_id": "ORD_123456",
                    "merchant_id": "test_merchant"
                }
            },
            "expected_action": "test_integration"
        },
        {
            "title": "Error Fixing",
            "message": "Fix this error in my Python code",
            "context": {
                "error_message": "Invalid amount format",
                "code": "amount = '100.00'  # Should be in paisa",
                "language": "python"
            },
            "expected_action": "fix_error"
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print_section(f"Demo {i}: {scenario['title']}")
        
        print(f"{Fore.BLUE}👤 User Request:{Style.RESET_ALL} {scenario['message']}")
        
        if scenario.get('context'):
            print(f"{Fore.BLUE}📋 Context:{Style.RESET_ALL} {json.dumps(scenario['context'], indent=2)}")
        
        # Process through ReAct agent
        response = agent.reason_and_act(
            scenario['message'], 
            scenario.get('context', {})
        )
        
        # Show the ReAct process
        print(f"\n{Fore.MAGENTA}🧠 ReAct Process Breakdown:{Style.RESET_ALL}")
        print(f"1. {Fore.YELLOW}REASON{Style.RESET_ALL}: Agent analyzes the request")
        print(f"2. {Fore.YELLOW}ACT{Style.RESET_ALL}: Agent performs action ({response.get('action_taken', 'None')})")
        print(f"3. {Fore.YELLOW}OBSERVE{Style.RESET_ALL}: Agent reviews results")
        print(f"4. {Fore.YELLOW}RESPOND{Style.RESET_ALL}: Agent provides response")
        
        # Show response details
        print_agent_response(response, "Final Response")
        
        # Show result details if available
        if response.get('result'):
            result = response['result']
            if result.get('code'):
                print(f"\n{Fore.GREEN}📝 Generated Code Preview:{Style.RESET_ALL}")
                print(result['code'][:200] + "..." if len(result['code']) > 200 else result['code'])
            
            elif result.get('valid') is not None:
                status = "✅ Valid" if result['valid'] else "❌ Invalid"
                print(f"\n{Fore.GREEN}🔍 Validation Result:{Style.RESET_ALL} {status}")
                if not result['valid'] and result.get('errors'):
                    print(f"   Errors: {result['errors']}")
        
        print(f"\n{Fore.CYAN}⏳ Press Enter to continue to next demo...{Style.RESET_ALL}")
        input()
    
    # Show conversation history
    print_section("Conversation Summary")
    history = agent.get_conversation_history()
    print(f"Total messages in conversation: {len(history)}")
    
    for i, msg in enumerate(history[-4:], 1):  # Show last 4 messages
        role = "👤 User" if msg['role'] == 'user' else "🤖 Agent"
        print(f"{i}. {role}: {msg['content'][:80]}...")
    
    print(f"\n{Fore.GREEN}✅ Demo completed! The ReAct agent successfully handled all integration tasks.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}💡 Key Benefits of ReAct Approach:{Style.RESET_ALL}")
    print("   • Transparent reasoning process")
    print("   • Actionable task execution")
    print("   • Contextual awareness")
    print("   • Error recovery and fixing")
    print("   • Self-explanatory workflow")

if __name__ == "__main__":
    try:
        demo_react_agent()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}👋 Demo interrupted by user{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}❌ Demo failed: {str(e)}{Style.RESET_ALL}")
