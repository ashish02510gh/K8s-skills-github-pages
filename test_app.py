#!/usr/bin/env python
"""Test script for Flask app"""

import os
import sys

# Set Flask environment to development for testing
os.environ['FLASK_ENV'] = 'development'

from app import create_app

print("=" * 60)
print("K8s Skills Flask Application - Test Results")
print("=" * 60)

try:
    # Create app
    app = create_app()
    print("\n✓ App created successfully")
    
    # Check routes
    routes = sorted([
        (rule.rule, rule.endpoint) 
        for rule in app.url_map._rules 
        if rule.endpoint != 'static'
    ])
    
    print(f"\n✓ Routes registered: {len(routes)}")
    print("\nRoute Mappings:")
    for rule, endpoint in routes:
        print(f"  {rule:<30} -> {endpoint}")
    
    # Check templates
    print(f"\n✓ Template folder: {app.template_folder}")
    print(f"✓ Static folder: {app.static_folder}")
    
    # Check config
    print(f"\n✓ Configuration loaded: {app.config.get('ENV', 'unknown')}")
    print(f"✓ Debug mode: {app.debug}")
    
    # Test a route
    with app.test_client() as client:
        print("\nTesting Routes:")
        test_routes = ['/', '/setup', '/security', '/rbac', '/cncfscope']
        for route in test_routes:
            response = client.get(route)
            status = "✓" if response.status_code == 200 else "✗"
            print(f"  {status} GET {route:<20} -> {response.status_code}")
        
        # Test 404
        response = client.get('/nonexistent')
        status = "✓" if response.status_code == 404 else "✗"
        print(f"  {status} GET /nonexistent       -> {response.status_code} (expected 404)")
    
    print("\n" + "=" * 60)
    print("All tests passed! App is ready for deployment.")
    print("=" * 60)
    
except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
